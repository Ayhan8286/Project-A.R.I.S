#!/bin/bash
echo "🛑 Stopping GTM Engine..."
cd deploy
docker compose down
echo "✅ Stack stopped."
