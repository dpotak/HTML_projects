from bs4 import BeautifulSoup
import unittest

file_code = "C:\\Users\\darja\\OneDrive\\Desktop\\html_Progects\\HTML_projects\\HTML_Portfolio2_official\\Portfolio.html"
with open (file_code, "r", encoding="utf-8") as file:
    html_code = file.read()

soup = BeautifulSoup(html_code, "html.parser")