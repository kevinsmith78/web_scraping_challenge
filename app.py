from flask import Flask, render_template,redirect,jsonify
from flask_pymongo import PyMongo
import scrape_mars

#flask_pymongo connection
app = (Flask__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/Mars"
mongo= PyMongo

@app.route("/")
def index():
    mars=mongo.db.Mars.find_one()
    return render_template("index.html"),mars=mars)

@app route("/scrape")
def scrape():

    mars=mongo.db.Mars
    mars_data = scrape_mars.scrape()
    mars.update({},mars_data,upsert=True)
    return redirect("/")

    
if__name__=="__main__":
    app.run(debug=True)

