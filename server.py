from flask import Flask, jsonify
from flask.ext.cache import Cache

from Quora import ScrapeQuora

app = Flask(__name__)
app.config['CACHE_TYPE'] = 'simple'
app.cache = Cache(app)


### Index viz: help menu ###
@app.route('/')
@app.cache.cached(timeout=300)
def index():
    return jsonify({
        'author': 'Lakshay Kalbhor',
        'author_url': 'https://lakshaykalbhor.github.io',
        'base_url': '',
        'project_url': 'https://github.com/lakshaykalbhor/Unofficial-Quora-API',
        'endpoints': {
            'user_profile': '/{user}',
            'user_followers': '/{user}/followers',
            'user_following': '/{user}/following',
            'user_questions': '/{user}/questions',
            'user_answers': '/{user}/answers',
            'user_posts': '/{user}/posts',
            #TODO: 'question': '/questions/{question}', (Add these option later)
            #TODO: 'answer': '/answers/{answer}', (Add this option later)
        }
    })


### User profile info ###
@app.route('/<user>', methods=['GET'])
@app.cache.cached(timeout=300)
def user_info(user):
    count = ScrapeQuora.count(user)
    links = ScrapeQuora.links(user)

    response = {
        'count': count,
        'url': links,
    }

    return jsonify(response)


### User followers info ###
@app.route('/<user>/followers', methods=['GET'])
@app.cache.cached(timeout=240)
def user_followers(user):
    return jsonify(ScrapeQuora(user).followers())


### User following info ###
@app.route('/<user>/following', methods=['GET'])
@app.cache.cached(timeout=240)
def user_following(user):
    return jsonify(ScrapeQuora(user).following())


### Recent questions asked by user ###
@app.route('/<user>/questions', methods=['GET'])
@app.cache.cached(timeout=300)
def user_questions(user):
    return jsonify(ScrapeQuora(user).questions())


### Recent answers by user ###
@app.route('/<user>/answers', methods=['GET'])
@app.cache.cached(timeout=300)
def user_answers(user):
    return jsonify(ScrapeQuora(user).answers())


### Recent blog posts by user ###
@app.route('/<user>/posts', methods=['GET'])
@app.cache.cached(timeout=300)
def user_posts(user):
    return jsonify(ScrapeQuora(user).posts())


if __name__ == '__main__':
    app.run(debug=True)
