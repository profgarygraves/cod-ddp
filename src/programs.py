# Single source of DDP program data. Every page is built from this file.
# Source: College of the Desert 2026-2027 Catalog, checked October 20, 2026.
#   Awards:  https://catalog.collegeofthedesert.edu/programs/digital-design-production/
#   Courses: https://catalog.collegeofthedesert.edu/courses/ddp/
# Course requirements always link to the official catalog, so the catalog stays the authority.

CAT = "https://catalog.collegeofthedesert.edu/programs/"
COURSES_URL = "https://catalog.collegeofthedesert.edu/courses/ddp/"

ADVISOR = {"name": "Mari Abril", "role": "Program Advisor",
           "email": "mabril@collegeofthedesert.edu", "phone": "760.674.5684"}

# ---------------------------------------------------------------------------
# Creative paths: how students browse. Each award belongs to one path.
# ---------------------------------------------------------------------------
PATHS = [
  dict(key="design", name="Graphic Design &amp; Branding", color="gold", file="design.html",
       jobs="Graphic designer, brand designer, marketing designer, art director", pay=["graphic", "marketing", "industrial", "artdir"],
       intro="Graphic designers turn ideas into logos, posters, packaging, ads, publications, and social content. You'll learn the design process from research and sketches to finished work, on the Adobe tools studios use, and you'll leave with a portfolio.",
       transfer_note="Planning a bachelor's degree? The Design Studies AA and the Graphic Design &amp; Marketing AA are built for transfer.",
       pitch="Logos, posters, packaging, ads, and type. Make ideas look like something.",
       start=("DDP 100", "Introduction to Digital Art &amp; Media"),
       awards=["design-studies-aa", "gdm-aa", "graphic-design-ca", "ddp-ca"]),
  dict(key="motion", name="Video, Motion &amp; Animation", color="chia", file="motion.html",
       jobs="Video editor, motion designer, animator, content creator", pay=["editor", "animator", "producer", "avtech", "camera"],
       intro="Editors, motion designers, and animators make the video, titles, and characters behind film, social media, games, and advertising. You'll learn Premiere Pro, After Effects, storyboarding, and 3D, then build a reel.",
       pitch="Edit video, animate titles, build 3D characters, and tell stories that move.",
       start=("DDP 120", "Video Post Production"),
       awards=["video-ca", "animation-ca"]),
  dict(key="photo", name="Photography &amp; Drones", color="willow", file="photo.html",
       jobs="Commercial photographer, drone pilot, photo editor", pay=["photographer", "mapping", "camera"],
       intro="Photographers and drone operators create images for advertising, real estate, events, publications, and the web. You'll learn the camera, the digital darkroom, commercial lighting and editing, and aerial imaging, from Joshua Tree to the studio.",
       pitch="Shoot, edit, and publish professional images, from studio to sky.",
       start=("DDP 131", "Digital Photography"),
       awards=["photography-ca", "drone-ca"]),
  dict(key="interactive", name="Web, UX &amp; Games", color="cholla", file="interactive.html",
       jobs="UX designer, web designer, front-end developer, game designer", pay=["uxweb", "webdev", "softdev"],
       intro="UX and web designers make websites and apps that are easy and enjoyable to use. Game designers build playable worlds. You'll learn user research, prototyping, HTML and CSS, and game engines.",
       pitch="Design websites, apps, and games people actually enjoy using.",
       start=("DDP 151", "User Experience Design"),
       awards=["interaction-as", "web-ca", "game-ca"]),
  dict(key="access", name="Accessibility", color="smoketree", file="digital-accessibility.html",
       jobs="Accessibility specialist, assistive technology specialist, document remediation specialist", pay=["compliance", "support", "techwriter", "uxweb"],
       unique="The only California community college offering this certificate. Can be completed online.",
       intro="Every college, government agency, and large company must make its websites and documents usable by people with disabilities. Accessibility specialists know the law, fix inaccessible content, and match people with assistive technology.",
       pitch="Make digital content work for everyone, and learn the laws behind it.",
       start=("DDP 200", "Accessibility Compliance"),
       awards=["accessibility-ca"]),
  dict(key="software", name="Job-Ready Software Skills", color="white", file="software.html",
       jobs="Adobe Certified skills for any creative or marketing job", pay=["marketing", "graphic", "avtech", "desktop"],
       intro="Noncredit classes are tuition-free, need no experience, and can be repeated. Each certificate pairs an A class (the basics) with a B class (practice exams and portfolio projects) to prepare you for the Adobe Certified exam.",
       pitch="Tuition-free Adobe classes that prepare you for certification. No experience needed.",
       start=("DDP 301A", "Digital Imaging A (Photoshop)"),
       awards=["ae-cc", "ai-cc", "id-cc", "ps-cc", "pr-cc"]),
]

# kind: AA / AS (associate degree), CA (Certificate of Achievement), CC (noncredit Certificate of Completion)
# units: catalog total. core: DDP courses the award requires (for cross-links). other: non-DDP requirements.
AWARDS = {
 "design-studies-aa": dict(kind="AA", name="Design Studies", units="61", transfer=True,
   url=CAT + "digital-design-production/digital-design-studies-aa/",
   desc="A broad foundation in graphic, UX, and motion design, built to transfer to a four-year design program.",
   core=["100", "110", "151", "111", "112"], choose=(1, ["120", "121", "144"]),
   other=["ARTH C1100", "ARTH C1200", "CIS 087"], ge="Cal-GETC"),
 "gdm-aa": dict(kind="AA", name="Graphic Design &amp; Marketing", units="62-63", transfer=True,
   url=CAT + "digital-design-production/graphic_design_aa/",
   desc="Graphic design plus business and marketing, for designers who want to understand the client side.",
   core=["102", "103", "110", "111", "112", "113", "151", "095A"],
   other=["BUAC 020A or SOC 003", "BUMA 027"], ge="Cal-GETC"),
 "interaction-as": dict(kind="AS", name="Interaction Design", units="60",
   url=CAT + "digital-design-production/interaction-design-as/",
   desc="Web, front-end, and mobile app design, with coding, UX, AI, and accessibility built in.",
   core=["100", "106", "110", "112", "116", "150", "151", "195", "201", "095A"],
   other=["CIS 023A", "CIS 085C", "CIS 087"], ge="COD GE"),

 "graphic-design-ca": dict(kind="CA", name="Graphic Design", units="41.5",
   url=CAT + "digital-design-production/graphic-design-certificate-of-achievement/",
   desc="The full design studio: typography, advertising, packaging, social media, UX, and a portfolio.",
   core=["102", "103", "104", "106", "110", "111", "112", "113", "114", "115", "116", "150", "151", "195", "095A"]),
 "ddp-ca": dict(kind="CA", name="Digital Design &amp; Production", units="24",
   url=CAT + "digital-design-production/digital-design-production-certificate-of-achievement/",
   desc="Core Adobe skills across imaging, illustration, layout, video, motion, and photo. Prepares you for Adobe certification.",
   core=["101", "102", "103", "120", "121", "131"], electives="6 units"),
 "video-ca": dict(kind="CA", name="Video Post-Production", units="30",
   url=CAT + "digital-design-production/video-post-production-certificate-of-achievement/",
   desc="Editing, motion graphics, storyboarding, and 3D, for film, social, and broadcast work.",
   core=["101", "102", "116", "120", "121", "142", "144", "195"], other=["FILM 003", "MUS 078B"]),
 "animation-ca": dict(kind="CA", name="Animation", units="30",
   url=CAT + "digital-design-production/animation-certificate-of-achievement/",
   desc="2D and 3D animation for entertainment, games, advertising, and social media.",
   core=["102", "112", "121", "140", "142", "144", "195"], other=["ART 020A", "ART 005A", "FILM 003"]),
 "photography-ca": dict(kind="CA", name="Photography", units="26.5-30.5",
   url=CAT + "art/applied-photography-certficate/",
   desc="Camera skills, digital darkroom, commercial photography, and the business side of shooting.",
   core=["100", "130", "101", "131", "132", "195", "103", "095A"], other=["ART 030A", "ARTH 033"]),
 "drone-ca": dict(kind="CA", name="Commercial Drone Imaging", units="22.5",
   url=CAT + "digital-design-production-commercial-drone-imaging-certificate-of-achievement",
   desc="Aerial photo and video capture and editing for real estate, construction, mapping, and media.",
   core=["101", "120", "130", "132", "136", "095A"], other=["CJ 001", "CM 001", "GIS 021"]),
 "web-ca": dict(kind="CA", name="Web Design", units="30",
   url=CAT + "digital-design-production/web-design-certificate-of-achievement/",
   desc="Design and build websites, from UX and visuals to HTML, CSS, and Python basics.",
   core=["100", "111", "101", "116", "132", "150", "151", "195"], other=["CIS 082C", "CIS 087"]),
 "game-ca": dict(kind="CA", name="Game Design &amp; Development", units="28",
   url=CAT + "digital-design-production/game-design-certificate-of-achievement/",
   desc="Game history, design, art, animation, and prototyping in real game engines.",
   core=["095A", "140", "142", "144", "151", "160", "161", "162"], other=["CIS 087"], electives="one course"),
 "accessibility-ca": dict(kind="CA", name="Foundations for Accessibility", units="9",
   url=CAT + "digital-design-production/foundations-for-accessibility-certificate-of-achievement/",
   desc="Three courses on accessibility law, accessible documents, and assistive technology. The only certificate of its kind at a California community college, and it can be completed online.",
   unique="Only California community college offering this certificate. Can be completed online.",
   core=["200", "201", "202"]),

 "ps-cc": dict(kind="CC", name="Photoshop Skills", units="0", noncredit=True,
   url=CAT + "digital-design-production/digital-imaging-certificate-of-completion-noncredit/", core=["301A", "301B"]),
 "ai-cc": dict(kind="CC", name="Illustrator Skills", units="0", noncredit=True,
   url=CAT + "digital-design-production/illustrator-skills-certificate-of-completion-noncredit/", core=["302A", "302B"]),
 "id-cc": dict(kind="CC", name="InDesign", units="0", noncredit=True,
   url=CAT + "digital-design-production/indesign-certificate-of-completion-noncredit/", core=["303A", "303B"]),
 "pr-cc": dict(kind="CC", name="Premiere Pro", units="0", noncredit=True,
   url=CAT + "digital-design-production/premier-pro-certificate-of-completion-noncredit/", core=["320A", "320B"]),
 "ae-cc": dict(kind="CC", name="After Effects", units="0", noncredit=True,
   url=CAT + "digital-design-production/after-effects-certificate-of-completion-noncredit/", core=["321A", "321B"]),
}

KIND = {"AA": "Associate in Arts", "AS": "Associate in Science",
        "CA": "Certificate of Achievement", "CC": "Certificate of Completion (noncredit)"}

# ---------------------------------------------------------------------------
# Courses: code -> (title, units, transfer, COD GE area, path, short blurb)
# transfer: "CSU/UC", "CSU", or "" ; noncredit courses have units "0".
# ---------------------------------------------------------------------------
COURSES = {
 "095A": ("Digital Design &amp; Production Work Experience", "1-5", "CSU", "", "career", "Earn units for a design job or internship (54 hours per unit)."),
 "100": ("Introduction to Digital Art &amp; Media", "3", "CSU/UC", "A3", "design", "The open-to-everyone survey: imaging, illustration, layout, animation, 3D, and new tech. C-ID ARTS 250."),
 "101": ("Digital Imaging", "3", "CSU", "", "design", "Photoshop: retouching, compositing, color correction, and output."),
 "102": ("Digital Illustration", "3", "CSU", "", "design", "Illustrator: vector graphics, logos, type, and illustration."),
 "103": ("Publication Design &amp; Production", "3", "CSU", "", "design", "InDesign: multipage print and digital publications, including EPUB."),
 "104": ("Print Production", "1.5", "", "", "design", "Prepare files for professional printing: paper, ink, color, and fonts."),
 "106": ("Generative AI for Creatives", "3", "CSU", "", "design", "Use generative AI for text, images, video, and audio, creatively, legally, and ethically."),
 "110": ("Graphic Design", "3", "CSU/UC", "", "design", "The design process from research and thumbnails to finished comps."),
 "111": ("Advertising Design", "3", "CSU/UC", "", "design", "Type, grids, and campaign systems across formats. Prerequisite: DDP 102."),
 "112": ("Digital Typography", "3", "CSU/UC", "", "design", "Letterforms, type as image, and designing your own typeface."),
 "113": ("Design for Social Change", "3", "CSU/UC", "", "design", "Design as activism: research, prototype, and test a call to action."),
 "114": ("History of Graphic Design", "3", "CSU", "C3", "design", "Movements, pioneers, and the story of posters, branding, and the web."),
 "115": ("Package Design", "3", "CSU", "", "design", "Structural packaging, 3D rendering, sustainability, and print setup."),
 "116": ("Social Media Design", "3", "CSU", "", "design", "Create and evaluate content for social platforms."),
 "120": ("Video Post Production", "3", "CSU", "", "motion", "Premiere Pro: editing picture and sound, formats, and delivery."),
 "121": ("Motion Graphics", "3", "CSU", "", "motion", "After Effects: titles, broadcast design, and visual effects."),
 "128": ("Portfolio Preparation", "1.5", "CSU/UC", "", "career", "Online portfolio, artist statement, CV, and a public student exhibition."),
 "130": ("Digital Darkroom", "1.5", "CSU/UC", "", "photo", "Lightroom-style workflow: import, rank, edit, publish, archive. Bring a DSLR."),
 "131": ("Digital Photography", "3", "CSU/UC", "C3", "photo", "Camera fundamentals, exposure, and preparing images for display. Manual camera required."),
 "132": ("Commercial Photography", "3", "CSU/UC", "", "photo", "Advanced shooting and editing for web, advertising, and print. Prerequisite: DDP 131."),
 "133": ("Nature Photography", "1.5", "CSU", "", "photo", "Field trips to Joshua Tree, The Living Desert, Anza-Borrego, and more."),
 "135": ("Beginning Black &amp; White Photography", "3", "CSU/UC", "", "photo", "Film photography and darkroom fundamentals. 35mm manual camera required."),
 "136": ("Introduction to Drone Imaging", "3", "CSU", "", "photo", "Drone flight practice plus aerial photo and video editing. Not an FAA certification course."),
 "140": ("Character Animation", "3", "CSU/UC", "", "motion", "Timing, weight, acting, and traditional character animation."),
 "142": ("Digital Storyboarding", "3", "CSU", "", "motion", "Visual storytelling for film, games, ads, and animation."),
 "144": ("3D Animation", "3", "CSU/UC", "", "motion", "Modeling, rigging, lighting, rendering, and an individual 3D project."),
 "150": ("Web Design &amp; Development", "3", "CSU", "", "interactive", "Usability, interface, HTML, CSS, and content management systems."),
 "151": ("User Experience Design", "3", "CSU/UC", "", "interactive", "User research, information architecture, prototyping, and usability testing."),
 "160": ("History of Games", "3", "CSU/UC", "", "interactive", "From ancient games to video games; design a non-digital game."),
 "161": ("Introduction to Game Design", "3", "CSU/UC", "", "interactive", "Game theory and working video game prototypes."),
 "162": ("Introduction to Game Development", "3", "CSU/UC", "", "interactive", "2D and 3D game engines, world building, and playtesting."),
 "195": ("Business Practices and Portfolio Preparation for Creatives", "3", "CSU", "", "career", "Freelancing, pricing, clients, contracts, taxes, and your portfolio."),
 "200": ("Accessibility Compliance", "3", "CSU/UC", "", "access", "Accessibility law and standards: Section 504, Section 508, ADA, and WCAG."),
 "201": ("Creating Accessible Content", "3", "CSU", "", "access", "Build and fix accessible Word, PowerPoint, and PDF files."),
 "202": ("Accommodations and Assistive Technology", "3", "CSU", "", "access", "Match assistive technologies to learners and workers."),
 "301A": ("Digital Imaging A", "0", "", "", "software", "Photoshop basics. No experience needed."),
 "301B": ("Digital Imaging B", "0", "", "", "software", "Photoshop practice tests and portfolio projects for Adobe certification."),
 "302A": ("Illustrator A", "0", "", "", "software", "Illustrator basics. No experience needed."),
 "302B": ("Illustrator B", "0", "", "", "software", "Illustrator certification prep and portfolio projects."),
 "303A": ("InDesign A", "0", "", "", "software", "InDesign basics. No experience needed."),
 "303B": ("InDesign B", "0", "", "", "software", "InDesign certification prep and portfolio projects."),
 "320A": ("Premiere Pro A", "0", "", "", "software", "Premiere Pro editing basics. No experience needed."),
 "320B": ("Premiere Pro B", "0", "", "", "software", "Premiere Pro certification prep and portfolio projects."),
 "321A": ("After Effects A", "0", "", "", "software", "After Effects basics. No experience needed."),
 "321B": ("After Effects B", "0", "", "", "software", "After Effects certification prep and portfolio projects."),
 "331": ("Digital Photo for Noncredit", "0", "", "", "software", "Noncredit digital photography fundamentals. Manual camera required."),
}

# ---------------------------------------------------------------------------
# Careers. Pay: BLS Occupational Employment and Wage Statistics (OEWS), May 2025,
# Riverside-San Bernardino-Ontario metro (includes the Coachella Valley); area="CA" means
# BLS does not publish that job for the metro, so the California figure is shown.
# Outlook: BLS Employment Projections 2025-2035 (national): percent change, openings per year
# (thousands), percent self-employed, typical education needed to enter.
# key: (title, jobs in area, median hourly, median yearly, area, growth %, openings k/yr, self-employed %, entry education)
# ---------------------------------------------------------------------------
JOBS = {
 "graphic":    ("Graphic designers", "1,370", "$31.68", "$65,900", "metro", -1.7, 16.0, 20.5, "BA"),
 "marketing":  ("Marketing specialists", "5,280", "$33.58", "$69,840", "metro", 7.0, 82.0, 3.8, "BA"),
 "industrial": ("Commercial &amp; industrial designers (including packaging)", "290", "$38.60", "$80,300", "metro", 2.4, 2.8, 6.5, "BA"),
 "artdir":     ("Art directors", "320", "$50.18", "$104,360", "metro", 4.2, 12.2, 62.1, "BA"),
 "pr":         ("Public relations specialists", "1,470", "$37.03", "$77,010", "metro", 1.8, 23.0, 1.1, "BA"),
 "editor":     ("Film &amp; video editors", "90", "$33.54", "$69,760", "metro", 3.7, 3.1, 35.5, "BA"),
 "animator":   ("Special effects artists &amp; animators", "40", "$45.88", "$95,420", "metro", -0.3, 4.2, 62.9, "BA"),
 "producer":   ("Producers &amp; directors", "470", "$46.81", "$97,360", "metro", 4.0, 12.1, 20.4, "BA"),
 "avtech":     ("Audio &amp; video technicians", "490", "$28.07", "$58,380", "metro", 3.9, 6.6, 10.0, "PS"),
 "camera":     ("Camera operators", "4,700", "$51.39", "$106,900", "CA", 1.3, 2.5, 34.7, "BA"),
 "photographer": ("Photographers", "460", "$21.02", "$43,710", "metro", -0.7, 10.7, 66.7, "HS"),
 "mapping":    ("Surveying &amp; mapping technicians (including drone mapping)", "380", "$34.73", "$72,230", "metro", 5.8, 6.9, 1.1, "HS"),
 "uxweb":      ("Web &amp; digital interface designers (UX/UI)", "27,090", "$65.44", "$136,110", "CA", 6.0, 8.3, 13.3, "BA"),
 "webdev":     ("Web developers", "290", "$34.81", "$72,400", "metro", 3.8, 5.3, 17.5, "BA"),
 "softdev":    ("Software developers (including games and apps)", "4,150", "$64.07", "$133,270", "metro", 10.2, 95.3, 1.5, "BA"),
 "compliance": ("Compliance officers (including accessibility compliance)", "3,480", "$38.42", "$79,920", "metro", 3.8, 32.7, 0.7, "BA"),
 "support":    ("Computer user support specialists", "3,540", "$34.68", "$72,140", "metro", -3.5, 39.7, 2.5, "SC"),
 "techwriter": ("Technical writers", "140", "$41.10", "$85,500", "metro", 0.8, 3.2, 1.0, "BA"),
 "desktop":    ("Desktop publishers", "320", "$34.58", "$71,930", "CA", -14.5, 0.3, 19.8, "AA"),
}
EDU = {"BA": "Bachelor&#39;s degree", "HS": "High school diploma", "PS": "Postsecondary certificate",
       "SC": "Some college", "AA": "Associate degree"}
JOBS_SOURCE = "U.S. Bureau of Labor Statistics: Occupational Employment and Wage Statistics, May 2025, Riverside-San Bernardino-Ontario metro (California where marked); Employment Projections 2025-2035 (national)."

# Career details for each path's Careers section
CAREERS = {
 "design": dict(
   work="Designers plan and build the visual side of a brand: logos, ads, packaging, signs, social posts, publications, and websites. A typical week mixes client meetings, sketching, building files in Adobe tools, and revising work after feedback.",
   ladder=[("Start", "Production artist, junior designer, marketing coordinator"), ("Grow", "Graphic designer, brand designer, packaging designer"), ("Lead", "Senior designer, art director, creative director")],
   employers=["In-house marketing teams at resorts, hotels, and golf clubs", "Advertising and design agencies", "Music festivals, events, and nonprofits", "Print shops, sign makers, and packaging companies", "Cities, colleges, and health systems", "Your own studio or freelance clients"],
   skills=["Photoshop, Illustrator, and InDesign", "Typography, layout, and color", "Brand systems and style guides", "Presenting ideas and taking feedback", "Adobe Certified Professional exams", "A portfolio of finished projects"],
   note="About 1 in 5 graphic designers and 3 in 5 art directors are self-employed."),
 "motion": dict(
   work="Editors, motion designers, and animators shape footage, graphics, and characters into finished video for social media, advertising, film, games, and events. The work moves from storyboards to editing, animation, sound, and delivery.",
   ladder=[("Start", "Production assistant, assistant editor, social video creator"), ("Grow", "Video editor, motion designer, 3D or character animator"), ("Lead", "Senior editor, animation lead, producer or director")],
   employers=["Marketing and social media teams", "Production companies and post-production houses", "Film festivals, music festivals, and live events", "Broadcast and streaming media", "Game and animation studios", "Freelance projects and your own channel"],
   skills=["Premiere Pro and After Effects", "Storyboarding and visual storytelling", "3D modeling, rigging, and animation", "Sound, color, and delivery formats", "Adobe Certified Professional exams", "A demo reel"],
   note="About 1 in 3 film and video editors, and about 3 in 5 animators, are self-employed."),
 "photo": dict(
   work="Photographers and drone operators make images for clients: real estate listings, weddings and events, products, food, and advertising. Drone work adds aerial photo, video, and mapping for real estate, construction, agriculture, and inspections.",
   ladder=[("Start", "Photo assistant, photo editor, event photographer"), ("Grow", "Commercial, real estate, or wedding photographer; licensed drone pilot"), ("Lead", "Studio owner, aerial imaging business, photo director")],
   employers=["Real estate and vacation rental marketing", "Weddings, resorts, and events", "Construction, solar, and agriculture (drone mapping and inspection)", "Advertising, product, and food photography", "News, publishing, and tourism", "Your own photography business"],
   skills=["Camera, exposure, and lighting", "Editing and asset management (digital darkroom)", "Drone flight and aerial imaging", "FAA Part 107 Remote Pilot Certificate: required to fly drones for pay", "Pricing, contracts, and client service (DDP 195)", "A portfolio for each kind of work you want"],
   note="About 2 in 3 photographers are self-employed, so business skills matter as much as camera skills."),
 "interactive": dict(
   work="UX and web designers research what people need, then design and test websites and apps that are easy to use. Game designers plan the rules, worlds, and art that make a game fun. Many roles mix design with front-end code.",
   ladder=[("Start", "UX intern, junior web designer, QA or playtester"), ("Grow", "UX designer, web designer, front-end developer, game designer"), ("Lead", "Senior or lead UX designer, product designer, design manager")],
   employers=["Tech companies and startups, often remote", "Marketing and web agencies", "Colleges, cities, and health systems", "Game studios", "Hospitality and real estate companies", "Freelance web design for local businesses"],
   skills=["User research, wireframes, and prototypes", "HTML, CSS, and Python basics", "Usability testing", "Accessibility (WCAG)", "Game engines and playtesting", "A case-study portfolio"],
   note="UX and web design pay is highest in California's large metros, and many jobs are remote."),
 "access": dict(
   work="Accessibility specialists make sure websites, documents, and courses work for people with disabilities. They test pages, fix inaccessible files, train staff, and match people with assistive technology. Colleges, governments, and large companies are required to do this work.",
   ladder=[("Start", "Accessibility tester, document remediation specialist, alternate media assistant"), ("Grow", "Accessibility specialist or coordinator, assistive technology specialist"), ("Lead", "Accessibility manager, compliance lead, consultant")],
   employers=["Colleges and school districts", "City, county, state, and tribal governments", "Health systems", "Banks, retailers, and tech companies", "Web agencies", "Consulting and freelance remediation"],
   skills=["Section 504, Section 508, ADA, and WCAG", "Accessible Word, PowerPoint, and PDF files", "Screen readers and other assistive technology", "Testing websites for accessibility", "IAAP CPACC certification (optional, widely recognized)", "Clear writing and training others"],
   note="There is no single government job category for accessibility, so the pay data shows the closest related jobs."),
 "software": dict(
   work="Adobe skills are expected in most creative and marketing jobs. These tuition-free classes get you working in the software fast, prepare you for Adobe certification, and give you portfolio pieces you can show employers.",
   ladder=[("Start", "Marketing assistant, production assistant, social media assistant"), ("Grow", "Content creator, production artist, video editor"), ("Lead", "Move into a credit certificate or degree for designer roles")],
   employers=["Small businesses and nonprofits", "Marketing and print shops", "Resorts, hotels, and events", "Schools and community organizations", "Freelance and side projects"],
   skills=["Adobe Certified Professional exams in Photoshop, Illustrator, InDesign, Premiere Pro, and After Effects", "File setup for print, web, and video", "Portfolio projects", "A path into credit DDP courses"],
   note="Desktop publishing on its own is shrinking. Pair software skills with design, video, or marketing for the strongest job prospects."),
}
