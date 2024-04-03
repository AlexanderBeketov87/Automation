from selenium import webdriver
import time

# Открываем страницу в Chrome
chrome_driver_path = "chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")  # Открыть браузер на весь экран
chrome_browser = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

chrome_browser.get("http://the-internet.herokuapp.com/add_remove_elements/")

# Кликаем на кнопку "Add Element" пять раз
for _ in range(5):
    add_button = chrome_browser.find_element_by_xpath("//button[text()='Add Element']")
    add_button.click()
    time.sleep(1) 

# Получаем список кнопок "Delete" и выводим его размер
delete_buttons = chrome_browser.find_elements_by_xpath("//button[text()='Delete']")
print("Размер списка кнопок 'Delete' в Chrome:", len(delete_buttons))

chrome_browser.quit()