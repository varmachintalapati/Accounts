import requests
import json

# Test the API endpoints
BASE_URL = "http://localhost:5000"

def test_api():
    """Test the users API endpoints"""
    
    print("Testing Users API")
    print("=" * 50)
    
    # Test 1: Health check
    print("\n1. Testing health check endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/api/health")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    
    # Test 2: Get all users (3 users)
    print("\n2. Testing get all users (should return 3 users)...")
    try:
        response = requests.get(f"{BASE_URL}/api/users")
        print(f"Status Code: {response.status_code}")
        users = response.json()
        print(f"Total users: {len(users)}")
        print(f"User IDs: {[user['id'] for user in users]}")
        print(f"First user: {json.dumps(users[0], indent=2)}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    
    # Test 3: Get active users only
    print("\n3. Testing get active users...")
    try:
        response = requests.get(f"{BASE_URL}/api/users?userType=ACTIVE")
        print(f"Status Code: {response.status_code}")
        users = response.json()
        print(f"Active users: {len(users)}")
        for user in users:
            print(f"  - {user['name']} ({user['username']})")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    
    # Test 4: Get inactive users only
    print("\n4. Testing get inactive users...")
    try:
        response = requests.get(f"{BASE_URL}/api/users?userType=INACTIVE")
        print(f"Status Code: {response.status_code}")
        users = response.json()
        print(f"Inactive users: {len(users)}")
        for user in users:
            print(f"  - {user['name']} ({user['username']})")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    
    # Test 5: Test invalid user type
    print("\n5. Testing invalid user type...")
    try:
        response = requests.get(f"{BASE_URL}/api/users?userType=INVALID")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    
    # Test 6: Test API documentation endpoint
    print("\n6. Testing API documentation endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("Make sure the API server is running (python app.py) before running this test.")
    input("Press Enter to continue...")
    test_api()
