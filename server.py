from bottle import route, run, template, get, request, static_file, Bottle, TEMPLATE_PATH

from main import bmi_calculator

TEMPLATE_PATH.insert(0,'/home/bertraps/BMI_calculator/')

app = Bottle()

@app.route('/')
def question():
    return template('question')

@app.route("/form")
def form():
    return template('form')

@app.route('/calculate')
def calculate():
    weight = request.query.weight
    height = request.query.height
    bmi = bmi_calculator (weight, height)
    return template('calculate', bmi = bmi)

@app.get('/style.css')
def stylesheet():
    return static_file ('style.css', root='static/css')

#app.run()