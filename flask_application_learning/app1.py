from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/") #"/" refers to the starting page.

def hello_world():
    return "<h1> Hello World </h1>"  #h1 is the heading-1 tag in HTML coding.

@app.route("/home1")
def hello_world1():
    return "<h1> Hello World1 </h1>" 

@app.route("/about")
def hello_world2():
    return "<h1> Hello World2 </h1>" 

@app.route("/test")  #Routing and binding the function to the URL.Path
def input_req():
    name = request.args.get("name") # to take the data from the user using request.args while saving it at the server's end and then pass the data at the client end.
    return "<h1>Your name is {}</h1>".format(name)

if __name__ == "__main__":
    app.run(host = "0.0.0.0")