import datetime
import telebot
import requests
from bs4 import BeautifulSoup

TOKEN = '1850062110:AAFJTXGQNF5KsWRcN27-vacqau8vMHG3nAM'
bot = telebot.TeleBot(TOKEN)
keyboard = telebot.types.ReplyKeyboardMarkup()
button1 = telebot.types.KeyboardButton(1)
button2 = telebot.types.KeyboardButton(2)
button3 = telebot.types.KeyboardButton(3)
button4 = telebot.types.KeyboardButton(4)
button5 = telebot.types.KeyboardButton(5)
button6 = telebot.types.KeyboardButton(6)
button7 = telebot.types.KeyboardButton(7)
button8 = telebot.types.KeyboardButton(8)
button9 = telebot.types.KeyboardButton(9)
button10 = telebot.types.KeyboardButton(10)
button11 = telebot.types.KeyboardButton(11)
button12 = telebot.types.KeyboardButton(12)
button13 = telebot.types.KeyboardButton(13)
button14 = telebot.types.KeyboardButton(14)
button15 = telebot.types.KeyboardButton(15)
button16 = telebot.types.KeyboardButton(16)
button17 = telebot.types.KeyboardButton(17)
button18 = telebot.types.KeyboardButton(18)
button19 = telebot.types.KeyboardButton(19)
button20 = telebot.types.KeyboardButton(20)
keyboard.add(button1, button2, button3, button4, button5, button6, button7,
             button8, button9, button10, button11, button12, button13, button14,
             button15, button16, button17, button18, button19, button20)



url = f'https://kaktus.media/?lable=8&date={datetime.date.today()}&order=time'
html = requests.get(url).text
soup = BeautifulSoup(html, 'lxml')
news = soup.find_all('div', class_='ArticleItem')[:20]

@bot.message_handler(commands=['start', 'news'])
def start(message):
    for i in range(len(news)):
        bot.send_message(message.chat.id, f'{i+1}.{news[i].text.strip()}', reply_markup=keyboard)
    bot.register_next_step_handler(message, check)

def check(message):
    link = news[int(message.text)-1].find('a', class_='ArticleItem--image').get('href')
    title = news[int(message.text)-1].find('a', class_='ArticleItem--name').text
    bot.send_message(message.chat.id, f'{title}\n\n{link}')

bot.polling()