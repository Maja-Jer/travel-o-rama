import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'It is travel time soon'

if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=os.environ.get('PORT', '5000'),
            debug=True)