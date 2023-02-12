from flask import Flask, request
from flask_cors import CORS
from database import DatabaseConnection
from pypika import Query, Table, CustomFunction
import json
import datetime

app = Flask(__name__)
CORS(app)


@app.route("/buildings")
def list_buildings():
    with DatabaseConnection("test.db") as db:
        cur = db.cursor()

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
        q = q.where(strftime("%Y", sql_datetime(
            samples.timestamp, "unixepoch")) == request.args["year"])

    if "month" in request.args:
        q = q.where(strftime("%m", sql_datetime(samples.timestamp,
                    "unixepoch")) == request.args["month"].zfill(2))

    if "day" in request.args:
        q = q.where(strftime("%d", sql_datetime(samples.timestamp,
                    "unixepoch")) == request.args["day"].zfill(2))

    q = q.select("timestamp")

    with DatabaseConnection("test.db") as db:
        db.row_factory = lambda _, row: {"value": row[0], "timestamp": datetime.datetime.fromtimestamp(
            row[1]).strftime("%Y-%m-%d %H-%M-%S")}
        cur = db.cursor()

        print(str(q))

        cur.execute(str(q))

        data = list(cur)
        return json.dumps(data[::24])


@app.route("/headline-stats")
def headline_stats():
    with DatabaseConnection("test.db") as db_conn:
        cur = db_conn.cursor()

        cur.execute(
            "SELECT SUM(average) FROM samples WHERE strftime('%Y', datetime(timestamp, 'unixepoch')) = '2020'")
        power_consumption_2020, = next(cur)

        cur.execute(
            "SELECT SUM(average) FROM samples WHERE strftime('%Y', datetime(timestamp, 'unixepoch')) = '2019'")
        power_consumption_2019, = next(cur)

        cur.execute("SELECT building_code, SUM(average) FROM samples WHERE strftime('%Y', datetime(timestamp, 'unixepoch')) = '2020' GROUP BY 1 ORDER BY 2 DESC LIMIT 1")
        most_consuming_building, building_consumption = next(cur)

        return json.dumps({
            "power_consumption_2019": power_consumption_2019,
            "power_consumption_2020": power_consumption_2020,
            "most_consuming_building": {
                "building_code": most_consuming_building,
                "consumption": building_consumption
            }
        })


if __name__ == "__main__":
    app.run(port=8080)
