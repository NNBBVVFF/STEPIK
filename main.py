from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class webform_test(unittest.TestCase):

    def test_web1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your first name"]')
        input1.send_keys("Ramzan")
        time.sleep(1)
        input2 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your last name"]')
        input2.send_keys("Zahaev")
        time.sleep(1)
        input3 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your email"]')
        input3.send_keys("Bibas@gmail.com")
        time.sleep(1)
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        browser.quit()
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, msg="Fucking Bitch")

    def test_web2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your first name"]')
        input1.send_keys("Ramzan")
        time.sleep(1)
        input2 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your last name"]')
        input2.send_keys("Zahaev")
        time.sleep(1)
        input3 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your email"]')
        input3.send_keys("Bibas@gmail.com")
        time.sleep(1)
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        browser.quit()
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, msg="Fucking Bitch")
        # link = "http://suninjuly.github.io/registration2.html"
        # browser = webdriver.Chrome()
        # browser.get(link)
        # input1 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your name"]')
        # input1.send_keys("Ramzan")
        # time.sleep(0.5)
        # input2 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your email"]')
        # input2.send_keys("Bibas@gmail.com")
        # time.sleep(0.5)
        # button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        # button.click()
        # welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # welcome_text = welcome_text_elt.text
        # self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


if __name__ == "__main__":
    unittest.main()
