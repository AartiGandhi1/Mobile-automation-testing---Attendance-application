import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='com.example.aplikasi_absen',
    appActivity='.StartActivity',
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723'


class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, capabilities)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def testRegistration(self) -> None:
        driver = self.driver
        driver.find_element(by=AppiumBy.ID, value="com.example.aplikasi_absen:id/avStart_card_signup").click()
        driver.implicitly_wait(4)
        fullname_textfield = driver.find_element(by=AppiumBy.ID, value="com.example.aplikasi_absen:id/ipt_fullname")
        fullname_textfield.click()
        fullname_textfield.send_keys("Aarti Gandhi")
        email_textfield = driver.find_element(by=AppiumBy.ID, value="com.example.aplikasi_absen:id/ipt_email")
        email_textfield.click()
        email_textfield.send_keys("aartikshah.1@gmail.com")
        phone_number_field = driver. find_element(by=AppiumBy.ID, value="com.example.aplikasi_absen:id/ipt_phonenumber")
        phone_number_field.click()
        phone_number_field.send_keys("+46764555748")
        address_textfield = driver.find_element(by=AppiumBy.ID, value="com.example.aplikasi_absen:id/ipt_address")
        address_textfield.click()
        address_textfield.send_keys("Solna")
        password_textfield = driver.find_element(by=AppiumBy.ID, value="com.example.aplikasi_absen:id/ipt_password")
        password_textfield.click()
        password_textfield.send_keys("testing1234*")
        confirm_password = driver.find_element(by=AppiumBy.ID, value="com.example.aplikasi_absen:id/ipt_confirmpassword")
        confirm_password.click()
        confirm_password.send_keys("testing1234*")
