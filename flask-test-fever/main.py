import os
from flask import Flask
from dotenv import load_dotenv
from utils.response import Response
from utils.database import db
from api.model import Model_b

load_dotenv()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.environ.get(
    "DB_URL", "db.sqlite"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#initialize db
db.init_app(app)

#register API 
app.register_blueprint(Model_b)

@app.errorhandler(404)
def basic_pages(wargs=None):
    #whatever custom things come here
    return Response.error("That page is not found", 404)


