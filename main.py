from flask import Flask,redirect,render_template,url_for
app = Flask(__name__)

posts = [
    {
        'author': 'James Hawkins',
        'date_posted':'June'
    }
]
@app.route('/<human>')
def index(human):
    return render_template('index.html', content = human)

@app.route('/<groot>') # if you use an angle bracket you can have the chance to type a custom word to the url and place it in your function
def about(groot):
    return f'you did it now 2{groot}'

@app.route('/admin')
def admin():
    return redirect(url_for('about'))

if __name__ =='__main__':
    app.run(debug=True)

