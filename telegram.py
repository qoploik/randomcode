import telebot

bot = telebot.TeleBot("1844485254:AAFW3WVhY-F6WHdDgMgWlGFc2wEosqO6-b8")

@bot.message_handler(content_types=['text'])
def send_echo (message):
	#bot.reply_to(message, "Howdy, how are you doing?")
    bot.reply_to(message.chat.id, message.text)

bot.polling ( none_stop = True )