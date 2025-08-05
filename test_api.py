import requests
import json

# Test the API endpoints
BASE_URL = "http://localhost:5000"

def test_api():
    """Test the transactions API endpoints"""
    
    print("Testing Transactions API")
    print("=" * 50)
    
    # Test 1: Health check
    print("\n1. Testing health check endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/api/health")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    
    # Test 2: Get all transactions
    print("\n2. Testing get all transactions...")
    try:
        response = requests.get(f"{BASE_URL}/api/transactions")
        print(f"Status Code: {response.status_code}")
        transactions = response.json()
        print(f"Total transactions: {len(transactions)}")
        print(f"First transaction: {json.dumps(transactions[0], indent=2)}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    
    # Test 3: Get credit transactions only
    print("\n3. Testing get credit transactions...")
    try:
        response = requests.get(f"{BASE_URL}/api/transactions?transactionType=CREDIT")
        print(f"Status Code: {response.status_code}")
        transactions = response.json()
        print(f"Credit transactions: {len(transactions)}")
        for tx in transactions:
            print(f"  - {tx['type']}: ${tx['amount']} ({tx['debitCredit']})")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    
    # Test 4: Get debit transactions only
    print("\n4. Testing get debit transactions...")
    try:
        response = requests.get(f"{BASE_URL}/api/transactions?transactionType=DEBIT")
        print(f"Status Code: {response.status_code}")
        transactions = response.json()
        print(f"Debit transactions: {len(transactions)}")
        for tx in transactions:
            print(f"  - {tx['type']}: ${tx['amount']} ({tx['debitCredit']})")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    
    # Test 5: Test invalid transaction type
    print("\n5. Testing invalid transaction type...")
    try:
        response = requests.get(f"{BASE_URL}/api/transactions?transactionType=INVALID")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("Make sure the API server is running (python app.py) before running this test.")
    input("Press Enter to continue...")
    test_api()
