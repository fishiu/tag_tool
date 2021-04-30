# -*- coding: utf-8 -*-

""" 
@author: Jin.Fish
@file: routes.py
@version: 1.0
@time: 2021/04/27 02:34:25
@contact: jinxy@pku.edu.cn

routes
"""

from tagtool import app, db
from flask import render_template, request
from sqlalchemy import TEXT


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True)
    xml = db.Column(TEXT)
    done = db.Column(db.BOOLEAN)

    def __repr__(self):
        return f'<Article {self.id}>'


@app.route('/')
@app.route('/index')
def index():
    article_id = request.args.get('page', 1, int)
    per_page = 1
    article_pagination = Article.query.paginate(page=article_id, per_page=per_page)
    article = article_pagination.items[0]
    return render_template("index.html", article=article, pagination=article_pagination)


@app.route('/save', methods=['POST'])
def save():
    content = request.form.get('content', type=str)
    article_id = request.form.get('id', type=int)
    # print(content)
    article = Article.query.get(article_id)
    article.xml = content
    article.done = True
    db.session.add(article)
    db.session.commit()
    return 'success', 204


if __name__ == '__main__':
    app.run()
    # db.drop_all()
    # db.create_all()
