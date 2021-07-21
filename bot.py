from removebg import RemoveBg
from telegram import *
from telegram.ext import *
import os


# rmbg.remove_background_from_img_file("hi.jpeg")

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

def read_image(update: Update, context: CallbackContext) -> None:
    """Send reply of user's message."""
    chat_id = update.message.chat_id
    # try:
    photo_file = update.message.photo[-1].get_file()
    img_name = str(chat_id)+'.jpg'
    photo_file.download(img_name)
    # update.message.reply_text("Hi, Got Your Photo And Downloaded It, Now Removing Background")
    update.message.reply_document(document=open('here.webp', 'rb'))
    # update.message.reply_animation('https://media3.giphy.com/media/xT5LMuVBDfoBDtf3tS/giphy.gif')
    rmbg = RemoveBg("y7WH8N1vKNLY6aniq4DsVFph", "error.log")
    rmbg.remove_background_from_img_file(img_name)
    no_bg = (f"{img_name}"+"_no_bg.png")
    # update.message.reply_text("Here Is Your Removed Background Photo.👇")
    update.message.reply_document(document=open(no_bg, 'rb'))
    import os
    os.remove (img_name)
    os.remove (no_bg)

updater = Updater('1088372261:AAG0vx-av9dfib7PD5R2hNJu3n7suuclvFg')

dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.photo, read_image))

updater.start_polling()
updater.idle()
