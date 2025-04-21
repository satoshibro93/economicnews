import asyncio
from telegram import Bot
from telegram.constants import ParseMode
from config import BOT_TOKEN, CHANNEL_USERNAME
from utils import fetch_mock_news, rephrase_text

bot = Bot(token=BOT_TOKEN)

async def post_news_loop():
    while True:
        news = fetch_mock_news()
        if news:
            text = rephrase_text(news)
            await bot.send_message(chat_id=CHANNEL_USERNAME, text=text, parse_mode=ParseMode.HTML)
        await asyncio.sleep(1500)  # 25 минут

if __name__ == "__main__":
    asyncio.run(post_news_loop())