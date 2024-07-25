from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from linkedin import LinkedIn
from Extension.youchat import YouChat
# from youchat import YouChat
from tkinter_display import display_report

# cmd : "C:\Users\jd100\OneDrive\Desktop\Boomconsole\Chrome\chrome-win64\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\Users\jd100\OneDrive\Desktop\Boomconsole\Chrome\chrome-win64\User Data"

# Path to your ChromeDriver executable
CHROMEDRIVER_PATH = "C:/Users/jd100/OneDrive/Desktop/Boomconsole/Chrome/chromedriver-win64/chromedriver.exe"
# Path to your Chrome binary
CHROME_PATH = "C:/Users/jd100/OneDrive/Desktop/Boomconsole/Chrome/chrome-win64/chrome.exe"

# Set up Chrome options to use the specified binary
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_options.binary_location = CHROME_PATH
chrome_options.add_argument('--no-sandbox')

# Set up ChromeDriver service
service = Service(CHROMEDRIVER_PATH)

# Create a new instance of the Chrome driver with the specified options and service
driver = webdriver.Chrome(service=service, options=chrome_options)

time.sleep(1)
# Perform actions on the webpage
print(driver.title)

# Go to the linkedin website
# linkedIn = "https://www.linkedin.com/in/saugatsingh/"
# driver.get(linkedIn)
# Create an instance of LinkedIn class and perform the check
# linkedin_instance = LinkedIn(driver)
# linkedin_instance.check_linkedin()
# linkedin_profile_url = "https://www.linkedin.com/in/saugatsingh/"
# linkedin_instance.get_linkedin_data(linkedin_profile_url)

# Create an instance of YouChat and call the method
youchat_instance = YouChat(driver)
report = youchat_instance.check_boom()
# report = youchat_instance.check_boom_all()
# report = youchat_instance.discover_you_dom()

# Display Report with tkinter
# display_report(report)

# Close the browser
driver.quit()