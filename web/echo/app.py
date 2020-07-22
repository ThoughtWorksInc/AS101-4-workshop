from flask import Flask, render_template, request

from .db import db
from .models import Post

app = Flask(__name__)
app.config.from_pyfile('config.py')
db.init_app(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        post = Post(text)
        db.session.add(post)
        db.session.commit()
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    return render_template('index.html', posts=posts)


if __name__ == '__main__':
    app.run()
