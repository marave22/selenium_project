# Negative - check that the name field contains only letters and is not empty
# Negative - check that the email is valid
# Negative - phone only digits, not letters, not empty
# Negative - Country only letters and spaces
# Negative- Company cannot have more than 20 letters, can be empty
# Negative- Message cannot have more than 180 letters, can be empty


from form.base_page import Base
import pytest
from time import sleep
from form.contactus_form import ContactUs


@pytest.mark.usefixtures('set_up')
class TestNegative(Base):

    @pytest.mark.parametrize("name_input, name_output",
                             [("35", "John Smith"), (" ", "John Smith"), (")*&*^&", "John Smith")])
    def test_3(self, name_input, name_output):
        driver = self.driver
        contact = ContactUs(driver)
        contact.input_name(name_input)
        assert name_input == name_output, "test failed"
        driver.implicitly_wait(10)

    @pytest.mark.parametrize("email_input, email_output", [("35", "test.email@mail.com"), (" ", "test.email@mail.com"),
                                                           ("test.email_mail.com", "test.email@mail.com"),
                                                           ("test.email@", "test.email@mail.com")])
    def test_4(self, email_input, email_output):
        driver = self.driver
        contact = ContactUs(driver)
        contact.input_email(email_input)
        assert email_input == email_output, "test failed"
        driver.implicitly_wait(10)

    @pytest.mark.parametrize("phone_input, phone_output", [("text", "+37490233223"), ("37490233223", "+37490233223"),
                                                           (" ", "+37490233223")])
    def test_5(self, phone_input, phone_output):
        driver = self.driver
        contact = ContactUs(driver)
        contact.input_telephone(phone_input)
        assert phone_input == phone_output, "test failed"
        driver.implicitly_wait(10)

    @pytest.mark.parametrize("country_input, country_output", [("456789", "Portugal"), ("$*(%&$*", "+37490233223"),
                                                               (" ", "+37490233223")])
    def test_6(self, country_input, country_output):
        driver = self.driver
        contact = ContactUs(driver)
        contact.input_country(country_input)
        assert country_input == country_output, "test failed"
        driver.implicitly_wait(10)

    @pytest.mark.parametrize("company_input, company_output", [(" ", "A while back I needed to count the amount"),
                                                               ("test", "A while back I needed to count the amount")])
    def test_7(self, company_input, company_output):
        driver = self.driver
        contact = ContactUs(driver)
        contact.input_country(company_input)
        count = len(company_input)
        assert company_input == company_output or count >= 20, "test failed"
        driver.implicitly_wait(10)

    @pytest.mark.parametrize("message_input, message_output", [(" ", "A while back I needed to count the amount"),
                                                               ("test", "A while back I needed to count the amount")])
    def test_8(self, message_input, message_output):
        driver = self.driver
        contact = ContactUs(driver)
        contact.input_message(message_input)
        count = len(message_input)
        assert message_input == message_output or count >= 180, "test failed"
        driver.implicitly_wait(10)
        sleep(3)
