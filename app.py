from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import winsound

class instagramBot:
  def __init__(self, username, password, hashtag):
    self.username = username
    self.password = password
    self.hashtag = hashtag
    self.bot = webdriver.Firefox()
  def login(self):
    bot = self.bot
    bot.get('https://www.instagram.com/?hl=eng')
    time.sleep(3)
    bot.find_element_by_css_selector('a[href="/accounts/login/?source=auth_switcher"]').click()
    time.sleep(3)
    username = bot.find_element_by_name('username')
    password = bot.find_element_by_name('password')
    username.clear()
    password.clear()
    username.send_keys(self.username)
    password.send_keys(self.password)
    password.send_keys(Keys.RETURN)
    time.sleep(7)
    bot.get('https://www.instagram.com/explore/tags/' + self.hashtag + '/?hl=eng')
    time.sleep(5)
    for i in range(0, 3):
      bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
      time.sleep(3)
    photos = bot.find_elements_by_class_name('v1Nh3')
    links = [elem.find_element_by_css_selector('a').get_attribute('href') for elem in photos]
    number = 0
    for link in links:
      print(number)
      number = number+1
      bot.get(link)
      time.sleep(2)
      bot.find_element_by_css_selector('.fr66n > button').click()
      time.sleep(3)
    winsound.PlaySound('hey', winsound.SND_FILENAME)

me_username = input('Input instagram username/email: ')
me_password = input('Input instagram username password: ')
me_hashtag = input('Input hashtag to loop throught: ')
me = instagramBot( me_username, me_password, me_hashtag)
me.login()
quit()