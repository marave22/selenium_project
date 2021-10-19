from locators.locators import LocatorsXPath


class ContactUs:
    def __init__(self, driver):
        self.driver = driver
        self.name = LocatorsXPath.name
        self.email = LocatorsXPath.email
        self.telephone = LocatorsXPath.telephone
        self.country = LocatorsXPath.country
        self.company = LocatorsXPath.company
        self.message = LocatorsXPath.message
        self.form_submit = LocatorsXPath.submit
        self.form_clear = LocatorsXPath.clear
        # self.success_submit = LocatorsXPath.success_message

    def input_name(self, text):
        input_name = self.driver.find_element_by_xpath(self.name)
        input_name.send_keys(text)

    def input_email(self, text):
        input_email = self.driver.find_element_by_xpath(self.email)
        input_email.send_keys(text)

    def input_telephone(self, number):
        input_telephone = self.driver.find_element_by_xpath(self.telephone)
        input_telephone.send_keys(number)

    def input_country(self, text):
        input_country = self.driver.find_element_by_xpath(self.country)
        input_country.send_keys(text)

    def input_company(self, text):
        input_company = self.driver.find_element_by_xpath(self.company)
        input_company.send_keys(text)

    def input_message(self, text):
        input_message = self.driver.find_element_by_xpath(self.message)
        input_message.send_keys(text)

    def submit_form(self):
        form_submit = self.driver.find_element_by_xpath(self.form_submit)
        form_submit.click()

    def clear_form(self):
        form_clear = self.driver.find_element_by_xpath(self.form_clear)
        form_clear.click()
