from selenium import webdriver

login = '*****'
password = '*****'

driver = webdriver.Firefox()
driver.get('https://vk.com/')
assert 'VK' in driver.title
el = driver.find_element_by_id('quick_email')
el.send_keys(login)
el = driver.find_element_by_id('quick_pass')
el.send_keys(password)
el = driver.find_element_by_id('quick_login_button')
el.click()
driver.implicitly_wait(10)
el = driver.find_element_by_id('myprofile')
el.click()
el = driver.find_element_by_id('post_field')
el.send_keys('ololo! this is test')
el = driver.find_element_by_id('send_post')
el.click()