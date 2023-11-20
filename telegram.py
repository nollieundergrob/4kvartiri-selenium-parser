import telebot
import random




class Telegram_Callback():
    def __init__(self):
        self.bot=telebot.TeleBot('ENTER YOUR TELEBOT API')
        self.owner_list=['ENTER THE PERSONS WHOS NEED TO MESSAGE',
                         'ENTER THE PERSONS WHOS NEED TO MESSAGE'
                         ]
        random_value =["мачо-дача-хата-хаус","Ищу квартиру","Подбираю новые варики..."]
        [self.bot.send_message(i,random.choice(random_value)) for i in self.owner_list]
    def send_message(self,text):
        for i in self.owner_list:
            try:
                self.bot.send_message(i,text,parse_mode='HTML')
            except:
                pass