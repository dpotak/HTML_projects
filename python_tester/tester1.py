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

# Tester css 
class TestContentCSSCode():
    
    def css_test1():
        driver = webdriver.Chrome()
        driver.get("C:\\Users\\darja\\OneDrive\\Desktop\\html_Progects\\HTML_projects\\HTML_Portfolio2_official\\Portfolio.html")
        
        try:
            # Ожидание появления заголовка <h1> на странице
            header = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "h1"))
            )
            
            # Получение CSS свойства 'font-size'
            header_font_size = header.value_of_css_property("font-size")
            expected_font_size = "35px"
            
            # Проверка, что размер шрифта совпадает с ожидаемым
            assert header_font_size == expected_font_size, f"Expected font size {expected_font_size}, but got {header_font_size}"
        
        finally:
            # Закрытие драйвера
            driver.quit()

if __name__ == "__main__":
    TestContentCSSCode.css_test1()
    unittest.main()

