# Open items

Last updated: October 20, 2026. Check items off as they are confirmed.

## Final audit (October 20, before review)
- [x] Faculty filter uses each course's home program (catalog); filter buttons only for programs with 2026 instructors
- [x] All 34 pages: internal links and anchors, HTML validation, one h1 and no skipped headings, image alt text
- [x] External links: 66 catalog pages and course searches, 23 COD pages, Self-Service, Simple Syllabus, Handshake (checked in Chrome)
- [x] axe-core WCAG 2.2 AA: light, dark, and both forced themes, desktop and phone
- [x] No sideways scrolling at 320, 768, 1024, and 1920 px, and with WCAG text-spacing overrides at 320 px
- [x] Keyboard: skip link first on every page; visible focus on every stop; filters work with arrow keys
- [x] Touch targets 24 px or larger; reduced motion honored; filters and theme switch work with JavaScript off
- [ ] Still worth doing by a person: a screen reader pass (VoiceOver or NVDA) and a real-phone check

## Decisions for Gary
- [x] Faculty & Staff and Contact combined into one page, "Faculty, Staff & Contact" (contact.html); faculty.html forwards there (October 20)
- [x] Web gallery is named the "DDP Online Gallery"; Gary is listed for "Submit student work for the DDP Online Gallery" (October 20)
- [x] Navigation simplified (October 20): Programs, Get Started, Student Work, Contact. Course finder, Careers, and Transfer live under Programs; each program page has its own Courses, Careers, and Transfer sections.
- [x] Program titles in Title Case (October 20)
- [x] Homepage direction: C, Creative Careers (red and gold frame, desert-bloom path colors, light/dark switch). Chosen October 20.
- [ ] Where the site will live: GitHub Pages linked from COD, or ported into COD's website system (OmniUpdate)
- [ ] COD brand guide from the Public Information Office (logo files, official colors, web typeface). The Campus Standards Handbook (2005) covers signage only: Neutraface type, desert-flora color coding.
- [ ] Use the official COD logo image in the header? The mockups use a text wordmark for now.

## Facts to confirm (2026-2027 catalog, checked October 20)
- [ ] The DDP AS degree is no longer in the 2026-2027 catalog. The college's pathway page still lists it, plus the old Digital Design Studies name. Confirm it was retired.
- [ ] 17 current awards. Degrees: Design Studies AA, Graphic Design & Marketing AA, Interaction Design AS. Certificates of Achievement: Animation, Commercial Drone Imaging, Digital Design & Production, Foundations for Accessibility, Game Design & Development, Graphic Design, Photography, Video Post-Production, Web Design. Noncredit Certificates of Completion: After Effects, Illustrator Skills, InDesign, Photoshop Skills, Premiere Pro.
- [ ] Six creative paths and their start courses: DDP 100 (design), DDP 120 (video and animation), DDP 131 (photography and drone), DDP 151 (web, UX, games), DDP 200 (accessibility), DDP 301A (noncredit software)
- [ ] Design Studies AA transfer target. The older catalog named CSU San Bernardino; the 2026-2027 text says "transfer and career preparation" without naming a campus.
- [ ] Photography certificate lives under Art in the catalog. Keep it on the DDP site?
- [ ] Catalog spells "Premier Pro" in the certificate name. The website uses Premiere Pro, Adobe's spelling.
- [ ] Noncredit classes are free and repeatable (catalog: "Repeatable: Yes"). Confirm the "free" claim with the noncredit office.

## Site content to confirm (October 20 build)
- [ ] **KSAs (Knowledge, Skills, Abilities) for all 17 programs** in `src/ksa.py`: drafted from catalog course descriptions and learning outcomes. Faculty in each area should review and edit.
- [ ] Encouragement band claims: start courses have no prerequisite (catalog: DDP 100, 120, 131, 151, 200, 301A); most 3-unit DDP courses include 54 lab hours (catalog)
- [x] Foundations for Accessibility: the only certificate of its kind at a California community college, and can be completed online (stated by Gary, October 20). Featured on the homepage tile, Programs page, Accessibility page, and certificate card. Keep a source on file (for example, a Chancellor's Office program inventory search) in case anyone asks.
- [ ] Career titles listed for each path
- [ ] "Noncredit classes are tuition-free" (California noncredit has no enrollment fee; confirm wording with the noncredit office)
- [ ] Software access for students: Adobe Creative Cloud licenses and lab hours (placeholder on Student Resources)
- [x] Gary Graves: ggraves@collegeofthedesert.edu, on Contact and as student work gallery curator (October 20)
- [x] Spanish version of every page (October 20): docs/es/, linked with hreflang and an English/Español switch
- [ ] Spanish review by a fluent speaker: src/programs_es.py, src/ksa_es.py, src/site_data_es.py, and the Spanish strings in build.py. Word choices to check: "título" (degree), "licenciatura" (bachelor's), "colegiatura" (tuition), "sin crédito" (noncredit), "prácticas" (internships), "asesora del programa", office names kept in English with a Spanish note

## Links added October 20 (from Gary)
- [x] Class schedule: Self-Service search. Each course links to its own search (keyword=DDP-106); all DDP classes use subjects=DDP
- [x] Counseling: /students/counseling/default.php
- [x] Catalog search per course (catalog.collegeofthedesert.edu/search/?search=DDP+106)
- [x] Syllabus library (Simple Syllabus). Its search is not in the URL, so pages link to the library and tell students to search by course code
- [ ] Ask COD web staff to replace or redirect the old DDP page (still lists Flash and ActionScript): collegeofthedesert.edu/students/acad-prog/social-science-art/arts/digital-design-and-production.php

## People and places
- [ ] Program advisor: Mari Abril, mabril@collegeofthedesert.edu, 760.674.5684 (from the 2026-2027 catalog)
- [x] Faculty & Staff page (October 20): 19 instructors from the Spring, Summer, and Fall 2026 class schedule; titles and emails from the COD directory; Dean Vanessa Fountain, Chair Dr. Mari Abril, and Tina Gonzalez from the School of Social Sciences and Arts page
- [x] Headshots added for Vanessa Fountain, Gary Graves, Kent Kay, Kerri Seichter (AI-edited drafts, published at Gary's direction, October 20)
- [ ] Headshots for the other faculty and staff (600x750, docs/img/people/first-last.jpg) and LinkedIn links (src/people.py LINKEDIN; Graves, Abril, Kay, Fountain added October 20)
- [x] Kent Kay listed as Adjunct Faculty (Gary, October 20; directory said "Faculty, Film and Media Studies")
- [ ] Directory lists Roxanne Brazell, Tina Cleveland-Gorges, Jonathan Gorges, and Jaime Lilly as "Instructor". Confirm: Adjunct Faculty, or full-time?
- [ ] Confirm faculty who taught only in Spring or Summer 2026 should stay listed: Aaron Baldon, John Goodwin, Kent Kay, Jonathan Gorges
- [ ] Denise Ferraccioli's directory email is dreilley@collegeofthedesert.edu; confirm
- [ ] Department office, labs, and campus locations (Palm Desert, Palm Springs temporary campus)
- [ ] Counselors who work with DDP students
- [ ] Department social media accounts

## Content to gather
- [ ] 10-20 pieces of student work with signed releases. Add each to src/work.py and docs/img/work/ (instructions at the top of work.py)
- [ ] Pay data for photographers and film and video editors (BLS request limit reached October 20; add next pass)
- [ ] Palm Springs campus: link to an official COD campus page when one exists
- [ ] Software access for students (Adobe Creative Cloud licenses, lab hours)
- [ ] Camera requirements: DDP 130 and 133 need a DSLR; DDP 131 needs manual f-stop and shutter; DDP 135 needs a 35mm film camera
