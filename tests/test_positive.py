from form.base_page import Base
import pytest
from time import sleep
from form.contactus_form import ContactUs


@pytest.mark.usefixtures('set_up')
class TestPositive(Base):

    # def test_1(self):
    #     driver = self.driver
    #     contact = ContactUs(driver)
    #     name_input = "John Doe"
    #     name_output = "John Doe"
    #     contact.input_name(name_input)
    #     driver.implicitly_wait(10)
    #     assert name_input == name_output, "positive test failed"
    #
    #     email_input = "example@test.com"
    #     email_output = "example@test.com"
    #     contact.input_email(email_input)
    #     driver.implicitly_wait(10)
    #     assert email_input == email_output, "positive test failed"
    #
    #     phone_input = "+37490233223"
    #     phone_output = "+37490233223"
    #     contact.input_telephone(phone_input)
    #     driver.implicitly_wait(10)
    #     assert phone_input == phone_output, "positive test failed"
    #
    #     country_input = "Portugal"
    #     country_output = "Portugal"
    #     contact.input_country(country_input)
    #     driver.implicitly_wait(10)
    #     assert country_input == country_output, "positive test failed"
    #
    #     company_input = "Python"
    #     company_output = "Python"
    #     contact.input_company(company_input)
    #     driver.implicitly_wait(10)
    #     assert company_input == company_output, "positive test failed"
    #
    #     message_input = "Lorem ipsum dolor sit amet, sit ame"
    #     message_output = "Lorem ipsum dolor sit amet, sit ame"
    #     contact.input_message(message_input)
    #     driver.implicitly_wait(10)
    #     assert message_input == message_output, "positive test failed"
    #
    #     driver.implicitly_wait(5)
    #     contact.clear_form()
    #     sleep(5)

    def test_2(self):
        driver = self.driver
        contact = ContactUs(driver)
        name_input = "John Doe"
        name_output = "John Doe"
        contact.input_name(name_input)
        driver.implicitly_wait(10)
        assert name_input == name_output, "positive test failed"

        email_input = "example@test.com"
        email_output = "example@test.com"
        contact.input_email(email_input)
        driver.implicitly_wait(10)
        assert email_input == email_output, "positive test failed"

        phone_input = "+37490233223"
        phone_output = "+37490233223"
        contact.input_telephone(phone_input)
        driver.implicitly_wait(10)
        assert phone_input == phone_output, "positive test failed"

        country_input = "Portugal"
        country_output = "Portugal"
        contact.input_country(country_input)
        driver.implicitly_wait(10)
        assert country_input == country_output, "positive test failed"

        company_input = "Python"
        company_output = "Python"
        contact.input_company(company_input)
        driver.implicitly_wait(10)
        assert company_input == company_output, "positive test failed"

        message_input = "Lorem ipsum dolor sit amet, sit ame"
        message_output = "Lorem ipsum dolor sit amet, sit ame"
        contact.input_message(message_input)
        driver.implicitly_wait(10)
        assert message_input == message_output, "positive test failed"

        # success_message = "Feedback has been sent to the administrator"
        contact.submit_form()
        # text = contact.success_submit()
        # assert success_message == text
        # driver.implicitly_wait(5)
        sleep(5)
