from flask import Flask, render_template,redirect,jsonify
from flask_pymongo import PyMongo
import scrape_mars

#flask_pymongo connection
app = (Flask__name__)
mongo= Pymongo(app, url="mongo://localhost:27017/Mars_db")

@app.route("/")
def index():
    mars=mongo.db.Mars.find_one()
    return render_template("index.html"),mars=mars)

@app route("/scrape")
def scrape():

    mars=mongo.db.mars
    mars_data = scrape_mars.scrape()
    mars.update({},mars_data,upsert=True)

    return redirect("http://localhost:5000/",code=302)
    
    if__name=="main":
    app.run(debug=True)

