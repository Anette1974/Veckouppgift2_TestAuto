"""
3 Skriv ett regex som matchar ett datum skrivet enligt den internationella standarden ISO 8601,
alltså 10 tecken med bindestreck mellan avdelningarna. Exempel: 2025-03-10.
"""

import re
from playwright.sync_api import Page, expect

def test_date():
    date = "Dagens datum är 2025-03-16."
    # kontrollera om det finns ett datum i strängen med regular expression
    expected = re.compile(r"\d{4}-\d{2}-\d{2}")

    # Hämta det faktiska värdet
    match = expected.search(date)
    actual = match.group() if match else None

    # Kontrollera att ett postnummer hittades
    assert actual is not None, "Fel! Inget postnummer."

    print(f"Testet lyckades! Hittade postnummer: {actual}")

test_date()