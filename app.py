from flask import Flask, request, jsonify
import requests, uuid

app = Flask(__name__)
products = []  # temporary, use database later

# Mock product catalog for demo
DEMO_PRODUCTS = [
    {
        "brand": "alexandra wang",
        "desc": "black large calfskin geo bag",
        "name": "Black Large Calfskin Geo Bag",
        "image": "https://images.unsplash.com/photo-1512436991641-6745cdb1723f", # replace with real product image
        "official_price": 2200,
        "lowest_price": 2050,
    },
    {
        "brand": "sony",
        "desc": "headphones noise cancelling",
        "name": "Sony WH-1000XM5 Headphones",
        "image": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8",
        "official_price": 349,
        "lowest_price": 299,
    },
    {
        "brand": "nike",
        "desc": "running shoes vaporfly",
        "name": "Nike Vaporfly 3 Running Shoes",
        "image": "https://images.unsplash.com/photo-1519864600555-211c5e9c5dfb",
        "official_price": 250,
        "lowest_price": 180,
    }
]

def match_product(desc, brand):
    desc = desc.lower()
    brand = brand.lower()
    for p in DEMO_PRODUCTS:
        if brand in p["brand"] and any(word in p["desc"] for word in desc.split()):
            return p
    # fallback dummy product if not found
    return {
        "brand": brand.title(),
        "desc": desc.title(),
        "name": desc.title(),
        "image": "https://images.unsplash.com/photo-1512436991641-6745cdb1723f",
        "official_price": 99,
        "lowest_price": 75,
    }

@app.route("/products", methods=["GET"])
def list_products():
    for p in products:
        # prices already set during add
        p["is_discounted"] = p["target_price"] and float(p["lowest_price"]) < float(p["target_price"])
    return jsonify(products)

@app.route("/add", methods=["POST"])
def add_product():
    data = request.json
    prod = match_product(data["desc"], data["brand"])
    new_product = {
        "id": str(uuid.uuid4()),
        "name": prod["name"],
        "brand": prod["brand"].title(),
        "image": prod["image"],
        "official_price": prod["official_price"],
        "lowest_price": prod["lowest_price"],
        "target_price": data.get("target_price"),
        "is_discounted": False
    }
    products.append(new_product)
    return jsonify({"message": "Product added"}), 201

@app.route("/delete/<id>", methods=["DELETE"])
def delete_product(id):
    global products
    products = [p for p in products if p["id"] != id]
    return jsonify({"message": "Deleted"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
