#!/usr/bin/env python3
"""_summary_
"""


from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index() -> str:
    """_summary_
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
