# DDP faculty and staff.
# Sources, checked October 20, 2026:
#   Instructors: every DDP section in the class schedule (Self-Service), Spring, Summer, and Fall 2026.
#   Titles and emails: College of the Desert Faculty and Staff Directory.
#   Leadership: School of Social Sciences and Arts page.
# Photos: put a 600x750 (4:5) headshot at docs/img/people/<first-last>.jpg and it appears on the next build.
# No photo -> initials on the color of the instructor's main career path.

LEADERSHIP = [  # (name, title, email, phone)
 ("Dr. Vanessa Fountain", "Dean, School of Social Sciences and Arts", "vfountain@collegeofthedesert.edu", "760.636.7987"),
 ("Dr. Mari Abril", "Professor, Digital Design &amp; Production; Department Chair, Arts &amp; Media; Program Advisor", "mabril@collegeofthedesert.edu", "760.674.5684"),
 ("Tina Gonzalez", "Administrative Assistant, School of Social Sciences and Arts", "tigonzalez@collegeofthedesert.edu", "760.773.2574"),
]

# (name, email, title, DDP courses taught in 2026, terms)
FACULTY = [
 ("Dr. Mari Abril", "mabril@collegeofthedesert.edu", "Professor and Department Chair", ["095A", "102", "110", "111", "112", "114", "116", "142", "150", "151", "195"], "Spring, Summer, Fall 2026"),
 ("Aaron Baldon", "abaldon@collegeofthedesert.edu", "Adjunct Faculty", ["101", "102"], "Spring 2026"),
 ("Roxanne Brazell", "rbrazell@collegeofthedesert.edu", "Instructor", ["103"], "Spring, Fall 2026"),
 ("Tina Cleveland-Gorges", "tcleveland@collegeofthedesert.edu", "Instructor", ["200", "202"], "Spring, Summer, Fall 2026"),
 ("Benjamin Davis", "bdavis@collegeofthedesert.edu", "Adjunct Faculty", ["140"], "Spring, Fall 2026"),
 ("Denise Ferraccioli", "dreilley@collegeofthedesert.edu", "Adjunct Faculty", ["101", "102"], "Spring, Fall 2026"),
 ("Alejandra Garbutt", "agarbutt@collegeofthedesert.edu", "Adjunct Faculty", ["100", "116"], "Spring, Fall 2026"),
 ("John Goodwin", "jgoodwin@collegeofthedesert.edu", "Adjunct Faculty", ["121"], "Spring 2026"),
 ("Jonathan Gorges", "jgorges@collegeofthedesert.edu", "Instructor", ["201"], "Summer 2026"),
 ("Gary Graves", "ggraves@collegeofthedesert.edu", "Adjunct Faculty; DDP Online Gallery submissions", ["106", "116", "195"], "Spring, Fall 2026"),
 ("Kent Kay", "kkay@collegeofthedesert.edu", "Faculty, Film and Media Studies", ["095A", "120"], "Spring 2026"),
 ("Maile Klein", "mklein@collegeofthedesert.edu", "Adjunct Faculty", ["131", "133", "135"], "Spring, Summer, Fall 2026"),
 ("Jaime Lilly", "jlilly@collegeofthedesert.edu", "Instructor", ["144", "160"], "Summer, Fall 2026"),
 ("Debra McFadden", "dmcfadden@collegeofthedesert.edu", "Adjunct Faculty", ["102", "110"], "Spring, Fall 2026"),
 ("Michael Patterson", "mpatterson@collegeofthedesert.edu", "Adjunct Faculty", ["100", "161"], "Spring, Fall 2026"),
 ("Kerri Seichter", "kseichter@collegeofthedesert.edu", "Adjunct Faculty", ["120", "121", "130"], "Spring, Summer, Fall 2026"),
 ("Rebecca Soltes", "rsoltes@collegeofthedesert.edu", "Adjunct Faculty", ["100", "103", "113"], "Spring, Summer, Fall 2026"),
 ("Daniel Stiel", "dstiel@collegeofthedesert.edu", "Adjunct Faculty", ["132", "136"], "Spring, Fall 2026"),
 ("Zebulon Zang", "zzang@collegeofthedesert.edu", "Adjunct Faculty", ["100"], "Spring, Summer, Fall 2026"),
]

# LinkedIn profiles: email -> the part after linkedin.com/in/
# Faculty can send theirs; a link appears on their card on the next build.
LINKEDIN = {
 "ggraves@collegeofthedesert.edu": "garygraves",
}
