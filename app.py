# app.py
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

DISCORD_BOT_TOKEN = 'MTI4ODc2NzAyMDU0Mzc3NDcyMA.GkySIp.o2_6goRltN0HKUe_WR8Y6PvlI2IIyO3R_elfC4'
CHANNEL_ID = '1288921771382280263'  # ID des Discord-Kanals

@app.route('/')
def home():
    return "<h1>Willkommen beim Bot Dashboard!</h1>"

@app.route('/send_message', methods=['POST'])
def send_message():
    content = request.json.get('content')
    if content:
        url = f'https://discord.com/api/v9/channels/{CHANNEL_ID}/messages'
        headers = {
            'Authorization': f'Bot {DISCORD_BOT_TOKEN}',
            'Content-Type': 'application/json'
        }
        data = {'content': content}
        response = requests.post(url, headers=headers, json=data)
        return jsonify({'status': 'success', 'data': response.json()}), response.status_code
    return jsonify({'status': 'error', 'message': 'Kein Inhalt angegeben.'}), 400

if __name__ == '__main__':
    app.run(port=5000)
