from bottle import route, run, template, get, request, static_file, Bottle

from main import bmi_calculator

app = Bottle()

@route('/')
def question():
    return template('question')

@route("/form")
def form():
    return template('form')

@route('/calculate')
def calculate():
    weight = request.query.weight
    height = request.query.height
    bmi = bmi_calculator (weight, height)
    return template('calculate', bmi = bmi)




@get('/style.css')
def stylesheet():
    return static_file ('style.css', root='static/css')

app.run()