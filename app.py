from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_craigslist


app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/_____________" #need db name 
mongo = PyMongo(app)


@app.route("/markers")
def markers():
    markers = mongo.db.moms_market
    return jsonify(markers)


@app.route("/income")
def incomeView():
    # incomeView = mongo.db. #insert collection name here 
    return jsonify(incomeView)


@app.route("/Age")
def ageView():
    # ageView = mongo.db. #insert collection name here 


@app.route("/education")
def edView():
    # edView = mongo.db. #insert collection name here 



if __name__ == "__main__":
    app.run(debug=True)