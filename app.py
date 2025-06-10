from flask import Flask, render_template, request
import requests
from urllib.parse import urlparse

app = Flask(__name__)

# Replace this with your actual Telegram Bot API
TELEGRAM_BOT_TOKEN = "6435298977:AAG6Svklfq3FPI5Hq8CpuqRhxxdBLImmKZs"
TELEGRAM_CHAT_ID = "@your_channel_or_user_id"  # Replace with actual chat ID or user ID

def terabox_to_mxplayer(terabox_link):
    """
    Dummy function to simulate conversion.
    Replace with real logic if needed.
    """
    parsed_url = urlparse(terabox_link)
    video_id = parsed_url.path.split('/')[-1]
    mxplayer_link = f"https://mxplayer.example.com/stream/{video_id}"
    download_link = f"https://mxplayer.example.com/download/{video_id}"
    return mxplayer_link, download_link

def send_to_telegram(download_link):
    message = f"Here is your download link: {download_link}"
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    response = requests.post(url, data=data)
    return response.ok

@app.route('/', methods=['GET', 'POST'])
def index():
    mxplayer_link = None
    download_link = None
    if request.method == 'POST':
        terabox_link = request.form.get('terabox_link')
        if terabox_link:
            mxplayer_link, download_link = terabox_to_mxplayer(terabox_link)
            send_to_telegram(download_link)
    return render_template('index.html', mxplayer_link=mxplayer_link, download_link=download_link)

if __name__ == '__main__':
    app.run(debug=True)
