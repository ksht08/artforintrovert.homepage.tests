import allure
from selene import browser
from pages.artforintrovert_homepage import HomePage

allure.feature("UI Tests for Art for Introvert Homepage")
@allure.title("Art for Introvert Homepage Tests")
@allure.description("This suite verifies key UI elements and behaviors on https://online.artforintrovert.ru page.")
def test_artforintrovert_homepage():
    home_page = HomePage()

    with allure.step("Open homepage"):
        home_page.open()

    with allure.step("Verify homepage title"):
        home_page.check_title(
            "Правое полушарие Интроверта. "
            "Сервис, где поощряют саморазвитие"
            )

    with allure.step("Verify homepage description"):
        home_page.check_description(
            "2000+ лекций по 30 направлениям: "
            "от психологии и кино до философии и карьеры. "
            "По подписке за 300 рублей в месяц."
            )

    with allure.step("Close ad banner"):
        home_page.close_ad_banner()

    with allure.step("Accept cookies"):
        with allure.step("Cookies banner screenshot"):
            allure.attach(
                browser.driver.get_screenshot_as_png(),
                name="Cookies banner",
                attachment_type=allure.attachment_type.PNG
            )
        home_page.consent_to_cookies()

    with allure.step("Check text animation"):
        home_page.text_animation(
            ["Компания из отечественного реестра ПО",
             "Резидент Сколково",
             "Apple editors choice",
             "Образовательная лицензия",
             "Аккредитованная IT компания"]
        )

    with allure.step("Verify courses section"):
        courses_per_page=3
        home_page.courses_section(courses_per_page)
        with allure.step(f"Courses section screenshot (expected '{courses_per_page}' courses per page)"):
            allure.attach(
                browser.driver.get_screenshot_as_png(),
                name="Courses section",
                attachment_type=allure.attachment_type.PNG
            )
    
    with allure.step("Verify error message on invalid email"):
        home_page.check_footer_form_error("test.email@artforintrovert")
        with allure.step("Footer error message screenshot"):
            allure.attach(
                browser.driver.get_screenshot_as_png(),
                name="Error message",
                attachment_type=allure.attachment_type.PNG
            )