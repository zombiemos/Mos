from flask import Flask, request, jsonify
from flask_cors import CORS
import csv
import random
import json

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/", methods=["POST"])
def home():
    if request.method == "POST":
        data = json.loads(request.json["data"])
        avg = json.loads(request.json["avg"])
        table = [
            [
                "ST_N",
                "C_1_N",
                "C_1_T",
                "C_2_N",
                "C_2_T",
                "C_3_N",
                "C_3_T",
                "C_4_N",
                "C_4_T",
            ],
            data,
            avg,
        ]
        print(table)
        with open(f"mos_{random.randint(0,100000000)}.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(table)

    return "success"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8765)
