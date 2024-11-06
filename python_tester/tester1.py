from bs4 import BeautifulSoup
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Tester HTML
class TestContentHTMLCode(unittest.TestCase):
    # Open file html
    file_code = "C:\\Users\\darja\\OneDrive\\Desktop\\html_Progects\\HTML_projects\\HTML_Portfolio2_official\\Portfolio.html"
    with open (file_code, "r", encoding="utf-8") as file:
        html_code = file.read()
        
    soup = BeautifulSoup(html_code, "html.parser")

    def title_test(self):
        title = self.soup.title
        self.assertIsNotNone(title)
        self.assertEqual(title.string, "Test Page")

    def h1_test(self):
        h1 = self.soup.find('h1')
        self.assertIsNotNone(h1)
        self.assertEqual(h1.string, "h1 , done!")

    def body_test(self):
        pass

# Tester css 
class TestContentCSSCode():
    # Start testing CSS file
    def css_test1():
        driver = webdriver.Chrome()
        driver.get("C:\\Users\\darja\\OneDrive\\Desktop\\html_Progects\\HTML_projects\\HTML_Portfolio2_official\\Portfolio.html")
        
        try:
            # Expecting the title <h1> on the page
            header = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "h1"))
            )
            
            # Gaining CSS a font-size character
            header_font_size = header.value_of_css_property("font-size")
            expected_font_size = "35px"
            
            # Check that the font size matches the expected font
            assert header_font_size == expected_font_size, f"Expected font size {expected_font_size}, but got {header_font_size}"

            # Verification of the presence of element h1
            header_h1 = driver.find_elements(By.TAG_NAME, 'h1')
            if header_h1:
                print('Element found!')
            else:
                print('Element not found!')

            # Verification of the presence of element h2
            header_h2 = driver.find_elements(By.TAG_NAME, 'h2')
            if header_h2:
                print('Element found!')
            else:
                print('Element not found!')

            # Verification of the presence of element h3
            header_h3 = driver.find_elements(By.TAG_NAME, 'h3')
            if header_h3:
                print('Element found!')
            else:
                print('Element not found!')

            # Verification of the presence of element h4
            header_h4 = driver.find_elements(By.TAG_NAME, 'h4')
            if header_h4:
                print('Element found!')
            else:
                print('Element not found!')



        finally:
            # Закрытие драйвера
            driver.quit()



if __name__ == "__main__":
    TestContentCSSCode.css_test1()
    unittest.main()

