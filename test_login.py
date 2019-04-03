import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@pytest.mark.usefixtures("driver_init")
class BaseTest:
    url = "https://uat.ormuco.com/login"
    email = "qa@ormuco.com"
    password = "testpass"
    errorMessage = "The user or password is incorrect."

    def parse_element(self, ele):
        text = [i.text for i in ele]
        text = " ".join(text)
        return text


class TestLogin(BaseTest):
    # Test not part of technical test case.
    def test_open_url(self):
        self.driver.get(self.url)
        title = self.driver.title
        assert title == "Portal - stratosphere"

    def test_blank_password_and_wrong_email(self):
        wait = WebDriverWait(self.driver, 3)
        self.driver.get(self.url)
        wait.until(EC.element_to_be_clickable((By.NAME, 'username'))
                   ).send_keys(self.email)
        wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".button-login"))).click()

        warning = self.driver.find_elements_by_xpath(
            "//span[@class='warning']")
        warning_text = self.parse_element(warning)

        assert warning_text == self.errorMessage

    def test_blank_email_and_wrong_password(self):
        wait = WebDriverWait(self.driver, 3)
        self.driver.get(self.url)
        wait.until(EC.element_to_be_clickable((By.NAME, 'password'))
                   ).send_keys(self.password)
        wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".button-login"))).click()

        warning = self.driver.find_elements_by_xpath(
            "//span[@class='warning']")
        warning_text = self.parse_element(warning)

        assert warning_text == self.errorMessage

    def test_blank_email_and_blank_password(self):
        wait = WebDriverWait(self.driver, 3)
        self.driver.get(self.url)
        wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".button-login"))).click()

        warning = self.driver.find_elements_by_xpath(
            "//span[@class='warning']")
        warning_text = self.parse_element(warning)

        assert warning_text == self.errorMessage

    def test_wrong_email_and_wrong_password(self):
        wait = WebDriverWait(self.driver, 3)
        self.driver.get(self.url)
        wait.until(EC.element_to_be_clickable((By.NAME, 'username'))
                   ).send_keys(self.email)
        wait.until(EC.element_to_be_clickable((By.NAME, 'password'))
                   ).send_keys(self.password)
        wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".button-login"))).click()

        warning = self.driver.find_elements_by_xpath(
            "//span[@class='warning']")
        warning_text = self.parse_element(warning)

        assert warning_text == self.errorMessage
