from selenium import webdriver
import time

# Открываем страницу в Firefox
firefox_driver_path = "geckodriver"
firefox_browser = webdriver.Firefox(executable_path=firefox_driver_path)

firefox_browser.get("http://the-internet.herokuapp.com/add_remove_elements/")

# Кликаем на кнопку "Add Element" пять раз
for _ in range(5):
    add_button = firefox_browser.find_element_by_xpath("//button[text()='Add Element']")
    add_button.click()
    time.sleep(1) 

# Получаем список кнопок "Delete" и выводим его размер
delete_buttons = firefox_browser.find_elements_by_xpath("//button[text()='Delete']")
print("Размер списка кнопок 'Delete' в Firefox:", len(delete_buttons))

firefox_browser.quit()