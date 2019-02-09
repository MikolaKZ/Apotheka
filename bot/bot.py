from telegram.ext import Updater,CommandHandler,MessageHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup 
from settings import API_KEY, PROXY
import logging, random
from db import setDBUserPassword

def main():
    mybot = Updater(API_KEY, request_kwargs=PROXY)
    logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CallbackQueryHandler(inline_button_pressed))
    mybot.start_polling()
    mybot.idle()

def greet_user(bot, update):
    inlinekeyboard = [[InlineKeyboardButton("Авторизоваться", callback_data='1')]]
    reply_markup = InlineKeyboardMarkup(inlinekeyboard)
    update.message.reply_text("Добро пожаловать! Нажмите авторизоваться для связи бота с порталом", 
        reply_markup=reply_markup)

def inline_button_pressed(bot, update):
    query = update.callback_query
    chat_id=query.message.chat.id
    psw=getRandomValue(8)
    bot.answerCallbackQuery(query.id,"Ваш пароль подтверждение:\n {}" .format(psw),True)
    bot.sendMessage(chat_id=chat_id,text="Ваш пароль подтверждение:\n {}" .format(psw))
    if setDBUserPassword(psw,chat_id) ==False:
          bot.sendMessage(chat_id=chat_id,text="Что то пошло не так, попробуйте позже")

    
def getRandomValue(lengthNumber):
    psw=(''.join([random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')) for x in range(lengthNumber)]))
    return psw


if __name__ == "__main__":
    main()