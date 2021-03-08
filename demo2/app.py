from flask import Flask
from flask import render_template
from flask import request
import subprocess

## OVERALL SUMMARY cmdInput is route  which will retrive Data using GET method and cmdOutput will process the data(cmd)  using subprocess module
## and return the output using /cmdOutput route

app = Flask("demo2")                                 # creating instance of Flask class 

@app.route("/cmdInput")                              # this route will get the request from page/view
def inputPage():
   return render_template("input.html")              # render_template read the file inside template folder

@app.route("/cmdOutput", methods=['GET'])            # this  route will route to  cmdOutput and will retrive all data send by cmdInput by method=['GET']
def outputPage():
   cmd  = request.args.get("var")		     # request module provide args that has method called get which is used to get the data which page want to send to the route /cmdOutput
   return f"<pre>{subprocess.getoutput(cmd)}</pre>"  # <pre> tag  is used to format the html code
                                                     # subprocess has method called getoutput that will process command output
							
   
