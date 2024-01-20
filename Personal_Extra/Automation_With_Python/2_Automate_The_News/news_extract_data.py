from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd


web_url = 'https://www.thesun.co.uk/sport/football/'
chrome_driver_path = "C:/Program Files/chromedriver-win64/chromedriver.exe"  # introduce path here


# Creating the driver
driver_service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=driver_service)
driver.get(web_url)

# Finding Elements
containers = driver.find_elements(by='xpath', value='//div[@class="teaser__copy-container"]')

titles = []
subtitles = []
links = []
for container in containers:
    title = container.find_element(by='xpath', value='./a/h2').text
    subtitle = container.find_element(by='xpath', value='./a/p').text
    link = container.find_element(by='xpath', value='./a').get_attribute('href')
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

# Exporting data to a CSV file
my_dict = {'title': titles, 'subtitle': subtitles, 'link': links}
df_headlines = pd.DataFrame(my_dict)
df_headlines.to_csv('headline.csv')

driver.quit()
