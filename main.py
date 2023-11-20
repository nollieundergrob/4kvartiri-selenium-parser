from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import sqlite3
import time
import datetime
import telegram



def parse_algorithm():
    options =webdriver.FirefoxOptions()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)
    driver.get('https://4kzn.agency/')
    username = '9083345918'
    password = 'yshiteri'
    username_input = driver.find_element(by=By.NAME, value='username')
    password_input = driver.find_element(by=By.NAME, value='password')
    username_input.send_keys(username)
    password_input.send_keys(password)
    login_button = driver.find_element(by=By.NAME, value='submit')
    login_button.click()
    driver.get('https://4kzn.agency/map.php?typeID=0&areaID=0&price_min=0&price_max=25000&sort=1&submit=ПОИСК')
    last_height = driver.execute_script("return document.body.scrollHeight")
    iframe = driver.find_element(By.ID,'listid')
    for i in range(25):
        iframe.send_keys(Keys.PAGE_DOWN)
        iframe.send_keys(Keys.PAGE_DOWN)
        iframe.send_keys(Keys.PAGE_DOWN)
        iframe.send_keys(Keys.PAGE_DOWN)
        iframe.send_keys(Keys.PAGE_DOWN)
    iframe = driver.find_element(By.XPATH,'/html/body/table/tbody/tr/td[2]/iframe')
    driver.switch_to.frame(iframe)
    td = driver.find_elements(By.TAG_NAME,'table')
    result_table = []
    for i in td:
        result_table.append(i.text)
    driver.quit()
    return result_table

class Database():
    def __init__(self):
        self.db=sqlite3.connect('hata.db')
        self.cursor=self.db.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS doma(blog)')
        self.db.commit()
    def write_new(self,record):
        self.cursor.execute('INSERT INTO doma(blog) VALUES(?)',((record),))
        self.db.commit()
    def check_blog(self):
        self.cursor.execute('SELECT * FROM doma')
        return list(self.cursor.fetchall())
    

def looking_for_new_blog(parse_list,sql_list,tg):
        print(sql_list.check_blog())
        sql_list_arr = [tup[0] for tup in sql_list.check_blog()]
        for ad in parse_list:
            if ad not in sql_list_arr :
                sql_list.write_new(ad)
                tg.send_message(ad)
            else:
                print(parse_list.index(ad))
                pass



if __name__ == "__main__":
    sql_list = Database()
    tg = telegram.Telegram_Callback()
    while True:
        time.sleep(60*5)
        print('trick ',print(datetime.datetime.now()))
        parse_list = list(parse_algorithm())
        looking_for_new_blog(parse_list,sql_list,tg)
        