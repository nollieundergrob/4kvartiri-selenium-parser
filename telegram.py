import telebot
import random




class Telegram_Callback():
    def __init__(self):
        self.bot=telebot.TeleBot('5970795201:AAE_tCispiE9cegcMkNyOQw3MxgFlxPWebg')
        self.owner_list=['1041676367',
                         '1366212051'
                         ]
        random_value =["мачо-дача-хата-хаус","Ищу квартиру","Подбираю новые варики..."]
        [self.bot.send_message(i,random.choice(random_value)) for i in self.owner_list]
    def send_message(self,text):
        for i in self.owner_list:
            try:
                self.bot.send_message(i,text,parse_mode='HTML')
            except:
                pass