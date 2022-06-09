# Generated by Selenium IDE
# import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestEditevent():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_editevent(self):
    self.driver.get("https://thundermeet.netlify.app/")
    self.driver.set_window_size(1054, 742)
    self.driver.find_element(By.ID, "login_userId").click()
    self.driver.find_element(By.ID, "login_userId").send_keys("1234")
    self.driver.find_element(By.ID, "login_password").click()
    self.driver.find_element(By.ID, "login_password").send_keys("1234")
    self.driver.find_element(By.CSS_SELECTOR, ".ant-btn:nth-child(1) > span").click()

    self.driver.implicitly_wait(20)
    self.driver.find_element(By.CSS_SELECTOR, ".ant-btn-primary:nth-child(2)").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.CSS_SELECTOR, ".ant-btn-primary:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".iconify").click()
    self.driver.find_element(By.CSS_SELECTOR, "#root > div > div > div").click()
    self.driver.find_element(By.ID, "eventName").send_keys("event_2")
    self.driver.find_element(By.CSS_SELECTOR, ".confirmbutton > span").click()
    self.driver.find_element(By.CSS_SELECTOR, ".container > .ant-btn > span:nth-child(2)").click()
    self.driver.close()

actor = TestEditevent()
actor.setup_method("foo")
actor.test_editevent()
print("Sleep for 5 seconds")
time.sleep(5)
# actor.get_title()
print("all steps completed.")