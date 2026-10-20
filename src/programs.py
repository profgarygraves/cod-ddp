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
       jobs="Graphic designer, brand designer, marketing designer, art director", pay=["graphic", "marketing", "artdir"],
       intro="Graphic designers turn ideas into logos, posters, packaging, ads, publications, and social content. You'll learn the design process from research and sketches to finished work, on the Adobe tools studios use, and you'll leave with a portfolio.",
       transfer_note="Planning a bachelor's degree? The Design Studies AA and the Graphic Design &amp; Marketing AA are built for transfer.",
       pitch="Logos, posters, packaging, ads, and type. Make ideas look like something.",
       start=("DDP 100", "Introduction to Digital Art &amp; Media"),
       awards=["design-studies-aa", "gdm-aa", "graphic-design-ca", "ddp-ca"]),
  dict(key="motion", name="Video, Motion &amp; Animation", color="chia", file="motion.html",
       jobs="Video editor, motion designer, animator, content creator", pay=["animator", "designer"],
       intro="Editors, motion designers, and animators make the video, titles, and characters behind film, social media, games, and advertising. You'll learn Premiere Pro, After Effects, storyboarding, and 3D, then build a reel.",
       pitch="Edit video, animate titles, build 3D characters, and tell stories that move.",
       start=("DDP 120", "Video Post Production"),
       awards=["video-ca", "animation-ca"]),
  dict(key="photo", name="Photography &amp; Drones", color="willow", file="photo.html",
       jobs="Commercial photographer, drone pilot, photo editor", pay=[],
       intro="Photographers and drone operators create images for advertising, real estate, events, publications, and the web. You'll learn the camera, the digital darkroom, commercial lighting and editing, and aerial imaging, from Joshua Tree to the studio.",
       pitch="Shoot, edit, and publish professional images, from studio to sky.",
       start=("DDP 131", "Digital Photography"),
       awards=["photography-ca", "drone-ca"]),
  dict(key="interactive", name="Web, UX &amp; Games", color="cholla", file="interactive.html",
       jobs="UX designer, web designer, front-end developer, game designer", pay=["webdev"],
       intro="UX and web designers make websites and apps that are easy and enjoyable to use. Game designers build playable worlds. You'll learn user research, prototyping, HTML and CSS, and game engines.",
       pitch="Design websites, apps, and games people actually enjoy using.",
       start=("DDP 151", "User Experience Design"),
       awards=["interaction-as", "web-ca", "game-ca"]),
  dict(key="access", name="Accessibility", color="smoketree", file="digital-accessibility.html",
       jobs="Accessibility specialist, assistive technology specialist, document remediation specialist", pay=[],
       intro="Every college, government agency, and large company must make its websites and documents usable by people with disabilities. Accessibility specialists know the law, fix inaccessible content, and match people with assistive technology.",
       pitch="Make digital content work for everyone, and learn the laws behind it.",
       start=("DDP 200", "Accessibility Compliance"),
       awards=["accessibility-ca"]),
  dict(key="software", name="Job-Ready Software Skills", color="white", file="software.html",
       jobs="Adobe Certified skills for any creative or marketing job", pay=[],
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
   desc="Three courses on accessibility law, accessible documents, and assistive technology.",
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
# Careers: BLS Occupational Employment and Wage Statistics, May 2025,
# Riverside-San Bernardino-Ontario metro (includes the Coachella Valley).
# (title, jobs in metro, median hourly, median annual, usually needs a bachelor's)
# ---------------------------------------------------------------------------
JOBS = {
 "graphic":  ("Graphic designers", "1,370", "$31.68", "$65,900", False),
 "marketing": ("Marketing specialists", "5,280", "$33.58", "$69,840", True),
 "webdev":   ("Web developers", "290", "$34.81", "$72,400", False),
 "animator": ("Special effects artists &amp; animators", "40", "$45.88", "$95,420", True),
 "artdir":   ("Art directors", "320", "$50.18", "$104,360", True),
 "designer": ("Designers, all other", "110", "$31.43", "$65,370", False),
}
JOBS_SOURCE = "U.S. Bureau of Labor Statistics, Occupational Employment and Wage Statistics, May 2025, Riverside-San Bernardino-Ontario metro."
