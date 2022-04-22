from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import json

app = Flask(__name__)

f = open('../lesson.json')
lesson = json.load(f)
f1 = open('../quiz.json')
quiz = json.load(f1)

right_choices = 0

# ROUTES
@app.route('/')
def home():
   return render_template('home.html', lesson = lesson)   

@app.route('/lesson')
def menu():
    return render_template('menu.html', lesson = lesson)

@app.route('/lesson/clef/<id>')
def clef(id = None):
    return render_template('clef.html', lesson = lesson["clef"][id], id = id)

@app.route('/lesson/staff/<id>')
def staff(id = None):
    return render_template('staff.html', lesson = lesson["staff"][id], id = id)

@app.route('/quiz/<id>')
def quizyourself(id = None):
    return render_template('quiz.html', quiz = quiz["quiz"][id], id = id, right = right_choices)

@app.route('/quiz/<id>', methods=['POST'])
def add_right(id=None):
    json_data = request.get_json() 
    global right_choices
    right_choices += json_data["right"]
    print(right_choices)
    return jsonify(result = right_choices)


if __name__ == '__main__':
   app.run(debug = True)



