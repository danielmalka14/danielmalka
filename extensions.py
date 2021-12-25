from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
chrome_driver = webdriver.Chrome(executable_path=r"c:\users\daniel.malka\downloads\chromedriver_win32\chromedriver.exe")
firefox_driver = webdriver.Firefox(executable_path=r"c:\users\daniel.malka\downloads\geckodriver-v0.30.0-win64\geckodriver.exe")
explorer_driver = webdriver.Ie(executable_path=r"C:\Users\daniel.malka\Downloads\IEDriverServer_x64_4.0.0\IEDriverServer.exe")
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_driver(chrome_options=chrome_options)


