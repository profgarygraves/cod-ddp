# Links, navigation, people, and page text for the DDP site.
# COD links were checked October 20, 2026.
from programs import AWARDS, COURSES, JOBS, JOBS_SOURCE, PATHS, ADVISOR, COURSES_URL, KIND

COD = "https://www.collegeofthedesert.edu"
SS = "https://ss.collegeofthedesert.edu/Student/Courses"   # Self-Service class schedule search
SCHEDULE = SS
SCHEDULE_DDP = SS + "/Search?subjects=DDP"                   # every DDP course with open sections
def sched(code): return f"{SS}/Search?keyword=DDP-{code}"      # one course, e.g. DDP-106
def cat_search(code): return f"https://catalog.collegeofthedesert.edu/search/?search=DDP+{code}"
SYLLABI = "https://collegeofthedesert.simplesyllabus.com/en-US/syllabus-library"
CATALOG = "https://catalog.collegeofthedesert.edu/"
REVIEWED = "Fall 2026"

PREVIEW = ('Design preview for faculty review. Not the official site. '
           '<a href="https://github.com/profgarygraves/cod-ddp/issues">Send comments on GitHub</a>.')

TOP_LINKS = [("Apply", COD + "/students/admissions/"), ("Class Schedule", SCHEDULE),
             ("Catalog", CATALOG), ("Financial Aid", COD + "/students/fin-aid/")]

NAV = [("programs", "Programs", "programs.html"), ("start", "Get Started", "get-started.html"),
       ("work", "Student Work", "student-work.html"), ("contact", "Contact", "contact.html")]

# Second-level links shown on the Programs, Course finder, Careers, and Transfer pages
SUBNAV = [("programs.html", "All programs"), ("courses.html", "Course finder"),
          ("careers.html", "Careers &amp; pay"), ("transfer.html", "Transfer")]

L = {  # COD services
 "admissions": COD + "/students/admissions/",
 "noncredit": COD + "/students/admissions/noncredit/",
 "award_app": COD + "/students/admissions/form-degree-application.php",
 "graduation": COD + "/students/admissions/graduation.php",
 "finaid": COD + "/students/fin-aid/",
 "finaid_apply": COD + "/students/fin-aid/applying-for-financial-aid.php",
 "counseling": COD + "/students/counseling/default.php",
 "career": COD + "/students/cwsc/",
 "career_fairs": COD + "/students/cwsc/job-career-fair.php",
 "handshake": "https://collegeofthedesert.joinhandshake.com/login",
 "transfer": COD + "/students/transfer-center/",
 "tutoring": COD + "/students/asc/",
 "library": COD + "/students/library/",
 "dsps": COD + "/students/dsps/",
 "eops": COD + "/students/eops/",
 "veterans": COD + "/students/vet-services/",
 "basic": COD + "/students/basic-needs/",
 "palmsprings": COD + "/students/locations/palm-springs/",
 "a11y": COD + "/accessibility.php",
 "report": COD + "/report-problem.php",
 "entr": "https://catalog.collegeofthedesert.edu/courses/entr/",
 "assist": "https://assist.org/",
 "csusb": "https://www.csusb.edu/",
}

FOOT_LINKS = [
 ("Students", [("Admissions", L["admissions"]), ("Financial Aid", L["finaid"]), ("Counseling", L["counseling"]), ("Student Services", COD + "/students/")]),
 ("About", [("COD Accessibility", L["a11y"]), ("Privacy Policy", COD + "/privacy-policy.php"), ("Directory", COD + "/directory/")]),
]

HOME = dict(
  h1="Turn your creativity into a career.",
  lede="Designers, editors, animators, photographers, and UX designers start here. Choose a career path, take its first class, and build a portfolio employers want to see.",
)

STEPS = [
 ("Apply to COD", "Admission is free. Already a student? Make a DDP program your major.",
  f'Apply online through COD Admissions; there is no application fee. If you already take classes at COD, ask Counseling to update your major so your education plan matches your goal. <a href="{L["admissions"]}">Apply to COD</a>'),
 ("Take a start course", "DDP 100, or the first course on your path. It counts toward your award.",
  'Each career path lists one start course. It counts toward that path&#39;s certificates and degrees, so nothing is wasted while you decide. Not sure which path? Take DDP 100. <a href="programs.html">Compare the programs</a>'),
 ("Plan with the advisor", "Map your semesters with Mari Abril, DDP program advisor, and a counselor.",
  f'Meet with {ADVISOR["name"]}, the DDP program advisor, about classes and portfolios, and with a counselor for a full education plan, including general education and transfer. <a href="{L["counseling"]}">Make a counseling appointment</a>'),
 ("Build and apply", "Finish your portfolio in DDP 195, then apply for your certificate or degree.",
  f'Certificates and degrees are not automatic. Apply in the term you finish your last required course. <a href="{L["award_app"]}">Application for a Degree or Certificate</a>'),
]

PEOPLE = [
 dict(name="Mari Abril", role="Program Advisor, Digital Design &amp; Production", email="mabril@collegeofthedesert.edu", phone="760.674.5684"),
 dict(name="Gary Graves", role="Faculty and student work gallery curator. Teaches DDP 106 Generative AI for Creatives and DDP 195 Business Practices and Portfolio Preparation", email="ggraves@collegeofthedesert.edu", phone=""),
]

def initials(n): return "".join(w[0] for w in n.split()[:2])

def pages(pay_section, course_link):
    out = []
    links = lambda items: '<ul class="links">' + "".join(f'<li><a href="{u}"><b>{t}</b><span>{d}</span></a></li>' for t, d, u in items) + "</ul>"

    # ---------------- Careers ----------------
    rows = "".join(f'<tr><td>{JOBS[k][0]}</td><td>{JOBS[k][2]}</td><td>{JOBS[k][3]}</td><td>{JOBS[k][1]}</td><td>{"Usually" if JOBS[k][4] else "Not always"}</td></tr>'
                   for k in ["graphic", "designer", "marketing", "webdev", "animator", "artdir"])
    path_rows = "".join(f'<li><a href="{p["file"]}"><b>{p["name"]}</b><span>{p["jobs"]}</span></a></li>' for p in PATHS)
    out.append(dict(file="careers.html", section="programs", title="Creative careers",
      lede="What DDP graduates do, what the work pays in the Inland Empire and Coachella Valley, and how to build experience while you study.",
      body=f'''<section><div class="wrap">
  <h2 class="h2">Careers by path</h2>
  <p class="sub">Each career path leads to a set of jobs. Many creative professionals also freelance or run their own studios.</p>
  <ul class="links">{path_rows}</ul>
</div></section>
<section class="pay-wrap"><div class="wrap">
  <h2 class="h2">What creative work pays here</h2>
  <p class="sub">Median pay in the Riverside-San Bernardino-Ontario metro, which includes the Coachella Valley. Half of workers earn more and half earn less.</p>
  <table class="list"><caption class="sr">Median pay for creative jobs</caption>
    <thead><tr><th scope="col">Job</th><th scope="col">Hourly</th><th scope="col">Yearly</th><th scope="col">Jobs in the metro</th><th scope="col">Bachelor&#39;s degree needed?</th></tr></thead>
    <tbody>{rows}</tbody></table>
  <p class="src">Source: {JOBS_SOURCE} Pay for photographers and film and video editors will be added.</p>
</div></section>
<section><div class="wrap">
  <h2 class="h2">Build experience while you study</h2>
  <p class="sub">Employers hire from portfolios. These courses and services help you build one and get it in front of people.</p>
  <ul class="links">
    <li><a href="courses.html#ddp-195"><b>DDP 195: Business Practices and Portfolio Preparation</b><span>Freelancing, pricing, clients, contracts, taxes, and a professional portfolio.</span></a></li>
    <li><a href="courses.html#ddp-128"><b>DDP 128: Portfolio Preparation</b><span>Online portfolio, artist statement, CV, and a public exhibition of student work.</span></a></li>
    <li><a href="courses.html#ddp-095a"><b>DDP 095A: Work Experience</b><span>Earn 1 to 5 units for a design job or internship you already have.</span></a></li>
    <li><a href="{L["handshake"]}"><b>Find jobs and internships on Handshake</b><span>COD&#39;s job board for students and alumni. Sign in with your COD account.</span></a></li>
    <li><a href="{L["career"]}"><b>Career and Workforce Solutions Center</b><span>Career counseling, resumes, assessments, and job and career fairs.</span></a></li>
    <li><a href="{L["entr"]}"><b>Start your own creative business</b><span>Pair DDP with COD&#39;s Entrepreneurship (ENTR) courses.</span></a></li>
  </ul>
</div></section>'''))

    # ---------------- Transfer ----------------
    tr_awards = [k for k, a in AWARDS.items() if a.get("transfer")]
    tr_cards = "".join(f'<li><a href="{a["url"]}"><b>{a["name"]} {a["kind"]}</b><span>{a["desc"]} {a["units"]} units, with {a["ge"]}.</span></a></li>' for a in (AWARDS[k] for k in tr_awards))
    uc = [c for c, v in COURSES.items() if "UC" in v[2]]
    csu = [c for c, v in COURSES.items() if "CSU" in v[2]]
    out.append(dict(file="transfer.html", section="programs", title="Transfer to a four-year school",
      lede="Start your bachelor&#39;s degree in design at COD. Two DDP degrees are built for transfer, and most DDP courses transfer to the CSU.",
      body=f'''<section><div class="wrap">
  <h2 class="h2">Transfer degrees</h2>
  <p class="sub">Both degrees use Cal-GETC, the general education pattern accepted by the CSU and UC.</p>
  <ul class="links">{tr_cards}</ul>
</div></section>
<section class="tight"><div class="wrap prose">
  <h2 class="h2">Courses that transfer</h2>
  <p>{len(csu)} DDP courses transfer to the California State University, and {len(uc)} of them also transfer to the University of California. {course_link("100")} has a C-ID number (ARTS 250), so it counts the same way at many California universities. Use the <a href="courses.html">course finder</a> to filter by CSU or UC.</p>
  <p>Transfer credit is not the same as major credit. Each university decides which courses count toward its design major. Check <a href="{L["assist"]}">ASSIST.org</a>, the official transfer agreement site for California public colleges and universities.</p>
</div></section>
<section class="pay-wrap"><div class="wrap">
  <h2 class="h2">Plan your transfer</h2>
  <ol class="steps v">
    <li><h3>Pick your target schools early</h3><p>Design majors differ a lot from school to school. CSU San Bernardino has a campus in Palm Desert; ask a counselor which programs fit your goals. <a href="{L["csusb"]}">CSU San Bernardino</a></p></li>
    <li><h3>Meet with a counselor</h3><p>Build an education plan that covers your major preparation, Cal-GETC, and admission deadlines. <a href="{L["counseling"]}">Counseling</a></p></li>
    <li><h3>Use the Transfer Center</h3><p>Workshops, university representatives, and application help. <a href="{L["transfer"]}">Transfer Center</a></p></li>
    <li><h3>Build your portfolio</h3><p>Many design programs review portfolios. {course_link("128")} and {course_link("195")} help you prepare one.</p></li>
  </ol>
</div></section>'''))

    # ---------------- Get started ----------------
    steps = "".join(f'<li><h3>{h}</h3><p>{long}</p></li>' for h, short, long in STEPS)
    out.append(dict(file="get-started.html", section="start", title="Get started",
      lede="From your first class to a finished certificate, in four steps. New to college? You belong here.",
      body=f'''<section><div class="wrap">
  <ol class="steps v">{steps}</ol>
</div></section>
<section class="tight"><div class="wrap two">
  <article class="panel-gold"><h3>Want to try it first?</h3><p>Noncredit Adobe classes are tuition-free and need no experience. They use a separate, shorter registration.</p><a href="software.html">Job-ready software skills</a></article>
  <article class="panel-red"><h3>Paying for college</h3><p>Most COD students qualify for help with fees, books, and supplies. Apply every year, as early as you can.</p><a href="{L["finaid_apply"]}">Applying for financial aid</a></article>
</div></section>
<section><div class="wrap">
  <h2 class="h2">Support for every student</h2>
  <p class="sub">Need gear lists, forms, or campus help? See <a href="resources.html">student resources</a>.</p>
  <ul class="links">
    <li><a href="{L["counseling"]}"><b>Counseling</b><span>Education plans, majors, and transfer.</span></a></li>
    <li><a href="{L["tutoring"]}"><b>Tutoring</b><span>The Academic Skills Center offers free tutoring.</span></a></li>
    <li><a href="{L["dsps"]}"><b>Disabled Students Programs &amp; Services</b><span>Accommodations for classes and labs.</span></a></li>
    <li><a href="{L["eops"]}"><b>EOPS &amp; CARE</b><span>Counseling, book help, and more for eligible students.</span></a></li>
    <li><a href="{L["veterans"]}"><b>Veterans Resource Center</b><span>Benefits and support for veterans.</span></a></li>
    <li><a href="{L["basic"]}"><b>Basic needs</b><span>Food, housing, and other support.</span></a></li>
  </ul>
</div></section>'''))

    # ---------------- Resources ----------------
    out.append(dict(file="resources.html", section="start", title="Student resources",
      lede="Gear, software, forms, and help for DDP students.",
      body=f'''<section><div class="wrap">
  <h2 class="h2">Cameras and gear</h2>
  <p class="sub">Some photography courses ask you to bring your own camera. The catalog lists these requirements.</p>
  <table class="list"><caption class="sr">Camera requirements by course</caption>
    <thead><tr><th scope="col">Course</th><th scope="col">What you need</th></tr></thead>
    <tbody>
      <tr><td>{course_link("130")}</td><td>Your own digital SLR (DSLR) camera</td></tr>
      <tr><td>{course_link("131")}</td><td>A digital camera with manual f-stop and shutter speed, and its manual</td></tr>
      <tr><td>{course_link("132")}</td><td>A digital camera (3 megapixels or more); image editing software and a photo printer recommended</td></tr>
      <tr><td>{course_link("133")}</td><td>Your camera and its manual; field trips</td></tr>
      <tr><td>{course_link("135")}</td><td>A 35mm film camera with manual f-stop and shutter speed</td></tr>
      <tr><td>{course_link("136")}</td><td>Drones or drone simulators are provided in class</td></tr>
    </tbody></table>
  <p class="note">Software access: ask your instructor how to get Adobe Creative Cloud for your class. <span class="ph">(Department to confirm lab and license details.)</span></p>
</div></section>
<section class="pay-wrap"><div class="wrap">
  <h2 class="h2">Forms</h2>
  <ul class="links">
    <li><a href="{L["award_app"]}"><b>Application for a Degree or Certificate</b><span>Apply in the term you finish your last course.</span></a></li>
    <li><a href="{L["graduation"]}"><b>Graduation</b><span>Deadlines and commencement.</span></a></li>
    <li><a href="{SYLLABI}"><b>Past syllabi</b><span>Preview any DDP course. Search the library by course code, for example DDP 106.</span></a></li>
    <li><a href="{L["noncredit"]}"><b>Noncredit registration</b><span>For the tuition-free Adobe certificate classes.</span></a></li>
  </ul>
</div></section>
<section><div class="wrap">
  <h2 class="h2">Help on campus</h2>
  <ul class="links">
    <li><a href="contact.html"><b>DDP program advisor</b><span>{ADVISOR["name"]}, {ADVISOR["email"]}</span></a></li>
    <li><a href="{L["counseling"]}"><b>Counseling</b><span>Education plans and transfer.</span></a></li>
    <li><a href="{L["tutoring"]}"><b>Academic Skills Center</b><span>Free tutoring.</span></a></li>
    <li><a href="{L["library"]}"><b>Library</b><span>Research help, study space, and computers.</span></a></li>
    <li><a href="{L["career"]}"><b>Career center</b><span>Resumes, career counseling, and job fairs.</span></a></li>
    <li><a href="{L["handshake"]}"><b>Handshake</b><span>Jobs and internships for COD students.</span></a></li>
    <li><a href="{L["dsps"]}"><b>DSPS</b><span>Accommodations for students with disabilities.</span></a></li>
  </ul>
</div></section>'''))

    # ---------------- Student work ----------------
    pieces = [
     ("background:#A30E22", '<span style="position:absolute;left:8%;bottom:8%;font:600 2.2rem/.9 var(--display);color:#fff">desert<br>x<br>film fest</span><span style="position:absolute;width:60%;aspect-ratio:1;border-radius:50%;background:#FFC423;top:10%;right:-10%"></span>', "Festival poster", "Digital illustration", "111"),
     ("background:linear-gradient(180deg,#f0b38a 0 38%,#d98b6a 38% 52%,#8a6a5a 52% 64%,#3d3a3a 64%)", "", "Joshua Tree, dusk", "Digital photograph", "133"),
     ("background:radial-gradient(circle at 35% 30%,#b8c7d6,#4c6178 60%,#1f2a36)", '<span style="position:absolute;inset:28%;border-radius:50%;background:radial-gradient(circle at 35% 30%,#fff 0 6%,#FFC423 14%,#b5810a 70%)"></span>', "Brass sphere study", "3D render", "144"),
     ("background:#f7f7f7", '<span style="position:absolute;left:9%;right:9%;top:8%;height:36%;background:#103355;border-radius:8px"></span><span style="position:absolute;left:9%;width:50%;top:52%;height:9%;background:#A30E22;border-radius:6px"></span>', "Trail app", "UX prototype", "151"),
     ("background:#141619", '<span style="position:absolute;left:8%;right:8%;top:42%;height:14%;background:repeating-linear-gradient(90deg,#FFC423 0 10%,transparent 10% 14%)"></span>', "Title sequence", "Motion graphics", "121"),
     ("background:#e9e3d6;display:grid;place-items:center", '<span style="font:300 6rem/1 var(--display);color:#103355">Ag</span>', "Mojave Sans", "Original typeface", "112"),
    ]
    figs = "".join(f'<li><figure class="piece"><div class="art" style="{st}" role="img" aria-label="Placeholder for student work: {t}">{inner}<span class="ph-tag">Placeholder</span></div>'
                   f'<figcaption><b>Student name</b><i>{t}</i>, 2026. {m}. {course_link(c)} {COURSES[c][0]}</figcaption></figure></li>' for st, inner, t, m, c in pieces)
    out.append(dict(file="student-work.html", section="work", title="Student work",
      lede="Posters, photographs, animation, apps, and type from DDP classes.",
      body=f'''<section><div class="wrap">
  <p class="note">These are placeholders. Real student work will appear here once students give written permission.</p>
  <ul class="wall">{figs}</ul>
</div></section>
<section class="pay-wrap"><div class="wrap prose">
  <h2 class="h2">Share your work</h2>
  <p>DDP students can submit finished pieces for this gallery. Ask your instructor to nominate a piece, or email the gallery curator, Prof. Gary Graves, at <a href="mailto:ggraves@collegeofthedesert.edu">ggraves@collegeofthedesert.edu</a>. Every piece needs a signed release, and you choose how your name appears.</p>
</div></section>'''))

    # ---------------- Contact ----------------
    people = "".join(f'<li class="person"><span class="ini" aria-hidden="true">{initials(p["name"])}</span><div><h3>{p["name"]}</h3><p class="role">{p["role"]}</p>'
                     + (f'<p><a href="mailto:{p["email"]}">{p["email"]}</a></p>' if p["email"] else "")
                     + (f'<p>{p["phone"]}</p>' if p["phone"] else "") + '</div></li>' for p in PEOPLE)
    out.append(dict(file="contact.html", section="contact", title="Contact and locations",
      lede="Questions about a program, a class, or your portfolio? Start with the program advisor.",
      body=f'''<section><div class="wrap">
  <h2 class="h2">People</h2>
  <ul class="people">{people}</ul>
  <p class="note">More faculty profiles are coming. <span class="ph">(Department to supply the full faculty list.)</span></p>
</div></section>
<section class="pay-wrap"><div class="wrap">
  <h2 class="h2">Where DDP classes meet</h2>
  <ul class="links">
    <li><a href="{COD}/map/"><b>Palm Desert campus</b><span>43-500 Monterey Ave, Palm Desert, CA 92260. Main campus.</span></a></li>
    <li><a href="{L["palmsprings"]}"><b>Palm Springs</b><span>Temporary campus at 1300 E. Baristo Rd. The new Palm Springs campus is planned to open in fall 2027.</span></a></li>
    <li><a href="courses.html"><b>Online</b><span>Many DDP courses are offered online. Check the class schedule each term.</span></a></li>
  </ul>
  <p class="note"><span class="ph">Department office, labs, and hours to confirm.</span></p>
</div></section>
<section><div class="wrap prose">
  <h2 class="h2">College of the Desert</h2>
  <p>43-500 Monterey Ave, Palm Desert, CA 92260<br>760.346.8041<br><a href="{COD}/directory/">Campus directory</a></p>
</div></section>'''))

    # ---------------- Accessibility ----------------
    out.append(dict(file="accessibility.html", section=None, title="Accessibility",
      lede="This site is built so everyone can use it.",
      body=f'''<section><div class="wrap prose">
  <p>The Digital Design &amp; Production website is designed to meet the Web Content Accessibility Guidelines (WCAG) 2.2, Level AA. Every page is checked with automated tests in light and dark modes, at desktop and phone sizes, and by keyboard.</p>
  <ul>
    <li>Text and controls meet color contrast standards in both color themes.</li>
    <li>Every page works with a keyboard, starts with a skip link, and shows where keyboard focus is.</li>
    <li>Pages reflow on small screens and at 200 percent zoom without side scrolling.</li>
    <li>Course filters and the color theme switch work without JavaScript.</li>
  </ul>
  <p>Found a problem? <a href="{L["report"]}">Report it to College of the Desert</a> or email the program advisor at <a href="mailto:{ADVISOR["email"]}">{ADVISOR["email"]}</a>. For accommodations in classes and labs, contact <a href="{L["dsps"]}">Disabled Students Programs &amp; Services</a>.</p>
  <p>Read the <a href="{L["a11y"]}">College of the Desert accessibility statement</a>.</p>
</div></section>'''))
    return out
