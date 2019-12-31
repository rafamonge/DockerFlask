from flask import Flask, render_template, request
import AwesomeModel
import pandas as pd
import os
import sys


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/proxy")
def proxy():
    temp = "</p><p>{os.environ['HTTP_PROXY']}</p><p>{os.environ['http_proxy']}</p><p>{os.environ['HTTPS_PROXY']}</p>"
    temp = os.environ['http_proxy']
    temp = "<h1>Proxies</h1><p>"  + temp
    return temp

@app.route("/predict/<int:input>")
def predict(input):
    model = AwesomeModel.Model()
    output = model.predict(input)
    return render_template("predict.html", input=input, output=output)

@app.route("/predict_simple", methods=['GET', 'POST'])
def predict_simple():
    content = request.json
    model = AwesomeModel.Model()
    df = pd.DataFrame(content["data"])
    res = model.predict_df(df)
    return res.to_json(orient='records', lines=True)

@app.route("/networktest/<hostname>")
def networktest(hostname):
    print(hostname)
    response = os.system("ping -c 1 " + hostname)
    if response == 0:
        pingstatus = "Network Active"
    else:
        pingstatus = "Network ErroR"

    return pingstatus


if __name__ == "__main__":
    print("Python version")
    print (sys.version)
    app.run(debug=True, host='0.0.0.0')
