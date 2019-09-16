from selenium.webdriver import Chrome, ChromeOptions
import time

EXPECTED_COLOR = "rgba(222, 20, 33, 1)"

# Visit chrome://version/ and copy profile path in place of '<chrome user profile>'
options = ChromeOptions().add_argument("--user-data-dir=<chrome user profile>")

browser = Chrome(chrome_options=options)
browser.get('https://www.browserstack.com')

# to accept cookie notification so that it doesn't interfare
cookie_cta = browser.find_element_by_id('accept-cookie-notification')
cookie_cta.click()

# Navigate to Signup Page
button = browser.find_element_by_id('signupModalButton')
button.click()

time.sleep(4)

def check_color(color, orginal_color):
    return color == orginal_color


# click on signup page
signupbutton = browser.find_element_by_id('user_submit')
signupbutton.click()


username = browser.find_element_by_id('user_full_name')
if "error" in username.get_attribute('outerHTML'):
    obtained_color = username.value_of_css_property('border-bottom-color')
    if not check_color(obtained_color, "rgba(222, 20, 33, 1)"):
        print(f"expected color is {EXPECTED_COLOR} and got {obtained_color}")

email = browser.find_element_by_id('user_email_login')
if "error" in email.get_attribute('outerHTML'):
    obtained_color = email.value_of_css_property('border-bottom-color')
    if not check_color(obtained_color, "rgba(222, 20, 33, 1)"):
        print(f"expected color is {EXPECTED_COLOR} and got {obtained_color}")

password = browser.find_element_by_id('user_password')
if "error" in password.get_attribute('outerHTML'):
    obtained_color = password.value_of_css_property('border-bottom-color')
    if not check_color(obtained_color, "rgba(222, 20, 33, 1)"):
        print(f"expected color is {EXPECTED_COLOR} and got {obtained_color}")

error_messages = ["At least 3 characters", "Invalid Email", "At least 6 characters"]
message_body_html_elements = browser.find_elements_by_class_name('msg-body')
for msg in message_body_html_elements:
    error_msg = msg.get_attribute('innerHTML').split("span")[1][1:-2]
    if error_msg not in error_messages:
        print(f"{msg.get_attribute('outerHTML')} is missing error message")

browser.close()
