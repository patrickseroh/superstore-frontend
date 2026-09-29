import os
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

BACKEND_URL = os.environ.get("BACKEND_URL", "http://127.0.0.1:8000")

@app.route("/")
def home():
    return render_template("index.html", prediction=None, clf_result=None, clf_probability=None, active_tab="sales-section")

@app.route("/predict-sales", methods=["POST"])
def predict_sales():
    form = request.form
    features = {
        "discount": float(form["discount"]),
        "quantity": int(form["quantity"]),
        "shipping_cost": float(form["shipping_cost"]),
        "delivery_duration": int(form["delivery_duration"]),
        "year": int(form["year"]),
        "week_num": int(form["week_num"]),
        f"category_{form['category']}": 1,
        f"sub_category_{form['sub_category']}": 1,
        f"region_{form['region']}": 1,
        f"market_{form['market']}": 1,
        f"segment_{form['segment']}": 1,
        f"ship_mode_{form['ship_mode']}": 1,
        f"order_priority_{form['order_priority']}": 1,
    }
    response = requests.post(f"{BACKEND_URL}/predict/regression", json={"features": features})
    result = response.json()
    return render_template(
        "index.html",
        prediction=result.get("predicted_sales"),
        clf_result=None,
        clf_probability=None,
        active_tab="sales-section"
    )

@app.route("/predict-profitability", methods=["POST"])
def predict_profitability():
    form = request.form
    features = {
        "discount": float(form["discount"]),
        "quantity": int(form["quantity"]),
        "sales": float(form["sales"]),
        "shipping_cost": float(form["shipping_cost"]),
        "delivery_duration": int(form["delivery_duration"]),
        "year": int(form["year"]),
        "week_num": int(form["week_num"]),
        f"category_{form['category']}": 1,
        f"sub_category_{form['sub_category']}": 1,
        f"region_{form['region']}": 1,
        f"market_{form['market']}": 1,
        f"segment_{form['segment']}": 1,
        f"ship_mode_{form['ship_mode']}": 1,
        f"order_priority_{form['order_priority']}": 1,
    }
    response = requests.post(f"{BACKEND_URL}/predict/classification", json={"features": features})
    result = response.json()
    return render_template(
        "index.html",
        prediction=None,
        clf_result=result.get("is_profitable"),
        clf_probability=result.get("probability_profitable"),
        active_tab="profit-section"
    )

if __name__ == "__main__": 
    app.run(debug=True)