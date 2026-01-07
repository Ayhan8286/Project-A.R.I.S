import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient, models

# Configuration
QDRANT_URL = "http://localhost:6333"
COLLECTION_NAME = "gtm_brain"
DATA_PATH = "src/brain_data/knowledge.txt"

def ingest_data():
    print(f"🚀 Starting ingestion for {COLLECTION_NAME}...")

    # 1. Load Data
    if not os.path.exists(DATA_PATH):
        print(f"❌ Error: Data file not found at {DATA_PATH}")
        return

    loader = TextLoader(DATA_PATH)
    documents = loader.load()
    print(f"✅ Loaded {len(documents)} document(s).")

    # 2. Split Text
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)
    print(f"✅ Split into {len(docs)} chunk(s).")

    # 3. Initialize Embeddings
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    print("✅ Embeddings model loaded.")

    # 4. Initialize Qdrant Client & Recreate Collection
    client = QdrantClient(url=QDRANT_URL)

    # Check if collection exists and recreate it to ensure fresh start
    client.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=models.VectorParams(size=384, distance=models.Distance.COSINE),
    )
    print(f"✅ Collection '{COLLECTION_NAME}' (re)created.")

    # 5. Ingest into Qdrant using LangChain wrapper
    # Note: We use the client we just configured
    QdrantVectorStore.from_documents(
        docs,
        embeddings,
        url=QDRANT_URL,
        prefer_grpc=False,
        collection_name=COLLECTION_NAME,
        force_recreate=True
    )

    print("🎉 Ingestion Complete! The Brain has been fed.")

if __name__ == "__main__":
    ingest_data()
