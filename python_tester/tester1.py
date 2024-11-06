from bs4 import BeautifulSoup
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

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
class TestContentCSSCode(unittest.TestCase):
    # Open file css
    file_code_css = "C:\\Users\\darja\\OneDrive\\Desktop\\html_Progects\\HTML_projects\\HTML_Portfolio2_official\\css_prog\\portfolio_1.css"
    with open (file_code_css, "r") as file_css:
        css_code = file_css.read()

    driver = webdriver.Chrome()
    driver.get("C:\\Users\\darja\\OneDrive\\Desktop\\html_Progects\\HTML_projects\\HTML_Portfolio2_official\\css_prog\\portfolio_1.css")

    def css_test1():
        pass

if __name__ == "__main__":
    unittest.main()
