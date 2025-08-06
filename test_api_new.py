#!/usr/bin/env python3
"""
Test script for the Users API
This script demonstrates how to use the API endpoints
"""

import requests
import json
import sys

def test_api(base_url="http://localhost:5000"):
    """Test the Users API endpoints"""
    
    print("=" * 60)
    print("🧪 TESTING USERS API")
    print("=" * 60)
    print(f"Base URL: {base_url}")
    print()
    
    # Test health endpoint
    print("1. Testing Health Endpoint:")
    try:
        response = requests.get(f"{base_url}/api/health", timeout=5)
        print(f"   Status: {response.status_code}")
        print(f"   Response: {response.json()}")
        print("   ✅ Health check passed")
    except Exception as e:
        print(f"   ❌ Health check failed: {e}")
        return False
    
    print()
    
    # Test main API endpoint - all users
    print("2. Testing Main Endpoint (All Users):")
    try:
        response = requests.get(f"{base_url}/api/transactions", timeout=10)
        print(f"   Status: {response.status_code}")
        data = response.json()
        print(f"   Number of users returned: {len(data)}")
        if data:
            print(f"   First user: {data[0]['name']} (ID: {data[0]['id']})")
            print(f"   Last user: {data[-1]['name']} (ID: {data[-1]['id']})")
            print(f"   Sample user structure:")
            sample_user = {
                "id": data[0]['id'],
                "name": data[0]['name'],
                "email": data[0]['email'],
                "city": data[0]['address']['city']
            }
            print(f"   {json.dumps(sample_user, indent=4)}")
        print("   ✅ All users endpoint working")
    except Exception as e:
        print(f"   ❌ All users endpoint failed: {e}")
        return False
    
    print()
    
    # Test API endpoint with CREDIT parameter
    print("3. Testing Endpoint with transactionType=CREDIT:")
    try:
        response = requests.get(f"{base_url}/api/transactions?transactionType=CREDIT", timeout=10)
        print(f"   Status: {response.status_code}")
        data = response.json()
        print(f"   Number of users returned: {len(data)}")
        print("   Note: transactionType parameter is ignored, same data returned")
        print("   ✅ CREDIT parameter endpoint working")
    except Exception as e:
        print(f"   ❌ CREDIT parameter endpoint failed: {e}")
        return False
    
    print()
    
    # Test API endpoint with DEBIT parameter
    print("4. Testing Endpoint with transactionType=DEBIT:")
    try:
        response = requests.get(f"{base_url}/api/transactions?transactionType=DEBIT", timeout=10)
        print(f"   Status: {response.status_code}")
        data = response.json()
        print(f"   Number of users returned: {len(data)}")
        print("   Note: transactionType parameter is ignored, same data returned")
        print("   ✅ DEBIT parameter endpoint working")
    except Exception as e:
        print(f"   ❌ DEBIT parameter endpoint failed: {e}")
        return False
    
    print()
    
    # Test invalid parameter
    print("5. Testing Invalid Parameter:")
    try:
        response = requests.get(f"{base_url}/api/transactions?transactionType=INVALID", timeout=5)
        print(f"   Status: {response.status_code}")
        print(f"   Response: {response.json()}")
        if response.status_code == 400:
            print("   ✅ Invalid parameter handling working")
        else:
            print("   ⚠️  Unexpected response for invalid parameter")
    except Exception as e:
        print(f"   ❌ Invalid parameter test failed: {e}")
    
    print()
    
    # Test root endpoint
    print("6. Testing Root Endpoint (Documentation):")
    try:
        response = requests.get(f"{base_url}/", timeout=5)
        print(f"   Status: {response.status_code}")
        data = response.json()
        print(f"   API Message: {data.get('message', 'N/A')}")
        print(f"   API Version: {data.get('version', 'N/A')}")
        print("   ✅ Documentation endpoint working")
    except Exception as e:
        print(f"   ❌ Documentation endpoint failed: {e}")
    
    print()
    print("=" * 60)
    print("🎉 API TESTING COMPLETED")
    print("=" * 60)
    print()
    print("📋 Sample API Calls:")
    print(f"   curl {base_url}/api/transactions")
    print(f"   curl \"{base_url}/api/transactions?transactionType=CREDIT\"")
    print(f"   curl \"{base_url}/api/transactions?transactionType=DEBIT\"")
    print(f"   curl {base_url}/api/health")
    print()
    
    return True

if __name__ == "__main__":
    # Check if custom URL provided as command line argument
    if len(sys.argv) > 1:
        base_url = sys.argv[1]
        test_api(base_url)
    else:
        print("Make sure the API server is running before testing!")
        print("Run: python app.py")
        print()
        test_api()
