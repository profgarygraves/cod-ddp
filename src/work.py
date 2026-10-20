# Student work gallery.
# To add a real piece:
#   1. Save the image as docs/img/work/<file>.jpg (long side about 1600px, under 400 KB).
#   2. Add or edit an entry below: set img="<file>.jpg", the student's name as they approved it,
#      and alt text that describes the piece for people who cannot see it.
#   3. Run python3 build.py.
# Entries with img=None show a labeled placeholder.
# path: design, motion, photo, interactive, access, software
# shape: tall, wide, or square (how much space the piece takes in the gallery)

WORKS = [
 dict(title="Desert X Film Fest", student="Student name", year="2026", medium="Festival poster, digital illustration", course="111", path="design", shape="tall", art="poster", img=None, alt=""),
 dict(title="Joshua Tree, Dusk", student="Student name", year="2026", medium="Digital photograph", course="133", path="photo", shape="wide", art="dusk", img=None, alt=""),
 dict(title="Title Sequence", student="Student name", year="2026", medium="Motion graphics, 0:45", course="121", path="motion", shape="wide", art="motion", img=None, alt=""),
 dict(title="Trail App", student="Student name", year="2026", medium="UX prototype", course="151", path="interactive", shape="tall", art="ui", img=None, alt=""),
 dict(title="Mojave Sans", student="Student name", year="2026", medium="Original typeface", course="112", path="design", shape="square", art="type", img=None, alt=""),
 dict(title="Brass Sphere Study", student="Student name", year="2026", medium="3D render", course="144", path="motion", shape="square", art="sphere", img=None, alt=""),
 dict(title="Date Farm From Above", student="Student name", year="2026", medium="Aerial drone photograph", course="136", path="photo", shape="square", art="aerial", img=None, alt=""),
 dict(title="Agave Tea Packaging", student="Student name", year="2026", medium="Package design", course="115", path="design", shape="tall", art="package", img=None, alt=""),
 dict(title="Roadrunner Run", student="Student name", year="2026", medium="Game prototype", course="161", path="interactive", shape="wide", art="game", img=None, alt=""),
 dict(title="Accessible Event Flyer", student="Student name", year="2026", medium="Accessible PDF", course="201", path="access", shape="square", art="access", img=None, alt=""),
 dict(title="Palm Canyon Portrait", student="Student name", year="2026", medium="Retouched photograph, Photoshop", course="301B", path="software", shape="tall", art="portrait", img=None, alt=""),
 dict(title="Join the Cleanup", student="Student name", year="2026", medium="Social campaign", course="113", path="design", shape="square", art="social", img=None, alt=""),
]
