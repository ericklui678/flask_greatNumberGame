from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
randomNum = random.randrange(0,101)

@app.route('/')
def index():
    try:
        userNum = session['userNum']
    except KeyError: # if userNum is undefined, just render index.html
        return render_template('index.html')
    else: # if userNum is defined
        userNum = str(userNum)  # convert input from unicode to str
        print randomNum
        for i in userNum:   # if there are any alphabets, return error
            if i.isalpha():
                return render_template('index.html', msg='Invalid input!', id='red')
        userNum = int(userNum)
        if userNum < randomNum:
            msgInput = 'Too low!'
            idInput = 'red'
        elif userNum > randomNum:
            msgInput = 'Too high!'
            idInput = 'red'
        elif userNum == randomNum:
            msgInput = str(userNum) + ' was the number!'
            idInput = 'green'
        return render_template('index.html', msg=msgInput, id=idInput)

    return render_template('index.html')

@app.route('/process', methods=['POST'])
def saveRandomNum():
    # if request.form['action'] == 'reset':
    #     print 'reset'
    session['userNum'] = request.form['userInput']
    return redirect('/')

# @app.route('/check')
# def logicRoute():
#     userNum = str(session['userNum'])
#     print userNum
#     print randomNum
#     for i in userNum:
#         if i.isalpha():
#             return render_template('incorrect.html')
#     if (userNum < randomNum):
#         print 'too low'
#         return render_template('tooLow')

    # return redirect('/')

# @app.route('/test')
# def test():
#     # userNum = int(userNum)
#     userNum = str(userNum)
#     # check if any characters are alphabet
#     for i in userNum:
#         if i.isalpha():
#             return render_template('incorrect.html')
#
#     # convert to int type
#     userNum = int(userNum)
#     print userNum
#     print randomNum
#     if (userNum >= 1 and userNum <= 100):
#         if (userNum == randomNum):
#             print "YOU WINNER"
#         else:
#             print "YOU LOSER"

app.run(debug = True)
