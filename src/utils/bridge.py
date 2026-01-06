import redis

def test_redis_connection():
    try:
        # Connect to Redis (assuming localhost for local testing, or service name 'redis' in docker)
        r = redis.Redis(host='localhost', port=6379, db=0)
        # Set a key
        r.set('test_key', 'Hello from Python Bridge')
        # Get the key
        value = r.get('test_key')
        print(f"Redis Test: Retrieved value: {value.decode('utf-8')}")
    except Exception as e:
        print(f"Redis Connection Failed: {e}")

if __name__ == "__main__":
    test_redis_connection()
