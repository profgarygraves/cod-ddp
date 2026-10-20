# Digital Design & Production Website (College of the Desert)

A student-focused departmental website for the Digital Design & Production (DDP) department at College of the Desert. It is modeled on the [Fullerton College Business & CIS site](https://profgarygraves.github.io/buscis-2026-website/), but rebuilt for a creative department.

**Design review:** https://profgarygraves.github.io/cod-ddp/

This preview is for faculty review. It is not the official site.

## Status

| Phase | What | Status |
|---|---|---|
| 1 | Content inventory from the 2026-2027 catalog (`src/programs.py`) | Done, needs faculty check |
| 2 | Homepage design directions (`docs/mockups/`) | **Pick one** |
| 3 | Homepage and program pages | Next |
| 4 | Course finder, careers, transfer, student resources | |
| 5 | Spanish version, accessibility audit, faculty review | |
| 6 | Handoff to COD hosting | |

Open questions and facts to confirm are in [CHECKLIST.md](CHECKLIST.md).

## How to give feedback

- **Email** Prof. Gary Graves with the page name and what to change.
- **GitHub users:** [open an issue](https://github.com/profgarygraves/cod-ddp/issues) for each page or topic.

## How the site is built

Content lives in data files, so most updates are a one-line edit. Course requirements always link to the official COD catalog, so the catalog stays the authority.

| File | What it holds |
|---|---|
| `src/programs.py` | Six creative paths, 17 awards, 46 DDP courses, advisor, and local career pay data |
| `docs/` | Published preview (GitHub Pages serves this folder) |
| `docs/fonts/` | Self-hosted Jost and Roboto (open licenses included) |

## Design principles

- **Brand:** COD Roadrunner red `#A30E22` and gold `#FFC423` from collegeofthedesert.edu. COD's Campus Standards Handbook names Neutraface as the campus typeface, so headings use Jost, a free geometric face in the same mid-century spirit. Licensed Neutraface webfonts can replace it later. Body text is Roboto, matching collegeofthedesert.edu.
- **Student first:** organized by what students want to make, not by catalog structure. Every path has a start course.
- **Low maintenance:** no news feed. Requirements link to the catalog, and class links go to the live schedule.
- **Accessible:** WCAG 2.2 AA, light and dark modes, phone layouts. Checked with axe-core.
- **Plain HTML and CSS:** no framework and no build step on the live server.
