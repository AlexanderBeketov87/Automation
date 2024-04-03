from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Пути к драйверам 
chrome_driver_path = "chromedriver"

# Создание экземпляров 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")  # Открыть окно браузера в максимальном размере
chrome_driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

# Открытие страницы 
url = "http://the-internet.herokuapp.com/login"
chrome_driver.get(url)

# Определение локаторов полей ввода и кнопки
username_locator = "#username"
password_locator = "#password"
login_button_locator = "button[type='submit']"

# Ввод значений в поля и нажатие кнопки 
chrome_username_field = chrome_driver.find_element_by_css_selector(username_locator)
chrome_username_field.send_keys("Alex")

chrome_password_field = chrome_driver.find_element_by_css_selector(password_locator)
chrome_password_field.send_keys("Password!")

chrome_login_button = chrome_driver.find_element_by_css_selector(login_button_locator)
chrome_login_button.click()


# Закрытие браузера
time.sleep(5)  
chrome_driver.quit()

