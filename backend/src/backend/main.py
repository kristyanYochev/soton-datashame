from flask import Flask, request
from database import DatabaseConnection
from pypika import Query
import json

app = Flask(__name__)

@app.route("/buildings")
def list_buildings():
    with DatabaseConnection("test.db") as db:
        cur = db.cursor();

        result = cur.execute("SELECT DISTINCT building_code FROM samples")
        buildings = [bdg_code for bdg_code, in result]
        return json.dumps(buildings)


@app.route("/buildings/<bdg_code>")
def query_data(bdg_code: str):
    q = Query.from_("samples")
    match request.args["stat_type"]:
        case "min":
            q = q.select("min")
        case "max":
            q = q.select("max")
        case "average":
            q = q.select("average")
        case _:
            return "WTF?"
    ...

if __name__ == "__main__":
    app.run(port=8080)
