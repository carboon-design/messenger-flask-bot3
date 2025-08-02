import os
import random
from flask import Flask, request
from pymessenger.bot import Bot

app = Flask(__name__)

ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
VERIFY_TOKEN = os.environ.get('VERIFY_TOKEN')

bot = Bot(ACCESS_TOKEN)

@app.route('/', methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    else:
        output = request.get_json()
        for event in output.get('entry', []):
            for message in event.get('messaging', []):
                if message.get('message'):
                    sender_id = message['sender']['id']
                    if message['message'].get('text'):
                        send_message(sender_id, get_message())
                    elif message['message'].get('attachments'):
                        send_message(sender_id, get_message())
        return "Message Processed", 200

def verify_fb_token(token_sent):
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token', 403

def get_message():
    responses = [
        "You are stunning!",
        "We're proud of you.",
        "Keep on being you!",
        "We're grateful to know you :)"
    ]
    return random.choice(responses)

def send_message(recipient_id, response):
    bot.send_text_message(recipient_id, response)
    return "success"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
