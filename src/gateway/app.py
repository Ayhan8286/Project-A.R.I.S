from flask import Flask, request, jsonify
import requests
import os
from sentence_transformers import SentenceTransformer

app = Flask(__name__)

# Configuration
# Use 'qdrant' as hostname when running inside Docker, 'localhost' otherwise
QDRANT_HOST = os.environ.get('QDRANT_HOST', 'qdrant')
QDRANT_PORT = os.environ.get('QDRANT_PORT', '6333')
QDRANT_URL = f"http://{QDRANT_HOST}:{QDRANT_PORT}"
COLLECTION_NAME = "gtm_brain"

print(f"🚀 Gateway starting. Connecting to Qdrant at {QDRANT_URL}...")

# Load Model (This happens once on startup)
try:
    model = SentenceTransformer('all-MiniLM-L6-v2')
    print("✅ Embedding model loaded.")
except Exception as e:
    print(f"❌ Failed to load model: {e}")
    model = None

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "online", "service": "gateway"}), 200

@app.route('/search', methods=['POST'])
def search():
    if not model:
        return jsonify({"error": "Model not loaded"}), 500

    data = request.json
    query_text = data.get('query')
    limit = data.get('limit', 3)

    if not query_text:
        return jsonify({"error": "No query provided"}), 400

    print(f"🧠 Processing query: '{query_text}'")

    try:
        # 1. Vectorize
        vector = model.encode(query_text).tolist()

        # 2. Search Qdrant via API
        payload = {
            "vector": vector,
            "limit": limit,
            "with_payload": True
        }

        api_endpoint = f"{QDRANT_URL}/collections/{COLLECTION_NAME}/points/search"
        response = requests.post(api_endpoint, json=payload)

        if response.status_code == 200:
            results = response.json().get('result', [])
            return jsonify({"results": results}), 200
        else:
            return jsonify({"error": f"Qdrant Error: {response.text}"}), response.status_code

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
