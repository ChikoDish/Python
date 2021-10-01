from instabot import Bot
bot = Bot()
user_name = ''
user_password = ''
bot.login(username = user_name, password = user_password)
bot.upload_photo("profile.png", caption="Pic from Python Program")
