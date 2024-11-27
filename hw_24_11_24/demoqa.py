import unittest
from datetime import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()


    def test1(self):
        self.driver.get('https://demoqa.com/text-box')
        element1 = self.driver.find_element(By.CLASS_NAME, "text-center")
        print(f'Тест 1 працює')

    def test2(self):
        self.driver.get("https://demoqa.com/text-box")
        element2 = self.driver.find_element(By.XPATH, "//input[@placeholder='Full Name']")
        element2.click()
        element2.send_keys("ostap")
        print(f' тест 2 працює')

    def test3(self):
        self.driver.get("https://demoqa.com/text-box")

        input_full_name = self.driver.find_element(By.ID, 'userName')
        input_full_name.click()
        input_full_name.send_keys('ostap')

        input_email = self.driver.find_element(By.ID, 'userEmail')
        input_email.click()
        input_email.send_keys('ostap@gmail.com')

        input_current_address = self.driver.find_element(By.ID, 'currentAddress')
        input_current_address.click()
        input_current_address.send_keys('zbyranka')

        input_permanent_address = self.driver.find_element(By.CLASS_NAME, 'form-control')
        input_permanent_address.click()
        input_permanent_address.send_keys('solar street')

        click_on_submit = self.driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]")
        click_on_submit.click()

        out_put_div = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "border"))
        )

        self.assertTrue("ostap" in out_put_div.text)
        self.assertTrue("ostap@gmail.com" in out_put_div.text)
        self.assertTrue("zbyranka" in out_put_div.text)
        self.assertTrue("solar street" in out_put_div.text)


        print("Тест3 успішно пройшов!")

    def test4(self):
        checkbox_btn = self.driver.find_element(By.CLASS_NAME, "btn")
        checkbox_btn.click()

        checkbox = self.driver.find_element(By.CLASS_NAME, "rct-icon")
        plus_btn = self.driver.find_element(By.XPATH, '//*[@stroke="currentColor"]')
        plus_btn.click()

        desktop_checkbox = self.driver.find_element(By.XPATH,"//span[text()='desktop']//preceding::input[@type='checkbox']")
        desktop_checkbox.click()

        minus_btn = self.driver.find_element(By.XPATH, '//*[@fill="currentColor"]')
        minus_btn.click()

        result_div = self.driver.find_element(By.ID, "result")
        result_text = result_div.text

        expected_text = '''You have selected :
                                documents
                                workspace
                                react
                                angular
                                veu
                                office
                                public
                                private
                                classified
                                general
                                downloads
                                wordFile
                                excelFile'''

        self.assertEqual(result_text, expected_text)  # Перевіряємо, чи текст збігається з очікуваним

        print("Тест пройшов успішно!")

    def test5(self):
        try:
            self.check_box_element = self.wait.until(EC.element_to_be_clickable((By.ID, "item-1")))
            self.check_box_element.click()
            self.show_all = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".rct-icon-expand-all")))
            self.show_all.click()
            self.all_elements = self.wait.until(lambda driver: driver.find_elements(By.CLASS_NAME, 'rct-icon-uncheck'))
            self.all_elements[3].click()
            self.assertEqual(self.driver.find_element(By.CLASS_NAME, "text-success").text, "commands")
        finally:
            self.driver.quit()

      def test6(self):
        try:
            self.radio_button = self.driver.find_element(By.ID, "item-2")
            self.radio_button.click()
            self.yes_radio_button = self.driver.find_element(By.CLASS_NAME, "custom-control-label")
            self.yes_radio_button.click()
            self.assertEqual(self.yes_radio_button.text, "Yes")
        finally:
            self.driver.quit()
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
