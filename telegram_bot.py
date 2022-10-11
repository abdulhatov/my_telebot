import telebot
from io import BytesIO
import os
from dotenv import load_dotenv

load_dotenv()

class MyBot:
    def __init__(self, token):
        self.bot = telebot.TeleBot(token)

    def start_bot(self):

        def start_image():
            with open('image.jpeg', 'rb') as file:
                obj = BytesIO(file.read())
                obj.name = 'Picture.jpg'
                return obj

        @self.bot.message_handler(content_types=['text', 'document', 'number'])
        def get_message(message):
            if message.text.lower() == 'hello':
                self.bot.send_message(message.from_user.id, "Hi")
            elif message.text.lower() == 'hi':
                self.bot.send_message(message.from_user.id, "Hello")
            elif message.text.lower() == 'image':
                image = start_image()
                self.bot.send_document(message.chat.id, document=image, caption="Your Picture")
            else:
                self.bot.send_message(message.chat.id, "I don't know")

        self.bot.polling(none_stop=True)


myBot = MyBot(os.getenv('TOKEN'))
myBot.start_bot()
