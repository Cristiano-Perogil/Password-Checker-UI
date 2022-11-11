from flask import Flask, render_template, request
from password import passwordChecking

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.get('/testeGetLegal')
def teste():
    return {"Hellow": "World"}

    
@app.route('/submit', methods=['POST', 'GET'])
def gettingUserInput():
    if request.method == 'POST':
        data= request.form.to_dict()
        input = data['password-field']
        res = passwordChecking(input)
        return render_template('index.html', response=res)
    else:
        return print("sorry, but something went wrong")