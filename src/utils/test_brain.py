import requests
import json
from sentence_transformers import SentenceTransformer

# Configuration
QDRANT_URL = "http://localhost:6333"
COLLECTION_NAME = "gtm_brain"
QUERY_TEXT = "What components are in the GTM Engine?"

def test_brain():
    print(f"🧠 Testing Brain with query: '{QUERY_TEXT}'")

    # 1. Generate Embedding for the Query
    # We must use the SAME model as ingestion
    model = SentenceTransformer('all-MiniLM-L6-v2')
    vector = model.encode(QUERY_TEXT).tolist()
    print("✅ Query vector generated.")

    # 2. Construct Search Payload
    payload = {
        "vector": vector,
        "limit": 3,
        "with_payload": True
    }

    # 3. Hit Qdrant API
    api_endpoint = f"{QDRANT_URL}/collections/{COLLECTION_NAME}/points/search"

    try:
        response = requests.post(api_endpoint, json=payload)

        if response.status_code == 200:
            results = response.json().get('result', [])
            print(f"\n🔍 Found {len(results)} relevant results:\n")
            for i, res in enumerate(results):
                score = res.get('score')
                content = res.get('payload', {}).get('page_content', 'No content')
                print(f"Result {i+1} (Score: {score:.4f}):")
                print(f"  {content}\n")
        else:
            print(f"❌ Error: {response.status_code} - {response.text}")

    except Exception as e:
        print(f"❌ Connection Failed: {e}")

if __name__ == "__main__":
    test_brain()
