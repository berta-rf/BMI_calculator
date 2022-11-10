from bottle import route, run, template, get, request, static_file

from main import bmi_calculator

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

run(host='0.0.0.0', port=8080)
