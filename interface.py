from flask import Flask,render_template,jsonify,request
import config
app = Flask(__name__)
@app.route('/')
def hello_flask():
    print('Welcome to flask')
    return 'Hello flask'

from project_app.utils import IPLProbability
@app.route('/probability')
def get_IPL_probability():
    data = request.form
    batting_team = data['batting_team']
    bowling_team = data['bowling_team']
    city = data['city']
    runs_left = eval(data['runs_left'])
    balls_left = eval(data['balls_left'])
    wickets = eval(data['wickets'])
    total_runs_x = eval(data['total_runs_x'])
    crr = eval(data['crr'])
    rrr = eval(data['rrr'])
       

app.run()