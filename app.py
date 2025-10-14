{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from flask import Flask, request, jsonify\
import requests, uuid\
\
app = Flask(__name__)\
products = []  # temporary, use MongoDB or SQLite later\
\
def fake_price_check(url):\
    import random\
    return \{\
        "official": round(random.uniform(10, 100), 2),\
        "lowest": round(random.uniform(5, 95), 2)\
    \}\
\
@app.route("/products", methods=["GET"])\
def list_products():\
    for p in products:\
        prices = fake_price_check(p["url"])\
        p["official_price"] = prices["official"]\
        p["lowest_price"] = prices["lowest"]\
        p["is_discounted"] = p["target_price"] and prices["lowest"] < float(p["target_price"])\
    return jsonify(products)\
\
@app.route("/add", methods=["POST"])\
def add_product():\
    data = request.json\
    new_product = \{\
        "id": str(uuid.uuid4()),\
        "name": data["name"],\
        "url": data["url"],\
        "target_price": data.get("target_price"),\
        "official_price": 0,\
        "lowest_price": 0,\
        "is_discounted": False\
    \}\
    products.append(new_product)\
    return jsonify(\{"message": "Product added"\}), 201\
\
@app.route("/delete/<id>", methods=["DELETE"])\
def delete_product(id):\
    global products\
    products = [p for p in products if p["id"] != id]\
    return jsonify(\{"message": "Deleted"\}), 200\
\
if __name__ == "__main__":\
    app.run(host="0.0.0.0", port=5000)\
}