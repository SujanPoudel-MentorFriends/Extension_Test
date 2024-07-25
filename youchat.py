from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from api import fetch_api
import time


class YouChat:
    def __init__(self, driver):
        self.driver = driver
        self.youChat_url = "https://www.you.com/"
        self.questions_answers_boom = [
            ("hello", "Hello! How can I assist you today?", "1. Boom"),
            ("hello again", "Hello! How can I help you today? If you have any questions or need assistance with anything, feel free to ask.", "2. Boom")
        ]
        self.boom_button_class = "boomconsole2023_boom_button"

        self.api_response = fetch_api()['you_chat']
        self.question_dom = self.api_response['you_chat']['text_question_class']
        self.answer_dom_unprocessed = self.api_response['you_chat']['text_answer_class']
        self.answer_dom = self.answer_dom_unprocessed.split(' ')[1]

        self.report = {
            'date_time': time.strftime("%Y/%m/%d, %H:%M:%S",time.localtime()),
            'url': self.youChat_url,
            'category': None,
            'result': {
                'expected_question': [],
                'actual_question': [],
                'expected_answer': [],
                'actual_answer': [],
                'expected_boom_button_text': [],
                'actual_boom_button_text': [],
                'question_match': [],
                'boom_answer_match': [],
                'boom_button_status': [],
                'errors': []
            }
        }

    def _log_error(self, error_message):
        print(error_message)
        self.report['result']['errors'].append(error_message)

    def _find_element(self, by, value, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
            return element
        except Exception as e:
            self._log_error(f"Error finding element by {by} with value {value}: {e}")
            return None

    def _wait_for_element_visibility(self, by, value, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((by, value))
            )
            return element
        except Exception as e:
            self._log_error(f"Error waiting for element visibility by {by} with value {value}: {e}")
            return None

    def ask_you_chat(self, question):
        text_area = self._find_element(By.ID, 'search-input-textarea')
        if text_area:
            try:
                text_area.clear()
                text_area.send_keys(question)
                time.sleep(2)
                text_area.send_keys(Keys.RETURN)
                print("Question sent and Enter key pressed in YouChat.")
            except Exception as e:
                self._log_error(f"Error interacting with the text area: {e}")

    def check_boom(self):
        try:
            self.driver.get(self.youChat_url)
            self.report['category'] = "Boom"

            for question, answer, boom_btn_text in self.questions_answers_boom:
                self.ask_you_chat(question)
                self.report['report']['expected_question'].append(question)
                self.report['report']['expected_answer'].append(answer)

                time.sleep(5)
            
                question_element = self._find_element(By.CSS_SELECTOR, self.question_dom)
                if question_element:
                    actual_question = question_element.text
                    self.report['report']['actual_question'].append(actual_question)
                    question_match_response = "Question Match" if actual_question == question else "Question does not match."
                    self.report['report']['question_match'].append(question_match_response)


                answer_element = self._wait_for_element_visibility(By.CSS_SELECTOR, self.answer_dom)
                if answer_element:
                    actual_answer = answer_element.text
                    cleaned_response = actual_answer.replace(boom_btn_text, "").strip()
                    self.report['report']['actual_answer'].append(cleaned_response)

                boom_element = self._find_element(By.CLASS_NAME, self.boom_button_class)
                if boom_element:
                    boom_btn_text = boom_element.text
                    self.report['report']['actual_boom_button_text'].append(boom_btn_text)
                    self.report['report']['boom_button_status'].append(boom_status)
                    cleaned_response = actual_answer.replace(boom_btn_text, "").strip()
                    # self.report['actual_answer'].append(cleaned_response)
                    response_match = "Response matches expected answer." if cleaned_response == answer else "Response does not match expected answer."
                    boom_status = "Boom button exists in YouChat." if boom_btn_text == boom_btn_text else "Boom button missing in YouChat."
                    self.report['report']['boom_answer_match'].append(response_match)

                print("Report : \n", self.report)
                return self.report
                
        except Exception as e:
            self._log_error(f"Error in check_boom: {e}")

    def check_boom_all(self):
        try:
            self.driver.get(self.youChat_url)
            self.report['category'] = "Boom All" 
            for question, answer, boom_btn_text in self.questions_answers_boom:
                self.ask_you_chat(question)
                self.report['result']['expected_question'].append(question)
                self.report['result']['expected_answer'].append(answer)
                self.report['result']['expected_boom_button_text'].append(boom_btn_text)

                time.sleep(5)

            question_elements = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, self.question_dom))
            )
            answer_elements = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, self.answer_dom))
            )
            boom_btn_elemets = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, self.boom_button_class))
            )
 
            if len(question_elements) == len(answer_elements) == len(boom_btn_elemets):
                for index, (q_element, a_element, b_element) in enumerate(zip(question_elements, answer_elements, boom_btn_elemets)):
                    boom_btn_text = b_element.text
                    actual_answer = a_element.text
                    cleaned_response = actual_answer.replace(boom_btn_text, "").strip()

                    self.report['result']['actual_question'].append(q_element.text)
                    self.report['result']['actual_answer'].append(cleaned_response)
                    self.report['result']['actual_boom_button_text'].append(b_element.text)

                    expected_question = self.questions_answers_boom[index][0]
                    expected_answer = self.questions_answers_boom[index][1]
                    expected_boom_button_text = self.questions_answers_boom[index][2]

                    # print(f"A : {expected_question} : {expected_answer} : {expected_boom_button_text}")
                    # print(f"b : {q_element.text} : {cleaned_response} : {b_element.text}")

                    question_match = "Question match" if q_element.text == expected_question else "Question doesn't match"
                    answer_match = "Answer match" if expected_answer == cleaned_response else "Answer doesn't match"
                    boom_btn_match = "Boom button text match" if b_element.text == expected_boom_button_text else "Boom button text doesn't match"

                    self.report['result']['question_match'].append(question_match)
                    self.report['result']['boom_button_status'].append(boom_btn_match)
                    self.report['result']['boom_answer_match'].append(answer_match)
            else:
                print("The number of question and answer elements does not match.")

            print("Report : \n", self.report)
            return self.report
        except Exception as e:
            self._log_error(f"Error in boom_all: {e}")

    def discover_you_dom(self):
        try:
            self.driver.get(self.youChat_url)
            self.ask_you_chat(question=self.questions_answers_boom[0][0])
            time.sleep(5)

            elements = self.driver.find_elements(By.XPATH, f"//*[contains(text(), '{self.questions_answers_boom[0][1]}')]")
            for element in elements:
                print("HTML:", element.get_attribute('outerHTML'))
                print("Class:", element.get_attribute('class'))
                print(element.text)

                parent_element = element.find_element(By.XPATH, "..")
                print("Parent HTML:", parent_element.get_attribute('outerHTML'))
                print("Parent Class:", parent_element.get_attribute('class'))
                print("Parent Text:", parent_element.text)

                grandparent_element = element.find_element(By.XPATH, "../..")
                print("Grandparent HTML:", grandparent_element.get_attribute('outerHTML'))
                print("Grandparent Class:", grandparent_element.get_attribute('class'))
                print("Grandparent Text:", grandparent_element.text)

            time.sleep(5)
        except Exception as e:
            self._log_error(f"Error in discover_you_dom: {e}")
