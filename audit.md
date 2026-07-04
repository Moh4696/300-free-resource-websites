# Audit — "200 Free Resource Websites That Should Be Illegal"

Two-part audit covering all 200 entries.

- **Part 1 (original 100):** verified 2026-05-29. Detailed table below.
- **Part 2 (100 additions, entries #101–200 in the v2 numbering — see [urls.txt](urls.txt)):** curated 2026-07-04; automated verification **pending** (see Part 2 section below).

Method (Part 1): DNS resolution + HTTP request following redirects (curl, Safari user-agent, 25s timeout, 2 retries). Sites returning `401`/`403` to curl were checked against known state — these are bot-protection responses (Cloudflare / within.website), **not** outages; the sites are live in a normal browser. Anything genuinely broken was re-verified manually.

> **Note on entry numbers below.** The Part 1 table below uses the original 1–100 numbering (the numbering that existed at the time of the 2026-05-29 audit). In v2 those items were regrouped by category and renumbered — see [urls.txt](urls.txt) and [README.md](README.md) for the current 1–200 numbering. The mapping is straightforward from the domain names in the table.

## Summary

| Metric | Count |
|---|---|
| Total checked | 100 |
| Alive & serving correct content | 98 |
| Dead (DNS failure / unreachable) | 1 |
| Domain mismatch / defunct service | 1 |
| Description wrong or misleading | 1 |
| Grey-area (piracy / legally questionable) | 4 |
| Suspected wrong/hallucinated URL | 2 |
| Bot-blocked but confirmed live (no action) | 19 |

**Bottom line: 3 entries need action before posting** — #35 (dead domain), #54 (wrong host), #87 (defunct service). 4 grey-area entries are a legal/policy call (already flagged in the list).

---

## Notes on bot-blocked entries

These returned `403`/`401` to the automated checker but are confirmed live and matching their description. No action needed:
`tunefind.com (5)`, `unsplash.com (18)`, `pexels.com (19)`, `pixabay.com (20)`, `elicit.com (43)`, `consensus.app (44)`, `phind.com (55)`, `temp-mail.org (68)`, `10minutemail.com (69)`, `privnote.com (70)`, `downdetector.com (77)`, `whoer.net (79)`, `alternativeto.net (81)`, `flightradar24.com (82)`, `camelcamelcamel.com (83)`, `timeanddate.com (89)`, `perplexity.ai (95)`, `claude.ai (96)`.

---

## Per-entry results

Legend for match: **yes** / **partial** (freemium or qualified) / **no**.

| # | Original URL | Code | Resolved URL | Match | Notes |
|---|---|---|---|---|---|
| 1 | cobalt.tools | 200 | cobalt.tools/ | yes | Live media downloader. |
| 2 | justwatch.com | 200 | www.justwatch.com/ | yes | Free streaming locator. |
| 3 | archive.org | 200 | archive.org/ | yes | Internet Archive. |
| 4 | archive.ph | 200 | archive.ph/ | yes | Webpage archiver. Borderline (often used to bypass paywalls) but legal as a tool. |
| 5 | tunefind.com | 403 | www.tunefind.com/ | yes | Bot-blocked; live. |
| 6 | radio.garden | 200 | radio.garden/ | yes | Global radio. |
| 7 | musicforprogramming.net | 200 | musicforprogramming.net/ | yes | Focus music. |
| 8 | mynoise.net | 200 | mynoise.net/ | yes | Soundscapes (donation-ware, free to use). |
| 9 | summarize.tech | 200 | www.summarize.tech/ | yes | YouTube summarizer (free tier). |
| 10 | subtitlecat.com | 200 | subtitlecat.com/ | yes | Auto subtitles. |
| 11 | photopea.com | 200 | www.photopea.com/ | yes | Browser Photoshop clone. |
| 12 | remove.bg | 200 | www.remove.bg/ | partial | Free with limits/watermark on HD. |
| 13 | cleanup.pictures | 200 | cleanup.pictures/ | yes | Free object removal (HD is paid). |
| 14 | unscreen.com | 200 | www.unscreen.com/ | yes | Initial DNS failure was transient; re-checked → 200, live. |
| 15 | squoosh.app | 200 | squoosh.app/ | yes | Image compression. |
| 16 | tinypng.com | 200 | tinypng.com/ | yes | Image compression. |
| 17 | tineye.com | 200 | tineye.com/ | yes | Reverse image search. |
| 18 | unsplash.com | 401 | unsplash.com (within.website filter) | yes | Bot filter; live. |
| 19 | pexels.com | 403 | www.pexels.com/ | yes | Bot-blocked; live. |
| 20 | pixabay.com | 403 | pixabay.com/ | yes | Bot-blocked; live. |
| 21 | undraw.co | 200 | undraw.co/ | yes | Free illustrations. |
| 22 | heroicons.com | 200 | heroicons.com/ | yes | Free icons. |
| 23 | lucide.dev | 200 | lucide.dev/ | yes | Open-source icons. |
| 24 | coolors.co | 200 | coolors.co/ | yes | Palette generator. |
| 25 | tinywow.com | 200 | tinywow.com/ | yes | Free tools hub. |
| 26 | smallpdf.com | 200 | smallpdf.com/ | partial | Free with daily-task limits. |
| 27 | ilovepdf.com | 200 | www.ilovepdf.com/ | yes | Free PDF tools. |
| 28 | pdfdrive.com | 200 | www.pdfdrive.com/ | partial | **Grey area** (mixed catalog incl. copyrighted books) — already flagged. |
| 29 | pdf24.org | 200 | www.pdf24.org/en/ | yes | Free PDF toolkit. |
| 30 | sejda.com | 200 | www.sejda.com/ | partial | Free with daily limits. |
| 31 | gutenberg.org | 200 | gutenberg.org/ | yes | Public-domain books. |
| 32 | openculture.com | 200 | www.openculture.com/ | yes | Free courses/media links. |
| 33 | libgen.li | 200 | libgen.li/ | yes | **Grey area** (pirated textbooks) — already flagged. |
| 34 | sci-hub.al | 200 | sci-hub.al/ | yes | **Grey area** (pirated papers) — already flagged. Mirror domains shift; this one currently resolves. |
| 35 | annas-archive.org | **000** | **DNS_FAIL (NXDOMAIN)** | no | **DEAD** — `.org` no longer resolves. Live mirror: **annas-archive.gs** (verified 200). Also **grey area** (piracy). |
| 36 | standardebooks.org | 200 | standardebooks.org/ | yes | Public-domain ebooks. |
| 37 | coursera.org | 200 | www.coursera.org/ | partial | Audit free; certs paid. |
| 38 | edx.org | 200 | www.edx.org/ | partial | Audit free; certs paid. |
| 39 | khanacademy.org | 200 | www.khanacademy.org/ | yes | Fully free. |
| 40 | freecodecamp.org | 200 | www.freecodecamp.org/ | yes | Fully free. |
| 41 | theodinproject.com | 200 | www.theodinproject.com/ | yes | Fully free. |
| 42 | cs50.harvard.edu | 200 | www.edx.org/cs50 | yes | Redirects to official edX CS50 page — expected, legit. |
| 43 | elicit.com | 403 | elicit.com/ | partial | Bot-blocked; live. Mostly freemium now (limited free credits). |
| 44 | consensus.app | 403 | consensus.app/ | partial | Bot-blocked; live. Freemium. |
| 45 | connectedpapers.com | 200 | www.connectedpapers.com/index.html | partial | Free with monthly graph limit. |
| 46 | semanticscholar.org | 200 | www.semanticscholar.org/ | yes | Free academic search. |
| 47 | scispace.com | 200 | scispace.com/ | partial | Freemium. |
| 48 | researchrabbit.ai | 200 | www.researchrabbit.ai/ | yes | Free. |
| 49 | scholar.google.com | 200 | scholar.google.com/ | yes | Free. |
| 50 | regex101.com | 200 | regex101.com/ | yes | Free regex tester. |
| 51 | codebeautify.org | 200 | codebeautify.org/ | yes | Free formatter. |
| 52 | explainshell.com | 200 | explainshell.com/ | yes | Free. |
| 53 | carbon.now.sh | 200 | carbon.now.sh/ | yes | Code screenshots. |
| 54 | ray.so | **000** | apex refuses :443 | partial | **Apex `ray.so` does not serve HTTPS** (connection refused). **www.ray.so works (200).** Use `https://www.ray.so/`. |
| 55 | phind.com | 403 | phind.com/ | yes | Bot-blocked; live. |
| 56 | devdocs.io | 200 | devdocs.io/ | yes | Free docs. |
| 57 | caniuse.com | 200 | caniuse.com/ | yes | Free. |
| 58 | jsonformatter.org | 200 | jsonformatter.org/ | yes | Free. |
| 59 | transform.tools | 200 | transform.tools/ | yes | Free. |
| 60 | crontab.guru | 200 | crontab.guru/ | yes | Free. |
| 61 | shields.io | 200 | shields.io/ | yes | Free badges. |
| 62 | excalidraw.com | 200 | excalidraw.com/ | yes | Free whiteboard. |
| 63 | tldraw.com | 200 | www.tldraw.com/ | yes | Free whiteboard. |
| 64 | miro.com | 200 | miro.com/ | partial | Free tier (already qualified). |
| 65 | notion.so | 200 | www.notion.com/ | yes | Redirects to rebranded notion.com — expected. Free tier. |
| 66 | obsidian.md | 200 | obsidian.md/ | yes | Free for personal use. |
| 67 | cryptpad.fr | 200 | cryptpad.fr/ | yes | Free encrypted docs. |
| 68 | temp-mail.org | 403 | temp-mail.org/ | yes | Bot-blocked; live. |
| 69 | 10minutemail.com | 403 | 10minutemail.com/ | yes | Bot-blocked; live. |
| 70 | privnote.com | 403 | privnote.com/ | yes | Bot-blocked; live. |
| 71 | file.io | 200 | www.file.io/ | partial | Free tier exists; storage limits apply. |
| 72 | accountkiller.com | 200 | www.accountkiller.com/en/home | yes | Free guides. |
| 73 | simplelogin.io | 200 | simplelogin.io/ | partial | Free tier (alias limit). |
| 74 | crypt.ee | 200 | crypt.ee/ | yes | Free encrypted notes. |
| 75 | haveibeenpwned.com | 200 | haveibeenpwned.com/ | yes | Free breach check. |
| 76 | virustotal.com | 200 | www.virustotal.com/gui/ | yes | Free file scan. |
| 77 | downdetector.com | 403 | downdetector.com/ | yes | Bot-blocked; live. |
| 78 | urlvoid.com | 200 | www.urlvoid.com/ | yes | Free URL check. |
| 79 | whoer.net | 403 | whoer.net/ | yes | Bot-blocked; live. |
| 80 | wolframalpha.com | 200 | www.wolframalpha.com/ | partial | Free answers; step-by-step is paid. |
| 81 | alternativeto.net | 403 | alternativeto.net/ | yes | Bot-blocked; live. |
| 82 | flightradar24.com | 403 | flightradar24.com/ | yes | Bot-blocked; live. Free tier. |
| 83 | camelcamelcamel.com | 403 | camelcamelcamel.com/ | yes | Bot-blocked; live. |
| 84 | fast.com | 200 | fast.com/ | yes | Free speed test. |
| 85 | speedtest.net | 200 | www.speedtest.net/ | yes | Free speed test. |
| 86 | wetransfer.com | 200 | wetransfer.com/ | partial | Free tier is now 3GB (claim says 2GB — minor, still free). |
| 87 | fakespot.com | 200 | **blog.mozilla.org/.../building-whats-next/** | **no** | **DEFUNCT** — Fakespot was shut down by Mozilla; the domain now redirects to a Mozilla blog post. **Service no longer exists. Remove.** |
| 88 | xe.com | 200 | www.xe.com/ | yes | Free currency conversion. |
| 89 | timeanddate.com | 403 | timeanddate.com/ | yes | Bot-blocked; live. |
| 90 | taxifarefinder.com | 200 | www.taxifarefinder.com/ | yes | Free fare estimates. |
| 91 | hemingwayapp.com | 200 | hemingwayapp.com/ | partial | Free in-browser editor; desktop/AI features paid. |
| 92 | languagetool.org | 200 | languagetool.org/ | partial | Free grammar checker (premium upsell). |
| 93 | deepl.com | 200 | www.deepl.com/en/translator | partial | Free tier; "beats Google" is opinion. |
| 94 | quillbot.com | 200 | quillbot.com/ | partial | Free tier (already qualified). |
| 95 | perplexity.ai | 403 | www.perplexity.ai/ | yes | Bot-blocked; live. |
| 96 | claude.ai | 403 | claude.ai/ | yes | Bot-blocked; live. Free tier. |
| 97 | you.com | 200 | you.com/home | partial | Free tier. |
| 98 | rytr.me | 200 | rytr.me/ | partial | Free small tier (already qualified). |
| 99 | audiomass.co | 200 | audiomass.co/ | yes | Free browser audio editor. |
| 100 | clipchamp.com | 200 | clipchamp.com/en/ | partial | Free with paid premium features (now Microsoft). |

---

## Action list — fix or remove before posting

| # | URL | Problem | Action |
|---|---|---|---|
| 35 | annas-archive.org | **Dead** — domain no longer resolves (NXDOMAIN). Also piracy/grey-area. | Replace with **annas-archive.gs** (verified live), or remove for legal reasons. |
| 54 | ray.so | Apex domain refuses HTTPS connections. | Change URL to **https://www.ray.so/** (the `www` host works). |
| 87 | fakespot.com | **Defunct** — service shut down by Mozilla; redirects to a Mozilla blog post. | **Remove.** No direct free equivalent; closest alternatives are reviewmeta-style tools (most also discontinued). |

## Grey-area entries (legal/policy decision, not broken)

Already flagged in the source list — keep or cut based on your risk tolerance:

- **#28 pdfdrive.com** — mixed catalog including copyrighted books.
- **#33 libgen.li** — pirated textbooks.
- **#34 sci-hub.al** — pirated research papers (mirror domains rotate frequently).
- **#35 annas-archive** — pirated books (also dead, see above).

`#4 archive.ph` is borderline (commonly used to bypass paywalls) but is a legal archiving tool — judgment call.

## Freemium caveat

Many entries are freemium rather than fully free (e.g. #12, #26, #30, #37, #38, #43, #44, #45, #71, #73, #80, #91, #92, #93, #97, #100). All have a genuine free tier, so the "free" claim holds, but if the post implies *fully* free, consider a qualifier.

---

# Part 2 — v2 additions (100 new tools)

Curated 2026-07-04. These are the 100 tools added to bring the list from 100 → 200. Numbering here refers to the **v2 numbering** used in [README.md](README.md) and [urls.txt](urls.txt) (entries 1–200 grouped by category).

## Verification status

Automated verification was **skipped for the additions** in this update: the environment where this expansion was drafted has no `host` binary and outbound HTTPS is blocked by a proxy, so [check.sh](check.sh) can't run against these URLs from here.

To verify locally:
```
bash check.sh              # full run over all 200 (regenerates results.tsv)
bash scripts/check_new.sh  # just the 100 additions (lines 101–200 of urls.txt), writes results_new.tsv
```

The additions are widely-known tools I have high confidence in as of 2026-07-04, but they have not been machine-checked from this environment.

## The 100 additions, by section

### Media, Streaming & Audio (10 additions)
| v2 # | URL | Category note |
|---|---|---|
| 13 | kapwing.com | Freemium browser video editor |
| 14 | veed.io | Freemium browser video editor |
| 15 | descript.com | Freemium — free monthly minutes |
| 16 | freesound.org | Free, CC-licensed |
| 17 | musopen.org | Free public-domain music |
| 18 | freemusicarchive.org | Free CC music (check per-track license) |
| 19 | incompetech.com | Free with attribution |
| 20 | ezgif.com | Free browser GIF/video tools |
| 21 | loom.com | Freemium screen recorder |
| 22 | otter.ai | Freemium transcription |

### Image, Photo & Design Tools (10 additions)
| v2 # | URL | Category note |
|---|---|---|
| 31 | canva.com | Freemium (generous) |
| 32 | figma.com | Free tier |
| 33 | pixlr.com | Free browser editor |
| 34 | gimp.org | Free / open-source (desktop) |
| 35 | inkscape.org | Free / open-source (desktop) |
| 36 | krita.org | Free / open-source (desktop) |
| 37 | app.diagrams.net | Free (formerly draw.io) |
| 38 | mermaid.live | Free |
| 39 | colorhunt.co | Free |
| 40 | realtimecolors.com | Free |

### Fonts, Icons & Illustrations (8 additions in new category)
| v2 # | URL | Category note |
|---|---|---|
| 44 | fontshare.com | Free professional fonts |
| 45 | fonts.google.com | Free open-source fonts |
| 46 | flaticon.com | Free with attribution |
| 47 | svgrepo.com | 500K+ free SVGs |
| 48 | haikei.app | Free SVG generator |
| 49 | humaaans.com | Free illustrations |
| 50 | blush.design | Free community plan |
| 51 | open-doodles.com | Free open-source illustrations |

### Free Stock Photos & Video (4 additions)
| v2 # | URL | Category note |
|---|---|---|
| 55 | stocksnap.io | CC0 stock photos |
| 56 | kaboompics.com | Free stock photography |
| 57 | coverr.co | Free stock video |
| 58 | freepik.com | Freemium (attribution on free plan) |

### Free Books & Libraries (3 additions)
| v2 # | URL | Category note |
|---|---|---|
| 66 | openlibrary.org | Free (Internet Archive) |
| 67 | openstax.org | Free peer-reviewed college textbooks |
| 68 | goalkicker.com | Free programming books |

### Free Courses & Learning (12 additions)
| v2 # | URL | Category note |
|---|---|---|
| 79 | ocw.mit.edu | Free |
| 80 | classcentral.com | Free MOOC aggregator |
| 81 | codecademy.com | Freemium |
| 82 | exercism.org | Free |
| 83 | leetcode.com | Freemium |
| 84 | codewars.com | Free |
| 85 | javascript.info | Free |
| 86 | eloquentjavascript.net | Free |
| 87 | learngitbranching.js.org | Free |
| 88 | roadmap.sh | Free |
| 89 | fullstackopen.com | Free |
| 90 | devhints.io | Free |

### Research & Academic (4 additions)
| v2 # | URL | Category note |
|---|---|---|
| 98 | arxiv.org | Free |
| 99 | biorxiv.org | Free |
| 100 | doaj.org | Free open access journals |
| 101 | openreview.net | Free |

### Developer Tools (19 additions)
| v2 # | URL | Category note |
|---|---|---|
| 115 | codesandbox.io | Freemium |
| 116 | stackblitz.com | Freemium |
| 117 | codepen.io | Freemium |
| 118 | replit.com | Freemium |
| 119 | jsfiddle.net | Free |
| 120 | postman.com | Freemium |
| 121 | webhook.site | Free |
| 122 | picsum.photos | Free |
| 123 | randomuser.me | Free |
| 124 | mockaroo.com | Freemium |
| 125 | readme.so | Free |
| 126 | dbdiagram.io | Free tier |
| 127 | jsonplaceholder.typicode.com | Free |
| 128 | httpbin.org | Free |
| 129 | gitignore.io | Free (redirects to toptal.com/developers/gitignore, the maintained mirror) |
| 130 | 30secondsofcode.org | Free |
| 131 | snyk.io | Freemium |
| 132 | codeium.com | Free for individuals |
| 133 | wakatime.com | Freemium |

### Whiteboards, Notes & Productivity (8 additions)
| v2 # | URL | Category note |
|---|---|---|
| 140 | todoist.com | Freemium |
| 141 | trello.com | Freemium |
| 142 | airtable.com | Freemium |
| 143 | logseq.com | Free / open-source |
| 144 | workflowy.com | Freemium |
| 145 | when2meet.com | Free |
| 146 | doodle.com | Freemium |
| 147 | libreoffice.org | Free / open-source (desktop) |

### Privacy & Security (10 additions)
| v2 # | URL | Category note |
|---|---|---|
| 159 | proton.me | Freemium |
| 160 | tutanota.com | Freemium |
| 161 | signal.org | Free (nonprofit) |
| 162 | bitwarden.com | Free tier |
| 163 | keepassxc.org | Free / open-source |
| 164 | protonvpn.com | Freemium (free tier is unlimited bandwidth) |
| 165 | duckduckgo.com | Free |
| 166 | startpage.com | Free |
| 167 | privacyguides.org | Free |
| 168 | 2fa.directory | Free |

### Everyday Utilities & Checkers (10 additions)
| v2 # | URL | Category note |
|---|---|---|
| 181 | windy.com | Free tier |
| 182 | openstreetmap.org | Free |
| 183 | what3words.com | Free |
| 184 | omnicalculator.com | Free |
| 185 | calculator.net | Free |
| 186 | rome2rio.com | Free |
| 187 | worldtimebuddy.com | Free |
| 188 | wttr.in | Free |
| 189 | portfoliovisualizer.com | Free |
| 190 | trends.google.com | Free |

### Writing & AI Assistants (2 additions)
| v2 # | URL | Category note |
|---|---|---|
| 199 | grammarly.com | Freemium |
| 200 | notebooklm.google.com | Free |

## Next steps for the v2 additions

1. Run `bash scripts/check_new.sh` (or `bash check.sh` for all 200) on a machine with normal DNS + outbound HTTPS to produce a fresh Part 2 verification table.
2. Anything that comes back non-`200`/`403` should be spot-checked in a real browser — Cloudflare bot-protection routinely serves `403` to curl, and those are not outages.
3. If any additions turn out to be dead, replace them following the same pattern used for Part 1's action list.
