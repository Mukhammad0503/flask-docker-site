import requests
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Telegram ma'lumotlaringni shu yerga yoz
BOT_TOKEN = '7822090210:AAHXaZUC0nazAme1JFwPUkwVaqdwLZXqSFE'
CHAT_ID = '1582731335'

def send_to_telegram(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': text
    }
    try:
        requests.post(url, data=payload)
    except:
        print("Telegramga yuborishda xatolik!")

def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ism TEXT,
                    familiya TEXT,
                    telefon TEXT
                )''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    ism = request.form['ism']
    familiya = request.form['familiya']
    telefon = request.form['telefon']
    if not telefon.startswith('+998') or len(telefon) != 13:
        return "Faqat O'zbekiston telefon raqamlari qabul qilinadi!"

    msg = f"✅ Yangi foydalanuvchi:\n👤 Ism: {ism}\n👥 Familiya: {familiya}\n📱 Telefon: {telefon}"
    send_to_telegram(msg)

    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (ism, familiya, telefon) VALUES (?, ?, ?)", (ism, familiya, telefon))
    conn.commit()
    conn.close()

    return render_template('success.html')

# Flask serverni ishga tushirish
if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
