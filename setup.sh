#!/bin/bash
echo "🛠️  Setting up GTM Engine Environment..."

# 1. Check for .env
if [ ! -f .env ]; then
    echo "📄 Creating .env file from template..."
    cp .env.example .env
    echo "⚠️  Please edit .env and add your API keys!"
else
    echo "✅ .env file found."
fi

# 2. Install Python Dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

# 3. Docker Setup
if ! command -v docker &> /dev/null; then
    echo "❌ Docker not found! Please install Docker Desktop."
    exit 1
fi

echo "✅ Setup Complete. Run ./start.sh to launch."
