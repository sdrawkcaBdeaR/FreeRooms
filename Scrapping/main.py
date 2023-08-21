from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
# Initialize the WebDriver (replace 'chromedriver_path' with the path to your ChromeDriver executable)
driver = webdriver.Chrome()

# Load the login page
login_url = 'https://erp.iitkgp.ac.in/SSOAdministration/login.htm?sessionToken=958813B359DF37FAB81DC7B19632545C.worker3&requestedUrl=https://erp.iitkgp.ac.in/IIT_ERP3/showmenu.htm'
driver.get(login_url)

# Find and fill in the username field
username_input = driver.find_element(By.ID, 'user_id')
username_input.send_keys('user_id')  # Replace with your username

# Find and fill in the password field
password_input = driver.find_element(By.ID, 'password')
password_input.send_keys('user-password')  # Replace with your password
time.sleep(2)
# Find and fill in the security answer field
security_answer_input = driver.find_element(By.ID, 'answer')
security_answer_input.send_keys('your-answer')  # Replace with your security answer

# Find and click the "Sign In" button
sign_in_button = driver.find_element(By.ID, 'loginFormSubmitButton')
sign_in_button.click()

time.sleep(5)  # You can adjust the sleep time as needed
target_url='https://erp.iitkgp.ac.in/Acad/timetable_track.jsp?action=first'
driver.get(target_url)
# The HTML content you provided
html_content = driver.page_source

# Parse the HTML content with Beautiful Soup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all <option> elements within the <select> tag
option_elements = soup.select('select#dept option[value]:not([value="0"])')

# Extract the values from the <option> elements and store them in a list
option_values = [option['value'] for option in option_elements]

time.sleep(5)
# Navigate to the target page
extracted_data = []
for val in option_values:
    target_url = f'https://erp.iitkgp.ac.in/Acad/timetable_track.jsp?action=second&dept={val}'
    driver.get(target_url)
    time.sleep(5)
    html_content =driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    tr_elements = soup.select('table#disptab tbody tr')
    for tr in tr_elements:
        td_elements = tr.find_all('td')
        if len(td_elements) >=7:
            fourth_td_value = td_elements[5].get_text()
            fifth_td_value = td_elements[6].get_text()
            extracted_data.append((fourth_td_value, fifth_td_value))
    
# print(extracted_data)
with open('extracted_data.txt', 'w') as f:
    for item in extracted_data:
        f.write(f'{item[0]}\t{item[1]}\n')
print("Data extracted to file extracted_data.txt")
driver.quit()