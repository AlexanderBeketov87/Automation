from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Пути к драйверам 
firefox_driver_path = "geckodriver"

# Создание экземпляров 
firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument("--start-maximized")
firefox_driver = webdriver.Firefox(executable_path=firefox_driver_path, options=firefox_options)

# Открытие страницы 
url = "http://the-internet.herokuapp.com/login"
firefox_driver.get(url)

# Определение локаторов полей ввода и кнопки
username_locator = "#username"
password_locator = "#password"
login_button_locator = "button[type='submit']"

# Ввод значений в поля и нажатие кнопки 
firefox_username_field = firefox_driver.find_element_by_css_selector(username_locator)
firefox_username_field.send_keys("Alex")

firefox_password_field = firefox_driver.find_element_by_css_selector(password_locator)
firefox_password_field.send_keys("Password!")

firefox_login_button = firefox_driver.find_element_by_css_selector(login_button_locator)
firefox_login_button.click()

# Закрытие браузера
time.sleep(5)  
firefox_driver.quit()
