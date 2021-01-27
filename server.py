from flask import Flask, render_template, request
import time

server = Flask(__name__)

messages = [
    {'username':'vikvas','text':'Привет','timestamp': time.time()},
    {'username':'egvas','text':'Здравствуйте!','timestamp': time.time()},
    {'username':'julia_a','text':'Добрый день','timestamp': time.time()}
]

@server.route('/')
def hello():
    return '''Hello, World!
    <br>
    <a target="_blank" href=/index>Index</a>'''
@server.route('/get_messages')
def get_messages():
    after = request.args['after']
    result = []

    return{
        'messages': messages
    }

@server.route('/index')
def index():
    name = 'Вика'
    return render_template("index.html")

@server.route('/day-<num>')
def day(num):
    return render_template(f"day-{num}.html")

@server.route('/send_messages')
def send_messages():

    messages.append({
        'username': request.json['username'],
         'text': request.json['text'],
         'timestamp': time.time()
    })


server.run()

