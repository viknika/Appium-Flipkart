import unittest
from appium import webdriver
import base64
import os
import time
#import selenium



class FlipkartTest(unittest.TestCase):


    def setUp(self):
       desired_cap = {
            "platformName": "Android",
            "deviceName": "Android Emulator",
            "app": "E:/Downloads/com.flipkart.android_6.10-970350_minAPI16(x86)(nodpi)_APKdot.com.apk",
            "appPackage": "com.flipkart.android",
            "appActivity": "com.flipkart.android.SplashActivity"
        }
       self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
       self.driver.implicitly_wait(20)
       self.driver.start_recording_screen()

    def test_Login(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.find_element_by_id("com.flipkart.android:id/btn_mlogin").click()
        driver.implicitly_wait(10)
        driver.find_element_by_id("com.flipkart.android:id/mobileNo").click()
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
        ts = (time.strftime("%y_%m_%d_%H%M%S"))
        activityname = driver.current_activity
        filename = activityname + ts
        driver.get_screenshot_as_file("D:/Veronika/PycharmProjects/Appium/Screenshots/" + filename + ".png")





    def tearDown(self):

        video_rawdata = self.driver.stop_recording_screen()
        video_name = self.driver.current_activity + time.strftime("%y_%m_%d_%H%M%S")
        filepath = os.path.join("D:/Veronika/PycharmProjects/Appium/Videos/", video_name + ".mp4")
        with open(filepath, "wb") as vd:
            vd.write(base64.b64decode(video_rawdata))
       #self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

