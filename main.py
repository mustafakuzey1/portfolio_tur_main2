# Import
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

# İçerik sayfasını çalıştırma
@app.route('/')
def index():
    return render_template('index.html')


# Dinamik beceriler
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    return render_template('index.html', button_python=button_python)

@app.route('/submit', methods=['POST'])
def feedback_form():
    email = request.form['email']
    text = request.form['text']
    with open("form.txt" , "a") as f:
        f.write("Emai : " + email  + "\n")
        f.write("Text : " + text + "\n")
        f.write("-------------------------------\n")
    f.close()
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
