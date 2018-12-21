
from telegram.ext import Updater, CommandHandler
import os
import datetime

path =  "/path/to/download/folder"
telegrambot = "your telegram bot key"
telegramuser = "your telegram user name"

def hello(bot, update):
    update.message.reply_text('Hello {}'.format(update.message.from_user.first_name))

def download_list(bot, update, args):
    link = " ".join(args)
    user = update.message.from_user.first_name
    print "-------------------- REQUEST BEGIN --------------------"
    print datetime.date.today()
    print "User:",user
    print "Link:",link
    if user == telegramuser:
        comanda = "spotdl --overwrite force --playlist " + link + " ; LIST=`ls | grep txt | cut -d '.' -f1`; spotdl --overwrite force --list $LIST.txt -f " + path +"$LIST; rm *.txt"
        print comanda	
        var = os.system(comanda)
        print "Result: ",var
        if var == 0:
			update.message.reply_text('Done')
        else:
            update.message.reply_text('Ooops. Something went wrong')
    else:
        update.message.reply_text('Nope')
    print "-------------------- REQUEST END --------------------"


updater = Updater(telegrambot)

updater.dispatcher.add_handler(CommandHandler('hello', hello))
#updater.dispatcher.add_handler(CommandHandler('song', download_song, pass_args=True))
#updater.dispatcher.add_handler(CommandHandler('album', donwload_album, pass_args=True))
updater.dispatcher.add_handler(CommandHandler('list', download_list, pass_args=True))

updater.start_polling()
updater.idle()

