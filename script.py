import arabic_reshaper
import requests
from bidi.algorithm import get_display
from PIL import Image, ImageDraw, ImageFont
import os
import logging
from datetime import datetime
import time
import re
from khayyam import *

def convert_to_persian(number):
    # Mapping of English digits to Persian digits
    persian_digits = {
        '0': '۰',
        '1': '۱',
        '2': '۲',
        '3': '۳',
        '4': '۴',
        '5': '۵',
        '6': '۶',
        '7': '۷',
        '8': '۸',
        '9': '۹'
    }
    
    # Convert the number to a string with comma separators
    formatted_number = f"{number:,}"
    
    # Replace English digits with Persian digits
    persian_number = re.sub(r'[0-9]', lambda x: persian_digits[x.group()], formatted_number)
    
    return persian_number

bot_token = '7759907035:AAGht_v717Q6II3NsEgmQ5sLB2zBp_8IkOk'
chat_id = -1002362960489
url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
while True:
    try:
        if (datetime.now().hour == 11 and datetime.now().minute == 30) or (datetime.now().hour == 17 and datetime.now().minute == 0) or (datetime.now().hour == 21 and datetime.now().minute == 0)  :
            response = requests.get("https://milli.gold/api/v1/public/milli-price/detail")
            price = convert_to_persian(int(response.json()['price18']) * 1000)
            img = Image.open("./11.png") if datetime.now().hour == 11 else Image.open("./17.png") 
            price_font = ImageFont.truetype('./YekanBakhFaNum-SemiBold.ttf',100, encoding='unic')
            persian_date_font = ImageFont.truetype('./YekanBakhFaNum-SemiBold.ttf',36, encoding='unic')
            rial_font = ImageFont.truetype('./YekanBakhFaNum-SemiBold.ttf',80, encoding='unic')
            draw = ImageDraw.Draw(img)
            now = JalaliDatetime.now()
            persian_date = now.strftime('%Y/%m/%d')
            price_text = get_display(arabic_reshaper.reshape(price))
            persian_date_text = get_display(arabic_reshaper.reshape(persian_date))
            rial_text = get_display(arabic_reshaper.reshape('ریال'))
            draw.text((645, 610), persian_date_text, fill =(255, 255, 255), font=persian_date_font)
            draw.text((200, 750), rial_text, fill =(61, 64, 74), font=rial_font)
            draw.text((350, 750), price_text, fill =(5, 16, 97), font=price_font)
            img.save('/var/www/html/result.png')
            link = 'https://mahdiyar.me/result.png'
            data = {'chat_id': chat_id, 'text': link, 'parse_mode': 'HTML'}
            response = requests.post(url, data=data)
            if response.status_code == 200:
                logging.info('Message sent successfully.')
            else:
                logging.info(f'Error sending message: {response.text}')
            time.sleep(59)
        else:
            logging.info("it's not time to send message")
    except Exception as e:
        logging.info('bot error {}'.format(e))
        

