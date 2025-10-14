import os
from flask import Flask, request, jsonify
import requests, uuid

app = Flask(__name__)
products = []

RAPIDAPI_KEY = "8421664c92mshaca660cd7641d02p146ed7jsn03245cadb9c2"

def match_product(desc, brand):
    # Use the Real-Time Product Search API
    # Documentation: https://rapidapi.com/letscrape-6bRBa3QguO5/api/real-time-product-search
    url = "https://real-time-product-search.p.rapidapi.com/search"
    query = f"{brand} {desc}"
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": "real-time-product-search.p.rapidapi.com"
    }
    params = {"q": query, "country": "us", "language": "en"}
    
    resp = requests.get(url, headers=headers, params=params)
    data = resp.json()
    # Get the first result with a price and image
    items = data.get("data", [])
    if items:
        best = None
        for item in items:
            if item.get("product_photo", "") and item.get("product_price", ""):
                best = item
                break
        if not best:
            best = items[0]
        name = best.get("product_title", query.title())
        image = best.get("product_photo", "https://via.placeholder.com/75")
        official_price = best.get("product_price", "N/A")
        lowest_price = official_price  # Simplification: best = official and lowest
        link = best.get("product_url", "#")
        return {
            "brand": brand.title(),
            "desc": desc.title(),
            "name": name,
            "image": image,
            "official_price": float(str(official_price).replace("$", "").split()[0]) if official_price and "$" in str(official_price) else official_price,
            "lowest_price": float(str(lowest_price).replace("$", "").split()[0]) if lowest_price and "$" in str(lowest_price) else lowest_price,
            "url": link
        }
    # fallback
    return {
        "brand": brand.title(),
        "desc": desc.title(),
        "name": query.title(),
        "image": "https://via.placeholder.com/75",
        "official_price": "N/A",
        "lowest_price": "N/A",
        "url": "#"
    }
