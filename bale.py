from telegram.ext import (Updater,MessageHandler,Filters)

def chat_id(bot, update):

    if update.message.forward_from is not None:

        forward_user_id = update.message.forward_from.id
        forward_user_name = update.message.forward_from.name
        all_info = f'''UserName :{forward_user_name}
Chatid : {forward_user_id}'''

        update.message.reply_text(all_info)

    elif update.message.forward_from_chat is not None : 

        user_id = str(update.message.forward_from_chat.id)
        user_name = str(update.message.forward_from_chat.username)
        all_usr_info = f'''UserName :{user_name}
Chatid : {user_id}'''
        update.message.reply_text(all_usr_info)

    elif update.message.forward_from_chat is None and update.message.forward_from is None:
        user_id = str(update.message.chat.id)
        user_name = str(update.message.chat.first_name)
        all_usr_info = f'''UserName :{user_name}
Chatid : {user_id}'''
        update.message.reply_text(all_usr_info)

updater = Updater(token='YOUR TOKEN',base_url="https://tapi.bale.ai/")
updater.dispatcher.add_handler(MessageHandler(Filters.all,callback=chat_id))
updater.bot.delete_webhook()
updater.start_polling(poll_interval=2)
updater.idle()
