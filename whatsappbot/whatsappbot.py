# The following "Whatsapp Bot" is made by Virej Dasani
from selenium import webdriver

browser_name = input(' m or f for Mozilla Firefox\n g or c for Google Chrome \n')

if (browser_name == "g" or browser_name == "c"):
	driver = webdriver.Chrome(executable_path="/home/virej/Downloads/Apps/drivers/chromedriver/chromedriver")
	driver.get("https://web.whatsapp.com/")
	# driver.maximize_window()

elif (browser_name == "f" or browser_name == "m"):
	driver = webdriver.Firefox(executable_path="/home/virej/Downloads/Apps/drivers/mozilladriver/geckodriver")
	driver.get("https://web.whatsapp.com/")
	# driver.maximize_window()

name = input("Enter Name of person or group: \n")
msg = input("Enter message: \n")
count = int(input("Enter Number of times to send message: \n"))


print(f"You will send: {msg} to: {name}, {count} times' \n")
input("Press any button to continue")


user = driver.find_element_by_xpath("//span[@title='{}']".format(name))
user.click()

msg_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")


for i in range(count):
	msg_box.send_keys(msg)
	driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button").click()


print(f'Success\n You have sent // {msg} // to // {name} //, // {count} // times')