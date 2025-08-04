from instabot import Bot
import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("IG_USERNAME")
PASSWORD = os.getenv("IG_PASSWORD")

if not USERNAME or not PASSWORD:
    raise Exception("Username or password not set in .env file")

bot = Bot()
bot.login(username=USERNAME, password=PASSWORD)

bot.follow("instagram")


user_id = bot.get_user_id_from_username("nasa")
user_posts = bot.get_user_medias(user_id, filtration=False)
if user_posts:
    bot.like(user_posts[0])

photo_path = "image.png"  
caption = "Posted via Instabot"
if os.path.exists(photo_path):
    bot.upload_photo(photo_path, caption=caption)
else:
    print(f"Photo '{photo_path}' not found.")

bot.send_message("Hello from Instabot!", ["user1","user2","user3"]) # Send message to multiple users using placeholders here

bot.unfollow("user1")
bot.logout()
