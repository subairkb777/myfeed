from flask import Flask, render_template, url_for
app = Flask(__name__)
posts = [
    {
        "author": "Jessi",
        "title": "Case Work",
        "content": 'MSW',
        "date_posted": "JAN 1 2020"
    },
    {
        "author": "Subair",
        "title": "Bug",
        "content": 'CS',
        "date_posted": "JAN 2 2020"
    }
]
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

if __name__ == "__main__":
    app.run(debug=True)
