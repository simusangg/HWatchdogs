================================================================================
HWatchdogs
Personal website watchers with Discord notifications
================================================================================

PLEASE READ THIS ENTIRE DOCUMENT BEFORE USING, COPYING, FORKING OR RUNNING
ANY PART OF THIS REPOSITORY. BY DOING ANY OF THOSE THINGS, YOU CONFIRM THAT YOU
HAVE READ, UNDERSTOOD AND AGREED TO EVERYTHING BELOW. IF YOU DO NOT AGREE, DO
NOT USE THIS REPOSITORY OR ANY CODE FROM IT.


--------------------------------------------------------------------------------
1. WHAT THIS PROJECT IS
--------------------------------------------------------------------------------

This repository contains small hobby scripts written for personal and
educational purposes. They:

  - read a publicly available RSS feed from OzBargain (ozbargain.com.au) and
    send a message to a Discord channel when a new deal is posted; and

  - read a publicly available product listing page on Hermes.com (Australia)
    and send a message to a Discord channel when a product appears on, or is
    removed from, that page.

The scripts only read publicly accessible pages that any visitor can view in a
normal web browser without logging in. They do not:

  - log in to any account or access any non-public area of any website;
  - purchase, reserve, add to cart or check out any product;
  - solve, bypass or attempt to circumvent CAPTCHAs, bot protection, rate
    limits, IP blocks or any other access control;
  - collect, store or process personal information about any person;
  - copy, store or republish images, product descriptions or other creative
    content from any website (only product names, prices and links are kept,
    solely to detect changes); or
  - resell, redistribute or commercially exploit any data.

The project is provided as a personal learning exercise and a demonstration of
scheduled automation, RSS parsing and webhook notifications.


--------------------------------------------------------------------------------
2. NO AFFILIATION OR ENDORSEMENT
--------------------------------------------------------------------------------

This project is an independent, unofficial hobby project. It is NOT affiliated
with, authorised, sponsored, approved or endorsed by, or in any way officially
connected with, any of the following or their related companies:

  - Hermes International, Hermes Sellier or any member of the Hermes Group;
  - OzBargain or its owners and operators;
  - Discord Inc.;
  - GitHub, Inc. or Microsoft Corporation;
  - cron-job.org or its operators; or
  - any other website, service or company referred to in this repository.

"Hermes", "OzBargain", "Discord", "GitHub" and all other names, trademarks,
logos and brands mentioned in this repository are the property of their
respective owners. They are used here solely to identify the websites and
services the code interacts with (nominative use). No claim of ownership or
association is made or implied.


--------------------------------------------------------------------------------
3. YOUR RESPONSIBILITY AS A USER
--------------------------------------------------------------------------------

The author publishes this code but has NO CONTROL over who copies it, how it is
modified, how often it is run, where it is run, or what it is used for. Every
person who uses, copies, forks, modifies or runs this code does so entirely on
their own initiative, at their own risk, and is solely responsible for that
use.

If you use this code, YOU are solely responsible for:

  a) Website terms of use. Reading and complying with the terms of use,
     conditions of sale, robots.txt rules and any other policies of every
     website you monitor. Some websites prohibit or restrict automated access.
     If a website's terms prohibit your intended use, do not use this code on
     that website.

  b) Laws and regulations. Complying with all laws and regulations that apply
     to you in your country, state and territory, and in the jurisdiction of
     any website or service you interact with. This includes (without
     limitation) laws about computer access, copyright, privacy, consumer
     protection, contracts and telecommunications.

  c) Platform policies. Complying with the terms of service, acceptable use
     policies and usage limits of every platform you run or connect this code
     to, including GitHub (and in particular the GitHub Actions terms for
     GitHub-hosted runners), Discord (including its webhook and developer
     policies), cron-job.org, any VPN provider, any VPS or cloud provider, and
     your internet service provider.

  d) Configuration. Every setting you choose, including check frequency,
     monitored URLs, keywords, webhooks, schedules, hosting location, network
     configuration and any modifications to the code.

  e) Consequences. Any consequence of your use, including (without
     limitation) IP blocks, account suspensions or terminations, repository
     or workflow disabling, service charges or overage fees, missed or
     incorrect notifications, data loss, and any claim, complaint or action
     brought against you by any website owner, platform or other person.

  f) Your own purchasing decisions. Any decision you make to buy or not buy
     any product, based on a notification from this code or otherwise.


--------------------------------------------------------------------------------
4. RESPONSIBLE USE GUIDELINES
--------------------------------------------------------------------------------

If you choose to use this code, the author asks that you, at minimum:

  - Use it only for personal, non-commercial purposes.
  - Keep check intervals polite (the defaults are no faster than every 5
    minutes for RSS feeds and every 10 minutes for web pages; slower is
    better). Do not reduce them further.
  - Respect any block, CAPTCHA, error or rate limit. If a website stops
    serving the page to the script, treat it as a request to stop or slow
    down. Do NOT attempt to bypass it by rotating IP addresses, using proxy
    pools, rotating VPN servers, spoofing browser fingerprints, randomising
    behaviour to avoid detection, solving CAPTCHAs or any similar technique.
  - Do not use this code, or anything built from it, to purchase, reserve or
    hoard products automatically, to give yourself an unfair advantage over
    other shoppers, or for resale or "scalping".
  - Do not use it to place unreasonable load on any website or service.
  - Do not use it to collect, store or process personal information.
  - Do not republish content (images, descriptions, articles) obtained from
    any website.
  - Stop using it on any website immediately if asked to do so by that
    website's owner.

These guidelines are a statement of the author's intent. They do not limit
the responsibilities described in section 3.


--------------------------------------------------------------------------------
5. NO WARRANTY
--------------------------------------------------------------------------------

THIS SOFTWARE IS PROVIDED "AS IS" AND "AS AVAILABLE", WITHOUT WARRANTY OF ANY
KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, ACCURACY, RELIABILITY,
AVAILABILITY, TIMELINESS, SECURITY AND NON-INFRINGEMENT.

Without limiting the above, the author does not warrant that:

  - the code will work, keep working, or work on any particular website;
  - websites will not change their layout, feeds or terms in ways that break
    the code or make its use inappropriate;
  - notifications will be accurate, complete, timely or delivered at all;
  - prices, availability or product information shown in notifications are
    correct (always check the official website before acting);
  - the code is free of bugs, errors, security issues or harmful effects; or
  - using the code complies with any website's terms, any platform's
    policies or any law in your jurisdiction.

Scheduled services (including GitHub Actions schedules and cron-job.org) may
run late, skip runs or stop without notice. Never rely on this code for
anything important or time-critical.


--------------------------------------------------------------------------------
6. LIMITATION OF LIABILITY
--------------------------------------------------------------------------------

TO THE MAXIMUM EXTENT PERMITTED BY LAW, IN NO EVENT SHALL THE AUTHOR OR ANY
CONTRIBUTOR BE LIABLE FOR ANY CLAIM, LOSS, DAMAGE OR OTHER LIABILITY OF ANY
KIND, WHETHER DIRECT, INDIRECT, INCIDENTAL, SPECIAL, CONSEQUENTIAL, EXEMPLARY
OR PUNITIVE, INCLUDING (WITHOUT LIMITATION) LOSS OF PROFITS, LOSS OF
OPPORTUNITY, LOSS OF DATA, ACCOUNT SUSPENSION, SERVICE CHARGES, OR ANY CLAIM BY
A THIRD PARTY, ARISING FROM OR IN CONNECTION WITH THE SOFTWARE, ITS USE OR
MISUSE BY ANY PERSON, OR ANY OTHER DEALINGS IN THE SOFTWARE, WHETHER IN AN
ACTION OF CONTRACT, TORT (INCLUDING NEGLIGENCE), STATUTE OR OTHERWISE, EVEN IF
ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Australian Consumer Law: Nothing in this document excludes, restricts or
modifies any right or remedy, or any guarantee, warranty or other term or
condition, implied or imposed by the Competition and Consumer Act 2010 (Cth)
or any other legislation, that cannot lawfully be excluded or limited. To the
extent such liability can be limited but not excluded, it is limited to the
maximum extent permitted by law. (This project is provided free of charge and
is not supplied in trade or commerce.)


--------------------------------------------------------------------------------
7. INDEMNITY
--------------------------------------------------------------------------------

To the maximum extent permitted by law, by using this code you agree to
indemnify and hold harmless the author and any contributors from and against
any claim, demand, loss, liability, cost or expense (including reasonable
legal fees) arising from or relating to your use, modification or
distribution of the code, your breach of this document, or your breach of any
law, website terms or platform policy.


--------------------------------------------------------------------------------
8. FORKS, COPIES AND MODIFIED VERSIONS
--------------------------------------------------------------------------------

The author is responsible only for the code as published in this original
repository, and only to the limited extent described above. The author is not
responsible for, and has no control over, any fork, copy, modified version,
derivative work or deployment created or operated by anyone else, including
any version changed to run more frequently, to monitor other websites, to
evade blocking or detection, to purchase products automatically, or for any
other purpose.

If you redistribute this code or any modified version of it, you must include
this document unchanged, and you take full responsibility for your version.


--------------------------------------------------------------------------------
9. SECRETS, TOKENS AND CREDENTIALS
--------------------------------------------------------------------------------

Never commit webhook URLs, API tokens, passwords or any other credentials to a
repository. Store them as encrypted secrets (for example, GitHub Actions
secrets) or environment variables. You are solely responsible for protecting
your own credentials and for anything done with them.


--------------------------------------------------------------------------------
10. NO PROFESSIONAL ADVICE
--------------------------------------------------------------------------------

Nothing in this repository, including this document, is legal, financial or
professional advice. If you are unsure whether your intended use is lawful or
permitted, obtain independent legal advice before using this code.


--------------------------------------------------------------------------------
11. FOR WEBSITE OWNERS AND RIGHTS HOLDERS
--------------------------------------------------------------------------------

The author has tried to build these scripts to be light, polite and
respectful of the websites they read. If you operate a website referred to in
this repository and you object to it being monitored, or you believe any part
of this repository infringes your rights or terms, please open an issue in
this repository or contact the repository owner through GitHub. The author
will review the request promptly and, where appropriate, stop monitoring the
website and/or remove the relevant code.


--------------------------------------------------------------------------------
12. CHANGES TO THIS DOCUMENT
--------------------------------------------------------------------------------

This document may be updated at any time without notice. The version in the
repository at the time you use the code applies to that use. Continued use
after an update means you accept the updated version.

If any part of this document is found to be invalid or unenforceable, that
part will be limited or removed to the minimum extent necessary, and the rest
of the document will remain in full effect.


================================================================================
BY USING THIS REPOSITORY YOU ACKNOWLEDGE THAT YOU HAVE READ THIS DOCUMENT IN
FULL AND THAT YOUR USE IS ENTIRELY AT YOUR OWN RISK AND RESPONSIBILITY.
================================================================================
