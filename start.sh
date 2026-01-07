#!/bin/bash
echo "🚀 Starting GTM Engine..."
cd deploy
docker compose up -d
echo "✅ Stack is running!"
echo "   - Mission Control: http://localhost:8501"
echo "   - n8n: http://localhost:5678"
echo "   - Portainer: http://localhost:9000"
