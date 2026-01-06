import redis
import json

client = redis.Redis(host='localhost', port=6379, db=0)
event = { "user_id": "visitor_99", "action": "view_pricing", "url": "https://v-list.ai/pricing" }
client.publish('website_events', json.dumps(event))
print("🚀 Signal Sent to Nervous System")
