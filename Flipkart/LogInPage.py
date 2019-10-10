from appium import webdriver

class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.Log_button = "com.flipkart.android:id/btn_mlogin]"
        self.MobileNo = "com.flipkart.android:id/mobileNo"
        self.signin_button = "//form[@id='login_form']//span[1]"

    def SignIn(self,email,passw):
        self.driver.find_element_by_xpath(self.email_address).send_keys(email)
        self.driver.find_element_by_xpath(self.password).send_keys(passw)
        self.driver.find_element_by_xpath(self.signin_button).click()

driver.implicitly_wait(10)
#driver.find_element_by_id("com.flipkart.android:id/btn_mlogin").click()
driver.implicitly_wait(10)
#driver.find_element_by_id("com.flipkart.android:id/mobileNo").click()
driver.implicitly_wait(10)
driver.find_element_by_id("com.flipkart.android:id/mobileNo").send_keys("4")
driver.implicitly_wait(10)
driver.find_element_by_id("com.flipkart.android:id/country_code_info").click()
driver.implicitly_wait(10)
driver.find_element_by_id("com.flipkart.android:id/search_country_name").send_keys("canada")
driver.find_element_by_id("com.flipkart.android:id/country_row_item_full_name").click()
driver.find_element_by_id("com.flipkart.android:id/mobileNo").clear()
driver.find_element_by_id("com.flipkart.android:id/mobileNo").send_keys("4168415052")
driver.find_element_by_id("com.flipkart.android:id/et_password").click()
driver.find_element_by_id("com.flipkart.android:id/et_password").send_keys("159357")
driver.find_element_by_id("com.flipkart.android:id/btn_mlogin").click()