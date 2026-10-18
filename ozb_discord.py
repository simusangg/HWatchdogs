"""
OzBargain -> Discord notifier.

Run once (for GitHub Actions / cron):   python ozb_discord.py
Run forever (for a VPS / Raspberry Pi): python ozb_discord.py --loop

Settings come from environment variables:
  DISCORD_WEBHOOK_URL  (required) your Discord channel webhook
  KEYWORDS             optional, comma-separated, e.g. "ssd,lego,costco" (empty = all deals)
  FEED_URL             optional, defaults to the OzBargain new-deals feed
  INTERVAL             optional, seconds between checks in --loop mode (default 300)
  STATE_FILE           optional, where seen deals are stored (default seen.json)
"""
import html
import json
import os
import re
import sys
import time
from pathlib import Path

import feedparser
import requests

FEED_URL = os.environ.get("FEED_URL", "https://www.ozbargain.com.au/deals/feed")
WEBHOOK = os.environ.get("DISCORD_WEBHOOK_URL", "")
KEYWORDS = [k.strip().lower() for k in os.environ.get("KEYWORDS", "").split(",") if k.strip()]
STATE = Path(os.environ.get("STATE_FILE", "seen.json"))
INTERVAL = int(os.environ.get("INTERVAL", "300"))
UA = "ozb-discord-notifier/1.0"
MAX_REMEMBERED = 300


def load_seen():
    if STATE.exists():
        return json.loads(STATE.read_text())
    return None  # first run


def save_seen(seen):
    STATE.write_text(json.dumps(seen[-MAX_REMEMBERED:], indent=0))


def clean(text, limit):
    text = html.unescape(re.sub(r"<[^>]+>", " ", text or ""))
    text = re.sub(r"\s+", " ", text).strip()
    return text if len(text) <= limit else text[: limit - 1] + "…"


def post_to_discord(entry):
    payload = {
        "embeds": [{
            "title": clean(entry.get("title"), 256),
            "url": entry.link,
            "description": clean(entry.get("summary"), 300),
            "color": 0xF26722,
        }]
    }
    for _ in range(3):
        r = requests.post(WEBHOOK, json=payload, timeout=15)
        if r.status_code == 429:  # Discord rate limit: wait and retry
            time.sleep(float(r.json().get("retry_after", 2)))
            continue
        r.raise_for_status()
        return


def wanted(entry):
    return not KEYWORDS or any(k in entry.get("title", "").lower() for k in KEYWORDS)


def check_once():
    feed = feedparser.parse(FEED_URL, agent=UA)
    if not feed.entries:
        print("No entries returned:", getattr(feed, "bozo_exception", "unknown error"))
        return

    seen = load_seen()
    if seen is None:
        # First run: remember what's already there so we don't spam the channel
        save_seen([e.link for e in feed.entries])
        print(f"First run: recorded {len(feed.entries)} existing deals, no alerts sent.")
        return

    seen_set = set(seen)
    new = [e for e in reversed(feed.entries) if e.link not in seen_set]  # oldest first
    sent = 0
    for e in new:
        if wanted(e):
            post_to_discord(e)
            sent += 1
            time.sleep(1)
        seen.append(e.link)
    save_seen(seen)
    print(f"{len(new)} new deal(s), {sent} sent to Discord.")


def main():
    if not WEBHOOK:
        sys.exit("Set the DISCORD_WEBHOOK_URL environment variable first.")
    if "--loop" in sys.argv:
        while True:
            try:
                check_once()
            except Exception as exc:  # keep running through temporary errors
                print("Error:", exc)
            time.sleep(INTERVAL)
    else:
        check_once()


if __name__ == "__main__":
    main()
