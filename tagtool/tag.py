# -*- coding: utf-8 -*-

""" 
@author: Jin.Fish
@file: tag.py
@version: 1.0
@time: 2021/04/27 09:40:42
@contact: jinxy@pku.edu.cn

tag convertor
"""

import re
import json
from tagtool import db
from routes import Article


def find_key(abstract, keylist):
    tokens = re.sub(r"([(),.;?!'])", r" \1 ", abstract).lower().split()
    max_length = 6
    i = 0
    j = i + max_length
    keywords = []
    while True:
        if i >= j:
            i += 1
            j = i + max_length
            continue
        if j > len(tokens):
            j = len(tokens)
        if i >= len(tokens):
            break
        phrase = " ".join(tokens[i:j])
        if phrase in keylist or phrase[:-1] in keylist:
            keywords.append([i, j])
            i = j
            j = i + max_length
            continue
        else:
            j -= 1
            continue
    tokens = re.sub(r"([(),.;?!'])", r" \1 ", abstract).split()
    new_abstract = list(range(len(tokens)))
    for key in keywords:
        new_abstract.insert(new_abstract.index(key[0]),
                            "<span class='keyphrase'>")
        if key[1] < len(tokens):
            new_abstract.insert(new_abstract.index(key[1]), "</span>")
        if key[1] == len(tokens):
            new_abstract.append("</span>")
    new_abstract = [tokens[index] if isinstance(index, int) else index for index
                    in new_abstract]
    new_abstract = " ".join(new_abstract)
    new_abstract = re.sub(r"([(),.;?!'])", r"\1", new_abstract)
    new_abstract = re.sub("<span class='keyphrase'> ",
                          "<span class='keyphrase'>", new_abstract)
    new_abstract = re.sub(" </span>", "</span>", new_abstract)
    return new_abstract


if __name__ == '__main__':
    keys = json.loads(open("./statics/new_keys.json", "r").read())
    articles = json.loads(open("./statics/articleInfo.json", "r").read())
    xml_abstracts = []
    for idx, article in enumerate(articles[0:50]):
        print(articles.index(article))
        key_dict = keys + [key.lower() for key in article.get("keys", []) if key]
        d = {i: 1 for i in key_dict}
        # db_article = Article()
        db_article = Article.query.get(idx)
        db_article.id = idx
        db_article.xml = find_key(article["abstract"], d)
        db.session.add(db_article)
        db.session.commit()
