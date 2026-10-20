#!/usr/bin/env python3
"""Build the DDP website preview into docs/ from the data in src/.

    python3 build.py

Content lives in src/programs.py (paths, awards, courses, careers) and src/site.py (links, people, page text).
"""
import os, re, shutil, sys
ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ROOT, "src"))
from programs import PATHS, AWARDS, KIND, COURSES, JOBS, JOBS_SOURCE, ADVISOR, COURSES_URL, CAREERS, EDU
import site_data as S

OUT = os.path.join(ROOT, "docs")
PBY = {p["key"]: p for p in PATHS}
AWARD_PATH = {a: p["key"] for p in PATHS for a in p["awards"]}

def esc_attr(s): return s.replace('"', "&quot;")
def strip(s): return re.sub(r"<[^>]+>", "", s).replace("&amp;", "&")

def ddp(code):  return f"DDP {code}"
def cid(code):  return "ddp-" + code.lower()
def course_link(code, prefix=""):
    return f'<a href="{prefix}courses.html#{cid(code)}">{ddp(code)}</a>'

def course_paths(code):
    """Primary path plus every path whose awards require the course."""
    ps = [COURSES[code][4]]
    for k, a in AWARDS.items():
        if code in a["core"] or code in a.get("choose", (0, []))[1]:
            ps.append(AWARD_PATH[k])
    return list(dict.fromkeys(ps))

def awards_using(code):
    return [k for k, a in AWARDS.items() if code in a["core"] or code in a.get("choose", (0, []))[1]]

FLOWER = '<svg class="flower" aria-hidden="true"><use href="#fl"/></svg>'
SPRITE = ('<svg width="0" height="0" style="position:absolute" aria-hidden="true"><symbol id="fl" viewBox="0 0 44 44">'
          '<g fill="currentColor" opacity=".45"><circle cx="22" cy="10" r="8"/><circle cx="34" cy="22" r="8"/><circle cx="22" cy="34" r="8"/>'
          '<circle cx="10" cy="22" r="8"/></g><circle cx="22" cy="22" r="6" fill="currentColor"/></symbol></svg>')

THEME = '''<fieldset class="theme">
        <legend>Color theme</legend>
        <input type="radio" name="theme" id="th-auto" value="auto" checked><label for="th-auto" title="Match my device"><svg width="16" height="16" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="M12 3.5a8.5 8.5 0 0 1 0 17z" fill="currentColor"/></svg><span class="sr">Match my device</span></label>
        <input type="radio" name="theme" id="th-light" value="light"><label for="th-light" title="Light"><svg width="16" height="16" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg><span class="sr">Light</span></label>
        <input type="radio" name="theme" id="th-dark" value="dark"><label for="th-dark" title="Dark"><svg width="16" height="16" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8.5 8.5 0 0 1 9.5 4a8.5 8.5 0 1 0 10.5 10.5z" fill="currentColor"/></svg><span class="sr">Dark</span></label>
      </fieldset>
      <script>(function(){var k="codddp-theme";try{var v=localStorage.getItem(k);if(v){var r=document.getElementById("th-"+v);if(r)r.checked=true;}}catch(e){}document.addEventListener("change",function(e){if(e.target&&e.target.name==="theme"){try{localStorage.setItem(k,e.target.value);}catch(x){}}});})();</script>'''

MARK = ('<svg class="mark" viewBox="0 0 44 44" aria-hidden="true"><g fill="currentColor"><circle cx="22" cy="10" r="8"/>'
        '<circle cx="34" cy="22" r="8"/><circle cx="22" cy="34" r="8"/><circle cx="10" cy="22" r="8"/></g><circle class="c" cx="22" cy="22" r="6"/></svg>')

def header(section):
    nav = "".join(
        f'<li><a href="{href}"{" aria-current=\"page\"" if key == section else ""}>{label}</a></li>'
        for key, label, href in S.NAV)
    top = "".join(f'<li><a href="{u}">{t}</a></li>' for t, u in S.TOP_LINKS)
    return f'''<header>
  <div class="college"><div class="wrap">
    <a class="cod" href="{S.COD}/">College of the Desert</a>
    <div class="tools">
      <ul>{top}</ul>
      {THEME}
    </div>
  </div></div>
  <div class="dept"><div class="wrap">
    <a class="name" href="index.html">{MARK}Digital Design &amp; Production</a>
    <nav aria-label="Department"><ul>{nav}</ul></nav>
  </div></div>
</header>'''

def footer():
    cols = "".join(f'<div><h2>{h}</h2><ul>' + "".join(f'<li><a href="{u}">{t}</a></li>' for t, u in links) + '</ul></div>'
                   for h, links in S.FOOT_LINKS)
    a = ADVISOR
    return f'''<footer>
  <div class="stripe" aria-hidden="true"></div>
  <div class="dept-foot"><div class="wrap">
    <div><h2>Digital Design &amp; Production</h2><p>Questions about a program or a class? Start with the program advisor.</p><p><a href="contact.html">Contact and locations</a></p></div>
    <div><h2>{a["role"]}</h2><p>{a["name"]}</p><p><a href="mailto:{a["email"]}">{a["email"]}</a></p><p>{a["phone"]}</p></div>
    <div><h2>Find classes</h2><p><a href="{S.SCHEDULE_DDP}">DDP classes in the schedule</a></p><p><a href="{S.SYLLABI}">Past syllabi</a></p><p><a href="{COURSES_URL}">DDP courses in the catalog</a></p><p><a href="courses.html">Course finder</a></p></div>
  </div></div>
  <div class="cod-foot"><div class="wrap">
    <div><h2>College of the Desert</h2><p>43-500 Monterey Ave<br>Palm Desert, CA 92260<br>760.346.8041</p></div>
    {cols}
    <p class="fine">College of the Desert is part of the Desert Community College District. <a href="accessibility.html">Accessibility of this site</a>. Page last reviewed: {S.REVIEWED}.</p>
  </div></div>
</footer>'''

def page(file, title, body, section=None, desc=""):
    full_title = f"{title} | Digital Design &amp; Production | College of the Desert" if file != "index.html" else "Digital Design &amp; Production | College of the Desert"
    html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{full_title}</title>
<meta name="description" content="{esc_attr(strip(desc))}">
<link rel="stylesheet" href="css/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="preview"><div class="wrap">{S.PREVIEW}</div></div>
{SPRITE}
{header(section)}
<main id="main">
{body}
</main>
{footer()}
</body>
</html>
'''
    with open(os.path.join(OUT, file), "w") as f:
        f.write(html)
    return file

def crumbs(items):
    lis = "".join(f'<li><a href="{u}">{t}</a></li>' if u else f'<li aria-current="page">{t}</li>' for t, u in items)
    return f'<nav class="crumbs" aria-label="Breadcrumb"><ol>{lis}</ol></nav>'

def subnav(current):
    items = "".join(f'<li><a href="{u}"{" aria-current=\"page\"" if u == current else ""}>{t}</a></li>' for u, t in S.SUBNAV)
    return f'<nav class="subnav" aria-label="Programs section"><ul>{items}</ul></nav>'

def simple_hero(title, lede, trail, sub=None):
    return f'''<div class="field"><div class="wrap">
  {crumbs(trail)}
  <h1>{title}</h1>
  <p class="lede">{lede}</p>
  {subnav(sub) if sub else ""}
</div></div>'''

def short_title(t):
    return re.sub(r" \(.*\)", "", t)

def pay_line(key):
    t, n, hr, yr, area, g, o, se, edu = JOBS[key]
    return hr, short_title(t), yr, area

def outlook(g):
    word = "Growing" if g > 3 else ("Shrinking" if g < -3 else "Steady")
    return f'{word} ({g:+.1f}%)'.replace("-", "&minus;")

def jobs_table(keys, caption):
    rows = []
    for k in keys:
        t, n, hr, yr, area, g, o, se, edu = JOBS[k]
        where = ' <span class="ca">California</span>' if area == "CA" else ""
        rows.append(f'<tr><th scope="row">{t}</th><td data-l="Median pay here"><b>{hr}</b>/hr<br><span class="yr">{yr}/yr</span>{where}</td><td data-l="Jobs in the region">{n}</td><td data-l="10-year outlook (U.S.)">{outlook(g)}</td><td data-l="Openings per year (U.S.)">{o:,.1f}k</td><td data-l="Self-employed">{se:.0f}%</td><td data-l="Typical entry education">{EDU[edu]}</td></tr>')
    return f'''<div class="tscroll"><table class="list jobs"><caption class="sr">{caption}</caption>
    <thead><tr><th scope="col">Job</th><th scope="col">Median pay here</th><th scope="col">Jobs in the region</th><th scope="col">10-year outlook (U.S.)</th><th scope="col">Openings per year (U.S.)</th><th scope="col">Self-employed</th><th scope="col">Typical entry education</th></tr></thead>
    <tbody>{"".join(rows)}</tbody></table></div>'''

def count_awards(keys):
    deg = sum(1 for k in keys if AWARDS[k]["kind"] in ("AA", "AS"))
    cert = sum(1 for k in keys if AWARDS[k]["kind"] == "CA")
    cc = sum(1 for k in keys if AWARDS[k]["kind"] == "CC")
    parts = []
    if deg: parts.append(f"{deg} degree" + ("s" if deg > 1 else ""))
    if cert: parts.append(f"{cert} certificate" + ("s" if cert > 1 else ""))
    if cc: parts.append(f"{cc} certificates of completion")
    return ", ".join(parts)

# ---------------------------------------------------------------------------
def tile(p, cls):
    wage = ""
    if p["pay"]:
        hr, t, yr, area = pay_line(p["pay"][0])
        wage = f'<p class="wage"><b>{hr}</b> median for {"local " if area == "metro" else ""}{t.lower()}{" in California" if area == "CA" else ""}</p>'
    extra = '<p class="wage">Or transfer to a four-year design program with the Design Studies AA.</p>' if p["key"] == "design" else ""
    free = ' <span class="badge">Free</span>' if p["key"] == "software" else ""
    jobs = p["jobs"] if p["key"] != "software" else "Adobe Certified skills in Photoshop, Illustrator, InDesign, Premiere Pro, and After Effects. Noncredit, no experience needed."
    fl = FLOWER
    uniq = f'<p class="unique">Only one in California. Online.</p>' if p.get("unique") else ""
    return (f'<li class="{cls} c-{p["color"]}">{fl}<div><h2><a href="{p["file"]}">{p["name"]}</a>{free}</h2>'
            f'<p class="jobs">{jobs}</p>{wage}{extra}{uniq}</div>'
            f'<p class="start"><span>Start with <b>{p["start"][0]}</b></span><span>{count_awards(p["awards"])}</span></p></li>')

def build_home():
    tiles = "".join(tile(p, "t-" + p["key"]) for p in PATHS)
    s = S.HOME
    n100 = sum(1 for a in AWARDS.values() if "100" in a["core"])
    body = f'''<div class="field home" id="paths"><div class="wrap hero-grid">
  <div>
    <h1>{s["h1"]}</h1>
    <p class="lede">{s["lede"]}</p>
  </div>
  <aside class="mini" aria-labelledby="here-h">
    <h2 id="here-h">Exploring? Start with DDP 100.</h2>
    <p>It samples every program and is open to everyone.</p>
    <a class="btn btn-gold" href="{S.sched("100")}">Find a DDP 100 section</a>
  </aside>
</div></div>
<div class="tiles"><div class="wrap">
  <h2 class="sr">Programs by career path</h2>
  <ul class="blooms">{tiles}</ul>
  <p class="src">Pay: {JOBS_SOURCE} The metro includes the Coachella Valley. Animators usually need a bachelor's degree. <a href="programs.html">Compare all programs</a>.</p>
</div></div>

<section class="tight" aria-label="More ways in"><div class="wrap two">
  <article class="panel-gold"><h3>Adobe classes that cost nothing</h3><p>Noncredit classes are tuition-free, need no experience, and can be repeated. Finish part A and part B to earn a Certificate of Completion and prepare for the Adobe Certified exam.</p><a href="software.html">How noncredit works</a></article>
  <article class="panel-red"><h3>Coming fall 2027: the Palm Springs campus</h3><p>COD's new campus at Farrell Drive and Tahquitz Canyon Way is planned to open in fall 2027, with studios and maker spaces for digital media and arts.</p><a href="{S.COD}/students/locations/palm-springs/">COD in Palm Springs</a></article>
</div></section>

<section class="tight" id="start" aria-labelledby="start-h"><div class="wrap">
  <h2 class="h2" id="start-h">Get started in four steps</h2>
  <p class="sub">From your first class to a finished certificate. <a href="get-started.html">See the details</a>.</p>
  <ol class="steps">{"".join(f'<li><h3>{h}</h3><p>{t}</p></li>' for h, t, _ in S.STEPS)}</ol>
</div></section>

{pay_section()}'''
    return page("index.html", "Home", body, "home", s["lede"])

def pay_section(keys=("graphic", "webdev", "animator"), heading="What creative work pays here"):
    items = "".join(f'<li><strong>{JOBS[k][2]}/hr</strong><span>{short_title(JOBS[k][0])} ({JOBS[k][3]} a year)</span></li>' for k in keys)
    return f'''<section class="pay-wrap" aria-labelledby="pay-h"><div class="wrap">
  <h2 class="h2" id="pay-h">{heading}</h2>
  <p class="sub">Median pay in the Riverside-San Bernardino-Ontario metro, which includes the Coachella Valley. <a href="careers.html">More on careers</a>.</p>
  <ul class="pay">{items}</ul>
  <p class="src">Source: {JOBS_SOURCE}</p>
</div></section>'''

# ---------------------------------------------------------------------------
ICON = {
 "catalog": '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4.5A2.5 2.5 0 0 1 6.5 2H20v17H6.5A2.5 2.5 0 0 0 4 21.5z"/><path d="M4 21.5A2.5 2.5 0 0 1 6.5 19H20v3H6.5"/></svg>',
 "schedule": '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="17" rx="2"/><path d="M16 2v4M8 2v4M3 10h18M8 14h2M14 14h2M8 17h2"/></svg>',
 "syllabus": '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h5"/></svg>',
}

def tools(code=None, label=""):
    """The three class tools, always named and explained the same way."""
    cat = S.cat_search(code) if code else COURSES_URL
    sch = S.sched(code) if code else S.SCHEDULE_DDP
    who = f" for {ddp(code)}" if code else ""
    find = f"Search for &ldquo;{ddp(code)}&rdquo;." if code else "Search by course code, like &ldquo;DDP 100&rdquo;."
    return f'''<ul class="ctools"{f' aria-label="{label}"' if label else ""}>
  <li><a href="{cat}"><span class="ic">{ICON["catalog"]}</span><b>Catalog<span class="sr">{who}</span></b><span>Official description, units, and requirements</span></a></li>
  <li><a href="{sch}"><span class="ic">{ICON["schedule"]}</span><b>Class schedule<span class="sr">{who}</span></b><span>Days, times, online sections, and registration</span></a></li>
  <li><a href="{S.SYLLABI}"><span class="ic">{ICON["syllabus"]}</span><b>Syllabus library<span class="sr">{who}</span></b><span>What past classes covered. {find}</span></a></li>
</ul>'''

def bloom_art():
    """Decorative desert-bloom cluster for program headers."""
    fl = [(330, 120, 1.9, .22), (210, 60, 1.1, .16), (420, 250, 1.3, .18), (250, 230, .8, .26), (120, 170, .7, .14), (380, 30, .6, .2), (470, 140, .5, .3)]
    g = "".join(f'<g transform="translate({x} {y}) scale({sc})" opacity="{o}"><circle cx="0" cy="-26" r="22"/><circle cx="26" cy="0" r="22"/><circle cx="0" cy="26" r="22"/><circle cx="-26" cy="0" r="22"/></g>' for x, y, sc, o in fl)
    c = "".join(f'<circle cx="{x}" cy="{y}" r="{15*sc}" class="ctr"/>' for x, y, sc, o in fl[:4])
    return f'<svg class="blooms-art" viewBox="0 0 520 320" aria-hidden="true" focusable="false"><g fill="currentColor">{g}</g>{c}</svg>'

def award_card(k):
    a = AWARDS[k]
    kind = KIND[a["kind"]]
    units = "no units" if a["kind"] == "CC" else f'{a["units"]} units'
    tr = ' <span class="badge">Transfer</span>' if a.get("transfer") else ""
    nc = ' <span class="badge nc">Tuition-free</span>' if a["kind"] == "CC" else ""
    nc += ' <span class="badge">Only one in California</span> <span class="badge">Online</span>' if a.get("unique") else ""
    core = "".join(f"<li>{course_link(c)}</li>" for c in a["core"])
    choose = ""
    if a.get("choose"):
        n, cs = a["choose"]
        choose = f'<p class="req">Plus one of: {", ".join(course_link(c) for c in cs)}</p>'
    other = f'<p class="req">Also requires {", ".join(a["other"])}.</p>' if a.get("other") else ""
    elect = f'<p class="req">Plus electives: {a["electives"]}.</p>' if a.get("electives") else ""
    ge = f'<p class="req">Degree also includes {a["ge"]} general education.</p>' if a.get("ge") else ""
    desc = a.get("desc", f'Earn this certificate by completing {ddp(a["core"][0])} and {ddp(a["core"][1])}.')
    return f'''<li class="award" id="{k}">
  <p class="kind">{kind}, {units}{tr}{nc}</p>
  <h3>{a["name"]}</h3>
  <p>{desc}</p>
  <p class="req">Required DDP courses:</p>
  <ul class="chips">{core}</ul>
  {choose}{elect}{other}{ge}
  <p class="go"><a href="#ksa-{k}">What you&#39;ll learn<span class="sr"> in {strip(a["name"])}</span></a><a href="{a["url"]}"><span class="ic">{ICON["catalog"]}</span>Catalog requirements<span class="sr"> for {strip(a["name"])}</span></a></p>
</li>'''

def ksa_block(k, open_=False):
    from ksa import KSA
    a = AWARDS[k]; q = KSA[k]
    col = lambda h, d, items: f'<div><h4>{h}</h4><p class="d">{d}</p><ul class="ticks">' + "".join(f"<li>{i}</li>" for i in items) + "</ul></div>"
    return f'''<details class="ksa" id="ksa-{k}"{" open" if open_ else ""}>
  <summary><span class="k">{a["kind"] if a["kind"] != "CC" else "Noncredit"}</span>{a["name"]}</summary>
  <div class="kgrid">
    {col("Knowledge", "What you&#39;ll understand", q["k"])}
    {col("Skills", "What you&#39;ll be able to do", q["s"])}
    {col("Abilities", "How you&#39;ll use it on the job", q["a"])}
  </div>
</details>'''

def confidence(p, sc):
    first = "No experience needed. Noncredit classes are tuition-free and can be repeated." if p["key"] == "software" else f"{sc} has no prerequisite. Bring your curiosity; your instructors will teach you the tools."
    return f'''<section class="confide" aria-labelledby="cf-h"><div class="wrap">
  <h2 class="h2" id="cf-h">Every designer started with a first class.</h2>
  <ul class="cf">
    <li><h3>Start where you are</h3><p>{first}</p></li>
    <li><h3>Learn by making</h3><p>Most 3-unit DDP courses include 54 hours of hands-on lab time, so you build real projects from week one.</p></li>
    <li><h3>Help is here</h3><p>Free tutoring at the <a href="{S.L["tutoring"]}">Academic Skills Center</a>, instructors who work in the field, and a <a href="contact.html">program advisor</a> to help you plan.</p></li>
  </ul>
</div></section>'''

def build_path(p):
    others = "".join(f'<li class="c-{o["color"]}"><a href="{o["file"]}">{o["name"]}</a></li>' for o in PATHS if o is not p)
    if p["pay"]:
        hr, t, yr, area = pay_line(p["pay"][0])
        place = "in the Inland Empire and Coachella Valley" if area == "metro" else "in California"
        aside = f'<aside><p><b>{hr}</b>median hourly pay for {t.lower()} {place}</p><p><a href="#car-h">Careers and pay</a></p></aside>'
    else:
        aside = ""
    sc, st = p["start"]
    start_code = sc.replace("DDP ", "")
    st_course = COURSES[start_code]
    trtext = {"CSU/UC": "Transfers to CSU and UC", "CSU": "Transfers to CSU", "": "Noncredit, tuition-free" if st_course[1] == "0" else "Career course"}[st_course[2]]
    codes = [c for c in COURSES if p["key"] in course_paths(c)]
    rows = "".join(
        f'<tr><td>{course_link(c)}</td><td>{COURSES[c][0]}</td><td>{"Noncredit" if COURSES[c][1]=="0" else COURSES[c][1]+" units"}</td><td>{COURSES[c][2] or "&nbsp;"}</td>'
        f'<td class="lk"><a href="{S.cat_search(c)}">Catalog<span class="sr"> for {ddp(c)}</span></a></td><td class="lk"><a href="{S.sched(c)}">Schedule<span class="sr"> for {ddp(c)}</span></a></td></tr>'
        for c in codes)
    trn = f'<p class="note">{p["transfer_note"]} <a href="#tr-h">Transfer options</a>.</p>' if p.get("transfer_note") else ""
    software_extra = ""
    if p["key"] == "software":
        software_extra = f'''<section class="tight" aria-labelledby="how-h"><div class="wrap prose">
  <h2 class="h2" id="how-h">How noncredit works</h2>
  <p>Noncredit classes have no tuition and no units. They are graded pass or no pass, and you can repeat them. Each Certificate of Completion pairs an A class, which teaches the basics, with a B class, which adds practice exams and portfolio projects for the Adobe Certified exam.</p>
  <p>Noncredit classes use a separate, shorter application. <a href="{S.COD}/students/admissions/noncredit/">Register for noncredit at COD</a>.</p>
  <p>Ready for more? Credit courses like {course_link("101")} (Photoshop), {course_link("102")} (Illustrator), and {course_link("120")} (Premiere Pro) count toward degrees and certificates.</p>
</div></section>'''
    pnav = "".join(f'<li><a href="#{i}">{t}</a></li>' for i, t in [("start-h", "Start here"), ("prog-h", "Programs"), ("learn-h", "What you&#39;ll learn"), ("crs-h", "Courses"), ("car-h", "Careers"), ("tr-h", "Transfer")])
    body = f'''<div class="phero c-{p["color"]}"><div class="wrap">
  <div class="pt">
    {crumbs([("Home", "index.html"), ("Programs", "programs.html"), (p["name"], None)])}
    <h1>{p["name"]}</h1>
    {f'<p class="unique">{p["unique"]}</p>' if p.get("unique") else ""}
    <p class="lede">{p["intro"]}</p>
    <p class="jobs-line"><strong>Careers:</strong> {p["jobs"]}</p>
  </div>
  <div class="pa">{bloom_art()}{aside}</div>
</div></div>
<nav class="pnav c-{p["color"]}" aria-label="Sections of this page"><div class="wrap"><span class="dot" aria-hidden="true"></span><ul>{pnav}</ul></div></nav>

<section aria-labelledby="start-h"><div class="wrap here">
  <div>
    <h2 class="h2" id="start-h">Start here: {sc}</h2>
    <p class="sub" style="margin:0 0 1rem">{st_course[5]} It counts toward the programs on this path, so you can try the field before you commit.</p>
  </div>
  <div class="ticket">
    <p class="code">{sc}</p>
    <p class="t">{st}, {"noncredit" if st_course[1]=="0" else st_course[1]+" units"}</p>
    <ul class="chips"><li>{trtext}</li>{"<li>COD GE Area "+st_course[3]+"</li>" if st_course[3] else ""}<li>No prerequisite</li></ul>
    {tools(start_code, "Class tools for " + sc)}
  </div>
</div></section>

{confidence(p, sc)}

{software_extra}

<section class="c-{p["color"]}" aria-labelledby="prog-h"><div class="wrap">
  <h2 class="h2" id="prog-h">Degrees and certificates</h2>
  <p class="sub">{count_awards(p["awards"]).capitalize()}. Requirements come from the 2026-2027 catalog, the official source.</p>
  <ul class="awards">{"".join(award_card(k) for k in p["awards"])}</ul>
  {trn}
</div></section>

<section class="tight" aria-labelledby="learn-h"><div class="wrap">
  <h2 class="h2" id="learn-h">What you&#39;ll learn</h2>
  <p class="sub">The knowledge, skills, and abilities each program builds. Open a program to see its list.</p>
  {"".join(ksa_block(k, i == 0) for i, k in enumerate(p["awards"]))}
</div></section>

<section class="tight" aria-labelledby="crs-h"><div class="wrap">
  <h2 class="h2" id="crs-h">Courses on this path</h2>
  <p class="sub">Every DDP course used by these programs. Three tools help you plan:</p>
  {tools(None, "Class tools for all DDP courses")}
  <table class="list crs"><caption class="sr">DDP courses for {strip(p["name"])}</caption>
    <thead><tr><th scope="col">Course</th><th scope="col">Title</th><th scope="col">Units</th><th scope="col">Transfers to</th><th scope="col">Catalog</th><th scope="col">Schedule</th></tr></thead>
    <tbody>{rows}</tbody></table>
  <p class="src">Select a course number for a short description in the <a href="courses.html">course finder</a>.</p>
</div></section>

{path_careers(p)}

{path_transfer(p, codes)}

<section aria-labelledby="oth-h"><div class="wrap">
  <h2 class="h2" id="oth-h">Explore other programs</h2>
  <ul class="others">{others}</ul>
</div></section>'''
    return page(p["file"], strip(p["name"]), body, "programs", p["intro"])


def path_careers(p):
    c = CAREERS[p["key"]]
    ladder = "".join(f'<li><h4>{st}</h4><p>{t}</p></li>' for st, t in c["ladder"])
    emp = "".join(f"<li>{e}</li>" for e in c["employers"])
    sk = "".join(f"<li>{e}</li>" for e in c["skills"])
    return f'''<section class="pay-wrap" aria-labelledby="car-h"><div class="wrap">
  <h2 class="h2" id="car-h">Careers</h2>
  <p class="sub">{c["work"]}</p>
  <h3 class="h3">Jobs and pay</h3>
  {jobs_table(p["pay"], "Jobs, pay, and outlook for " + strip(p["name"]))}
  <p class="src">Pay is the median for the Riverside-San Bernardino-Ontario metro, which includes the Coachella Valley, unless marked California. Outlook, openings, self-employment, and education are national. Source: {JOBS_SOURCE}</p>
  <p class="note">"Typical entry education" is what most people in the job have. Creative employers hire from portfolios, so a COD certificate plus strong work can start your career, and a transfer degree keeps the bachelor&#39;s option open. {c["note"]}</p>
  <div class="cgrid">
    <div><h3 class="h3">Career ladder</h3><ol class="ladder">{ladder}</ol></div>
    <div><h3 class="h3">Where the jobs are</h3><ul class="ticks">{emp}</ul></div>
    <div><h3 class="h3">Skills employers want</h3><ul class="ticks">{sk}</ul></div>
  </div>
  <ul class="links four" style="margin-top:2rem">
    <li><a href="{S.L["handshake"]}"><b>Find jobs on Handshake</b><span>Jobs and internships for COD students. Sign in with your COD account.</span></a></li>
    <li><a href="courses.html#ddp-195"><b>DDP 195</b><span>Business practices and portfolio preparation: freelancing, pricing, clients, and your portfolio.</span></a></li>
    <li><a href="courses.html#ddp-095a"><b>DDP 095A</b><span>Earn units for a design job or internship.</span></a></li>
    <li><a href="{S.L["career"]}"><b>Career center</b><span>Career counseling, resumes, and job fairs at COD.</span></a></li>
  </ul>
</div></section>'''

def path_transfer(p, codes):
    tr_awards = [k for k in p["awards"] if AWARDS[k].get("transfer")]
    csu = [c for c in codes if "CSU" in COURSES[c][2]]
    uc = [c for c in codes if "UC" in COURSES[c][2]]
    if p["key"] == "software":
        body = "<p>Noncredit classes do not earn transfer credit. When you are ready, credit courses like " + course_link("101") + " and " + course_link("102") + " count toward degrees and transfer to the CSU.</p>"
    else:
        lead = ""
        if tr_awards:
            joined = " and ".join(f'the <a href="#{k}">{AWARDS[k]["name"]} {AWARDS[k]["kind"]}</a>' for k in tr_awards)
            lead = "<p>" + joined[0].upper() + joined[1:] + (" are" if len(tr_awards) > 1 else " is") + " built for transfer, using Cal-GETC general education.</p>"
        body = lead + f"<p>{len(csu)} of the {len(codes)} DDP courses on this path transfer to the CSU, and {len(uc)} also transfer to the UC. Each university decides which courses count toward its major, so check <a href=\"{S.L['assist']}\">ASSIST.org</a> and meet with a counselor.</p>"
    return f'''<section class="tight" aria-labelledby="tr-h" style="padding-top:clamp(2.75rem,6vw,4.5rem)"><div class="wrap prose">
  <h2 class="h2" id="tr-h">Transfer</h2>
  {body}
  <p><a href="transfer.html">How transfer works</a></p>
</div></section>'''

# ---------------------------------------------------------------------------
def build_programs():
    rows = []
    for p in PATHS:
        aw = "".join(f'<li><a href="{p["file"]}#{k}"><span class="k">{AWARDS[k]["kind"] if AWARDS[k]["kind"]!="CC" else "Noncredit"}</span>{AWARDS[k]["name"]}</a></li>' for k in p["awards"])
        rows.append(f'''<li class="prog c-{p["color"]}">
  <div class="sw" aria-hidden="true"></div>
  <div class="pi">
    <h2><a href="{p["file"]}">{p["name"]}</a></h2>
    {f'<p class="unique">{p["unique"]}</p>' if p.get("unique") else ""}
    <p>{p["pitch"]}</p>
    <p class="meta"><span>Start with <b>{p["start"][0]}</b></span><span>{count_awards(p["awards"])}</span></p>
  </div>
  <ul class="aw" aria-label="Degrees and certificates in {strip(p["name"])}">{aw}</ul>
</li>''')
    key = "".join(f"<li><b>{k}</b> {v}</li>" for k, v in [("AA / AS", "Associate degree"), ("CA", "Certificate of Achievement"), ("Noncredit", "Certificate of Completion, tuition-free")])
    body = simple_hero("Programs", f"Six career paths and {len(AWARDS)} degrees and certificates. Pick a path to see its programs, courses, careers, and transfer options.",
                       [("Home", "index.html"), ("Programs", None)], "programs.html") + f'''
<section><div class="wrap">
  <ul class="progs">{"".join(rows)}</ul>
  <ul class="key" aria-label="Award types">{key}</ul>
</div></section>
<section class="pay-wrap"><div class="wrap">
  <h2 class="h2">Not sure where to start?</h2>
  <ul class="links">
    <li><a href="{S.sched("100")}"><b>Take DDP 100</b><span>Introduction to Digital Art &amp; Media samples every path. Open to everyone; transfers to CSU and UC.</span></a></li>
    <li><a href="courses.html"><b>Browse every course</b><span>Filter all {len(COURSES)} DDP courses by path, transfer, and general education.</span></a></li>
    <li><a href="contact.html"><b>Talk with the program advisor</b><span>{ADVISOR["name"]}, {ADVISOR["email"]}</span></a></li>
  </ul>
</div></section>'''
    return page("programs.html", "Programs", body, "programs", "Digital Design &amp; Production programs at College of the Desert by career path.")

# ---------------------------------------------------------------------------
def build_courses():
    order = sorted(COURSES, key=lambda c: (int(re.sub(r"\D", "", c)), c))
    items = []
    for c in order:
        t, u, tr, ge, prim, blurb = COURSES[c]
        paths = course_paths(c)
        color = PBY[prim]["color"] if prim in PBY else "gold"
        trd = " ".join(x.lower() for x in tr.split("/")) if tr else ""
        meta = []
        meta.append("Noncredit" if u == "0" else f"{u} units")
        if tr: meta.append(f"Transfers: {tr}")
        if ge: meta.append(f"COD GE {ge}")
        used = awards_using(c)
        used_html = ("<p class=\"used\">Counts toward: " + ", ".join(
            f'<a href="{PBY[AWARD_PATH[k]]["file"]}#{k}">{AWARDS[k]["name"]}</a>' for k in used) + "</p>") if used else ""
        items.append(f'''<li class="course c-{color}" id="{cid(c)}" data-path="{" ".join(paths)}" data-tr="{trd}"{' data-ge' if ge else ""}>
  <h3><span class="code">{ddp(c)}</span>{t}</h3>
  <p>{blurb}</p>
  <p class="meta">{"".join(f"<span>{m}</span>" for m in meta)}</p>
  {used_html}
  <p class="acts"><a href="{S.cat_search(c)}"><span class="ic">{ICON["catalog"]}</span>Catalog<span class="sr"> for {ddp(c)}</span></a><a href="{S.sched(c)}"><span class="ic">{ICON["schedule"]}</span>Schedule<span class="sr"> for {ddp(c)}</span></a><a href="{S.SYLLABI}"><span class="ic">{ICON["syllabus"]}</span>Syllabi<span class="sr"> (search for {ddp(c)})</span></a></p>
</li>''')
    popts = [("all", "All areas")] + [(p["key"], strip(p["name"]).replace("Job-Ready Software Skills", "Noncredit Software")) for p in PATHS] + [("career", "Career &amp; portfolio")]
    pr = "".join(f'<input type="radio" name="area" id="f-{k}" value="{k}"{" checked" if k=="all" else ""}><label for="f-{k}">{n}</label>' for k, n in popts)
    tr = "".join(f'<input type="radio" name="tr" id="t-{k}" value="{k}"{" checked" if k=="any" else ""}><label for="t-{k}">{n}</label>' for k, n in
                 [("any", "Any"), ("csu", "Transfers to CSU"), ("uc", "Transfers to UC"), ("ge", "Counts for COD GE")])
    body = f'''{simple_hero("Course finder", f"All {len(COURSES)} DDP courses in the 2026-2027 catalog. Filter by career path or by transfer, then find open sections in the class schedule.", [("Home","index.html"),("Programs","programs.html"),("Course finder",None)], "courses.html")}
<section><div class="wrap">
  <fieldset class="filters"><legend>Career path</legend><div class="opts">{pr}</div></fieldset>
  <fieldset class="filters"><legend>Transfer and general education</legend><div class="opts">{tr}</div></fieldset>
  {tools(None, "Class tools")}
  <ul class="courses" aria-label="DDP courses">{"".join(items)}</ul>
  <p class="src">Source: <a href="{COURSES_URL}">College of the Desert 2026-2027 Catalog, Digital Design &amp; Production courses</a>. Descriptions are shortened; the catalog lists prerequisites, advisories, and hours.</p>
</div></section>'''
    return page("courses.html", "Course finder", body, "programs", "Find DDP courses by career path, transfer, and general education.")

# ---------------------------------------------------------------------------
def build_content(pg):
    if pg.get("section") == "programs":
        hero = simple_hero(pg["title"], pg["lede"], [("Home", "index.html"), ("Programs", "programs.html"), (pg["title"], None)], pg["file"])
    else:
        hero = simple_hero(pg["title"], pg["lede"], [("Home", "index.html"), (pg["title"], None)])
    body = hero + pg["body"]
    return page(pg["file"], pg["title"], body, pg.get("section"), pg["lede"])

def build():
    shutil.copy(os.path.join(ROOT, "src", "style.css"), os.path.join(OUT, "css", "style.css"))
    made = [build_home(), build_programs(), build_courses()]
    made += [build_path(p) for p in PATHS]
    for pg in S.pages(pay_section, course_link, jobs_table):
        made.append(build_content(pg))
    print(f"Built {len(made)} pages:", ", ".join(made))

if __name__ == "__main__":
    os.makedirs(os.path.join(OUT, "css"), exist_ok=True)
    build()
