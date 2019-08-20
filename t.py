import telebot

# from telebot import apihelper
#
# apihelper.proxy = {'mtproto':'https://proxy.digitalresistance.dog:port443'}

bot = telebot.TeleBot("796942222:AAFgpkYRokccysuYFSBzZHckHh55BmuwO20")


@bot.message_handler(content_types=['text'])
def send_echo(message):
    bot.reply_to(message, message.text)


bot.polling(none_stop=True)
