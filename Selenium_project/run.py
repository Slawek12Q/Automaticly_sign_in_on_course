from selenium import webdriver

login = input("Please fill in your email\n")
password = input("Please fill in your password\n")

browser = webdriver.Chrome(executable_path='C:\driver\chromedriver.exe')
browser.get('https://www.usosweb.uj.edu.pl/kontroler.php?_action=actionx:news/default()')
browser.maximize_window()

loggin_button = browser.find_element_by_css_selector('div#casmenu > table > tbody > tr > td:nth-of-type(2) > a')
loggin_button.click()

loginField = browser.find_element_by_css_selector("input#username")
passwordField = browser.find_element_by_css_selector("input#password")

loginField.send_keys(login)
passwordField.send_keys(password)
passwordField.submit()


