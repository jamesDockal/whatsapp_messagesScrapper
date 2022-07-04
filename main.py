# Working with env file
import os
from dotenv import load_dotenv
load_dotenv()

from selenium import webdriver


driverPath = os.getenv("CHROME_DRIVE_PATH")
driver = webdriver.Chrome(driverPath)

driver.get('https://web.whatsapp.com/')