from flask import Flask, render_template, request, redirect, session 

app = Flask(__name__)
app.secret_key = "Ser o no ser"

@app.route('/')
def vista():
    return render_template("index.html")

@app.route('/show', methods = ['POST'])
def vista2():
    print(request.form)
    session['count'] = request.form['count']
    return redirect('/')

#@app.route('/process')
#def vista3():
#   session['count'] = count
#   return render_template("index.html",  count = session['count'])

if __name__ == "__main__":
    app.run(debug=True)