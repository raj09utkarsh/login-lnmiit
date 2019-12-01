from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import pynotify

def login():
	try:
		options = Options()
		options.add_argument("--headless")
		driver = webdriver.Chrome('/Users/utkarshraj/desktop/chromedriver', options = options)

		pynotify.notify("Loggin In...", "Connecting to 172.22.2.6/connect")

		driver.get("https://172.22.2.6/connect/PortalMain")

		time.sleep(1)


		username_xpath = '//*[@id="LoginUserPassword_auth_username"]'
		username = driver.find_elements_by_xpath(username_xpath)
		username[0].send_keys("ENTER YOUR USER NAME")

		time.sleep(1)


		password_xpath = '//*[@id="LoginUserPassword_auth_password"]'
		password = driver.find_elements_by_xpath(password_xpath)
		password[0].send_keys("ENTER YOUR PASSWORD")

		time.sleep(1)


		login_button = driver.find_elements_by_xpath('//*[@id="UserCheck_Login_Button_span"]')
		login_button[0].click()

		time.sleep(1)
		pynotify.notify("Loggin In...", "Connection successfull")
		driver.quit()
		return True
	except:
		pynotify.notify("Loggin In...", "Connection failed")
		return False


def timeOut():
	timeoutTime = time.time() + 5
	while True:
		if time.time() > timeoutTime:
			pynotify.notify("Loggin In...", "Taking too long to response")
			sys.exit()


if __name__ == "__main__":
	conn = login()
	if conn == False:
		timeOut()
