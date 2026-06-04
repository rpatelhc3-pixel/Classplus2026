#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "33891184"))
API_HASH = environ.get("API_HASH", "ba3af95840d1746b1bc0609cddb5800d")
BOT_TOKEN = environ.get("BOT_TOKEN", "8872760790:AAHsvubcuEXr_LsDYLaeKn_D_iL60XQ5qNc")

OWNER = int(environ.get("OWNER", "620932167"))
CREDIT = environ.get("CREDIT", "PATEL 𝘽𝙊𝙏𝙎")

TOTAL_USER = os.environ.get('TOTAL_USERS', '6201066540').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '6201066540').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello Flask!"

if __name__ == '__main__':
    app.run(debug=True, port=8000)
