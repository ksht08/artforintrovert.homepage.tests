
from selene import browser, have, be, command

class HomePage():

    def open(self):
        """
        Open homepage
        """
        browser.open("/")

        return self

    def check_title(self, value):
        """
        Check that the page title matches the expected value
        """
        browser.should(have.title(value))

        return self
    
    def check_description(self, value):
        """
        Check that the page description matches the expected value
        """
        page_description = browser.element("meta[name='description']")
        page_description.should(have.attribute("content").value(value))

        return self

    def close_ad_banner(self):
        """
        Close ad banner if present, skip if not
        """
        ad_banner = browser.element(".tn-elem__13446184011728998947890")
        if ad_banner.matching(be.visible):
            ad_banner.click()
            return True
        return False


    def consent_to_cookies(self):
        """
        Accept cookies by clicking the consent button on the cookie banner
        """
        cookie_banner = browser.element(".uc-cookie > .t657_rectangle")
        cookie_banner.should(be.visible)
        cookie_button = cookie_banner.element(".t657__btn")
        cookie_button.should(have.exact_text("Класс!")).click()

        return self

    def text_animation(self, values):
        """
        Verify the moving text section has correct animation speed and contains expected text phrases
        """
        moving_text = browser.element(".t1003__content")
        moving_text.perform(command.js.scroll_into_view)
        browser.driver.execute_script("window.scrollBy(0, -100);")
        moving_text.should(be.visible.and_(have.css_property("animation-duration").value("34.72s")))
        for value in values:
            moving_text.should(have.text(value))

        return self

    def courses_section(self, courses_per_page):
        """
        Verify that each course card has an image, a button, and total course count matches expected
        """
        courses_header = browser.element(".tn-elem__8348268181705321625736")
        courses_header.perform(command.js.scroll_into_view)
        browser.driver.execute_script("window.scrollBy(0, -50);")
        courses = browser.all(".t-store__card-nlm057")
        courses.should(have.size(courses_per_page))
        for course in courses:
            # course button
            course.element(".js-store-buttons-wrapper").should(be.visible.and_(have.text("Подробнее")))
            # course image
            course.element(".t-store__card__img").should(
                be.visible.and_(
                have.attribute("src").value_containing("https://optim.tildacdn.com/stor"))
                )

        return self


    def check_footer_form_error(self, invalid_email):
        """
        Validate error message when invalid email is submitted in the footer subscription form
        """
        footer_form = browser.element("#molecule-173833511338298900")
        footer_form.perform(command.js.scroll_into_view)
        error_message = browser.element(".tn-form__errorbox-popup")
        form_input = footer_form.element("[name='email']").should(be.visible)
        error_message.should(be.hidden)
        form_input.should(have.attribute("placeholder").value("Введи e-mail "))
        form_input.type(invalid_email)
        form_button = footer_form.element("[type='submit']")
        form_button.should(be.visible.and_(have.text("Подписаться"))).click()
        error_message.should(be.visible.and_(have.text("Укажите, пожалуйста, корректный email")))
        
        return self
