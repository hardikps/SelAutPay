from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(executable_path="C:\\Users\\hardik\\Desktop\\chromedriver_win32\\chromedriver.exe")

browser.get('https://apps.paybooks.in/')
assert 'Paybooks Login | Paybooks App | Paybooks Admin Login' in browser.title

inputElement = browser.find_element(By.NAME, 'txtUserName')  # Find the search box
inputElement.send_keys('279')

inputElement = browser.find_element(By.NAME, 'txtPassword')  # Find the search box
inputElement.send_keys('H@rdikp098')

inputElement = browser.find_element(By.NAME, 'txtDomain')  # Find the search box
inputElement.send_keys('ACC')

inputElement.send_keys(Keys.ENTER)

inputElement = browser.find_element(By.CLASS_NAME, 'ng-scope')
inputElement.
