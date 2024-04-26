from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")


@app.route("/math", methods= ["POST"])
def math_ops():
    if(request.method == "POST"):
        ops = request.form["operation"] #select id in index.html is operation so we have to pass the "id" name that we had taken while creating the form template.
        n1 = int(request.form["n1"]) #GET is public (equivalent to Google search operation), it is not secured whereas POST method is secured.
        n2 = int(request.form["n2"]) #We have to write name of the field that is written inside the form template and not id.
        
        if ops == "add":
            r = n1 + n2
            res = "The sum of " + str(n1) + " and " + str(n2) + " is equals to " + str(r)
        # return render_template("results.html", result = res)

        elif ops == "subtract":
            if n1 > n2:
                r = n1 - n2
                res = "The difference of " + str(n1) + " and " + str(n2) + " is equals to " + str(r)
            # return render_template("results.html", result = res)
            
            else:
                r = n2- n1
                res = "The difference of " + str(n1) + " and " + str(n2) + " is equals to " + str(r) + " while considering the difference from the larger number"
        
        elif ops == "multiply":
            r = n1 * n2
            res = "The multiplication of " + str(n1) + " and " + str(n2) + " is equals to " + str(r)
        
        elif ops == "divide":
            r = n1 /n2
            res = "The division of " + str(n1) + " and " + str(n2) + " is equals to " + str(r)

        
        return render_template("results.html", result = res)
        


if __name__ == "__main__":
    app.run(host="0.0.0.0")