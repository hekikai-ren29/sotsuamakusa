from flask import Flask,render_template




@app.route("/add")
def add_get():
    return render_template("base.html")




if __name__=="__main__":
    app.run(debug=True)
