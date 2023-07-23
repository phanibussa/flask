## Create a simple flask application

from flask import Flask, render_template,request,redirect,url_for

## create a flask application
app = Flask(__name__)                           ## create a flask application

@app.route('/')                                 # creating a home page
def home():                                     # home method will be called when we receive a request from '/'
    return "<b>Hello World</b>\n"               #JINJA 2 will identify the html tags and load html tags with Flask

@app.route('/welcome')                          # creating a another route page
def welcome():                                  # Welcome method will be called when we receive a request from '/welcome'
    return "Welcome to Flask"

@app.route('/index')                            # creating a another route page
def Index():                                    # Welcome method will be called when we receive a request from '/welcome'
    return render_template('index.html')

@app.route('/success/<int:score>')                                      # crating a application for person marks taking value from request ex: /success/27
def success(score):
    return "The person is passed and the score is " + str(score)         # returning the score value from browser request

@app.route('/fail/<int:score>')                                         # crating a application for person marks taking value from request ex: /success/27
def fail(score):
    return "The person is failed and the score is " + str(score)         # returning the score value from browser request

@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    if request.method == 'GET':
        return render_template('calculate.html')
    else:
        maths = float(request.form['maths'])
        science = float(request.form['science'])
        history = float(request.form['history'])

        average_marks = (maths+science+history) /3
        result = ""
        if average_marks > 50:
            result = "success"
        else:
            result = "fail"
        return redirect(url_for(result,score=average_marks))        ## redirect to with in the class functions
       #return render_template('result.html',results=average_marks)  ## redirect to html pages 
        ## Assignemnt Try for loop



if __name__ == '__main__':                      ## entry point for Flask
    app.run(debug=True)                         # debug = True will automatically realod application if we have any code changes
                                                # no need to restart the app if we have changes in the application