from flask import Flask, request, make_response
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

from models.recent import *
from repository.recents import *

app = Flask(__name__)
engine = create_engine("sqlite:///data.db", echo=True)

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

posts = session.execute(select(Recents)).all()
print(posts)

def CORS(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    return response

@app.route("/test")
def test():
    return "PASSED"

@app.route("/api/recentposts")
def recent_posts():
    posts = get_recentblogs(session)
    '''
    posts = {
        "title": [
            "Why plane waves cannot represent free particles?",
            "Significance of inner and outer products",
            "Continuous vector spaces"
        ]
    }
    '''
    response = make_response(posts)
    return CORS(response)

@app.route("/api/bloglists")
def blog_lists():
    posts = {
        0: [
            "Why plane waves cannot represent free particles?",
            "Significance of inner and outer products",
            "Continuous vector spaces"
        ],
        1: [
            "Writting hello world in C",
            "making convolutional Neural Net from scratch",
        ],
        2: []
    }
    response = make_response(posts)
    return CORS(response)

@app.route("/api/register", methods=["OPTIONS","POST"])
def register():

    if request.method == "OPTIONS":
        return CORS(make_response())

    elif request.method == "POST":
        user_data = dict(request.form)

        if user_data["type"] == "login":
            return CORS(make_response("LOGGEDIN"))

        elif user_data["type"] == "signup":
            pwd = user_data["password"].encode("utf-8")
            user_data["password"] = bcrypt.hashpw(pwd ,bcrypt.gensalt(rounds=16))
            return CORS(make_response("SIGNEDUP"))

        return CORS(make_response("INVALID"))

if __name__ == "__main__":
    app.run(debug=False)
