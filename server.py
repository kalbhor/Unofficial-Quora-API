from flask import Flask, jsonify, request
from Quora import ScrapeQuora

app = Flask(__name__)



### Routes ### 
@app.route('/')
def index():
	return '''<h1> Welcome to the unofficial Quora API </h1> 
	          <hr>
	          <h2><ul>Endpoints</ul></h2>
	          <ul>
	          <li>/<user></li>
	          <li>/<user>/followers</li>
	          <li>/<user>/following</li>
	          <li>/<user>/answers</li>
	          <li>/<user>/questions</li>
	          <li>/<user>/posts</li>
	          </ul>'''

@app.route('/<user>', methods=['GET'])
def user_info(user):
	response = {
	'followers': ScrapeQuora(user).followers(),
	'following': ScrapeQuora(user).following(),
	'questions': ScrapeQuora(user).questions(),
	'answers': ScrapeQuora(user).answers(),
	'posts': ScrapeQuora(user).posts(),
	}

	return jsonify(response)


@app.route('/<user>/followers', methods=['GET'])
def user_followers(user):
    return jsonify(ScrapeQuora(user).followers())

@app.route('/<user>/following', methods=['GET'])
def user_following(user):
    return jsonify(ScrapeQuora(user).following())

@app.route('/<user>/questions', methods=['GET'])
def user_questions(user):
    return jsonify(ScrapeQuora(user).questions())

@app.route('/<user>/answers', methods=['GET'])
def user_answers(user):
    return jsonify(ScrapeQuora(user).answers())

@app.route('/<user>/posts', methods=['GET'])
def user_posts(user):
    return jsonify(ScrapeQuora(user).posts())

if __name__ == '__main__':
    app.run(debug=True)

