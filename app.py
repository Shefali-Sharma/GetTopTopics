from flask import Flask, render_template, request
import processing
import sys
app = Flask(__name__)

Topics = []

@app.route('/')
def home():
    try:
        return render_template('home.html', topicsList = [])
    except:
        print ('Error encountered for this data: ' + str(sys.exc_info()[0]))
        return render_template('home.html', topicsList = [])

@app.route('/callback', methods = ['POST'])
def callback():
    try:
        with open("text.log",'w') as f:
            f.write(request.form['input'] + "\n")
        return render_template('home.html', topicsList = Topics)
    except:
        print ('Error encountered for this data: ' + str(sys.exc_info()[0]))
        return render_template('home.html', topicsList = [])

@app.route('/data', methods = ['GET'])
def getdata():
    try:
        with open("text.log",'r') as f:
            a = list(processing.top_keywords_from_url(f.readline().strip(),10).to_dict()["index"].values())
            if not a:
                return render_template('home.html', topicsList = [])
        return render_template('home.html', topicsList = a)
    except NameError as err:
        print ('NameError in this data: ' + str(err))
        return render_template('home.html', topicsList = [])
    except TypeError as err:
        print ('TypeError in this data: ' + str(err))
        return render_template('home.html', topicsList = [])
    except ValueError as err:
        print ('ValueError in this data: ' + str(err))
        return render_template('home.html', topicsList = [])
    except:
        print ('Error encountered for this data: ' + str(sys.exc_info()[0]))
        return render_template('home.html', topicsList = [])


if __name__ == '__main__':
    app.run(debug = True)
