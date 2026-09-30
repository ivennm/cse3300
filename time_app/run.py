from datetime import datetime, timezone
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world! Visit /time for the current time.'


@app.route('/time')
def current_time():
    now = datetime.now(timezone.utc)
    return 'Current time: ' + now.strftime('%Y-%m-%d %H:%M:%S UTC')


app.run(host='0.0.0.0', port=8080)