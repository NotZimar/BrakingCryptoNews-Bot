from functions import Search_for_news, Translate, importance_rate
from telethon import events, TelegramClient
import sqlite3 as sq
import asyncio


api_id = ''
api_hash = ''
bot_token = ''
Channel_id = 000000


conn = sq.connect('Main.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS members (user_id INTEGER PRIMARY KEY);''')
conn.commit()


bot = TelegramClient('Main', api_id, api_hash)
bot.start(bot_token=bot_token)


async def SendMessage(chat_id, text):
    try:
        await bot.send_message(chat_id, text, parse_mode="HTML")
    except Exception as e:
        print(f"Error while sending message: {e}")


async def Main():
    First_news = None
    while True:
        try:
            News = Search_for_news()  
            if News != First_news:
                translated = Translate(News['title'])
                importance_rated = importance_rate(News['title'])

              
                text = (
                    f"🔔 <b>خبر جدید</b>\n\n"
                    f"🌐 <b>EN:</b> {News['title']}\n\n"
                    f"🌍 <b>FA:</b> <span dir='rtl'>{translated}</span>\n\n"
                    f"📊 <b>امتیاز اهمیت:</b> {importance_rated}\n"
                    f"🔗 <a href='{News['url']}'>جزئیات بیشتر</a>"
                )


                await SendMessage(Channel_id, text)
                First_news = News
            else:
                print("It was repetition")
        except Exception as e:
            print(f"Error in Main loop: {e}")  

        await asyncio.sleep(300)


def delete_user(user_id):
    try:
        cursor.execute("DELETE FROM members WHERE user_id = ?", (user_id,))
        conn.commit()
    except Exception as e:
        print(f"Error deleting user: {e}")


def add_user(user_id):
    try:
        cursor.execute("INSERT OR IGNORE INTO members (user_id) VALUES (?)", (user_id,))
        conn.commit()
    except Exception as e:
        print(f"Error adding user: {e}")

@bot.on(events.ChatAction)
async def on_chat_action(event):
    try:
        target_channel = Channel_id
        if event.chat_id == target_channel:
            if event.user_added or event.user_joined:
                new_user = await event.get_user()
                user_id = new_user.id
                add_user(user_id)
                print(f"User added: {user_id}")
            elif event.user_left or event.user_removed:
                user = await event.get_user()
                user_id = user.id
                delete_user(user_id)
                print(f"User removed: {user_id}")
    except Exception as e:
        print(f"Error in chat action handler: {e}")

async def start_bot():
    try:
        task1 = asyncio.create_task(bot.run_until_disconnected())
        task2 = asyncio.create_task(Main())
        await asyncio.gather(task1, task2)
    except Exception as e:
        print(f"Error in start_bot: {e}")

if __name__ == '__main__':
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(start_bot())
    except Exception as e:
        print(f"An error occurred: {e}")
