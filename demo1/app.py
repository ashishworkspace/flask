from flask import Flask, render_template
import subprocess

app = Flask("demo1")

@app.route("/printCal")
def printCal():
   data = subprocess.getoutput("cal")
   return f"<pre>{data}</pre>"
@app.route("/readHtml")
def readHtml():
   return render_template("index.html")
