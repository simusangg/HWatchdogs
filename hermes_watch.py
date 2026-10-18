"""
Hermès AU -> Discord watcher.

Checks a Hermès category page and posts to Discord when a product appears
(new, or back online), and optionally when one disappears (sold out / removed).

Run once (GitHub Actions / cron):   python hermes_watch.py
Run forever (Pi / VPS):             python hermes_watch.py --loop

Environment variables:
  DISCORD_WEBHOOK_URL  (required) Discord channel webhook
  HERMES_URL           optional, category page to watch (default: women's bags and clutches)
  KEYWORDS             optional, comma-separated, matched against product names, e.g. "evelyne,picotin"
  NOTIFY_REMOVED       optional, "1" to also alert when a product leaves the page
  INTERVAL             optional, seconds between checks in --loop mode (default 900)
  STATE_FILE           optional (default hermes_state.json)
"""
import json
import os
import re
import sys
import time
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

URL = os.environ.get(
    "HERMES_URL",
    "https://www.hermes.com/au/en/category/leather-goods/bags-and-clutches/womens-bags-and-clutches/",
)
WEBHOOK = os.environ.get("DISCORD_WEBHOOK_URL", "")
KEYWORDS = [k.strip().lower() for k in os.environ.get("KEYWORDS", "").split(",") if k.strip()]
NOTIFY_REMOVED = os.environ.get("NOTIFY_REMOVED", "") == "1"
INTERVAL = int(os.environ.get("INTERVAL", "900"))
STATE = Path(os.environ.get("STATE_FILE", "hermes_state.json"))

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/124.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml",
    "Accept-Language": "en-AU,en;q=0.9",
}
PRODUCT_RE = re.compile(r"/product/[a-z0-9-]+-(H[0-9A-Z]+)/?")  # SKU like H056277CK89
PRICE_RE = re.compile(r"AU\$\s?[\d,]+")


# ---------- reading the page ----------

def find_price(link):
    """Walk up from the product link until we hit the card containing exactly one price."""
    node = link
    for _ in range(6):
        node = node.parent
        if node is None:
            return ""
        prices = PRICE_RE.findall(node.get_text(" ", strip=True))
        if len(prices) == 1:
            return prices[0]
        if len(prices) > 1:  # went too far up (into the whole grid)
            return ""
    return ""


def fetch_products():
    """Return {sku: {name, price, url}}, or None if the page couldn't be read."""
    try:
        r = requests.get(URL, headers=HEADERS, timeout=30)
    except requests.RequestException as exc:
        print("Request failed:", exc)
        return None
    if r.status_code != 200:
        print(f"HTTP {r.status_code} from Hermès (probably blocked).")
        return None

    soup = BeautifulSoup(r.text, "html.parser")
    products = {}
    for a in soup.find_all("a", href=True):
        m = PRODUCT_RE.search(a["href"])
        if not m:
            continue
        sku = m.group(1)
        title = (a.get("title") or "").strip()
        if sku in products and products[sku]["has_title"]:
            continue
        if not title:
            slug = a["href"].rstrip("/").split("/")[-1].rsplit("-", 1)[0]
            title = slug.replace("-", " ").title()
        products[sku] = {
            "name": title,
            "price": find_price(a),
            "url": urljoin("https://www.hermes.com", a["href"]),
            "has_title": bool(a.get("title")),
        }

    if not products:
        print("Page loaded but no products found (blocked, challenge page, or layout changed).")
        return None
    for p in products.values():
        p.pop("has_title")
    return products


# ---------- Discord ----------

def send(payload):
    for _ in range(3):
        r = requests.post(WEBHOOK, json=payload, timeout=15)
        if r.status_code == 429:
            time.sleep(float(r.json().get("retry_after", 2)))
            continue
        r.raise_for_status()
        return


def send_product(heading, p, color):
    embed = {"title": p["name"][:256], "url": p["url"], "description": heading, "color": color}
    if p.get("price"):
        embed["fields"] = [{"name": "Price", "value": p["price"], "inline": True}]
    send({"embeds": [embed]})


def wanted(name):
    return not KEYWORDS or any(k in name.lower() for k in KEYWORDS)


# ---------- main logic ----------

def load_state():
    return json.loads(STATE.read_text()) if STATE.exists() else None


def save_state(state):
    STATE.write_text(json.dumps(state, indent=1, ensure_ascii=False))


def check_once():
    state = load_state()
    current = fetch_products()

    if current is None:
        # Don't overwrite what we know; just warn once until it recovers.
        if state and not state.get("blocked"):
            send({"content": "⚠️ Hermès watcher can't read the page right now (blocked or layout "
                             "changed). It will keep trying and let you know when it recovers."})
            state["blocked"] = True
            save_state(state)
        return

    if state is None:
        save_state({"products": current, "blocked": False})
        print(f"First run: recorded {len(current)} products, no alerts sent.")
        return

    if state.get("blocked"):
        send({"content": "✅ Hermès watcher is reading the page again."})

    old = state["products"]
    added = [s for s in current if s not in old]
    removed = [s for s in old if s not in current]

    sent = 0
    for sku in added:
        if wanted(current[sku]["name"]):
            send_product("🆕 Now available online", current[sku], 0xF37021)
            sent += 1
            time.sleep(1)
    if NOTIFY_REMOVED:
        for sku in removed:
            if wanted(old[sku]["name"]):
                send_product("❌ No longer listed", old[sku], 0x95A5A6)
                sent += 1
                time.sleep(1)

    save_state({"products": current, "blocked": False})
    print(f"{len(current)} products on page, {len(added)} new, {len(removed)} gone, {sent} alert(s) sent.")


def main():
    if not WEBHOOK:
        sys.exit("Set the DISCORD_WEBHOOK_URL environment variable first.")
    if "--loop" in sys.argv:
        while True:
            try:
                check_once()
            except Exception as exc:
                print("Error:", exc)
            time.sleep(INTERVAL)
    else:
        check_once()


if __name__ == "__main__":
    main()
