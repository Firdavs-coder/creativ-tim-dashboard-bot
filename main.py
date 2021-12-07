import telebot
import requests
from bs4 import BeautifulSoup
from telebot import types

bot = telebot.TeleBot("5036007936:AAGgwAf8QgdAiwuJkskTCSy6S4JjmmcO-Ns", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

menu_text = '''
Frontend                     Backend
👉<b>Boostrap</b>           👉<b>Django</b>
👉<b>Angular</b>            👉<b>Flask</b>
👉<b>React</b>              👉<b>Next</b>
👉<b>Vue</b>                👉<b>Nuxt</b>
👉<b>Vuetify</b>            👉<b>Nodejs</b>
👉<b>React Bootstrap</b>    👉<b>Aspnet</b>
                             👉<b>Laravel</b>






'''

@bot.message_handler(commands=['start'])
def start(message):
    start_text = '✋Hello. This bot will give you a variety of dashboard templates. \n👉Most of these are free and some are paid. \n👉/menu'
    bot.send_message(message.chat.id,start_text)

@bot.message_handler(commands=['menu'])
def menu(message):
    bot.send_message(message.chat.id,menu_text,parse_mode='HTML')

def sendMsg(message):
    text = message.text.capitalize()
    sahifa = f"https://github.com/orgs/creativetimofficial/repositories?q={text}&type=&language=&sort="
    r = requests.get(sahifa)
    soup = BeautifulSoup(r.text, 'html.parser')
    get_three = soup.select('ul li[class="Box-row"] ')[:10]
    n=1
    general_text = """"""
    links=[]
    # print(get_three)
    # get_three = random.shuffle(get_three)
    for i in get_three:
        
        num = n
        link = i.select('a[itemprop="name codeRepository"]')[0]['href']
        links.append(link)
        try:
            title = i.select('p[itemprop="description"]')[0].text.replace('            ','').replace('\n','')
        except:
            title = None
        n+=1
        text = f"""
<b>{num}</b> {title} 
                """
        general_text +=text
    
    # print(links)

    markup = None
    if len(links) == 1:
        markup = types.InlineKeyboardMarkup(row_width=1)
        itembtna = types.InlineKeyboardButton('1', callback_data=links[0].replace('/creativetimofficial/',''))
        markup.add(itembtna,)
    elif len(links) == 2:
        markup = types.InlineKeyboardMarkup(row_width=2)
        itembtna2 = types.InlineKeyboardButton('1', callback_data=links[0].replace('/creativetimofficial/',''))
        itembtna3 = types.InlineKeyboardButton('2', callback_data=links[1].replace('/creativetimofficial/',''))
        markup.add(itembtna2,itembtna3,)
    elif len(links) == 3:
        markup = types.InlineKeyboardMarkup(row_width=2)
        itembtna2 = types.InlineKeyboardButton('1', callback_data=links[0].replace('/creativetimofficial/',''))
        itembtna3 = types.InlineKeyboardButton('2', callback_data=links[1].replace('/creativetimofficial/',''))
        itembtna4 = types.InlineKeyboardButton('3', callback_data=links[2].replace('/creativetimofficial/',''))
        markup.add(itembtna2,itembtna3,itembtna4)
    elif len(links) == 4:
        markup = types.InlineKeyboardMarkup(row_width=2)
        itembtna2 = types.InlineKeyboardButton('1', callback_data=links[0].replace('/creativetimofficial/',''))
        itembtna3 = types.InlineKeyboardButton('2', callback_data=links[1].replace('/creativetimofficial/',''))
        itembtna4 = types.InlineKeyboardButton('3', callback_data=links[2].replace('/creativetimofficial/',''))
        itembtna5 = types.InlineKeyboardButton('4', callback_data=links[3].replace('/creativetimofficial/',''))
        markup.add(itembtna2,itembtna3,itembtna4,itembtna5)
    elif len(links) == 5:
        markup = types.InlineKeyboardMarkup(row_width=3)
        itembtna2 = types.InlineKeyboardButton('1', callback_data=links[0].replace('/creativetimofficial/',''))
        itembtna3 = types.InlineKeyboardButton('2', callback_data=links[1].replace('/creativetimofficial/',''))
        itembtna4 = types.InlineKeyboardButton('3', callback_data=links[2].replace('/creativetimofficial/',''))
        itembtna5 = types.InlineKeyboardButton('4', callback_data=links[3].replace('/creativetimofficial/',''))
        itembtna6 = types.InlineKeyboardButton('5', callback_data=links[4].replace('/creativetimofficial/',''))
        markup.add(itembtna2,itembtna3,itembtna4,itembtna5,itembtna6)
    elif len(links) == 6:
        markup = types.InlineKeyboardMarkup(row_width=3)
        itembtna2 = types.InlineKeyboardButton('1', callback_data=links[0].replace('/creativetimofficial/',''))
        itembtna3 = types.InlineKeyboardButton('2', callback_data=links[1].replace('/creativetimofficial/',''))
        itembtna4 = types.InlineKeyboardButton('3', callback_data=links[2].replace('/creativetimofficial/',''))
        itembtna5 = types.InlineKeyboardButton('4', callback_data=links[3].replace('/creativetimofficial/',''))
        itembtna6 = types.InlineKeyboardButton('5', callback_data=links[4].replace('/creativetimofficial/',''))
        itembtna7 = types.InlineKeyboardButton('6', callback_data=links[5].replace('/creativetimofficial/',''))
        markup.add(itembtna2,itembtna3,itembtna4,itembtna5,itembtna6,itembtna7)
    elif len(links) == 7:
        markup = types.InlineKeyboardMarkup(row_width=4)
        itembtna2 = types.InlineKeyboardButton('1', callback_data=links[0].replace('/creativetimofficial/',''))
        itembtna3 = types.InlineKeyboardButton('2', callback_data=links[1].replace('/creativetimofficial/',''))
        itembtna4 = types.InlineKeyboardButton('3', callback_data=links[2].replace('/creativetimofficial/',''))
        itembtna5 = types.InlineKeyboardButton('4', callback_data=links[3].replace('/creativetimofficial/',''))
        itembtna6 = types.InlineKeyboardButton('5', callback_data=links[4].replace('/creativetimofficial/',''))
        itembtna7 = types.InlineKeyboardButton('6', callback_data=links[5].replace('/creativetimofficial/',''))
        itembtna8 = types.InlineKeyboardButton('7', callback_data=links[6].replace('/creativetimofficial/',''))
        markup.add(itembtna2,itembtna3,itembtna4,itembtna5,itembtna6,itembtna7,itembtna8)
    elif len(links) == 8:
        markup = types.InlineKeyboardMarkup(row_width=4)
        itembtna2 = types.InlineKeyboardButton('1', callback_data=links[0].replace('/creativetimofficial/',''))
        itembtna3 = types.InlineKeyboardButton('2', callback_data=links[1].replace('/creativetimofficial/',''))
        itembtna4 = types.InlineKeyboardButton('3', callback_data=links[2].replace('/creativetimofficial/',''))
        itembtna5 = types.InlineKeyboardButton('4', callback_data=links[3].replace('/creativetimofficial/',''))
        itembtna6 = types.InlineKeyboardButton('5', callback_data=links[4].replace('/creativetimofficial/',''))
        itembtna7 = types.InlineKeyboardButton('6', callback_data=links[5].replace('/creativetimofficial/',''))
        itembtna8 = types.InlineKeyboardButton('7', callback_data=links[6].replace('/creativetimofficial/',''))
        itembtna9 = types.InlineKeyboardButton('8', callback_data=links[7].replace('/creativetimofficial/',''))
        markup.add(itembtna2,itembtna3,itembtna4,itembtna5,itembtna6,itembtna7,itembtna8,itembtna9)
    elif len(links) == 9:
        markup = types.InlineKeyboardMarkup(row_width=5)
        itembtna2 = types.InlineKeyboardButton('1', callback_data=links[0].replace('/creativetimofficial/',''))
        itembtna3 = types.InlineKeyboardButton('2', callback_data=links[1].replace('/creativetimofficial/',''))
        itembtna4 = types.InlineKeyboardButton('3', callback_data=links[2].replace('/creativetimofficial/',''))
        itembtna5 = types.InlineKeyboardButton('4', callback_data=links[3].replace('/creativetimofficial/',''))
        itembtna6 = types.InlineKeyboardButton('5', callback_data=links[4].replace('/creativetimofficial/',''))
        itembtna7 = types.InlineKeyboardButton('6', callback_data=links[5].replace('/creativetimofficial/',''))
        itembtna8 = types.InlineKeyboardButton('7', callback_data=links[6].replace('/creativetimofficial/',''))
        itembtna9 = types.InlineKeyboardButton('8', callback_data=links[7].replace('/creativetimofficial/',''))
        itembtna10 = types.InlineKeyboardButton('9', callback_data=links[8].replace('/creativetimofficial/',''))
        markup.add(itembtna2,itembtna3,itembtna4,itembtna5,itembtna6,itembtna7,itembtna8,itembtna9,itembtna10)
    elif len(links) == 10:
        markup = types.InlineKeyboardMarkup(row_width=5)
        itembtna2 = types.InlineKeyboardButton('1', callback_data=links[0].replace('/creativetimofficial/',''))
        itembtna3 = types.InlineKeyboardButton('2', callback_data=links[1].replace('/creativetimofficial/',''))
        itembtna4 = types.InlineKeyboardButton('3', callback_data=links[2].replace('/creativetimofficial/',''))
        itembtna5 = types.InlineKeyboardButton('4', callback_data=links[3].replace('/creativetimofficial/',''))
        itembtna6 = types.InlineKeyboardButton('5', callback_data=links[4].replace('/creativetimofficial/',''))
        itembtna7 = types.InlineKeyboardButton('6', callback_data=links[5].replace('/creativetimofficial/',''))
        itembtna8 = types.InlineKeyboardButton('7', callback_data=links[6].replace('/creativetimofficial/',''))
        itembtna9 = types.InlineKeyboardButton('8', callback_data=links[7].replace('/creativetimofficial/',''))
        itembtna10 = types.InlineKeyboardButton('9', callback_data=links[8].replace('/creativetimofficial/',''))
        itembtna11 = types.InlineKeyboardButton('10', callback_data=links[9].replace('/creativetimofficial/',''))
        markup.add(itembtna2,itembtna3,itembtna4,itembtna5,itembtna6,itembtna7,itembtna8,itembtna9,itembtna10,itembtna11)
    


    # itembtna6 = types.InlineKeyboardButton('6', callback_data=links[5].replace('/creativetimofficial/',''))
    # itembtna7 = types.InlineKeyboardButton('7', callback_data=links[6].replace('/creativetimofficial/',''))
    # itembtna8 = types.InlineKeyboardButton('8', callback_data=links[7].replace('/creativetimofficial/',''))
    # itembtna9 = types.InlineKeyboardButton('9', callback_data=links[8].replace('/creativetimofficial/',''))
    # itembtna10 = types.InlineKeyboardButton('10', callback_data=links[9].replace('/creativetimofficial/',''))
    
    # markup.add(itembtna,itembtna2,itembtna3,itembtna4,itembtna5,itembtna6,itembtna7,itembtna8,itembtna9,itembtna10,)
    
    
    # print(markup)
    

    bot.send_message(message.chat.id,general_text,parse_mode='HTML',reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # try:
    sendMsg(message)
    # except:
    #     bot.send_message(message.chat.id,'Not Found')



@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    try:
        zip = 'https://github.com/creativetimofficial/' + call.data + '/archive/refs/heads/main.zip'
        bot.send_document(call.from_user.id, zip)
    except:
        zip = 'https://github.com/creativetimofficial/' + call.data + '/archive/refs/heads/master.zip'
        bot.send_document(call.from_user.id, zip)
    # print(zip)
# https://github.com/creativetimofficial/notus-nextjs/archive/refs/heads/main.zip

# https://github.com/creativetimofficial/material-dashboard/archive/refs/heads/master.zip




bot.infinity_polling()