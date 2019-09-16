from selenium.webdriver import Chrome, ChromeOptions
import time

EMAIL_ID = "<email id here>"

def slow_typing(element, text):
    for character in text:
        element.send_keys(character)
        time.sleep(0.3)


# Visit chrome://version/ and copy profile path in place of '<chrome user profile>'
options = ChromeOptions().add_argument("--user-data-dir=<chrome user profile>")

browser = Chrome(chrome_options=options)
browser.get('https://www.browserstack.com')

time.sleep(2)

# to accept cookie notification so that it doesn't interfare
cookie_cta = browser.find_element_by_id('accept-cookie-notification')
cookie_cta.click()


# Navigate to Signup Page
button = browser.find_element_by_id('signupModalButton')
button.click()

time.sleep(2)

# Fill user's full name
username = browser.find_element_by_id('user_full_name')
# username.send_keys('John Doe')
slow_typing(username, 'John Doe')

time.sleep(1)
# Fill user's email ID
email = browser.find_element_by_id('user_email_login')
slow_typing(email, EMAIL_ID)

time.sleep(2)
# Fill user's password
password = browser.find_element_by_id('user_password')

# Reads password from a text file because 
# saving the password in a script is just silly. 
with open('password.txt', 'r') as myfile: 
	Password = myfile.read().replace('\n', '') 
slow_typing(password, Password)

time.sleep(1)
# click on Terms and Condition
toc = browser.find_element_by_name('terms_and_conditions')
toc.click()

# click on signup page
signupbutton = browser.find_element_by_id('user_submit')
signupbutton.click()

time.sleep(20)

browser.close()
