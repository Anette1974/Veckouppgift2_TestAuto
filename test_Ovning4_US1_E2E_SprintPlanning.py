import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://lejonmanen.github.io/agile-helper/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Agile helper"))
"""
[US1]
Story: Som en användare, vill jag se mötet "sprint planning" som utspelar sig första dagen på en sprint, så att jag vet vad jag ska göra på mötet.

Scenario:
[ac1-1] Navigera till webbsidan https://lejonmanen.github.io/agile-helper/
[ac1-2] Klicka på knappen med texten "First"
[ac1-3] Klicka på knappen vars text innehåller "Sprint planning"
[ac1-4] Kontrollera att ett <dialog> element visas på sidan, som innehåller en rubrik <h> med texten "Sprint planning"
[ac1-5] Hovra över varje steg och se att "ikonen" längst till vänster blir markerad
[ac1-6] Verifiera att steg fyra innehåller texten "a digital tool" och att det finns en klickbar länk som öppnas i ny tab
[ac1-7] Klicka på knappen vars text innehåller "Ok we're done"
[ac1-8] Klicka på knappen vars text innehåller "Start over"
[ac1-9] Verifiera att du är tillbaks på startsidan genom att texten "What day of the sprint is it?" visas på sidan
"""

def test_view_daily_standup(page: Page):
#[ac1-1]
    page.goto("https://lejonmanen.github.io/agile-helper/")

#[ac1-2]
    button_locator = page.get_by_role("button")
    first_button = button_locator.get_by_text( re.compile("First") )
    first_button.click(timeout=500)

#[ac1-3]
    sprint_planning_button = page.get_by_role("button").get_by_text( re.compile("Sprint planning") )
    expect(sprint_planning_button).to_have_count(1, timeout=500)
    sprint_planning_button.click()

#[ac1-4]
    heading = page.get_by_role("heading").get_by_text( re.compile("Sprint planning"))
    expect(heading).to_be_visible(timeout=500)

#[ac1-5]
# TO DO, Här ska testet för att markera rad 1, rad 2 när man hovrar över steg 1, steg 2 osv vara.

#[ac1-6]
# TO DO, Här ska testet för att verifiera att länken till den externa sidan för "Planning poker online" vara

#[ac1-7]
# TO DO, Här ska testet vara för att verifiera att det går att klicka på knappen "Ok we're done. Start the sprint!"

#[ac1-8]
# TO DO, Här ska testet vara för att klicka och verifiera knappen "Start over"

#[ac1-9]
# TO DO, Här ska testet vara för att verifiera att vi är tillbaks på startsidan genom att texten "What day of the sprint is it?" visas


