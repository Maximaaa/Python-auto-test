from selenium import webdriver
import time
n=0
link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    fields=browser.find_elements_by_xpath("//input[@type='text']")
    print(fields)
    for field in fields:
        n+=1
        field.send_keys(str(n))

    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()