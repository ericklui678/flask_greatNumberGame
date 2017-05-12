from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
randomNum = random.randrange(1,101)

@app.route('/')
def index():
    try:
        userNum = session['userNum']
    except KeyError: # if userNum is undefined, just render index.html
        return render_template('index.html', resetId='resetHide', hideClass='show')
    else: # if userNum is defined
        userNum = str(userNum)  # convert input from unicode to str
        print randomNum
        for i in userNum:   # if there are any alphabets, return error
            if i.isalpha():
                return render_template('index.html', msg='Invalid input!', id='red', resetId='resetHide', hideClass='show')
        userNum = int(userNum)
        if userNum < randomNum:
            msgInput = 'Too low!'
            idInput = 'red'
            resetInput = 'resetHide'
            classHide = 'show'
        elif userNum > randomNum:
            msgInput = 'Too high!'
            idInput = 'red'
            resetInput = 'resetHide'
            classHide = 'show'
        elif userNum == randomNum:
            msgInput = str(userNum) + ' was the number!'
            idInput = 'green'
            resetInput = 'resetShow'
            classHide = 'hide'
        return render_template('index.html', msg=msgInput, id=idInput, resetId=resetInput, hideClass=classHide)

    return render_template('index.html')

@app.route('/process', methods=['POST'])
def saveRandomNum():
    if request.form['action'] == 'check':
        session['userNum'] = request.form['userInput']
        return redirect('/')
    if request.form['action'] == 'reset':
        global randomNum
        randomNum = random.randrange(1,101)
        return redirect('/')

app.run(debug = True)
