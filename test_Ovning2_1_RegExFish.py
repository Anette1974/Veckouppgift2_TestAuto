"""
1a Skriv ett regex som kontrollerar att det finns en längd i strängen, som anges i centimeter:
"Fiskarna som jag fångade var 55 cm långa."
"""

import re
from playwright.sync_api import Page, expect

def test_length_fish():
    fish_string = "Fiskarna som jag fångade var 55 cm långa."
    # kontrollera om det finns siffror i strängen med regular expression
    expected = re.compile(r"\d+\scm")

    # Hämta det faktiska värdet
    match = expected.search(fish_string)
    actual = match.group() if match else None

    # Kontrollera att en siffra hittades
    assert actual is not None, "Fel! Ingen siffra hittades."

    print(f"Testet lyckades! Hittade: {actual}")

test_length_fish()

"""
1b Denna gången vill vi veta om det finns två längder.
"""



"""
1c Längderna ska vara samma enhet.
"Fiskarna som jag fångade var 55 cm långa, så båda fick plats i min 1,23 m långa låda."
"""