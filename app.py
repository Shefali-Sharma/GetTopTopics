from flask import Flask, render_template, request
import processing
app = Flask(__name__)

Topics = ["2 slice toaster","asda","asdad","ad", "aa"]

@app.route('/')
def home():
    return render_template('layout.html', topicsList = [])

@app.route('/callback', methods = ['POST'])
def callback():
    with open("text.log",'w') as f:
        f.write(request.form['input'] + "\n")
    # myInput = request.form['inputURL']
    return render_template('layout.html', topicsList = Topics)

@app.route('/data', methods = ['GET'])
def getdata():
    with open("text.log",'r') as f:
        a = list(processing.top_keywords_from_url(f.readline().strip(),10).to_dict()["index"].values())
    return render_template('layout.html', topicsList = a)

if __name__ == '__main__':
    app.run(debug = True)
