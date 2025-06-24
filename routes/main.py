from flask import Blueprint, render_template, request, jsonify
import json
import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

main = Blueprint("main", __name__)

API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
API_TOKEN = os.getenv("HUGGING_FACE_API_TOKEN")  # Load Hugging Face API token from .env
headers = {"Authorization": f"Bearer {API_TOKEN}"}

@main.route("/")
def index():
    # Load all products from the JSON file
    with open("static/products.json", "r") as f:
        products = json.load(f)

    # Get the newest six items (assuming the newest are at the end of the list)
    newest_products = products[-6:]  # Slice the last six items

    return render_template("index.html", products=newest_products)

@main.route("/chat", methods=["POST"])
def chat():
    print("Chat route called")
    user_message = request.json.get("message", "")

    if not user_message.strip():
        print("Empty message received")
        return jsonify({"error": "質問が空です。"}), 400

    try:
        # Format Zephyr-compatible prompt
        prompt = f"{user_message}"

        response = requests.post(
            API_URL,
            headers={
                "Authorization": f"Bearer {API_TOKEN}",
                "Content-Type": "application/json"
            },
            json={
                "inputs": prompt,
                "parameters": {
                    "max_new_tokens": 512,
                    "temperature": 0.7,
                    "do_sample": True
                }
            }
        )
        response.raise_for_status()
        result = response.json()
        print("Raw API response:", result)

        # Zephyr's response is usually a list of dicts with "generated_text"
        if isinstance(result, list) and "generated_text" in result[0]:
            ai_response = result[0]["generated_text"]
        else:
            print("Unexpected API response format")
            return jsonify({"error": "APIレスポンスの形式が不正です。"}), 500

        print("AI response:", ai_response)
        return jsonify({"response": ai_response})

    except requests.exceptions.RequestException as e:
        print(f"Error calling Hugging Face API: {e}")
        return jsonify({"error": "AIの回答を生成できませんでした。"}), 500

 
