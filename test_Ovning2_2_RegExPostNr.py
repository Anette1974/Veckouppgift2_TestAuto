"""
2 Skriv ett regex som matchar ett svenskt postnummer.
Postnummer består av fem siffror indelade i två grupper med mellanslag emellan. Exempel: "123 45"
Om du vill övertänka fördjupa dig mera: https://sv.wikipedia.org/wiki/Postnummer_i_Sverige
"""

import re
from playwright.sync_api import Page, expect

def test_zip_code():
    zip_code = "Mitt postnummer är 417 27."
    # kontrollera om det finns postnummer i strängen med regular expression
    expected = re.compile(r"\d{3}\s\d{2}")

    # Hämta det faktiska värdet
    match = expected.search(zip_code)
    actual = match.group() if match else None

    # Kontrollera att ett postnummer hittades
    assert actual is not None, "Fel! Inget postnummer."

    print(f"Testet lyckades! Hittade postnummer: {actual}")

test_zip_code()