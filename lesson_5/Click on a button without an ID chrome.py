from selenium import webdriver
import time

# Функция для выполнения клика на кнопке
def click_blue_button(browser):
    blue_button = browser.find_element_by_xpath("//button[contains(text(), 'Click Me')]")
    blue_button.click()

# Открываем страницу в Chrome
url = "http://uitestingplayground.com/dynamicid"
chrome_driver_path = "chromedriver.exe" 
for _ in range(3):  # Запускаем скрипт 
    
    # Открываем браузер Chrome
    chrome_browser = webdriver.Chrome(executable_path=chrome_driver_path)
    chrome_browser.get(url)

    # Кликаем на синюю кнопку
    click_blue_button(chrome_browser)

    # Закрываем браузер Chrome
    time.sleep(2)  
    chrome_browser.quit()
