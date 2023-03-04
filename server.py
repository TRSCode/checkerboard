from flask import Flask, render_template
app = Flask (__name__)

@app.route('/')
def index():
    return render_template('index.html', num1=8, num2=8, color1='black', color2='red')

@app.route('/<int:num2>')
def row(num2):
    return render_template('index.html', num1=8, num2=num2, color1='black', color2='hotpink')

@app.route('/<int:num2>/<int:num1>')
def column(num2,num1):
    return render_template('index.html', num1=num1, num2=num2, color1='pink', color2='hotpink')

@app.route('/<int:num2>/<int:num1>/<string:color1>')
def color_first(num2,num1,color1):
    return render_template('index.html', num1=num1, num2=num2, color1=color1, color2='rebeccapurple')

@app.route('/<int:num2>/<int:num1>/<string:color1>/<string:color2>')
def color_second(num2,num1,color1, color2):
    return render_template('index.html', num1=num1, num2=num2, color1=color1, color2=color2)

@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response. Try again, Now!"

if __name__=="__main__":
    app.run(debug=True) 