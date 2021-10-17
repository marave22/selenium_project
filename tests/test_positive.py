from form.base_page import Base
import pytest
from time import sleep
from form.contactus_form import ContactUs


@pytest.mark.usefixtures('set_up')
class TestPositive(Base):

    def test_1(self):
        driver = self.driver
        contact = ContactUs(driver)

        @pytest.mark.parametrize("input1, output", [("John Doe", "John Doe")])
        def name_input(input1, output):
            txt = contact.input_name(input1)
            assert txt == output, "failed"

        @pytest.mark.parametrize("input1, output", [("email@example.com", "email@example.com")])
        def email_input(input1, output):
            txt = contact.input_name(input1)
            assert txt == output, "failed"

            # contact.input_email("example@test.com")
            # contact.input_telephone("+37490233223")
            # contact.input_country("UK")
            # contact.input_company("test company")
            # contact.input_message("test message")
            sleep(3)

