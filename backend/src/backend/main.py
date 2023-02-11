from flask import Flask
from flask_cors import CORS
from database import DatabaseConnection
from pypika import Query
import json

app = Flask(__name__)
CORS(app)

@app.route("/buildings")
def list_buildings():
    with DatabaseConnection("test.db") as db:
        cur = db.cursor();

        result = cur.execute("SELECT DISTINCT building_code FROM samples")
        buildings = [bdg_code for bdg_code, in result]
        return json.dumps(buildings)


if __name__ == "__main__":
    app.run(port=8080)
