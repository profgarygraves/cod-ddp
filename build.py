#!/usr/bin/env python3
"""Build the DDP website preview into docs/ (English) and docs/es/ (Spanish) from the data in src/.

    python3 build.py

English content: src/programs.py, src/ksa.py, src/site_data.py, src/people.py, src/work.py
Spanish content: src/programs_es.py, src/ksa_es.py, src/site_data_es.py (plus the small dictionaries below)
"""
import os, re, shutil, sys
ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ROOT, "src"))
from programs import PATHS, AWARDS, KIND, COURSES, JOBS, JOBS_SOURCE, ADVISOR, COURSES_URL, CAREERS, EDU
from programs_es import PATHS_ES, AWARDS_ES, KIND_ES, COURSES_ES, JOBS_ES, EDU_ES, CAREERS_ES
from ksa import KSA
from ksa_es import KSA_ES
import site_data as S_EN
import site_data_es as S_ES
from people import LEADERSHIP, FACULTY, LINKEDIN
from work import WORKS

DOCS = os.path.join(ROOT, "docs")
PBY = {p["key"]: p for p in PATHS}
AWARD_PATH = {a: p["key"] for p in PATHS for a in p["awards"]}

# ---------------------------------------------------------------------------
# Language state. build() runs once per language.
LANG = "en"
S = S_EN
OUT = DOCS
R = ""          # prefix for shared assets (css, fonts, images) from this language's folder

def T(en, es):
    return es if LANG == "es" else en

ROLE_ES = {
 "Dean, School of Social Sciences and Arts": "Decana, Escuela de Ciencias Sociales y Artes",
 "Professor, Digital Design &amp; Production; Department Chair, Arts &amp; Media; Program Advisor": "Profesora de Digital Design &amp; Production; jefa del Departamento de Artes y Medios; asesora del programa",
 "Administrative Assistant, School of Social Sciences and Arts": "Asistente administrativa, Escuela de Ciencias Sociales y Artes",
 "Professor and Department Chair": "Profesora y jefa del departamento",
 "Adjunct Faculty": "Docente adjunto",
 "Instructor": "Instructor",
 "Faculty, Film and Media Studies": "Docente de Cine y Medios",
 "Adjunct Faculty; DDP Online Gallery submissions": "Docente adjunto; envíos para la Galería en Línea de DDP",
 "Program Advisor": "Asesora del programa",
}
MEDIUM_ES = {
 "Festival poster, digital illustration": "Cartel de festival, ilustración digital",
 "Digital photograph": "Fotografía digital",
 "Motion graphics, 0:45": "Motion graphics, 0:45",
 "UX prototype": "Prototipo de UX",
 "Original typeface": "Tipografía original",
 "3D render": "Render 3D",
 "Aerial drone photograph": "Fotografía aérea con dron",
 "Package design": "Diseño de empaque",
 "Game prototype": "Prototipo de videojuego",
 "Accessible PDF": "PDF accesible",
 "Retouched photograph, Photoshop": "Fotografía retocada, Photoshop",
 "Social campaign": "Campaña social",
}

def role(t): return ROLE_ES.get(t, t) if LANG == "es" else t

# ---- data accessors (Spanish falls back to English if a field is missing) ----
def pf(p, field):
    if LANG == "es":
        return PATHS_ES.get(p["key"], {}).get(field, p.get(field))
    return p.get(field)
def pn(p): return pf(p, "name")
def adesc(k):
    a = AWARDS[k]
    en = a.get("desc", "")
    return AWARDS_ES.get(k, {}).get("desc", en) if LANG == "es" else en
def kname(kind): return KIND_ES[kind] if LANG == "es" else KIND[kind]
def cblurb(c): return COURSES_ES.get(c, COURSES[c][5]) if LANG == "es" else COURSES[c][5]
def jtitle(k): return JOBS_ES.get(k, JOBS[k][0]) if LANG == "es" else JOBS[k][0]
def edu(e): return EDU_ES[e] if LANG == "es" else EDU[e]
def careers(k): return CAREERS_ES[k] if LANG == "es" else CAREERS[k]
def ksa(k): return KSA_ES[k] if LANG == "es" else KSA[k]
def jobs_source(): return T(JOBS_SOURCE, "Oficina de Estadísticas Laborales de EE. UU. (BLS): Occupational Employment and Wage Statistics, mayo de 2025, área metropolitana de Riverside-San Bernardino-Ontario (California donde se indica); Employment Projections 2025-2035 (nacional).")
def units(u): return T(f"{u} units", f"{u} unidades")

def esc_attr(s): return s.replace('"', "&quot;")
def strip(s): return re.sub(r"<[^>]+>", "", s)

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

def theme():
    auto, light, dark, leg = T("Match my device", "Igual que mi dispositivo"), T("Light", "Claro"), T("Dark", "Oscuro"), T("Color theme", "Tema de color")
    return f'''<fieldset class="theme">
        <legend>{leg}</legend>
        <input type="radio" name="theme" id="th-auto" value="auto" checked><label for="th-auto" title="{auto}"><svg width="16" height="16" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="M12 3.5a8.5 8.5 0 0 1 0 17z" fill="currentColor"/></svg><span class="sr">{auto}</span></label>
        <input type="radio" name="theme" id="th-light" value="light"><label for="th-light" title="{light}"><svg width="16" height="16" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg><span class="sr">{light}</span></label>
        <input type="radio" name="theme" id="th-dark" value="dark"><label for="th-dark" title="{dark}"><svg width="16" height="16" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8.5 8.5 0 0 1 9.5 4a8.5 8.5 0 1 0 10.5 10.5z" fill="currentColor"/></svg><span class="sr">{dark}</span></label>
      </fieldset>
      <script>(function(){{var k="codddp-theme";try{{var v=localStorage.getItem(k);if(v){{var r=document.getElementById("th-"+v);if(r)r.checked=true;}}}}catch(e){{}}document.addEventListener("change",function(e){{if(e.target&&e.target.name==="theme"){{try{{localStorage.setItem(k,e.target.value);}}catch(x){{}}}}}});}})();</script>'''

MARK = ('<svg class="mark" viewBox="0 0 44 44" aria-hidden="true"><g fill="currentColor"><circle cx="22" cy="10" r="8"/>'
        '<circle cx="34" cy="22" r="8"/><circle cx="22" cy="34" r="8"/><circle cx="10" cy="22" r="8"/></g><circle class="c" cx="22" cy="22" r="6"/></svg>')

def lang_switch(file):
    if LANG == "en":
        return f'<a class="lang" href="es/{file}" lang="es" hreflang="es">Español</a>'
    return f'<a class="lang" href="../{file}" lang="en" hreflang="en">English</a>'

def header(section, file):
    nav = "".join(
        f'<li><a href="{href}"{" aria-current=\"page\"" if key == section else ""}>{label}</a></li>'
        for key, label, href in S.NAV)
    top = "".join(f'<li><a href="{u}">{t}</a></li>' for t, u in S.TOP_LINKS)
    return f'''<header>
  <div class="college"><div class="wrap">
    <a class="cod" href="{S.COD}/">College of the Desert</a>
    <div class="tools">
      <ul>{top}</ul>
      {lang_switch(file)}
      {theme()}
    </div>
  </div></div>
  <div class="dept"><div class="wrap">
    <a class="name" href="index.html">{MARK}Digital Design &amp; Production</a>
    <nav aria-label="{T("Department", "Departamento")}"><ul>{nav}</ul></nav>
  </div></div>
</header>'''

def footer():
    cols = "".join(f'<div><h2>{h}</h2><ul>' + "".join(f'<li><a href="{u}">{t}</a></li>' for t, u in links) + '</ul></div>'
                   for h, links in S.FOOT_LINKS)
    a = ADVISOR
    return f'''<footer>
  <div class="stripe" aria-hidden="true"></div>
  <div class="dept-foot"><div class="wrap">
    <div><h2>Digital Design &amp; Production</h2><p>{T("Questions about a program or a class? Start with the program advisor.", "¿Preguntas sobre un programa o una clase? Empieza con la asesora del programa.")}</p><p><a href="contact.html">{T("Contact and locations", "Contacto y ubicaciones")}</a></p></div>
    <div><h2>{role(a["role"])}</h2><p>{a["name"]}</p><p><a href="mailto:{a["email"]}">{a["email"]}</a></p><p>{a["phone"]}</p></div>
    <div><h2>{T("Find classes", "Encuentra clases")}</h2><p><a href="{S.SCHEDULE_DDP}">{T("DDP classes in the schedule", "Clases de DDP en el horario")}</a></p><p><a href="{S.SYLLABI}">{T("Past syllabi", "Programas de cursos anteriores")}</a></p><p><a href="{COURSES_URL}">{T("DDP courses in the catalog", "Cursos de DDP en el catálogo")}</a></p><p><a href="courses.html">{T("Course finder", "Buscador de cursos")}</a></p></div>
  </div></div>
  <div class="cod-foot"><div class="wrap">
    <div><h2>College of the Desert</h2><p>43-500 Monterey Ave<br>Palm Desert, CA 92260<br>760.346.8041</p></div>
    {cols}
    <p class="fine">{T("College of the Desert is part of the Desert Community College District.", "College of the Desert forma parte del Desert Community College District.")} <a href="accessibility.html">{T("Accessibility of this site", "Accesibilidad de este sitio")}</a>. {T("Page last reviewed", "Última revisión de la página")}: {S.REVIEWED}.</p>
  </div></div>
</footer>'''

def page(file, title, body, section=None, desc=""):
    site = "Digital Design &amp; Production | College of the Desert"
    full_title = f"{title} | {site}" if file != "index.html" else site
    en_href = ("" if LANG == "en" else "../") + file
    es_href = ("es/" if LANG == "en" else "") + file
    html = f'''<!doctype html>
<html lang="{LANG}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{full_title}</title>
<meta name="description" content="{esc_attr(strip(desc))}">
<link rel="alternate" hreflang="en" href="{en_href}">
<link rel="alternate" hreflang="es" href="{es_href}">
<link rel="stylesheet" href="{R}css/style.css">
</head>
<body>
<a class="skip" href="#main">{T("Skip to content", "Saltar al contenido")}</a>
<div class="preview"><div class="wrap">{S.PREVIEW}</div></div>
{SPRITE}
{header(section, file)}
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
    return f'<nav class="crumbs" aria-label="{T("Breadcrumb", "Ruta de navegación")}"><ol>{lis}</ol></nav>'

def home_crumb(): return (T("Home", "Inicio"), "index.html")
def prog_crumb(): return (T("Programs", "Programas"), "programs.html")

def subnav(current):
    items = "".join(f'<li><a href="{u}"{" aria-current=\"page\"" if u == current else ""}>{t}</a></li>' for u, t in S.SUBNAV)
    return f'<nav class="subnav" aria-label="{T("Programs section", "Sección de programas")}"><ul>{items}</ul></nav>'

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
    t, n, hr, yr, area, g, o, se, e = JOBS[key]
    return hr, short_title(jtitle(key)), yr, area

def outlook(g):
    word = T("Growing", "En crecimiento") if g > 3 else (T("Shrinking", "En descenso") if g < -3 else T("Steady", "Estable"))
    return f'{word} ({g:+.1f}%)'.replace("-", "&minus;")

def jobs_table(keys, caption):
    rows = []
    hdr = [T("Job", "Empleo"), T("Median pay here", "Salario medio aquí"), T("Jobs in the region", "Empleos en la región"), T("10-year outlook (U.S.)", "Perspectiva a 10 años (EE. UU.)"),
           T("Openings per year (U.S.)", "Vacantes por año (EE. UU.)"), T("Self-employed", "Por cuenta propia"), T("Typical entry education", "Estudios típicos para empezar")]
    for k in keys:
        t, n, hr, yr, area, g, o, se, e = JOBS[k]
        where = ' <span class="ca">California</span>' if area == "CA" else ""
        rows.append(f'<tr><th scope="row">{jtitle(k)}</th><td data-l="{hdr[1]}"><b>{hr}</b>{T("/hr", "/hora")}<br><span class="yr">{yr}{T("/yr", "/año")}</span>{where}</td><td data-l="{hdr[2]}">{n}</td><td data-l="{hdr[3]}">{outlook(g)}</td><td data-l="{hdr[4]}">{o:,.1f}k</td><td data-l="{hdr[5]}">{se:.0f}%</td><td data-l="{hdr[6]}">{edu(e)}</td></tr>')
    th = "".join(f'<th scope="col">{h}</th>' for h in hdr)
    return f'''<div class="tscroll"><table class="list jobs"><caption class="sr">{caption}</caption>
    <thead><tr>{th}</tr></thead>
    <tbody>{"".join(rows)}</tbody></table></div>'''

def count_awards(keys):
    deg = sum(1 for k in keys if AWARDS[k]["kind"] in ("AA", "AS"))
    cert = sum(1 for k in keys if AWARDS[k]["kind"] == "CA")
    cc = sum(1 for k in keys if AWARDS[k]["kind"] == "CC")
    parts = []
    if LANG == "es":
        if deg: parts.append(f"{deg} título" + ("s" if deg > 1 else "") + " de asociado")
        if cert: parts.append(f"{cert} certificado" + ("s" if cert > 1 else ""))
        if cc: parts.append(f"{cc} certificados de finalización")
    else:
        if deg: parts.append(f"{deg} degree" + ("s" if deg > 1 else ""))
        if cert: parts.append(f"{cert} certificate" + ("s" if cert > 1 else ""))
        if cc: parts.append(f"{cc} certificates of completion")
    return ", ".join(parts)

def kind_short(kind): return kind if kind != "CC" else T("Noncredit", "Sin crédito")

# ---------------------------------------------------------------------------
def tile(p, cls):
    wage = ""
    if p["pay"]:
        hr, t, yr, area = pay_line(p["pay"][0])
        if LANG == "es":
            wage = f'<p class="wage"><b>{hr}</b> salario medio de {t.lower()}{" en la región" if area == "metro" else " en California"}</p>'
        else:
            wage = f'<p class="wage"><b>{hr}</b> median for {"local " if area == "metro" else ""}{t.lower()}{" in California" if area == "CA" else ""}</p>'
    extra = f'<p class="wage">{T("Or transfer to a four-year design program with the Design Studies AA.", "O transfiérete a un programa universitario de diseño con el Design Studies AA.")}</p>' if p["key"] == "design" else ""
    free = f' <span class="badge">{T("Free", "Gratis")}</span>' if p["key"] == "software" else ""
    jobs = pf(p, "jobs") if p["key"] != "software" else T("Adobe Certified skills in Photoshop, Illustrator, InDesign, Premiere Pro, and After Effects. Noncredit, no experience needed.",
                                                       "Habilidades certificables por Adobe en Photoshop, Illustrator, InDesign, Premiere Pro y After Effects. Sin crédito y sin experiencia previa.")
    uniq = f'<p class="unique">{T("Only one in California. Online.", "Único en California. En línea.")}</p>' if p.get("unique") else ""
    return (f'<li class="{cls} c-{p["color"]}">{FLOWER}<div><h3><a href="{p["file"]}">{pn(p)}</a>{free}</h3>'
            f'<p class="jobs">{jobs}</p>{wage}{extra}{uniq}</div>'
            f'<p class="start"><span>{T("Start with", "Empieza con")} <b>{p["start"][0]}</b></span><span>{count_awards(p["awards"])}</span></p></li>')

def build_home():
    tiles = "".join(tile(p, "t-" + p["key"]) for p in PATHS)
    s = S.HOME
    body = f'''<div class="field home" id="paths"><div class="wrap hero-grid">
  <div>
    <h1>{s["h1"]}</h1>
    <p class="lede">{s["lede"]}</p>
  </div>
  <aside class="mini" aria-labelledby="here-h">
    <h2 id="here-h">{T("Exploring? Start with DDP 100.", "¿Explorando? Empieza con DDP 100.")}</h2>
    <p>{T("It samples every program and is open to everyone.", "Te da una muestra de todos los programas y está abierta a todos.")}</p>
    <a class="btn btn-gold" href="{S.sched("100")}">{T("Find a DDP 100 section", "Busca una sección de DDP 100")}</a>
  </aside>
</div></div>
<div class="tiles"><div class="wrap">
  <h2 class="sr">{T("Programs by career path", "Programas por trayectoria profesional")}</h2>
  <ul class="blooms">{tiles}</ul>
  <p class="src">{T("Pay", "Salarios")}: {jobs_source()} {T("The metro includes the Coachella Valley. Animators usually need a bachelor's degree.", "El área metropolitana incluye el Valle de Coachella. Los animadores suelen necesitar una licenciatura.")} <a href="programs.html">{T("Compare all programs", "Compara todos los programas")}</a>.</p>
</div></div>

<section class="tight" aria-label="{T("More ways in", "Más formas de empezar")}"><div class="wrap two">
  <article class="panel-gold"><h3>{T("Adobe classes that cost nothing", "Clases de Adobe sin costo")}</h3><p>{T("Noncredit classes are tuition-free, need no experience, and can be repeated. Finish part A and part B to earn a Certificate of Completion and prepare for the Adobe Certified exam.", "Las clases sin crédito no cobran colegiatura, no requieren experiencia y puedes repetirlas. Completa la parte A y la parte B para obtener un Certificado de Finalización y prepararte para el examen Adobe Certified.")}</p><a href="software.html">{T("How noncredit works", "Cómo funcionan las clases sin crédito")}</a></article>
  <article class="panel-red"><h3>{T("Coming fall 2027: the Palm Springs campus", "Otoño de 2027: el campus de Palm Springs")}</h3><p>{T("COD's new campus at Farrell Drive and Tahquitz Canyon Way is planned to open in fall 2027, with studios and maker spaces for digital media and arts.", "El nuevo campus de COD en Farrell Drive y Tahquitz Canyon Way abrirá en otoño de 2027, según lo planeado, con estudios y talleres para medios digitales y artes.")}</p><a href="{S.COD}/students/locations/palm-springs/">{T("COD in Palm Springs", "COD en Palm Springs")}</a></article>
</div></section>

<section class="tight" id="start" aria-labelledby="start-h"><div class="wrap">
  <h2 class="h2" id="start-h">{T("Get started in four steps", "Empieza en cuatro pasos")}</h2>
  <p class="sub">{T("From your first class to a finished certificate.", "De tu primera clase a un certificado terminado.")} <a href="get-started.html">{T("See the details", "Ve los detalles")}</a>.</p>
  <ol class="steps">{"".join(f'<li><h3>{h}</h3><p>{t}</p></li>' for h, t, _ in S.STEPS)}</ol>
</div></section>

{pay_section()}'''
    return page("index.html", T("Home", "Inicio"), body, "home", s["lede"])

def pay_section(keys=("graphic", "webdev", "animator"), heading=None):
    heading = heading or T("What creative work pays here", "Cuánto paga el trabajo creativo aquí")
    items = "".join(f'<li><strong>{JOBS[k][2]}{T("/hr", "/hora")}</strong><span>{short_title(jtitle(k))} ({JOBS[k][3]} {T("a year", "al año")})</span></li>' for k in keys)
    return f'''<section class="pay-wrap" aria-labelledby="pay-h"><div class="wrap">
  <h2 class="h2" id="pay-h">{heading}</h2>
  <p class="sub">{T("Median pay in the Riverside-San Bernardino-Ontario metro, which includes the Coachella Valley.", "Salario medio en el área metropolitana de Riverside-San Bernardino-Ontario, que incluye el Valle de Coachella.")} <a href="careers.html">{T("More on careers", "Más sobre carreras")}</a>.</p>
  <ul class="pay">{items}</ul>
  <p class="src">{T("Source", "Fuente")}: {jobs_source()}</p>
</div></section>'''

# ---------------------------------------------------------------------------
ICON = {
 "catalog": '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4.5A2.5 2.5 0 0 1 6.5 2H20v17H6.5A2.5 2.5 0 0 0 4 21.5z"/><path d="M4 21.5A2.5 2.5 0 0 1 6.5 19H20v3H6.5"/></svg>',
 "schedule": '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="17" rx="2"/><path d="M16 2v4M8 2v4M3 10h18M8 14h2M14 14h2M8 17h2"/></svg>',
 "syllabus": '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h5"/></svg>',
}

def tools(code=None):
    """The three class tools, always named and explained the same way."""
    cat = S.cat_search(code) if code else COURSES_URL
    sch = S.sched(code) if code else S.SCHEDULE_DDP
    who = (T(" for ", " para ") + ddp(code)) if code else ""
    if code:
        find = T(f"Search for &ldquo;{ddp(code)}&rdquo;.", f"Busca &ldquo;{ddp(code)}&rdquo;.")
    else:
        find = T("Search by course code, like &ldquo;DDP 100&rdquo;.", "Busca por código de curso, como &ldquo;DDP 100&rdquo;.")
    return f'''<ul class="ctools">
  <li><a href="{cat}"><span class="ic">{ICON["catalog"]}</span><b>{T("Catalog", "Catálogo")}<span class="sr">{who}</span></b><span>{T("Official description, units, and requirements", "Descripción oficial, unidades y requisitos")}</span></a></li>
  <li><a href="{sch}"><span class="ic">{ICON["schedule"]}</span><b>{T("Class schedule", "Horario de clases")}<span class="sr">{who}</span></b><span>{T("Days, times, online sections, and registration", "Días, horarios, secciones en línea e inscripción")}</span></a></li>
  <li><a href="{S.SYLLABI}"><span class="ic">{ICON["syllabus"]}</span><b>{T("Syllabus library", "Biblioteca de programas de curso")}<span class="sr">{who}</span></b><span>{T("What past classes covered.", "Lo que cubrieron las clases anteriores.")} {find}</span></a></li>
</ul>'''

def bloom_art():
    """Decorative desert-bloom cluster for program headers."""
    fl = [(330, 120, 1.9, .22), (210, 60, 1.1, .16), (420, 250, 1.3, .18), (250, 230, .8, .26), (120, 170, .7, .14), (380, 30, .6, .2), (470, 140, .5, .3)]
    g = "".join(f'<g transform="translate({x} {y}) scale({sc})" opacity="{o}"><circle cx="0" cy="-26" r="22"/><circle cx="26" cy="0" r="22"/><circle cx="0" cy="26" r="22"/><circle cx="-26" cy="0" r="22"/></g>' for x, y, sc, o in fl)
    c = "".join(f'<circle cx="{x}" cy="{y}" r="{15*sc}" class="ctr"/>' for x, y, sc, o in fl[:4])
    return f'<svg class="blooms-art" viewBox="0 0 520 320" aria-hidden="true" focusable="false"><g fill="currentColor">{g}</g>{c}</svg>'

def award_card(k):
    a = AWARDS[k]
    un = T("no units", "sin unidades") if a["kind"] == "CC" else units(a["units"])
    tr = f' <span class="badge">{T("Transfer", "Transferencia")}</span>' if a.get("transfer") else ""
    nc = f' <span class="badge nc">{T("Tuition-free", "Sin colegiatura")}</span>' if a["kind"] == "CC" else ""
    nc += f' <span class="badge">{T("Only one in California", "Único en California")}</span> <span class="badge">{T("Online", "En línea")}</span>' if a.get("unique") else ""
    core = "".join(f"<li>{course_link(c)}</li>" for c in a["core"])
    choose = ""
    if a.get("choose"):
        n, cs = a["choose"]
        choose = f'<p class="req">{T("Plus one of", "Más uno de")}: {", ".join(course_link(c) for c in cs)}</p>'
    other = f'<p class="req">{T("Also requires", "También requiere")} {", ".join(a["other"])}.</p>' if a.get("other") else ""
    elect = f'<p class="req">{T("Plus electives", "Más optativas")}: {T(a["electives"], a["electives"].replace("units", "unidades").replace("one course", "un curso"))}.</p>' if a.get("electives") else ""
    ge = f'<p class="req">{T("Degree also includes", "El título también incluye educación general")} {a["ge"]}{T(" general education", "")}.</p>' if a.get("ge") else ""
    desc = adesc(k) or T(f'Earn this certificate by completing {ddp(a["core"][0])} and {ddp(a["core"][1])}.',
                         f'Obtén este certificado al completar {ddp(a["core"][0])} y {ddp(a["core"][1])}.')
    return f'''<li class="award" id="{k}">
  <p class="kind">{kname(a["kind"])}, {un}{tr}{nc}</p>
  <h3>{a["name"]}</h3>
  <p>{desc}</p>
  <p class="req">{T("Required DDP courses", "Cursos de DDP requeridos")}:</p>
  <ul class="chips">{core}</ul>
  {choose}{elect}{other}{ge}
  <p class="go"><a href="#ksa-{k}">{T("What you&#39;ll learn", "Lo que aprenderás")}<span class="sr"> {T("in", "en")} {strip(a["name"])}</span></a><a href="{a["url"]}"><span class="ic">{ICON["catalog"]}</span>{T("Catalog requirements", "Requisitos en el catálogo")}<span class="sr"> {T("for", "para")} {strip(a["name"])}</span></a></p>
</li>'''

def ksa_block(k, open_=False):
    a = AWARDS[k]; q = ksa(k)
    col = lambda h, d, items: f'<div><h4>{h}</h4><p class="d">{d}</p><ul class="ticks">' + "".join(f"<li>{i}</li>" for i in items) + "</ul></div>"
    return f'''<details class="ksa" id="ksa-{k}"{" open" if open_ else ""}>
  <summary><span class="k">{kind_short(a["kind"])}</span><h3>{a["name"]}</h3></summary>
  <div class="kgrid">
    {col(T("Knowledge", "Conocimientos"), T("What you&#39;ll understand", "Lo que vas a entender"), q["k"])}
    {col(T("Skills", "Habilidades"), T("What you&#39;ll be able to do", "Lo que podrás hacer"), q["s"])}
    {col(T("Abilities", "Capacidades"), T("How you&#39;ll use it on the job", "Cómo lo usarás en el trabajo"), q["a"])}
  </div>
</details>'''

def confidence(p, sc):
    if p["key"] == "software":
        first = T("No experience needed. Noncredit classes are tuition-free and can be repeated.", "No necesitas experiencia. Las clases sin crédito no cobran colegiatura y puedes repetirlas.")
    else:
        first = T(f"{sc} has no prerequisite. Bring your curiosity; your instructors will teach you the tools.", f"{sc} no tiene requisito previo. Trae tu curiosidad; tus instructores te enseñarán las herramientas.")
    return f'''<section class="confide" aria-labelledby="cf-h"><div class="wrap">
  <h2 class="h2" id="cf-h">{T("Every designer started with a first class.", "Todo diseñador empezó con una primera clase.")}</h2>
  <ul class="cf">
    <li><h3>{T("Start where you are", "Empieza donde estás")}</h3><p>{first}</p></li>
    <li><h3>{T("Learn by making", "Aprende haciendo")}</h3><p>{T("Most 3-unit DDP courses include 54 hours of hands-on lab time, so you build real projects from week one.", "La mayoría de los cursos de DDP de 3 unidades incluyen 54 horas de laboratorio práctico, así que creas proyectos reales desde la primera semana.")}</p></li>
    <li><h3>{T("Help is here", "Aquí tienes apoyo")}</h3><p>{T("Free tutoring at the", "Tutoría gratuita en el")} <a href="{S.L["tutoring"]}">Academic Skills Center</a>{T(", instructors who work in the field, and a", ", instructores que trabajan en el campo y una")} <a href="contact.html">{T("program advisor", "asesora del programa")}</a> {T("to help you plan.", "para ayudarte a planear.")}</p></li>
  </ul>
</div></section>'''

def build_path(p):
    others = "".join(f'<li class="c-{o["color"]}"><a href="{o["file"]}">{pn(o)}</a></li>' for o in PATHS if o is not p)
    if p["pay"]:
        hr, t, yr, area = pay_line(p["pay"][0])
        if LANG == "es":
            place = "en el Inland Empire y el Valle de Coachella" if area == "metro" else "en California"
            aside = f'<aside><p><b>{hr}</b>salario medio por hora de {t.lower()} {place}</p><p><a href="#car-h">Carreras y salarios</a></p></aside>'
        else:
            place = "in the Inland Empire and Coachella Valley" if area == "metro" else "in California"
            aside = f'<aside><p><b>{hr}</b>median hourly pay for {t.lower()} {place}</p><p><a href="#car-h">Careers and pay</a></p></aside>'
    else:
        aside = ""
    sc, st = p["start"]
    start_code = sc.replace("DDP ", "")
    st_course = COURSES[start_code]
    trtext = {"CSU/UC": T("Transfers to CSU and UC", "Se transfiere a CSU y UC"), "CSU": T("Transfers to CSU", "Se transfiere a CSU"),
              "": T("Noncredit, tuition-free", "Sin crédito, sin colegiatura") if st_course[1] == "0" else T("Career course", "Curso profesional")}[st_course[2]]
    codes = [c for c in COURSES if p["key"] in course_paths(c)]
    rows = "".join(
        f'<tr><td>{course_link(c)}</td><td>{COURSES[c][0]}</td><td>{T("Noncredit", "Sin crédito") if COURSES[c][1]=="0" else units(COURSES[c][1])}</td><td>{COURSES[c][2] or "&nbsp;"}</td>'
        f'<td class="lk"><a href="{S.cat_search(c)}">{T("Catalog", "Catálogo")}<span class="sr"> {T("for", "para")} {ddp(c)}</span></a></td><td class="lk"><a href="{S.sched(c)}">{T("Schedule", "Horario")}<span class="sr"> {T("for", "para")} {ddp(c)}</span></a></td></tr>'
        for c in codes)
    trn = f'<p class="note">{pf(p, "transfer_note")} <a href="#tr-h">{T("Transfer options", "Opciones de transferencia")}</a>.</p>' if p.get("transfer_note") else ""
    software_extra = ""
    if p["key"] == "software":
        software_extra = f'''<section class="tight" aria-labelledby="how-h"><div class="wrap prose">
  <h2 class="h2" id="how-h">{T("How noncredit works", "Cómo funcionan las clases sin crédito")}</h2>
  <p>{T("Noncredit classes have no tuition and no units. They are graded pass or no pass, and you can repeat them. Each Certificate of Completion pairs an A class, which teaches the basics, with a B class, which adds practice exams and portfolio projects for the Adobe Certified exam.",
        "Las clases sin crédito no cobran colegiatura ni otorgan unidades. Se califican como aprobado o no aprobado, y puedes repetirlas. Cada Certificado de Finalización combina una clase A, que enseña lo básico, con una clase B, que agrega exámenes de práctica y proyectos de portafolio para el examen Adobe Certified.")}</p>
  <p>{T("Noncredit classes use a separate, shorter application.", "Las clases sin crédito usan una solicitud aparte y más corta.")} <a href="{S.COD}/students/admissions/noncredit/">{T("Register for noncredit at COD", "Inscríbete en clases sin crédito en COD")}</a>.</p>
  <p>{T("Ready for more? Credit courses like", "¿Listo para más? Cursos con crédito como")} {course_link("101")} (Photoshop), {course_link("102")} (Illustrator) {T("and", "y")} {course_link("120")} (Premiere Pro) {T("count toward degrees and certificates.", "cuentan para títulos y certificados.")}</p>
</div></section>'''
    pnav = "".join(f'<li><a href="#{i}">{t}</a></li>' for i, t in [("start-h", T("Start here", "Empieza aquí")), ("prog-h", T("Programs", "Programas")), ("learn-h", T("What you&#39;ll learn", "Lo que aprenderás")),
                                                                      ("crs-h", T("Courses", "Cursos")), ("car-h", T("Careers", "Carreras")), ("tr-h", T("Transfer", "Transferencia"))])
    unique = f'<p class="unique">{pf(p, "unique")}</p>' if p.get("unique") else ""
    body = f'''<div class="phero c-{p["color"]}"><div class="wrap">
  <div class="pt">
    {crumbs([home_crumb(), prog_crumb(), (pn(p), None)])}
    <h1>{pn(p)}</h1>
    {unique}
    <p class="lede">{pf(p, "intro")}</p>
    <p class="jobs-line"><strong>{T("Careers", "Carreras")}:</strong> {pf(p, "jobs")}</p>
  </div>
  <div class="pa">{bloom_art()}{aside}</div>
</div></div>
<nav class="pnav c-{p["color"]}" aria-label="{T("Sections of this page", "Secciones de esta página")}"><div class="wrap"><span class="dot" aria-hidden="true"></span><ul>{pnav}</ul></div></nav>

<section aria-labelledby="start-h"><div class="wrap here">
  <div>
    <h2 class="h2" id="start-h">{T("Start here", "Empieza aquí")}: {sc}</h2>
    <p class="sub" style="margin:0 0 1rem">{cblurb(start_code)} {T("It counts toward the programs on this path, so you can try the field before you commit.", "Cuenta para los programas de esta trayectoria, así que puedes probar el campo antes de decidir.")}</p>
  </div>
  <div class="ticket">
    <p class="code">{sc}</p>
    <p class="t">{st}, {T("noncredit", "sin crédito") if st_course[1]=="0" else units(st_course[1])}</p>
    <ul class="chips"><li>{trtext}</li>{"<li>COD GE " + T("Area ", "Área ") + st_course[3] + "</li>" if st_course[3] else ""}<li>{T("No prerequisite", "Sin requisito previo")}</li></ul>
    {tools(start_code)}
  </div>
</div></section>

{confidence(p, sc)}

{software_extra}

<section class="c-{p["color"]}" aria-labelledby="prog-h"><div class="wrap">
  <h2 class="h2" id="prog-h">{T("Degrees and certificates", "Títulos y certificados")}</h2>
  <p class="sub">{count_awards(p["awards"]).capitalize()}. {T("Requirements come from the 2026-2027 catalog, the official source.", "Los requisitos vienen del catálogo 2026-2027, la fuente oficial.")}</p>
  <ul class="awards">{"".join(award_card(k) for k in p["awards"])}</ul>
  {trn}
</div></section>

<section class="tight" aria-labelledby="learn-h"><div class="wrap">
  <h2 class="h2" id="learn-h">{T("What you&#39;ll learn", "Lo que aprenderás")}</h2>
  <p class="sub">{T("The knowledge, skills, and abilities each program builds. Open a program to see its list.", "Los conocimientos, habilidades y capacidades que desarrolla cada programa. Abre un programa para ver su lista.")}</p>
  {"".join(ksa_block(k, i == 0) for i, k in enumerate(p["awards"]))}
</div></section>

<section class="tight" aria-labelledby="crs-h"><div class="wrap">
  <h2 class="h2" id="crs-h">{T("Courses on this path", "Cursos de esta trayectoria")}</h2>
  <p class="sub">{T("Every DDP course used by these programs. Three tools help you plan:", "Todos los cursos de DDP que usan estos programas. Tres herramientas te ayudan a planear:")}</p>
  {tools(None)}
  <table class="list crs"><caption class="sr">{T("DDP courses for", "Cursos de DDP para")} {strip(pn(p))}</caption>
    <thead><tr><th scope="col">{T("Course", "Curso")}</th><th scope="col">{T("Title", "Título")}</th><th scope="col">{T("Units", "Unidades")}</th><th scope="col">{T("Transfers to", "Se transfiere a")}</th><th scope="col">{T("Catalog", "Catálogo")}</th><th scope="col">{T("Schedule", "Horario")}</th></tr></thead>
    <tbody>{rows}</tbody></table>
  <p class="src">{T("Select a course number for a short description in the", "Selecciona un número de curso para ver una breve descripción en el")} <a href="courses.html">{T("course finder", "buscador de cursos")}</a>.{T("", " Los títulos oficiales de los cursos están en inglés, como en el catálogo.")}</p>
</div></section>

{path_careers(p)}

{path_transfer(p, codes)}

<section aria-labelledby="oth-h"><div class="wrap">
  <h2 class="h2" id="oth-h">{T("Explore other programs", "Explora otros programas")}</h2>
  <ul class="others">{others}</ul>
</div></section>'''
    return page(p["file"], strip(pn(p)), body, "programs", pf(p, "intro"))


def path_careers(p):
    c = careers(p["key"])
    ladder = "".join(f'<li><h4>{st}</h4><p>{t}</p></li>' for st, t in c["ladder"])
    emp = "".join(f"<li>{e}</li>" for e in c["employers"])
    sk = "".join(f"<li>{e}</li>" for e in c["skills"])
    return f'''<section class="pay-wrap" aria-labelledby="car-h"><div class="wrap">
  <h2 class="h2" id="car-h">{T("Careers", "Carreras")}</h2>
  <p class="sub">{c["work"]}</p>
  <h3 class="h3">{T("Jobs and pay", "Empleos y salarios")}</h3>
  {jobs_table(p["pay"], T("Jobs, pay, and outlook for ", "Empleos, salarios y perspectivas para ") + strip(pn(p)))}
  <p class="src">{T("Pay is the median for the Riverside-San Bernardino-Ontario metro, which includes the Coachella Valley, unless marked California. Outlook, openings, self-employment, and education are national.", "El salario es la mediana del área metropolitana de Riverside-San Bernardino-Ontario, que incluye el Valle de Coachella, salvo donde dice California. Las perspectivas, vacantes, trabajo por cuenta propia y estudios son nacionales.")} {T("Source", "Fuente")}: {jobs_source()}</p>
  <p class="note">{T("&ldquo;Typical entry education&rdquo; is what most people in the job have. Creative employers hire from portfolios, so a COD certificate plus strong work can start your career, and a transfer degree keeps the bachelor&#39;s option open.", "&ldquo;Estudios típicos para empezar&rdquo; es lo que tiene la mayoría de las personas en ese empleo. Los empleadores creativos contratan por el portafolio, así que un certificado de COD y un buen trabajo pueden iniciar tu carrera, y un título de transferencia mantiene abierta la opción de la licenciatura.")} {c["note"]}</p>
  <div class="cgrid">
    <div><h3 class="h3">{T("Career ladder", "Escalera profesional")}</h3><ol class="ladder">{ladder}</ol></div>
    <div><h3 class="h3">{T("Where the jobs are", "Dónde están los empleos")}</h3><ul class="ticks">{emp}</ul></div>
    <div><h3 class="h3">{T("Skills employers want", "Habilidades que buscan los empleadores")}</h3><ul class="ticks">{sk}</ul></div>
  </div>
  <ul class="links four" style="margin-top:2rem">
    <li><a href="{S.L["handshake"]}"><b>{T("Find jobs on Handshake", "Busca empleos en Handshake")}</b><span>{T("Jobs and internships for COD students. Sign in with your COD account.", "Empleos y prácticas para estudiantes de COD. Inicia sesión con tu cuenta de COD.")}</span></a></li>
    <li><a href="courses.html#ddp-195"><b>DDP 195</b><span>{T("Business practices and portfolio preparation: freelancing, pricing, clients, and your portfolio.", "Prácticas de negocio y preparación de portafolio: trabajo independiente, precios, clientes y tu portafolio.")}</span></a></li>
    <li><a href="courses.html#ddp-095a"><b>DDP 095A</b><span>{T("Earn units for a design job or internship.", "Gana unidades por un empleo o una práctica en diseño.")}</span></a></li>
    <li><a href="{S.L["career"]}"><b>{T("Career center", "Centro de carreras")}</b><span>{T("Career counseling, resumes, and job fairs at COD.", "Orientación profesional, currículums y ferias de empleo en COD.")}</span></a></li>
  </ul>
</div></section>'''

def path_transfer(p, codes):
    tr_awards = [k for k in p["awards"] if AWARDS[k].get("transfer")]
    csu = [c for c in codes if "CSU" in COURSES[c][2]]
    uc = [c for c in codes if "UC" in COURSES[c][2]]
    if p["key"] == "software":
        body = (T("<p>Noncredit classes do not earn transfer credit. When you are ready, credit courses like ", "<p>Las clases sin crédito no otorgan crédito de transferencia. Cuando estés listo, cursos con crédito como ")
                + course_link("101") + T(" and ", " y ") + course_link("102") + T(" count toward degrees and transfer to the CSU.</p>", " cuentan para títulos y se transfieren a la CSU.</p>"))
    else:
        lead = ""
        if tr_awards:
            if LANG == "es":
                joined = " y ".join(f'el <a href="#{k}">{AWARDS[k]["name"]} {AWARDS[k]["kind"]}</a>' for k in tr_awards)
                lead = "<p>" + joined[0].upper() + joined[1:] + (" están diseñados" if len(tr_awards) > 1 else " está diseñado") + " para transferirte, con educación general Cal-GETC.</p>"
            else:
                joined = " and ".join(f'the <a href="#{k}">{AWARDS[k]["name"]} {AWARDS[k]["kind"]}</a>' for k in tr_awards)
                lead = "<p>" + joined[0].upper() + joined[1:] + (" are" if len(tr_awards) > 1 else " is") + " built for transfer, using Cal-GETC general education.</p>"
        body = lead + T(f"<p>{len(csu)} of the {len(codes)} DDP courses on this path transfer to the CSU, and {len(uc)} also transfer to the UC. Each university decides which courses count toward its major, so check <a href=\"{S.L['assist']}\">ASSIST.org</a> and meet with a counselor.</p>",
                        f"<p>{len(csu)} de los {len(codes)} cursos de DDP de esta trayectoria se transfieren a la CSU, y {len(uc)} también a la UC. Cada universidad decide qué cursos cuentan para su carrera, así que revisa <a href=\"{S.L['assist']}\">ASSIST.org</a> y reúnete con un consejero.</p>")
    return f'''<section class="tight" aria-labelledby="tr-h" style="padding-top:clamp(2.75rem,6vw,4.5rem)"><div class="wrap prose">
  <h2 class="h2" id="tr-h">{T("Transfer", "Transferencia")}</h2>
  {body}
  <p><a href="transfer.html">{T("How transfer works", "Cómo funciona la transferencia")}</a></p>
</div></section>'''

# ---------------------------------------------------------------------------
def build_programs():
    rows = []
    for p in PATHS:
        aw = "".join(f'<li><a href="{p["file"]}#{k}"><span class="k">{kind_short(AWARDS[k]["kind"])}</span>{AWARDS[k]["name"]}</a></li>' for k in p["awards"])
        unique = f'<p class="unique">{pf(p, "unique")}</p>' if p.get("unique") else ""
        rows.append(f'''<li class="prog c-{p["color"]}">
  <div class="sw" aria-hidden="true"></div>
  <div class="pi">
    <h2><a href="{p["file"]}">{pn(p)}</a></h2>
    {unique}
    <p>{pf(p, "pitch")}</p>
    <p class="meta"><span>{T("Start with", "Empieza con")} <b>{p["start"][0]}</b></span><span>{count_awards(p["awards"])}</span></p>
  </div>
  <ul class="aw">{aw}</ul>
</li>''')
    key = "".join(f"<li><b>{k}</b> {v}</li>" for k, v in [("AA / AS", T("Associate degree", "Título de asociado")), ("CA", T("Certificate of Achievement", "Certificado de Logro")),
                                                          (T("Noncredit", "Sin crédito"), T("Certificate of Completion, tuition-free", "Certificado de Finalización, sin colegiatura"))])
    body = simple_hero(T("Programs", "Programas"), T(f"Six career paths and {len(AWARDS)} degrees and certificates. Pick a path to see its programs, courses, careers, and transfer options.",
                                                     f"Seis trayectorias profesionales y {len(AWARDS)} títulos y certificados. Elige una trayectoria para ver sus programas, cursos, carreras y opciones de transferencia."),
                       [home_crumb(), (T("Programs", "Programas"), None)], "programs.html") + f'''
<section><div class="wrap">
  <ul class="progs">{"".join(rows)}</ul>
  <ul class="key">{key}</ul>
  {T("", '<p class="src">Los nombres oficiales de los programas están en inglés, como en el catálogo.</p>')}
</div></section>
<section class="pay-wrap"><div class="wrap">
  <h2 class="h2">{T("Not sure where to start?", "¿No sabes por dónde empezar?")}</h2>
  <ul class="links">
    <li><a href="{S.sched("100")}"><b>{T("Take DDP 100", "Toma DDP 100")}</b><span>{T("Introduction to Digital Art &amp; Media samples every path. Open to everyone; transfers to CSU and UC.", "Introduction to Digital Art &amp; Media te da una muestra de todas las trayectorias. Abierta a todos; se transfiere a CSU y UC.")}</span></a></li>
    <li><a href="courses.html"><b>{T("Browse every course", "Explora todos los cursos")}</b><span>{T(f"Filter all {len(COURSES)} DDP courses by path, transfer, and general education.", f"Filtra los {len(COURSES)} cursos de DDP por trayectoria, transferencia y educación general.")}</span></a></li>
    <li><a href="contact.html"><b>{T("Talk with the program advisor", "Habla con la asesora del programa")}</b><span>{ADVISOR["name"]}, {ADVISOR["email"]}</span></a></li>
  </ul>
</div></section>'''
    return page("programs.html", T("Programs", "Programas"), body, "programs", T("Digital Design &amp; Production programs at College of the Desert by career path.", "Programas de Digital Design &amp; Production en College of the Desert por trayectoria profesional."))

# ---------------------------------------------------------------------------
def build_courses():
    order = sorted(COURSES, key=lambda c: (int(re.sub(r"\D", "", c)), c))
    items = []
    for c in order:
        t, u, tr, ge, prim, _ = COURSES[c]
        paths = course_paths(c)
        color = PBY[prim]["color"] if prim in PBY else "gold"
        trd = " ".join(x.lower() for x in tr.split("/")) if tr else ""
        meta = [T("Noncredit", "Sin crédito") if u == "0" else units(u)]
        if tr: meta.append(f'{T("Transfers", "Se transfiere")}: {tr}')
        if ge: meta.append(f"COD GE {ge}")
        used = awards_using(c)
        used_html = (f'<p class="used">{T("Counts toward", "Cuenta para")}: ' + ", ".join(
            f'<a href="{PBY[AWARD_PATH[k]]["file"]}#{k}">{AWARDS[k]["name"]}</a>' for k in used) + "</p>") if used else ""
        items.append(f'''<li class="course c-{color}" id="{cid(c)}" data-path="{" ".join(paths)}" data-tr="{trd}"{' data-ge' if ge else ""}>
  <h3><span class="code">{ddp(c)}</span>{t}</h3>
  <p>{cblurb(c)}</p>
  <p class="meta">{"".join(f"<span>{m}</span>" for m in meta)}</p>
  {used_html}
  <p class="acts"><a href="{S.cat_search(c)}"><span class="ic">{ICON["catalog"]}</span>{T("Catalog", "Catálogo")}<span class="sr"> {T("for", "para")} {ddp(c)}</span></a><a href="{S.sched(c)}"><span class="ic">{ICON["schedule"]}</span>{T("Schedule", "Horario")}<span class="sr"> {T("for", "para")} {ddp(c)}</span></a><a href="{S.SYLLABI}"><span class="ic">{ICON["syllabus"]}</span>{T("Syllabi", "Programas de curso")}<span class="sr"> ({T("search for", "busca")} {ddp(c)})</span></a></p>
</li>''')
    popts = [("all", T("All areas", "Todas las áreas"))] + [(p["key"], strip(pn(p)).replace("Job-Ready Software Skills", "Noncredit Software")) for p in PATHS] + [("career", T("Career &amp; portfolio", "Carrera y portafolio"))]
    pr = "".join(f'<input type="radio" name="area" id="f-{k}" value="{k}"{" checked" if k=="all" else ""}><label for="f-{k}">{n}</label>' for k, n in popts)
    tr = "".join(f'<input type="radio" name="tr" id="t-{k}" value="{k}"{" checked" if k=="any" else ""}><label for="t-{k}">{n}</label>' for k, n in
                 [("any", T("Any", "Cualquiera")), ("csu", T("Transfers to CSU", "Se transfiere a CSU")), ("uc", T("Transfers to UC", "Se transfiere a UC")), ("ge", T("Counts for COD GE", "Cuenta para GE de COD"))])
    title = T("Course finder", "Buscador de cursos")
    body = f'''{simple_hero(title, T(f"All {len(COURSES)} DDP courses in the 2026-2027 catalog. Filter by career path or by transfer, then find open sections in the class schedule.", f"Los {len(COURSES)} cursos de DDP del catálogo 2026-2027. Filtra por trayectoria profesional o por transferencia, y luego busca secciones abiertas en el horario de clases."), [home_crumb(), prog_crumb(), (title, None)], "courses.html")}
<section><div class="wrap">
  <fieldset class="filters"><legend>{T("Career path", "Trayectoria profesional")}</legend><div class="opts">{pr}</div></fieldset>
  <fieldset class="filters"><legend>{T("Transfer and general education", "Transferencia y educación general")}</legend><div class="opts">{tr}</div></fieldset>
  {tools(None)}
  <h2 class="sr">{T("Courses", "Cursos")}</h2>
  <ul class="courses">{"".join(items)}</ul>
  <p class="src">{T("Source", "Fuente")}: <a href="{COURSES_URL}">College of the Desert 2026-2027 Catalog, Digital Design &amp; Production courses</a>. {T("Descriptions are shortened; the catalog lists prerequisites, advisories, and hours.", "Las descripciones son breves; el catálogo indica requisitos previos, recomendaciones y horas. Los títulos oficiales de los cursos están en inglés.")}</p>
</div></section>'''
    return page("courses.html", title, body, "programs", T("Find DDP courses by career path, transfer, and general education.", "Encuentra cursos de DDP por trayectoria profesional, transferencia y educación general."))

# ---------------------------------------------------------------------------
# Faculty & Staff
LI_ICON = '<svg viewBox="0 0 24 24" aria-hidden="true" width="16" height="16"><path fill="currentColor" d="M4.98 3.5A2.5 2.5 0 1 1 5 8.5a2.5 2.5 0 0 1-.02-5zM3 9.75h4V21H3zM9.5 9.75h3.83v1.54h.06c.53-1 1.84-2.06 3.79-2.06 4.05 0 4.8 2.66 4.8 6.13V21h-4v-4.9c0-1.17-.02-2.67-1.63-2.67-1.63 0-1.88 1.27-1.88 2.59V21h-4z"/></svg>'

def person_slug(n): return re.sub(r"[^a-z]+", "-", n.lower().replace("dr. ", "")).strip("-")
def initials2(n): return "".join(w[0] for w in n.replace("Dr. ", "").split()[:2])
def photo_of(n):
    f = f"img/people/{person_slug(n)}.jpg"
    return f if os.path.exists(os.path.join(DOCS, f)) else None

def main_path(courses):
    cnt = {}
    for c in courses:
        k = COURSES[c][4]
        if k in PBY: cnt[k] = cnt.get(k, 0) + 1
    return max(cnt, key=cnt.get) if cnt else "design"

def portrait(name, color):
    src = photo_of(name)
    if src: return f'<div class="ph c-{color}"><img src="{R}{src}" alt="" loading="lazy" width="600" height="750"></div>'
    return f'<div class="ph c-{color}" aria-hidden="true"><span>{initials2(name)}</span></div>'

def contact_links(email, name, phone=""):
    li = LINKEDIN.get(email)
    out = f'<a href="mailto:{email}">{email}</a>'
    if phone: out += f'<span>{phone}</span>'
    if li: out += f'<a class="li" href="https://www.linkedin.com/in/{li}/">{LI_ICON}LinkedIn<span class="sr">: {name}</span></a>'
    return f'<p class="ct">{out}</p>'

def build_contact():
    lead = "".join(f'''<li class="person lead">{portrait(n, "white")}<div class="pm"><h3>{n}</h3><p class="rl">{role(t)}</p>{contact_links(e, n, ph)}</div></li>''' for n, t, e, ph in LEADERSHIP)
    cards = []
    for n, e, t, cs, terms in sorted(FACULTY, key=lambda f: f[0].replace("Dr. ", "").split()[-1]):
        mp = main_path(cs)
        paths = sorted({COURSES[c][4] for c in cs if COURSES[c][4] in PBY} | {mp})
        chips = "".join(f'<li>{course_link(c)}</li>' for c in cs)
        cards.append(f'''<li class="person" data-path="{" ".join(paths)}">{portrait(n, PBY[mp]["color"])}<div class="pm">
  <h3>{n}</h3><p class="rl">{role(t)}</p>
  <p class="tc">{T("Teaches", "Enseña")}</p><ul class="chips">{chips}</ul>
  {contact_links(e, n)}
</div></li>''')
    taught = {COURSES[c][4] for f in FACULTY for c in f[3]} | {main_path(f[3]) for f in FACULTY}
    opts = [("all", T("All faculty", "Todos los docentes"))] + [(p["key"], strip(pn(p))) for p in PATHS if p["key"] in taught]
    radios = "".join(f'<input type="radio" name="fp" id="fp-{k}"{" checked" if k=="all" else ""}><label for="fp-{k}">{v}</label>' for k, v in opts)
    hide = ",\n".join(f'body:has(#fp-{k}:checked) .people.fac .person:not([data-path~="{k}"])' for k, _ in opts[1:])
    title = T("Faculty, Staff &amp; Contact", "Docentes, personal y contacto")
    a = ADVISOR
    body = simple_hero(title, T("Questions about a program, a class, or your portfolio? Start with the program advisor, then meet the faculty.",
                                "¿Preguntas sobre un programa, una clase o tu portafolio? Empieza con la asesora del programa y conoce a los docentes."),
                       [home_crumb(), (title, None)]) + f'''
<style>{hide}{{display:none}}</style>
<section aria-labelledby="help-h"><div class="wrap">
  <h2 class="h2" id="help-h">{T("Get help", "Pide ayuda")}</h2>
  <ul class="links">
    <li><a href="mailto:{a["email"]}"><b>{T("Program advisor", "Asesora del programa")}: {a["name"]}</b><span>{T("Programs, classes, and portfolios.", "Programas, clases y portafolios.")} {a["email"]}, {a["phone"]}</span></a></li>
    <li><a href="{S.L["counseling"]}"><b>{T("Counseling", "Consejería")}</b><span>{T("Education plans, general education, and transfer.", "Planes educativos, educación general y transferencia.")}</span></a></li>
    <li><a href="mailto:ggraves@collegeofthedesert.edu?subject=DDP%20Online%20Gallery%20submission"><b>{T("Submit student work for the DDP Online Gallery", "Envía trabajos estudiantiles a la Galería en Línea de DDP")}</b><span>Prof. Gary Graves, ggraves@collegeofthedesert.edu</span></a></li>
  </ul>
</div></section>
<section class="tight" aria-labelledby="ld-h"><div class="wrap">
  <h2 class="h2" id="ld-h">{T("Department and school leadership", "Liderazgo del departamento y de la escuela")}</h2>
  <ul class="people leads">{lead}</ul>
</div></section>
<section class="pay-wrap" id="faculty" aria-labelledby="fac-h"><div class="wrap">
  <h2 class="h2" id="fac-h">{T("Faculty", "Docentes")}</h2>
  <p class="sub">{T(f"Meet the {len(FACULTY)} instructors who taught Digital Design &amp; Production courses in 2026. Many work as designers, photographers, animators, and developers. Filter by program to see who teaches what.", f"Conoce a los {len(FACULTY)} instructores que impartieron cursos de Digital Design &amp; Production en 2026. Muchos trabajan como diseñadores, fotógrafos, animadores y desarrolladores. Filtra por programa para ver quién enseña qué.")}</p>
  <fieldset class="filters"><legend>{T("Show faculty who teach", "Mostrar docentes que enseñan")}</legend><div class="opts">{radios}</div></fieldset>
  <ul class="people fac">{"".join(cards)}</ul>
  <p class="src">{T("Instructors who taught DDP sections in Spring, Summer, or Fall 2026, from the class schedule. Titles and emails from the College of the Desert directory. Faculty: send a headshot or LinkedIn link to", "Instructores que impartieron secciones de DDP en primavera, verano u otoño de 2026, según el horario de clases. Cargos y correos del directorio de College of the Desert. Docentes: envíen una foto o su enlace de LinkedIn a")} <a href="mailto:ggraves@collegeofthedesert.edu">ggraves@collegeofthedesert.edu</a>{T(" to add it.", " para agregarlo.")}</p>
</div></section>
<section aria-labelledby="loc-h"><div class="wrap">
  <h2 class="h2" id="loc-h">{T("Where DDP classes meet", "Dónde se dan las clases de DDP")}</h2>
  <ul class="links">
    <li><a href="{S.COD}/map/"><b>{T("Palm Desert campus", "Campus de Palm Desert")}</b><span>43-500 Monterey Ave, Palm Desert, CA 92260. {T("Main campus.", "Campus principal.")}</span></a></li>
    <li><a href="{S.L["palmsprings"]}"><b>Palm Springs</b><span>{T("Temporary campus at 1300 E. Baristo Rd. The new Palm Springs campus is planned to open in fall 2027.", "Campus temporal en 1300 E. Baristo Rd. El nuevo campus de Palm Springs abrirá en otoño de 2027, según lo planeado.")}</span></a></li>
    <li><a href="{S.SCHEDULE_DDP}"><b>{T("Online", "En línea")}</b><span>{T("Many DDP courses are offered online. Check the class schedule each term.", "Muchos cursos de DDP se ofrecen en línea. Revisa el horario de clases cada semestre.")}</span></a></li>
  </ul>
  <p class="note"><span class="ph">{T("Department office, labs, and hours to confirm.", "Oficina del departamento, laboratorios y horarios por confirmar.")}</span></p>
  <p>College of the Desert, 43-500 Monterey Ave, Palm Desert, CA 92260. 760.346.8041. <a href="{S.COD}/directory/">{T("Campus directory", "Directorio del campus")}</a></p>
</div></section>'''
    page("contact.html", title, body, "contact", T("Faculty, staff, and contact information for Digital Design &amp; Production at College of the Desert.", "Docentes, personal e información de contacto de Digital Design &amp; Production en College of the Desert."))
    # the old Faculty & Staff address forwards here
    with open(os.path.join(OUT, "faculty.html"), "w") as f:
        f.write(f'<!doctype html><html lang="{LANG}"><head><meta charset="utf-8"><meta name="robots" content="noindex"><meta http-equiv="refresh" content="0; url=contact.html#faculty"><title>{title}</title></head>'
                f'<body><p><a href="contact.html#faculty">{title}</a></p></body></html>')
    return "contact.html"

# ---------------------------------------------------------------------------
# Student work gallery
ART = {
 "poster": '<rect width="400" height="400" fill="#A30E22"/><circle cx="300" cy="120" r="120" fill="#FFC423"/><text x="40" y="270" font-family="Jost,sans-serif" font-weight="600" font-size="54" fill="#fff">desert</text><text x="40" y="318" font-family="Jost,sans-serif" font-weight="600" font-size="54" fill="#fff">x film fest</text><rect x="40" y="340" width="120" height="6" fill="#FFC423"/>',
 "dusk": '<defs><linearGradient id="gd" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3b2a5a"/><stop offset=".45" stop-color="#e98b6a"/><stop offset=".62" stop-color="#f6c58e"/></linearGradient></defs><rect width="400" height="400" fill="url(#gd)"/><path d="M0 270 L80 220 L150 250 L240 200 L330 245 L400 225 L400 400 L0 400Z" fill="#2c2433"/><path d="M250 400 V250 M250 290 l-30 -26 M250 280 l26 -30 M220 264 l-8 -16 M276 250 l10 -14" stroke="#1a1520" stroke-width="9" stroke-linecap="round" fill="none"/>',
 "motion": '<rect width="400" height="400" fill="#16181b"/><g fill="#FFC423">' + "".join(f'<rect x="{30+i*44}" y="170" width="30" height="{40+ (i%3)*14}" rx="3"/>' for i in range(8)) + '</g><rect x="30" y="300" width="340" height="4" fill="#3b3f45"/><rect x="30" y="300" width="150" height="4" fill="#fff"/><circle cx="180" cy="302" r="8" fill="#fff"/>',
 "ui": '<rect width="400" height="400" fill="#efeee9"/><rect x="110" y="30" width="180" height="340" rx="26" fill="#fff" stroke="#1D2125" stroke-width="6"/><rect x="128" y="62" width="144" height="110" rx="10" fill="#103355"/><path d="M140 150 l30 -40 l26 26 l20 -16 l40 30z" fill="#FFC423"/><rect x="128" y="186" width="144" height="14" rx="7" fill="#d9d6cf"/><rect x="128" y="210" width="100" height="14" rx="7" fill="#d9d6cf"/><rect x="128" y="300" width="144" height="40" rx="20" fill="#A30E22"/>',
 "type": '<rect width="400" height="400" fill="#e9e3d6"/><text x="200" y="270" text-anchor="middle" font-family="Jost,sans-serif" font-weight="300" font-size="210" fill="#103355">Ag</text><text x="200" y="340" text-anchor="middle" font-family="Jost,sans-serif" font-size="22" letter-spacing="6" fill="#103355">MOJAVE SANS</text>',
 "sphere": '<defs><radialGradient id="gb" cx=".35" cy=".3"><stop offset="0" stop-color="#c8d4e0"/><stop offset=".6" stop-color="#4c6178"/><stop offset="1" stop-color="#1f2a36"/></radialGradient><radialGradient id="gs" cx=".35" cy=".3"><stop offset="0" stop-color="#fff"/><stop offset=".15" stop-color="#FFC423"/><stop offset="1" stop-color="#8a5f05"/></radialGradient></defs><rect width="400" height="400" fill="url(#gb)"/><ellipse cx="200" cy="320" rx="110" ry="18" fill="#000" opacity=".35"/><circle cx="200" cy="200" r="105" fill="url(#gs)"/>',
 "aerial": '<rect width="400" height="400" fill="#b89a6a"/>' + "".join(f'<circle cx="{25+c*50}" cy="{25+r*50}" r="16" fill="#3f5a1e"/><circle cx="{25+c*50}" cy="{25+r*50}" r="7" fill="#6e8b3d"/>' for r in range(8) for c in range(8)) + '<rect x="0" y="182" width="400" height="18" fill="#e3d2ae"/>',
 "package": '<rect width="400" height="400" fill="#f3efe6"/><path d="M120 110 L200 70 L280 110 L280 320 L200 360 L120 320Z" fill="#5B3F8C"/><path d="M200 150 L280 110 L280 320 L200 360Z" fill="#46306d"/><path d="M120 110 L200 150 L280 110 L200 70Z" fill="#7a5bb0"/><rect x="138" y="190" width="48" height="90" fill="#FFC423"/><text x="162" y="242" text-anchor="middle" font-family="Jost,sans-serif" font-size="16" font-weight="600" fill="#3a2a00" transform="rotate(-90 162 236)">AGAVE</text>',
 "game": '<rect width="400" height="400" fill="#7fc6e6"/><circle cx="320" cy="80" r="34" fill="#FFC423"/><rect y="280" width="400" height="120" fill="#c98b3f"/>' + "".join(f'<rect x="{i*40}" y="280" width="40" height="16" fill="#3f5a1e"/>' for i in range(0,10,2)) + '<rect x="90" y="230" width="44" height="50" fill="#5b3a1e"/><rect x="100" y="214" width="32" height="20" fill="#5b3a1e"/><rect x="124" y="208" width="18" height="10" fill="#A30E22"/><rect x="250" y="210" width="40" height="70" fill="#3f5a1e"/><rect x="236" y="230" width="14" height="30" fill="#3f5a1e"/>',
 "access": '<rect width="400" height="400" fill="#fff"/><rect x="0" y="0" width="400" height="120" fill="#103355"/><text x="30" y="80" font-family="Jost,sans-serif" font-weight="600" font-size="44" fill="#fff">Open House</text><text x="30" y="180" font-family="Roboto,sans-serif" font-size="26" fill="#1D2125">Saturday, 10 a.m.</text><text x="30" y="220" font-family="Roboto,sans-serif" font-size="26" fill="#1D2125">Room 101, ramp entrance</text><circle cx="330" cy="310" r="46" fill="none" stroke="#103355" stroke-width="8"/><circle cx="330" cy="290" r="9" fill="#103355"/><path d="M330 302 v28 M312 312 h36 M330 330 l-12 22 M330 330 l12 22" stroke="#103355" stroke-width="7" stroke-linecap="round"/>',
 "portrait": '<rect width="400" height="400" fill="#2b2f33"/><circle cx="200" cy="165" r="78" fill="#c99272"/><path d="M80 400 C80 290 320 290 320 400Z" fill="#A30E22"/><path d="M122 160 C122 80 278 80 278 160 C262 120 140 120 122 160Z" fill="#1d1a17"/>',
 "social": '<rect width="400" height="400" fill="#3F5A1E"/><text x="36" y="150" font-family="Jost,sans-serif" font-weight="600" font-size="64" fill="#FFC423">Join the</text><text x="36" y="220" font-family="Jost,sans-serif" font-weight="600" font-size="64" fill="#fff">cleanup.</text><text x="36" y="300" font-family="Roboto,sans-serif" font-size="22" fill="#fff">Whitewater Preserve, Saturday</text><circle cx="340" cy="340" r="30" fill="#FFC423"/>',
}

def work_art(w):
    if w.get("img"):
        return f'<img src="{R}img/work/{w["img"]}" alt="{esc_attr(w["alt"])}" loading="lazy">'
    return (f'<svg viewBox="0 0 400 400" preserveAspectRatio="xMidYMid slice" role="img" aria-label="{T("Placeholder artwork for", "Obra de muestra para")} {strip(w["title"])}">{ART[w["art"]]}</svg>'
            f'<span class="ph-tag">{T("Placeholder", "Muestra")}</span>')

def build_work():
    items = []
    for w in WORKS:
        c = w["course"]
        student = T(w["student"], "Nombre del estudiante") if w["student"] == "Student name" else w["student"]
        medium = MEDIUM_ES.get(w["medium"], w["medium"]) if LANG == "es" else w["medium"]
        items.append(f'''<li class="piece s-{w["shape"]}" data-path="{w["path"]}"><figure>
  <div class="art">{work_art(w)}</div>
  <figcaption><b>{student}</b><i>{w["title"]}</i>, {w["year"]}<br>{medium}<br>{course_link(c)} {COURSES[c][0]}</figcaption>
</figure></li>''')
    opts = [("all", T("All work", "Todos los trabajos"))] + [(p["key"], strip(pn(p))) for p in PATHS]
    radios = "".join(f'<input type="radio" name="wp" id="wp-{k}"{" checked" if k=="all" else ""}><label for="wp-{k}">{v}</label>' for k, v in opts)
    hide = ",\n".join(f'body:has(#wp-{k}:checked) .gallery .piece:not([data-path="{k}"])' for k, _ in opts[1:])
    title = T("Student Work", "Trabajos estudiantiles")
    body = f'''<style>{hide}{{display:none}}</style>
<div class="ghero"><div class="wrap">
  {crumbs([home_crumb(), (title, None)])}
  <h1>{title}</h1>
  <p class="lede">{T("Posters, photographs, animation, apps, games, and type, made in Digital Design &amp; Production classes. Every piece started as a first sketch.", "Carteles, fotografías, animación, apps, videojuegos y tipografía, creados en clases de Digital Design &amp; Production. Cada obra empezó como un primer boceto.")}</p>
</div></div>
<section class="gwall" aria-labelledby="gal-h"><div class="wrap">
  <h2 class="h2" id="gal-h">{T("The DDP Online Gallery", "La Galería en Línea de DDP")}</h2>
  <p class="note">{T("The pieces shown are placeholders. Real student work will appear here once students give written permission.", "Las obras que ves son de muestra. Aquí aparecerá trabajo real de estudiantes cuando den su permiso por escrito.")}</p>
  <fieldset class="filters"><legend>{T("Show work from", "Mostrar trabajos de")}</legend><div class="opts">{radios}</div></fieldset>
  <ul class="gallery">{"".join(items)}</ul>
</div></section>
<section aria-labelledby="show-h"><div class="wrap">
  <h2 class="h2" id="show-h">{T("Show your work", "Muestra tu trabajo")}</h2>
  <p class="sub">{T("Your work could appear in the DDP Online Gallery. Here is how to submit a finished piece.", "Tu trabajo podría aparecer en la Galería en Línea de DDP. Así puedes enviar una obra terminada.")}</p>
  <ol class="steps">
    <li><h3>{T("Pick your best piece", "Elige tu mejor obra")}</h3><p>{T("A finished project from any DDP class: poster, photo, video, animation, app, game, or type.", "Un proyecto terminado de cualquier clase de DDP: cartel, foto, video, animación, app, videojuego o tipografía.")}</p></li>
    <li><h3>{T("Ask your instructor", "Pregúntale a tu instructor")}</h3><p>{T("Your instructor can nominate it, or you can submit it yourself.", "Tu instructor puede nominarla, o puedes enviarla tú.")}</p></li>
    <li><h3>{T("Sign a release", "Firma una autorización")}</h3><p>{T("We need your written permission before anything is posted. You choose how your name appears.", "Necesitamos tu permiso por escrito antes de publicar algo. Tú decides cómo aparece tu nombre.")}</p></li>
    <li><h3>{T("Send it in", "Envíala")}</h3><p>{T("Email the file, title, course, and a one-line description to Prof. Gary Graves for the DDP Online Gallery.", "Envía por correo el archivo, el título, el curso y una descripción de una línea al profesor Gary Graves para la Galería en Línea de DDP.")}</p></li>
  </ol>
  <p style="margin-top:2rem"><a class="btn btn-red" href="mailto:ggraves@collegeofthedesert.edu?subject=DDP%20Online%20Gallery%20submission">{T("Submit work for the DDP Online Gallery", "Envía tu trabajo a la Galería en Línea de DDP")}</a></p>
  <p class="src">{T("In", "En")} {course_link("128")} Portfolio Preparation, {T("students also design and run a public exhibition of student work.", "los estudiantes también diseñan y organizan una exposición pública de trabajos estudiantiles.")}</p>
</div></section>'''
    return page("student-work.html", title, body, "work", T("Student work from Digital Design &amp; Production at College of the Desert.", "Trabajos estudiantiles de Digital Design &amp; Production en College of the Desert."))

# ---------------------------------------------------------------------------
def build_content(pg):
    if pg.get("section") == "programs":
        hero = simple_hero(pg["title"], pg["lede"], [home_crumb(), prog_crumb(), (pg["title"], None)], pg["file"])
    else:
        hero = simple_hero(pg["title"], pg["lede"], [home_crumb(), (pg["title"], None)])
    return page(pg["file"], pg["title"], hero + pg["body"], pg.get("section"), pg["lede"])

def build_lang(lang):
    global LANG, S, OUT, R
    LANG = lang
    S = S_ES if lang == "es" else S_EN
    OUT = os.path.join(DOCS, "es") if lang == "es" else DOCS
    R = "../" if lang == "es" else ""
    os.makedirs(OUT, exist_ok=True)
    made = [build_home(), build_programs(), build_courses(), build_contact(), build_work()]
    made += [build_path(p) for p in PATHS]
    for pg in S.pages(pay_section, course_link, jobs_table):
        if pg["file"] in ("student-work.html", "contact.html"): continue
        made.append(build_content(pg))
    return made

def build():
    os.makedirs(os.path.join(DOCS, "css"), exist_ok=True)
    shutil.copy(os.path.join(ROOT, "src", "style.css"), os.path.join(DOCS, "css", "style.css"))
    en = build_lang("en")
    es = build_lang("es")
    print(f"Built {len(en)} English pages and {len(es)} Spanish pages.")

if __name__ == "__main__":
    build()
