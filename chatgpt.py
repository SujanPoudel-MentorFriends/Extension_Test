from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ChatgptTest:
    def __init__(self, driver):
        self.driver = driver
        self.chatgpt_url = "https://chatgpt.com" 

    def ask_chatgpt(self, question):
        self.driver.get(self.chatgpt_url)
        time.sleep(2)
        prompt_area = self.driver.find_element(By.ID,"prompt-textarea")
        if prompt_area:
            prompt_area.clear()
            prompt_area.send_keys(question)
            time.sleep(1)
            prompt_area.send_keys(Keys.RETURN)
            print("Question sent and Enter key pressed in Chatgpt.")
            time.sleep(2)


         # Wait for the boom button to be clickable
        boom_area = self.driver.find_element(By.CLASS_NAME, "boomconsole2023_boom_button")
        boom_area.click()

        # Wait for the textarea to be present
        add_description = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "boomconsole2023_notes_textarea"))
        )
        time.sleep(1)

        # Clear the textarea if needed (optional)
        add_description.clear()
        time.sleep(1)
        
        # Add text to the textarea
        add_description.send_keys("chat")
        # add_description.send_keys(Keys.RETURN)
        print("Text added to the description.")
        time.sleep(2)


        capture_button = self.driver.find_element(By.CSS_SELECTOR, 'button[boomconsole2023_submit_dialog]')

        capture_button.click()