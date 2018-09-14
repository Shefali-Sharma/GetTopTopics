from flask import Flask, render_template, request
from core.Processing import Processing
from core.Logger import Logger
import sys
import os
app = Flask(__name__)

ErrorMessage = ['ERROR: No topics retreived. Please try another URL.']

@app.route('/')
def home():
    try:
        return render_template('home.html', topicsList = [])
    except:
        message = 'Error encountered for this data: ' + str(sys.exc_info()[0])
        Logger.error(os.path.basename(__file__), message)
        return render_template('home.html', topicsList = [])

@app.route('/callback', methods = ['POST'])
def callback():
    try:
        with open("core/storeURL.txt",'w') as f:
            f.write(request.form['input'] + "\n")
        return render_template('home.html', topicsList = [])
    except:
        message = 'Error encountered for this data: ' + str(sys.exc_info()[0])
        Logger.error(os.path.basename(__file__), message)
        return render_template('home.html', topicsList = [])

@app.route('/data', methods = ['GET'])
def getdata():
    try:
        with open("core/storeURL.txt",'r') as f:
            a = list(processObj.top_keywords_from_url(f.readline().strip(),10).to_dict()["index"].values())
            if not a:
                return render_template('home.html', topicsList = ErrorMessage)
        return render_template('home.html', topicsList = a)
    except NameError as err:
        message = 'NameError in this data: ' + str(err)
        Logger.error(os.path.basename(__file__), message)
        return render_template('home.html', topicsList = ErrorMessage)
    except TypeError as err:
        message = 'TypeError in this data: ' + str(err)
        Logger.error(os.path.basename(__file__), message)
        return render_template('home.html', topicsList = ErrorMessage)
    except ValueError as err:
        message = 'ValueError in this data: ' + str(err)
        Logger.error(os.path.basename(__file__), message)
        return render_template('home.html', topicsList = ErrorMessage)
    except AttributeError as err:
        message = 'AttributeError in this data: ' + str(err)
        loggerObj.error(os.path.basename(__file__), message)
        return render_template('home.html', topicsList = ErrorMessage)
    except:
        message = 'Error encountered for this data: ' + str(sys.exc_info()[0])
        Logger.error(os.path.basename(__file__), message)
        return render_template('home.html', topicsList = ErrorMessage)


@app.route('/about')
def about():
    return render_template('about.html', topicsList = [])

@app.route('/contact')
def contact():
    return render_template('contact.html', topicsList = [])

if __name__ == '__main__':
    loggerObj = Logger()
    processObj = Processing()
    app.run(debug = True)
