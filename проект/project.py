import os
import requests

TOKEN = "8513775712:AAEQ72SNKjbzggcc_ezBXgip5coU-UiBjDU"
CHAT_ID = "1053069113"


def send_fire_report(area, coords, image_path):

    if not os.path.exists(image_path):
        print(f"❌ Файл не найден: {image_path}")
        return

    caption = (
        f"🚨 ОБНАРУЖЕН ОЧАГ ВОЗГОРАНИЯ! 🚨\n\n"
        f"📍 Координаты: {coords}\n"
        f"🔥 Площадь: {area} Га\n"
        f"🛰 Снимок: Sentinel-2 (NDVI анализ)"
    )

    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"

    with open(image_path, "rb") as photo_file:
        files = {"photo": photo_file}
        data = {"chat_id": CHAT_ID, "caption": caption}
        response = requests.post(url, files=files, data=data)

    if response.status_code == 200:
        print("✅ Фото-отчет успешно доставлен в Telegram!")
    else:
        print(f"❌ Ошибка отправки: {response.text}")


# Укажи правильный путь!
image_path = r"image.jpeg"

send_fire_report(area=10, coords="51.2, 71.4", image_path=image_path)