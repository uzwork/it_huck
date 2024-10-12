import cv2
import telegram
import asyncio
from telegram.error import TelegramError

# Telegram bot tokeni va chat ID
bot_token = '7925588858:AAFGMuT9v_VYA0N58pz1xavBcyu-EkNhPxw'
chat_id = '5187636817'

# Kamera ochish va tasvir olish funktsiyasi
def capture_image(filename='frame.jpg'):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Kamera ochilmadi!")
        return False

    ret, frame = cap.read()
    if not ret:
        print("Kadro olishda xatolik!")
        cap.release()
        return False

    cv2.imwrite(filename, frame)
    cap.release()
    return filename

# Asinxron Telegram orqali rasm yuborish funktsiyasi
async def send_image_to_telegram(filename):
    bot = telegram.Bot(token=bot_token)
    try:
        with open(filename, 'rb') as image_file:
            # Asinxron yuborish uchun 'await' ishlatamiz
            await bot.send_photo(chat_id=chat_id, photo=image_file)
            print("Rasm muvaffaqiyatli yuborildi!")
    except TelegramError as e:
        print(f"Telegram orqali yuborishda xatolik: {e}")
    except FileNotFoundError:
        print(f"'{filename}' fayli topilmadi.")

# Asosiy dastur
async def main():
    image_file = capture_image()
    if image_file:
        await send_image_to_telegram(image_file)

# Dastur ishga tushishi
if __name__ == '__main__':
    asyncio.run(main())
