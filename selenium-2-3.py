from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
'''
Selenium lesson

    Open page http://suninjuly.github.io/explicit_wait2.html
    Wait for price decreasing to $100 (not less than 12 sec)
    Press button "Book"
    Solve mathematical task (by code) and send result
'''


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

	# Find button
    button = browser.find_element(By.ID, "book")  
	
	# HTML code  <h5 id="price" style="display:inline;float:right">$95</h5>
	# Waiting for the condition
	bu = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"),"$100"))
	button.click()


	# Scroll page down
	button2 = browser.find_element(By.ID, "solve")   
    _ = button2.location_once_scrolled_into_view	
	
	# HTML code with new button <button id="book" class="btn btn-primary" onclick="checkPrice();" style="margin-top: 20px;" disabled="">Book</button>

	# Reading х attribute and calculating the answer
    x = int(browser.find_element(By.ID, "input_value").get_attribute("textContent").strip())
    sum_xy = calc(x)
    print(sum_xy)

	# Entering answer
    input1 = browser.find_element(By.CSS_SELECTOR, '[id="answer"]')
    input1.send_keys(sum_xy)
	
	# Press button
    button2.click()

    time.sleep(1)

finally:
    time.sleep(5)
    # Close window
    browser.quit()