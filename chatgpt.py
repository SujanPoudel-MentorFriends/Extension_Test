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
        self.report = {
            "created_date": time.strftime("%Y/%m/%d, %H:%M:%S", time.localtime()),
            "type": "Extension",
            "sub-type": "AI Chats",
            "url": "chatgpt.com",
            "test_cases": {
                "button": {
                    "boom": False,
                    "boom_chats": False,
                    "boom_all": False
                },
                "capture_type": {
                    "answer_only": False,
                    "question_answer": False
                },
                "folders": [],
                "description": "",
                "capture_button": False
            }
        }

    def ask_chatgpt(self, question):

        # Find and enter the question in the prompt area
        prompt_area = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "prompt-textarea"))
        )
        # prompt_area = self.driver.find_element(By.ID, "prompt-textarea")
        if prompt_area:
            prompt_area.clear()
            prompt_area.send_keys(question)
            time.sleep(1)
            prompt_area.send_keys(Keys.RETURN)
            print("Question sent and Enter key pressed in ChatGPT.")
            time.sleep(2)

    def boom(self):
        
        self.driver.get(self.chatgpt_url)
        time.sleep(2)

        question_input = "hello"
        self.ask_chatgpt(question=question_input)
        
        # Wait for the Boom button to be clickable and click it
        boom_area = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "boomconsole2023_boom_button"))
        )
        boom_area.click()
        self.report["test_cases"]["button"]["boom"] = True

        # Wait for the textarea to be present
        add_description = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "boomconsole2023_notes_textarea"))
        )
        time.sleep(2)

        # Clear and add text to the description textarea
        add_description.clear()
        time.sleep(1)
        description = "This is a description"
        add_description.send_keys(description)
        self.report["test_cases"]["description"] = description
        print("Text added to the description.")
        time.sleep(2)

        # print("Folder Parent Element : ", self.driver.find_element(By.ID, "Boomconsole_FMS_2023_Test 1"))

        folder_parent_element = WebDriverWait(self.driver, 30).until(
                                                EC.presence_of_element_located((By.ID, 'boomconsole2023_folder_sidebar'))
                                            )

        folder_prefix = "Boomconsole_FMS_2023_"
        folder_to_save = "Test 1"
        folder_checkbox = folder_prefix + folder_to_save
        checkbox = folder_parent_element.find_element(By.ID, folder_checkbox)
        checkbox.click()
        time.sleep(2)

        # Click the capture button
        capture_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[boomconsole2023_submit_dialog]'))
              )
        self.report["test_cases"]["capture_button"] = True
        capture_button.click()
        print("Capture button clicked.")


        pass

    def boom_chats(self):

        self.driver.get(self.chatgpt_url)
        time.sleep(2)

        question_input1 = "hello"
        self.ask_chatgpt(question=question_input1)
        time.sleep(5)

        question_input2 = "hello again"
        self.ask_chatgpt(question=question_input2) 
        time.sleep(5)

        # Wait for the Boom button to be clickable and click it
        boom_chats_area = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "booom_the_chat"))
        )
        boom_chats_area.click()
        self.report["test_cases"]["button"]["boom_chats"] = True

        # Wait for the textarea to be present
        add_description = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "boomconsole2023_notes_textarea"))
        )
        time.sleep(2)

        # Clear and add text to the description textarea
        add_description.clear()
        time.sleep(1)
        description = "This is a description"
        add_description.send_keys(description)
        self.report["test_cases"]["description"] = description
        print("Text added to the description.")
        time.sleep(2)

        # print("Folder Parent Element : ", self.driver.find_element(By.ID, "Boomconsole_FMS_2023_Test 1"))

        folder_parent_element = WebDriverWait(self.driver, 30).until(
                                                EC.presence_of_element_located((By.ID, 'boomconsole2023_folder_sidebar'))
                                            )

        folder_prefix = "Boomconsole_FMS_2023_"
        folder_to_save = "Test 1"
        folder_checkbox = folder_prefix + folder_to_save
        checkbox = folder_parent_element.find_element(By.ID, folder_checkbox)
        checkbox.click()
        time.sleep(2)

        # Click the capture button
        capture_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[boomconsole2023_submit_dialog]'))
              )
        self.report["test_cases"]["capture_button"] = True
        capture_button.click()
        print("Capture button clicked.")


        pass

    def boom_all(self):
        self.driver.get(self.chatgpt_url)
        time.sleep(2)
        
        question_input = "The Semantic Concept Connection System"
        self.ask_chatgpt(question=question_input)
        time.sleep(1)


        # Wait for the Boom button to be clickable and click it
        boom_all_chats = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "boom_all_chats_full"))
        )
        boom_all_chats.click()
        self.report["test_cases"]["button"]["boom_all"] = True

        time.sleep(1)

        folder_parent_element = WebDriverWait(self.driver, 30).until(
                                                EC.presence_of_element_located((By.ID, "boomconsole2023_folder_sidebar_boom_all"))
                                            )

        folder_prefix = "Boomconsole_FMS_2023_"
        folder_to_save = "Test 1"
        folder_checkbox = folder_prefix + folder_to_save
        checkbox = folder_parent_element.find_element(By.ID, folder_checkbox)
        checkbox.click()
        time.sleep(2)

         # Click the capture button
        start_capture_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[boomconsole2023_submit_dialog]'))
              )
        self.report["test_cases"]["capture_button"] = True
        start_capture_button.click()
        print("Start Capture button clicked.")


        
        pass


