from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\dynamodb\chromedriver.exe')
driver.get('https://web.whatsapp.com/')

name = input("Enter name of user : ")
msg = input("Enter the msg : ")
count = int(input('enter the number of times : '))

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('_1Plpp')
for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_35EW6')
    button.click()