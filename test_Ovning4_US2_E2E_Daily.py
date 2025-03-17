import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://lejonmanen.github.io/agile-helper/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Agile helper"))
"""
[US2]
Story: Som en användare, vill jag se mötet "Daily standup" som utspelar sig varje dag i en sprint, så att jag vet vad jag ska göra på mötet.

Scenario:
[ac2-1] Navigera till webbsidan https://lejonmanen.github.io/agile-helper/
[ac2-2] Klicka på knappen med texten "First"
[ac2-3] Klicka på knappen vars text innehåller "Daily standup"
[ac2-4] Kontrollera att ett <dialog> element visas på sidan, som innehåller en rubrik <h> med texten "Daily standup"
[ac2-5] Kontrollera att det finns en knapp vars text innehåller "10 minutes"
[ac2-6] Klicka på knappen vars text innehåller "10 minutes"
[ac2-7] Kontrollera att timern räknar ner från 10 till 9
[ac2-8] Klicka på knappen vars text innehåller "Ok we're done"
[ac2-9] Klicka på knappen vars text innehåller "Start over"
[ac2-10] Verifiera att du är tillbaks på startsidan genom att texten "What day of the sprint is it?" visas på sidan
"""

def test_view_daily_standup(page: Page):
#[ac2-1]
    page.goto("https://lejonmanen.github.io/agile-helper/")

#[ac2-2]
    button_locator = page.get_by_role("button")
    first_button = button_locator.get_by_text( re.compile("First") )
    first_button.click(timeout=500)

#[ac2-3]
    daily_button = page.get_by_role("button").get_by_text( re.compile("Daily standup") )
    expect(daily_button).to_have_count(1, timeout=500)
    daily_button.click()

#[ac2-4]
    heading = page.get_by_role("heading").get_by_text( re.compile("Daily standup"))
    expect(heading).to_be_visible(timeout=500)

#[ac2-5]
# TO DO, Kontrollera att det finns en knapp vars text innehåller "10 minutes"

#[ac2-6]
# TO DO, Klicka på knappen vars text innehåller "10 minutes"

#[ac2-7]
# TO DO, Kontrollera att timern räknar ner från 10 till 9

#[ac2-8]
# TO DO, Klicka på knappen vars text innehåller "Ok we're done"

#[ac2-9]
# TO DO, Klicka på knappen vars text innehåller "Start over"

#[ac2-10]
# TO DO, Verifiera att du är tillbaks på startsidan genom att texten "What day of the sprint is it?" visas på sidan


