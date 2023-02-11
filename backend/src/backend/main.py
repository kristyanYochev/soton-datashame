from flask import Flask, request
from database import DatabaseConnection
from pypika import Query, Table, CustomFunction
import json

app = Flask(__name__)

@app.route("/buildings")
def list_buildings():
    with DatabaseConnection("test.db") as db:
        cur = db.cursor();

        result = cur.execute("SELECT DISTINCT building_code FROM samples")
        buildings = [bdg_code for bdg_code, in result]
        return json.dumps(buildings)


@app.route("/buildings/<path:bdg_code>")
def query_data(bdg_code: str):
    strftime = CustomFunction("strftime", ["format", "timestamp"])
    sql_datetime = CustomFunction("datetime", ["value", "format"])
    samples = Table("samples")
    q: Query = Query.from_(samples).where(samples.building_code == bdg_code)
    match request.args["stat_type"]:
        case "min":
            q = q.select("min")
        case "max":
            q = q.select("max")
        case "average":
            q = q.select("average")
        case _:
            return "Invalid stat_type", 400

    if "year" in request.args:
        q = q.where(strftime("%Y", sql_datetime(samples.timestamp, "unixepoch")) == request.args["year"])

    if "month" in request.args:
        q = q.where(strftime("%m", sql_datetime(samples.timestamp, "unixepoch")) == request.args["month"].zfill(2))

    if "day" in request.args:
        q = q.where(strftime("%d", sql_datetime(samples.timestamp, "unixepoch")) == request.args["day"].zfill(2))
    
    q = q.select("timestamp")

    with DatabaseConnection("test.db") as db:
        db.row_factory = lambda _, row: {"value": row[0], "timestamp": row[1]}
        cur = db.cursor()

        print(str(q))

        cur.execute(str(q))

        data = list(cur)
        return json.dumps(data)


if __name__ == "__main__":
    app.run(port=8080)
