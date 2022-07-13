from flask import (Flask, request, jsonify)

app = Flask(__name__)


@app.route("/add_slides",  methods=['POST'])
def add_values():
    value = request.get_json()
    slider_x_value = value['x']
    slider_y_value = value['y']

    added_value = slider_x_value + slider_y_value

    return jsonify({"sum": added_value})
