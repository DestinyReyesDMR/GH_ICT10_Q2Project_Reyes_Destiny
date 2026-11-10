
from pyscript import document


# PAGE NAVIGATION

def show_page(page_id):
    pages = ["home", "element", "clubs", "creator"]

    for page in pages:
        document.getElementById(page).style.display = "none"

    document.getElementById(page_id).style.display = "block"


def home_page(event):
    show_page("home")


def element_page(event):
    show_page("element")


def clubs_page(event):
    show_page("clubs")


def creator_page(event):
    show_page("creator")


# SEATWORK 1: CANDIDATE VERIFICATION

club_members = [
    "Destiny Reyes",
    "Kenneth Concepcion",
    "Vita De Guzman",
    "Franchesca Dela Rosa",
    "Santiago Valdez",
    "Chalanie Lumbang",
    "Gurleen Kaur",
    "Miguel Jimenez"
]


def verify_candidate(event):
    first = document.getElementById("first-name").value.strip().title()
    last = document.getElementById("last-name").value.strip().title()

    full_name = first + " " + last

    result = full_name in club_members

    messages = {
        True: "Congratulations " + full_name + "! You are now part of the ICT club.",
        False: "Sorry " + full_name + ", your name is not on the list."
    }

    document.getElementById("candidate-result").innerHTML = messages[result]


# SKILLS TEST: PERIODIC TABLE INFORMATION FINDER

nonmetals = {
    "H": ("Hydrogen", 1, 1.008),
    "He": ("Helium", 2, 4.0026),
    "C": ("Carbon", 6, 12.011),
    "N": ("Nitrogen", 7, 14.007),
    "O": ("Oxygen", 8, 15.999),
    "F": ("Fluorine", 9, 18.998),
    "Ne": ("Neon", 10, 20.180),
    "P": ("Phosphorus", 15, 30.974),
    "S": ("Sulfur", 16, 32.06),
    "Cl": ("Chlorine", 17, 35.45),
    "Ar": ("Argon", 18, 39.948),
    "Se": ("Selenium", 34, 78.971),
    "Br": ("Bromine", 35, 79.904),
    "Kr": ("Krypton", 36, 83.798),
    "I": ("Iodine", 53, 126.904),
    "Xe": ("Xenon", 54, 131.293),
    "Rn": ("Radon", 86, 222)
}


def check_element(event):
    symbol = document.getElementById("element-symbol").value.strip().capitalize()

    result = document.getElementById("element-result")

    if symbol in nonmetals:
        name, number, mass = nonmetals[symbol]

        result.innerHTML = (
            "<h5>" + name + " (" + symbol + ")</h5>"
            + "<p>Symbol: " + symbol + "</p>"
            + "<p>Element Name: " + name + "</p>"
            + "<p>Atomic Number: " + str(number) + "</p>"
            + "<p>Atomic Mass: " + str(mass) + "</p>"
        )
    else:
        result.innerHTML = "Element not found. Please enter a valid non-metal symbol."


# DRILL 2: SET OPERATORS

grade_7 = {
    "Kenneth Concepcion",
    "Vita De Guzman",
    "Franchesca Dela Rosa"
}

grade_8 = {
    "Raver Estacio",
    "Julia Hadji Gapor",
    "Miguel Jimenez"
}

grade_9 = {
    "Gurleen Kaur",
    "MJ Madrelejos",
    "Chalanie Lumbang"
}

grade_10 = {
    "Destiny Reyes",
    "Santiago Valdez",
    "Jesse Villante"
}


# Combine all grade sets
master_set = grade_7 | grade_8 | grade_9 | grade_10


def display_members():
    member_list = ", ".join(sorted(master_set))

    document.getElementById("all-members").innerHTML = (
        "<h5>ICT Club Members</h5><p>" + member_list + "</p>"
    )

    document.getElementById("total-members").innerHTML = str(len(master_set))


def add_member(event):
    global master_set

    first = document.getElementById("member-first").value.strip().title()
    last = document.getElementById("member-last").value.strip().title()

    full_name = first + " " + last

    new_member = {full_name}

    master_set = master_set | new_member

    display_members()

    document.getElementById("member-first").value = ""
    document.getElementById("member-last").value = ""


# SHOW INITIAL CLUB MEMBERS
display_members()
