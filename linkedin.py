import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from api import fetch_api
import time
import re

linkedin_dummy = {
    "full_name": "Saugat Singh",
    "phone": "9779814641008",
    "location": "Nepal",
    "link": "https://www.linkedin.com/in/saugatsingh/",
    "image": "https://media.licdn.com/dms/image/C4E03AQGayVRKsg5WGg/profile-displayphoto-shrink_400_400/0/1560835365647?e=1727308800&v=beta&t=M3V2rggtKoLlPcEkU6ILM5bS88qR5wtzByHkt64FGFQ",
    "about": (
        "With over 7 years of expertise in driving innovation through machine learning, cloud computing, and "
        "full-stack development, an accomplished Computer Engineering professional specializes in machine learning, "
        "deep learning, computer vision, and natural language processing. Notable accomplishments include published "
        "research in prestigious journals and conferences, demonstrating proficiency in Agile project management, "
        "cloud deployment, and full-stack versatility across Python, JavaScript, and more. Renowned for swiftly "
        "prototyping POCs and delivering scalable, high-performance software systems aligned with business objectives. "
        "Certified in Fundamentals of Deep Learning, Deep Learning with PyTorch, and Proficiency in Information System "
        "Management. Key projects include leading solution architecture and development for a London startup, employing "
        "technologies such as FastAPI for backend APIs, GCP for cloud infrastructure, and React for responsive "
        "frontends, yielding impactful outcomes. Open to new opportunities for leveraging ML/AI and full-stack skills."
    ),
}

class LinkedIn:
    def __init__(self, driver):
        self.driver = driver
        self.check_url = "https://www.linkedin.com/in/saugatsingh/"
        self.linkedIn = "https://www.linkedin.com/in/saugatsingh/"        
        # Wait for the page to load
        time.sleep(5)

        self.linkedin_class = fetch_api()
        self.image_dom = self.linkedin_class['linkedin']['image']
        self.about_exper_educ_dom = self.linkedin_class['linkedin']['about_exper_educ']
        self.username_dom = self.linkedin_class['linkedin']['username']
        self.location_dom = self.linkedin_class['linkedin']['location']
        self.appendable_boom_dom = self.linkedin_class['linkedin']['appendable_boom_dom']
        self.contact_type_dom = self.linkedin_class['linkedin']['contact_type']
        self.contactInfoLink_dom = self.linkedin_class['linkedin']['contactInfoLink']
        self.contactInfoElements_dom = self.linkedin_class['linkedin']['contactInfoElements']
        self.OverlayElements_dom = self.linkedin_class['linkedin']['OverlayElements']
        self.closeModal_dom = self.linkedin_class['linkedin']['closeModal']

    def check_linkedin(self):
        self.driver.get(self.linkedIn)

        print("Image Dom : ", self.image_dom)
        try:
            # Use WebDriverWait to wait for the element to be present
            image_element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, self.image_dom))
            )
            # Get the src attribute
            image_src = image_element.get_attribute("src")
            
            print("Image Required : ", self.image_dom)
            print("Image Element  : ", image_src)
            if image_src == linkedin_dummy['image']:
                print("Image found! and data matched")
            else:
                print("Image not found!")

            print("Experience DOM : ", self.about_exper_educ_dom)
            experience_element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, self.about_exper_educ_dom))
            )
            print("Experience Element : ", experience_element)
        except Exception as e:
            print(f"An error occurred: {e}")


    def get_linkedin_data(self, profile_url):
        # Open the LinkedIn profile page
        self.driver.get(profile_url)
        
        # Give the page time to load
        time.sleep(5)
        # self.driver.implicitly_wait(5) 

        user_name = self.driver.find_element(By.CSS_SELECTOR, self.username_dom).text
        location = self.driver.find_element(By.CSS_SELECTOR, self.location_dom).text
        image_element = self.driver.find_element(By.CLASS_NAME, self.image_dom)
        final_image = image_element.get_attribute("src")

        print("Username : ", user_name)
        
        # Split location into city and country
        parts = location.split(", ")
        city = parts[0] if len(parts) > 0 else ""
        country = parts[1] if len(parts) > 1 else ""

        print("Parts : ", parts)
        print("City : ", city)
        print("Country : ", country)
        print("Image : ", final_image)

        # Find all sections with the specified class name
        sections = self.driver.find_elements(By.CSS_SELECTOR, ".artdeco-card.pv-profile-card.break-words")
        # Loop over the found sections and print their text content
        for section in sections:
            if section.text.strip() == 'About':
                print("Section Text:", section.text)
            else:
                try:
                    extra = section.find_element(By.XPATH, ".//span[@aria-hidden='true']")
                    print("Extra Element Text:", extra.text)
                except:
                    print("No extra element found in this section")
            

        final_about = None
        final_experience = None
        final_education = None

        print("ABOUT : \n ", final_about)
        print("Experience : \n ", final_experience)
        print("Education : \n ", final_education)
        # Initialize email and phone variables
        final_email = None
        final_phone = None

        # def open_contact_modal():
        #     nonlocal final_email, final_phone 
        #     # Open the LinkedIn contact modal and retrieve contact details
        #     contact_info_link = self.driver.find_element(By.ID, "top-card-text-details-contact-info")
        #     if contact_info_link:
        #         contact_info_link.click()
                
        #         print("Contact Type DOM : ", self.contact_type_dom)
        #         contact_info_elements = self.driver.find_elements(By.XPATH, f"//section[@class='{self.contact_type_dom}']")
                
        #         # print("Contact Info : ", contact_info_elements)

        #         # Extract email
        #         for element in contact_info_elements:
        #             text = element.text
        #             # print("Element text:", text)
        #             # Extract phone number
        #             phone_number_pattern = re.compile(r'\d+')
        
        #             if "Email" in text:
        #                 final_email = text.replace("Email", "").strip()
        #             elif "Phone" in text:
        #                 match = phone_number_pattern.search(text)
        #                 if match:
        #                     final_phone = match.group()


        #         print("Email : ", final_email)
        #         print("Phone : ", final_phone)

        #         # Close the modal
        #         close_modal = self.driver.find_element(By.CSS_SELECTOR, self.closeModal_dom)
        #         if close_modal:
        #             close_modal.click()
                    
        # open_contact_modal()

        # final_data = {
        #     "name": user_name,
        #     "email": final_email,
        #     "phone": [{"number": final_phone}],
        #     "avatar": final_image,
        #     "about": final_about,
        #     "experience": final_experience,
        #     "education": final_education,
        #     "isActive": True,
        #     "tag": "prospect",
        #     "notes": [{}],
        #     "addresses": [{"location": f"{country} {city}".strip()}],
        # }
        
        # print("finalData", final_data)
        # return final_data

