"""
1.打开浏览器
2.建立Base类
"""
import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def open_browser(browser="chrome"):
    """打开浏览器"""
    driver=None
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser== "firefox":
        driver = webdriver.Firefox()
    elif browser=="ie":
        driver = webdriver.Ie()
    else:
        print("请输入正确的浏览器名称,如:'chrome','firefox','ie'")
    return driver
class Base:
    def __init__(self,driver):
        self.driver = driver

    def open_url(self,url):
        self.driver.get(url)
        self.driver.maximize_window()

    def find_element(self,locator,timeout=10):
        element = WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located(locator))
        return element

    def find_elements(self,locator,timeout):
        elements = WebDriverWait(self.driver,timeout).until(EC.presence_of_all_elements_located(locator))
        return elements

    def click(self,locator,timeout=10):
        element = self.find_element(locator=locator,timeout=timeout)
        element.click()

    def send_keys(self,locator,text,timeout=10):
        element = self.find_element(locator=locator,timeout=timeout)
        element.clear()
        element.send_keys(text)

    def is_text_in_element(self,locator,text,timeout=10):
        try:
            result = WebDriverWait(self.driver,timeout).until(EC.text_to_be_present_in_element(locator,text))
            return result
        except:
            return False
    def is_value_in_element(self,locator,value,timeout=10):
        try:
            result = WebDriverWait(self.driver,timeout).until(EC.text_to_be_present_in_element_value(locator,value))
            return result
        except:
            return False
    def close_browser(self):
        self.driver.quit()
if __name__ == '__main__':
    driver = open_browser()
    base = Base(driver)
    url ="http://localhost:8080/ecshop/user.php"
    base.open_url(url)
    time.sleep(2)
    locator_input = ("id","keyword")
    base.send_keys(locator=locator_input,text="手机")
    time.sleep(3)
    base.close_browser()
