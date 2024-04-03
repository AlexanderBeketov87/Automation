from selenium import webdriver
import time

# Функция для выполнения клика на кнопке
def click_blue_button(browser):
    blue_button = browser.find_element_by_xpath("//button[contains(text(), 'Click Me')]")
    blue_button.click()

# Открываем страницу в Firefox
url = "http://uitestingplayground.com/dynamicid"
firefox_driver_path = "geckodriver"  # Укажите путь к geckodriver
for _ in range(3):  

    # Открываем браузер Firefox
    firefox_browser = webdriver.Firefox(executable_path=firefox_driver_path)
    firefox_browser.get(url)

    # Кликаем на синюю кнопку
    click_blue_button(firefox_browser)

    # Закрываем браузер Firefox
    time.sleep(2)  # Даем немного времени для наблюдения
    firefox_browser.quit()