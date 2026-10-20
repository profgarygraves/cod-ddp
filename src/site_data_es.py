# Spanish text for site_data.py. Needs review by a fluent Spanish speaker before launch.
from site_data import *   # reuse links (L, COD, SCHEDULE, SYLLABI, sched, cat_search, etc.)
from programs import AWARDS, COURSES, JOBS, JOBS_SOURCE, PATHS, ADVISOR, COURSES_URL, KIND
from programs_es import PATHS_ES, AWARDS_ES, KIND_ES, JOBS_ES

REVIEWED = "otoño de 2026"

PREVIEW = ('Vista previa del diseño para revisión del profesorado. No es el sitio oficial. '
           '<a href="https://github.com/profgarygraves/cod-ddp/issues">Envía tus comentarios en GitHub</a>.')

TOP_LINKS = [("Solicitar admisión", COD + "/students/admissions/"), ("Horario de clases", SCHEDULE),
             ("Catálogo", CATALOG), ("Programas de curso", SYLLABI), ("Ayuda financiera", COD + "/students/fin-aid/")]

NAV = [("programs", "Programas", "programs.html"), ("start", "Cómo empezar", "get-started.html"),
       ("work", "Trabajos estudiantiles", "student-work.html"), ("contact", "Docentes y contacto", "contact.html")]

SUBNAV = [("programs.html", "Todos los programas"), ("courses.html", "Buscador de cursos"),
          ("careers.html", "Carreras y salarios"), ("transfer.html", "Transferencia")]

FOOT_LINKS = [
 ("Estudiantes", [("Admisiones", L["admissions"]), ("Ayuda financiera", L["finaid"]), ("Consejería", L["counseling"]), ("Servicios estudiantiles", COD + "/students/")]),
 ("Acerca de", [("Accesibilidad en COD", L["a11y"]), ("Política de privacidad", COD + "/privacy-policy.php"), ("Directorio", COD + "/directory/")]),
]

HOME = dict(
  h1="Convierte tu creatividad en una carrera.",
  lede="Si te interesa el diseño, la edición de video, la animación, la fotografía o el diseño UX, este es tu punto de partida.",
)

STEPS = [
 ("Solicita admisión a COD", "La admisión es gratis. ¿Ya eres estudiante? Elige un programa de DDP como tu especialidad.",
  f'Llena tu solicitud en línea con la oficina de Admisiones de COD; no tiene ningún costo. Si ya tomas clases en COD, pide en Consejería que actualicen tu especialidad (major) para que tu plan educativo vaya de acuerdo con tu meta. <a href="{L["admissions"]}">Solicita admisión a COD</a>'),
 ("Toma un curso inicial", "DDP 100, o el primer curso de tu ruta. Cuenta para tu certificado o título.",
  'Cada ruta profesional tiene un curso inicial. Ese curso cuenta para los certificados y títulos de esa ruta, así que no pierdes nada mientras decides. ¿No sabes qué ruta elegir? Toma DDP 100. <a href="programs.html">Compara los programas</a>'),
 ("Haz tu plan con la asesora del programa", "Planea tus semestres con Mari Abril, asesora del programa DDP, y con un consejero académico.",
  f'Reúnete con {ADVISOR["name"]}, asesora del programa DDP, para hablar de clases y portafolios, y con un consejero académico para armar tu plan educativo completo, incluyendo educación general y transferencia. <a href="{L["counseling"]}">Haz una cita de consejería</a>'),
 ("Crea tu portafolio y solicita tu certificado", "Termina tu portafolio en DDP 195 y luego solicita tu certificado o título.",
  f'Los certificados y títulos no se otorgan automáticamente. Haz la solicitud en el mismo semestre en que terminas tu último curso requerido. <a href="{L["award_app"]}">Application for a Degree or Certificate (solicitud de título o certificado)</a>'),
]


def pages(pay_section, course_link, jobs_table):
    out = []

    # ---------------- Careers ----------------
    alljobs = jobs_table(list(JOBS), "Salarios y perspectivas de empleos creativos")
    path_rows = "".join(f'<li><a href="{p["file"]}"><b>{PATHS_ES[p["key"]]["name"]}</b><span>{PATHS_ES[p["key"]]["jobs"]}</span></a></li>' for p in PATHS)
    out.append(dict(file="careers.html", section="programs", title="Carreras creativas",
      lede="A qué se dedican los graduados de DDP, cuánto se paga este trabajo en el Inland Empire y el Valle de Coachella, y cómo ganar experiencia mientras estudias.",
      body=f'''<section><div class="wrap">
  <h2 class="h2">Carreras por ruta</h2>
  <p class="sub">Cada ruta profesional te lleva a un grupo de empleos. Muchos profesionales creativos también trabajan por su cuenta (freelance) o tienen su propio estudio.</p>
  <ul class="links">{path_rows}</ul>
</div></section>
<section class="pay-wrap"><div class="wrap">
  <h2 class="h2">Cuánto se paga el trabajo creativo aquí</h2>
  <p class="sub">Salario medio en el área metropolitana de Riverside-San Bernardino-Ontario, que incluye el Valle de Coachella (o en California, donde se indica). La mitad de los trabajadores gana más y la otra mitad gana menos. Las perspectivas y las vacantes son proyecciones nacionales de 2025 a 2035.</p>
  {alljobs}
  <p class="src">Fuente: {JOBS_SOURCE}</p>
</div></section>
<section><div class="wrap">
  <h2 class="h2">Gana experiencia mientras estudias</h2>
  <p class="sub">Los empleadores contratan según tu portafolio. Estos cursos y servicios te ayudan a crear uno y a mostrarlo.</p>
  <ul class="links">
    <li><a href="courses.html#ddp-195"><b>DDP 195: Business Practices and Portfolio Preparation</b><span>Trabajo freelance, precios, clientes, contratos, impuestos y un portafolio profesional.</span></a></li>
    <li><a href="courses.html#ddp-128"><b>DDP 128: Portfolio Preparation</b><span>Portafolio en línea, declaración artística, currículum (CV) y una exposición pública de trabajos estudiantiles.</span></a></li>
    <li><a href="courses.html#ddp-095a"><b>DDP 095A: Work Experience</b><span>Gana de 1 a 5 unidades por un trabajo o una práctica de diseño que ya tengas.</span></a></li>
    <li><a href="{L["handshake"]}"><b>Encuentra empleos y prácticas en Handshake</b><span>La bolsa de trabajo de COD para estudiantes y egresados. Inicia sesión con tu cuenta de COD.</span></a></li>
    <li><a href="{L["career"]}"><b>Career and Workforce Solutions Center (centro de carreras)</b><span>Orientación profesional, currículums, evaluaciones y ferias de empleo.</span></a></li>
    <li><a href="{L["entr"]}"><b>Empieza tu propio negocio creativo</b><span>Combina DDP con los cursos de Emprendimiento (ENTR) de COD.</span></a></li>
  </ul>
</div></section>'''))

    # ---------------- Transfer ----------------
    tr_awards = [k for k, a in AWARDS.items() if a.get("transfer")]
    tr_cards = "".join(f'<li><a href="{a["url"]}"><b>{a["name"]} {a["kind"]}</b><span>{AWARDS_ES.get(k, {}).get("desc", a["desc"])} {a["units"]} unidades, con {a["ge"]}.</span></a></li>' for k, a in ((k, AWARDS[k]) for k in tr_awards))
    uc = [c for c, v in COURSES.items() if "UC" in v[2]]
    csu = [c for c, v in COURSES.items() if "CSU" in v[2]]
    out.append(dict(file="transfer.html", section="programs", title="Transfiérete a una universidad de cuatro años",
      lede="Empieza tu licenciatura en diseño en COD. Dos títulos de DDP están hechos para transferirte, y la mayoría de los cursos de DDP se transfieren a la CSU.",
      body=f'''<section><div class="wrap">
  <h2 class="h2">Títulos para transferencia</h2>
  <p class="sub">Los dos títulos usan Cal-GETC, el plan de educación general que aceptan la CSU y la UC.</p>
  <ul class="links">{tr_cards}</ul>
</div></section>
<section class="tight"><div class="wrap prose">
  <h2 class="h2">Cursos que se transfieren</h2>
  <p>{len(csu)} cursos de DDP se transfieren a la Universidad Estatal de California (CSU), y {len(uc)} de ellos también se transfieren a la Universidad de California (UC). {course_link("100")} tiene un número C-ID (ARTS 250), así que cuenta de la misma manera en muchas universidades de California. Usa el <a href="courses.html">buscador de cursos</a> para filtrar por CSU o UC.</p>
  <p>Que un curso se transfiera no significa que cuente para tu especialidad. Cada universidad decide qué cursos cuentan para su carrera de diseño. Consulta <a href="{L["assist"]}">ASSIST.org</a>, el sitio oficial de acuerdos de transferencia de los colegios y universidades públicas de California.</p>
</div></section>
<section class="pay-wrap"><div class="wrap">
  <h2 class="h2">Planea tu transferencia</h2>
  <ol class="steps v">
    <li><h3>Elige pronto las universidades que te interesan</h3><p>Las carreras de diseño cambian mucho de una universidad a otra. CSU San Bernardino tiene un campus en Palm Desert; pregúntale a un consejero qué programas van con tus metas. <a href="{L["csusb"]}">CSU San Bernardino</a></p></li>
    <li><h3>Reúnete con un consejero</h3><p>Arma un plan educativo que incluya la preparación para tu especialidad, Cal-GETC y las fechas límite de admisión. <a href="{L["counseling"]}">Consejería</a></p></li>
    <li><h3>Aprovecha el Transfer Center</h3><p>Talleres, representantes de universidades y ayuda con tus solicitudes. <a href="{L["transfer"]}">Transfer Center (centro de transferencia)</a></p></li>
    <li><h3>Crea tu portafolio</h3><p>Muchos programas de diseño revisan portafolios. {course_link("128")} y {course_link("195")} te ayudan a preparar el tuyo.</p></li>
  </ol>
</div></section>'''))

    # ---------------- Get started ----------------
    steps = "".join(f'<li><h3>{h}</h3><p>{long}</p></li>' for h, short, long in STEPS)
    out.append(dict(file="get-started.html", section="start", title="Cómo empezar",
      lede="De tu primera clase a tu certificado, en cuatro pasos. ¿Eres nuevo en la universidad? Este es tu lugar.",
      body=f'''<section><div class="wrap">
  <h2 class="sr">Cuatro pasos</h2>
  <ol class="steps v">{steps}</ol>
</div></section>
<section class="tight"><div class="wrap two">
  <article class="panel-gold"><h3>¿Quieres probar primero?</h3><p>Las clases de Adobe sin crédito no cobran colegiatura y no necesitas experiencia. Tienen un proceso de inscripción aparte y más corto.</p><a href="software.html">Habilidades de software para el trabajo</a></article>
  <article class="panel-red"><h3>Cómo pagar la universidad</h3><p>La mayoría de los estudiantes de COD califica para recibir ayuda con cuotas, libros y materiales. Haz tu solicitud cada año, lo antes posible.</p><a href="{L["finaid_apply"]}">Cómo solicitar ayuda financiera</a></article>
</div></section>
<section><div class="wrap">
  <h2 class="h2">Apoyo para cada estudiante</h2>
  <p class="sub">¿Necesitas listas de equipo, formularios o ayuda en el campus? Consulta los <a href="resources.html">recursos para estudiantes</a>.</p>
  <ul class="links">
    <li><a href="{L["counseling"]}"><b>Consejería</b><span>Planes educativos, especialidades y transferencia.</span></a></li>
    <li><a href="{L["tutoring"]}"><b>Tutoría</b><span>El Academic Skills Center (centro de tutoría) ofrece tutoría gratis.</span></a></li>
    <li><a href="{L["dsps"]}"><b>Disabled Students Programs &amp; Services (DSPS)</b><span>Adaptaciones para clases y laboratorios para estudiantes con discapacidades.</span></a></li>
    <li><a href="{L["eops"]}"><b>EOPS &amp; CARE</b><span>Consejería, ayuda con libros y más para estudiantes que califican.</span></a></li>
    <li><a href="{L["veterans"]}"><b>Veterans Resource Center (centro para veteranos)</b><span>Beneficios y apoyo para veteranos.</span></a></li>
    <li><a href="{L["basic"]}"><b>Necesidades básicas</b><span>Comida, vivienda y otros apoyos.</span></a></li>
  </ul>
</div></section>'''))

    # ---------------- Resources ----------------
    out.append(dict(file="resources.html", section="start", title="Recursos para estudiantes",
      lede="Equipo, software, formularios y ayuda para estudiantes de DDP.",
      body=f'''<section><div class="wrap">
  <h2 class="h2">Cámaras y equipo</h2>
  <p class="sub">Algunos cursos de fotografía te piden traer tu propia cámara. El catálogo indica estos requisitos.</p>
  <table class="list"><caption class="sr">Cámara requerida por curso</caption>
    <thead><tr><th scope="col">Curso</th><th scope="col">Lo que necesitas</th></tr></thead>
    <tbody>
      <tr><td>{course_link("130")}</td><td>Tu propia cámara réflex digital (DSLR)</td></tr>
      <tr><td>{course_link("131")}</td><td>Una cámara digital con control manual de apertura (f-stop) y velocidad de obturación, y su manual</td></tr>
      <tr><td>{course_link("132")}</td><td>Una cámara digital (de 3 megapíxeles o más); se recomienda software de edición de imágenes y una impresora de fotos</td></tr>
      <tr><td>{course_link("133")}</td><td>Tu cámara y su manual; salidas de campo</td></tr>
      <tr><td>{course_link("135")}</td><td>Una cámara de película de 35 mm con control manual de apertura (f-stop) y velocidad de obturación</td></tr>
      <tr><td>{course_link("136")}</td><td>En clase se proporcionan drones o simuladores de drones</td></tr>
    </tbody></table>
  <p class="note">Acceso al software: pregúntale a tu instructor cómo obtener Adobe Creative Cloud para tu clase. <span class="ph">(El departamento confirmará los detalles de laboratorios y licencias).</span></p>
</div></section>
<section class="pay-wrap"><div class="wrap">
  <h2 class="h2">Formularios</h2>
  <ul class="links">
    <li><a href="{L["award_app"]}"><b>Application for a Degree or Certificate (solicitud de título o certificado)</b><span>Haz la solicitud en el semestre en que terminas tu último curso.</span></a></li>
    <li><a href="{L["graduation"]}"><b>Graduación</b><span>Fechas límite y ceremonia de graduación.</span></a></li>
    <li><a href="{SYLLABI}"><b>Programas de curso anteriores</b><span>Mira de qué trata cualquier curso de DDP. Busca en la biblioteca por código de curso, por ejemplo DDP 106.</span></a></li>
    <li><a href="{L["noncredit"]}"><b>Inscripción a clases sin crédito</b><span>Para las clases de certificado de Adobe sin colegiatura.</span></a></li>
  </ul>
</div></section>
<section><div class="wrap">
  <h2 class="h2">Ayuda en el campus</h2>
  <ul class="links">
    <li><a href="contact.html"><b>Asesora del programa DDP</b><span>{ADVISOR["name"]}, {ADVISOR["email"]}</span></a></li>
    <li><a href="{L["counseling"]}"><b>Consejería</b><span>Planes educativos y transferencia.</span></a></li>
    <li><a href="{L["tutoring"]}"><b>Academic Skills Center</b><span>Tutoría gratis.</span></a></li>
    <li><a href="{L["library"]}"><b>Biblioteca</b><span>Ayuda con investigación, espacios para estudiar y computadoras.</span></a></li>
    <li><a href="{L["career"]}"><b>Centro de carreras</b><span>Currículums, orientación profesional y ferias de empleo.</span></a></li>
    <li><a href="{L["handshake"]}"><b>Handshake</b><span>Empleos y prácticas para estudiantes de COD.</span></a></li>
    <li><a href="{L["dsps"]}"><b>DSPS</b><span>Adaptaciones para estudiantes con discapacidades.</span></a></li>
  </ul>
</div></section>'''))

    # ---------------- Student work ----------------
    pieces = [
     ("background:#A30E22", '<span style="position:absolute;left:8%;bottom:8%;font:600 2.2rem/.9 var(--display);color:#fff">desert<br>x<br>film fest</span><span style="position:absolute;width:60%;aspect-ratio:1;border-radius:50%;background:#FFC423;top:10%;right:-10%"></span>', "Póster de festival", "Ilustración digital", "111"),
     ("background:linear-gradient(180deg,#f0b38a 0 38%,#d98b6a 38% 52%,#8a6a5a 52% 64%,#3d3a3a 64%)", "", "Joshua Tree al atardecer", "Fotografía digital", "133"),
     ("background:radial-gradient(circle at 35% 30%,#b8c7d6,#4c6178 60%,#1f2a36)", '<span style="position:absolute;inset:28%;border-radius:50%;background:radial-gradient(circle at 35% 30%,#fff 0 6%,#FFC423 14%,#b5810a 70%)"></span>', "Estudio de esfera de latón", "Render 3D", "144"),
     ("background:#f7f7f7", '<span style="position:absolute;left:9%;right:9%;top:8%;height:36%;background:#103355;border-radius:8px"></span><span style="position:absolute;left:9%;width:50%;top:52%;height:9%;background:#A30E22;border-radius:6px"></span>', "App de senderos", "Prototipo UX", "151"),
     ("background:#141619", '<span style="position:absolute;left:8%;right:8%;top:42%;height:14%;background:repeating-linear-gradient(90deg,#FFC423 0 10%,transparent 10% 14%)"></span>', "Secuencia de títulos", "Motion graphics", "121"),
     ("background:#e9e3d6;display:grid;place-items:center", '<span style="font:300 6rem/1 var(--display);color:#103355">Ag</span>', "Mojave Sans", "Tipografía original", "112"),
    ]
    figs = "".join(f'<li><figure class="piece"><div class="art" style="{st}" role="img" aria-label="Espacio reservado para un trabajo estudiantil: {t}">{inner}<span class="ph-tag">Ejemplo</span></div>'
                   f'<figcaption><b>Nombre del estudiante</b><i>{t}</i>, 2026. {m}. {course_link(c)} {COURSES[c][0]}</figcaption></figure></li>' for st, inner, t, m, c in pieces)
    out.append(dict(file="student-work.html", section="work", title="Trabajos estudiantiles",
      lede="Pósters, fotografías, animación, apps y tipografía de las clases de DDP.",
      body=f'''<section><div class="wrap">
  <p class="note">Estos son ejemplos temporales. Aquí aparecerán trabajos reales de estudiantes cuando ellos den su permiso por escrito.</p>
  <ul class="wall">{figs}</ul>
</div></section>
<section class="pay-wrap"><div class="wrap prose">
  <h2 class="h2">Comparte tu trabajo</h2>
  <p>Los estudiantes de DDP pueden enviar trabajos terminados para esta galería. Pídele a tu instructor que proponga una pieza, o escríbele al curador de la galería, el Prof. Gary Graves, a <a href="mailto:ggraves@collegeofthedesert.edu">ggraves@collegeofthedesert.edu</a>. Cada pieza necesita una autorización firmada, y tú decides cómo aparece tu nombre.</p>
</div></section>'''))

    # ---------------- Contact ----------------
    out.append(dict(file="contact.html", section="contact", title="Contacto y ubicaciones",
      lede="¿Tienes preguntas sobre un programa, una clase o tu portafolio? Empieza con la asesora del programa.",
      body=f'''<section><div class="wrap">
  <h2 class="h2">Personas</h2>
  <ul class="links">
    <li><a href="mailto:{ADVISOR["email"]}"><b>{ADVISOR["name"]}, asesora del programa</b><span>Programas, clases y portafolios. {ADVISOR["email"]}, {ADVISOR["phone"]}</span></a></li>
    <li><a href="faculty.html"><b>Docentes y personal</b><span>Todos los instructores de DDP, la jefa del departamento y la oficina de la decana.</span></a></li>
    <li><a href="mailto:ggraves@collegeofthedesert.edu"><b>Gary Graves, curador de la galería</b><span>Envía trabajos estudiantiles para la galería. ggraves@collegeofthedesert.edu</span></a></li>
  </ul>
</div></section>
<section class="pay-wrap"><div class="wrap">
  <h2 class="h2">Dónde se dan las clases de DDP</h2>
  <ul class="links">
    <li><a href="{COD}/map/"><b>Campus de Palm Desert</b><span>43-500 Monterey Ave, Palm Desert, CA 92260. Campus principal.</span></a></li>
    <li><a href="{L["palmsprings"]}"><b>Palm Springs</b><span>Campus temporal en 1300 E. Baristo Rd. Se planea abrir el nuevo campus de Palm Springs en el otoño de 2027.</span></a></li>
    <li><a href="courses.html"><b>En línea</b><span>Muchos cursos de DDP se ofrecen en línea. Revisa el horario de clases cada semestre.</span></a></li>
  </ul>
  <p class="note"><span class="ph">Falta confirmar la oficina del departamento, los laboratorios y el horario.</span></p>
</div></section>
<section><div class="wrap prose">
  <h2 class="h2">College of the Desert</h2>
  <p>43-500 Monterey Ave, Palm Desert, CA 92260<br>760.346.8041<br><a href="{COD}/directory/">Directorio del campus</a></p>
</div></section>'''))

    # ---------------- Accessibility ----------------
    out.append(dict(file="accessibility.html", section=None, title="Accesibilidad de este sitio",
      lede="Este sitio está hecho para que todas las personas lo puedan usar.",
      body=f'''<section><div class="wrap prose">
  <p>El sitio web de Digital Design &amp; Production está diseñado para cumplir con las Pautas de Accesibilidad para el Contenido Web (WCAG) 2.2, nivel AA. Cada página se revisa con pruebas automáticas en modo claro y oscuro, en tamaño de computadora y de teléfono, y con el teclado.</p>
  <ul>
    <li>El texto y los controles cumplen con los estándares de contraste de color en los dos temas de color.</li>
    <li>Cada página funciona con el teclado, empieza con un enlace para saltar al contenido y muestra dónde está el foco del teclado.</li>
    <li>Las páginas se ajustan en pantallas pequeñas y con un zoom de 200 por ciento sin que tengas que desplazarte hacia los lados.</li>
    <li>Los filtros de cursos y el cambio de tema de color funcionan sin JavaScript.</li>
  </ul>
  <p>¿Encontraste un problema? <a href="{L["report"]}">Repórtalo a College of the Desert</a> o escríbele a la asesora del programa a <a href="mailto:{ADVISOR["email"]}">{ADVISOR["email"]}</a>. Para adaptaciones en clases y laboratorios, comunícate con <a href="{L["dsps"]}">Disabled Students Programs &amp; Services (servicios para estudiantes con discapacidades)</a>.</p>
  <p>Lee la <a href="{L["a11y"]}">declaración de accesibilidad de College of the Desert</a>.</p>
</div></section>'''))
    return out
