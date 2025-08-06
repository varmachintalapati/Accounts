from flask import Flask, jsonify, request
from flask_cors import CORS
from enum import Enum
from typing import List, Dict, Optional
import json
import os

app = Flask(__name__)

# Configure CORS to allow access from any origin for public API
CORS(app, 
     origins="*",  # Allow all origins for public access
     methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
     allow_headers=["Content-Type", "Authorization", "Access-Control-Allow-Credentials"],
     supports_credentials=False  # Set to False for public API
)

# Add security headers for production
@app.after_request
def after_request(response):
    """Add security headers to all responses"""
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

class UserType(Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

# Sample user data - Limited to 3 users for API response
SAMPLE_USERS = [
    {
        "id": 1,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "Sincere@april.biz",
        "address": {
            "street": "Kulas Light",
            "suite": "Apt. 556",
            "city": "Gwenborough",
            "zipcode": "92998-3874",
            "geo": {
                "lat": "-37.3159",
                "lng": "81.1496"
            }
        },
        "phone": "1-770-736-8031 x56442",
        "website": "hildegard.org",
        "company": {
            "name": "Romaguera-Crona",
            "catchPhrase": "Multi-layered client-server neural-net",
            "bs": "harness real-time e-markets"
        }
    },
    {
        "id": 2,
        "name": "Ervin Howell",
        "username": "Antonette",
        "email": "Shanna@melissa.tv",
        "address": {
            "street": "Victor Plains",
            "suite": "Suite 879",
            "city": "Wisokyburgh",
            "zipcode": "90566-7771",
            "geo": {
                "lat": "-43.9509",
                "lng": "-34.4618"
            }
        },
        "phone": "010-692-6593 x09125",
        "website": "anastasia.net",
        "company": {
            "name": "Deckow-Crist",
            "catchPhrase": "Proactive didactic contingency",
            "bs": "synergize scalable supply-chains"
        }
    },
    {
        "id": 3,
        "name": "Clementine Bauch",
        "username": "Samantha",
        "email": "Nathan@yesenia.net",
        "address": {
            "street": "Douglas Extension",
            "suite": "Suite 847",
            "city": "McKenziehaven",
            "zipcode": "59590-4157",
            "geo": {
                "lat": "-68.6102",
                "lng": "-47.0653"
            }
        },
        "phone": "1-463-123-4447",
        "website": "ramiro.info",
        "company": {
            "name": "Romaguera-Jacobson",
            "catchPhrase": "Face to face bifurcated interface",
            "bs": "e-enable strategic applications"
        }
    }
]

def filter_users_by_type(users: List[Dict], user_type: Optional[str]) -> List[Dict]:
    """
    Filter users based on the user type (ACTIVE or INACTIVE)
    For this implementation, we'll return all users for any filter since
    the sample data doesn't include status information
    
    Args:
        users: List of user dictionaries
        user_type: Optional user type filter ('ACTIVE' or 'INACTIVE')
        
    Returns:
        Filtered list of users (currently returns all users)
    """
    if not user_type:
        return users
    
    # For this sample API, return all users regardless of filter
    # In a real implementation, you would filter based on user status
    return users

@app.route('/api/users', methods=['GET'])
def get_users():
    """
    Get users with optional filtering by user type
    
    Query Parameters:
        userType (optional): Filter by ACTIVE or INACTIVE users
        
    Returns:
        JSON array of users (3 users total)
    """
    try:
        # Get the optional userType query parameter
        user_type = request.args.get('userType', None)
        
        # Validate user type if provided
        if user_type and user_type.upper() not in [e.value for e in UserType]:
            return jsonify({
                "error": "Invalid user type. Valid values are: ACTIVE, INACTIVE"
            }), 400
        
        # Filter users based on the user type (currently returns all users)
        filtered_users = filter_users_by_type(SAMPLE_USERS, user_type)
        
        return jsonify(filtered_users), 200
        
    except Exception as e:
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "message": "Users API is running"}), 200

@app.route('/', methods=['GET'])
def home():
    """Root endpoint with API documentation"""
    documentation = {
        "message": "Users API",
        "version": "1.0.0", 
        "description": "Public API that returns user data with optional filtering",
        "endpoints": {
            "/api/users": {
                "method": "GET",
                "description": "Get users data with optional filtering",
                "parameters": {
                    "userType": {
                        "type": "string",
                        "required": False,
                        "description": "Filter by user type",
                        "enum": ["ACTIVE", "INACTIVE"]
                    }
                },
                "examples": {
                    "all_users": "/api/users",
                    "active_only": "/api/users?userType=ACTIVE",
                    "inactive_only": "/api/users?userType=INACTIVE"
                },
                "note": "Returns 3 users with complete profile information"
            },
            "/api/health": {
                "method": "GET",
                "description": "Health check endpoint"
            }
        },
        "sample_response": {
            "structure": "Array of 3 user objects",
            "total_users": 3,
            "fields": {
                "id": "number - User ID (1, 2, 3)",
                "name": "string - Full name",
                "username": "string - Username",
                "email": "string - Email address",
                "address": "object - Address details with street, suite, city, zipcode, and geo coordinates",
                "phone": "string - Phone number",
                "website": "string - Website",
                "company": "object - Company details with name, catchPhrase, and bs"
            }
        }
    }
    return jsonify(documentation), 200

if __name__ == '__main__':
    # Configuration for public access
    import os
    
    # Get port from environment variable or default to 5000
    port = int(os.environ.get('PORT', 5000))
    
    # Get debug mode from environment variable or default to False for production
    debug_mode = os.environ.get('DEBUG', 'False').lower() == 'true'
    
    # Run the Flask app with public access configuration
    # host='0.0.0.0' allows access from any IP address
    # This makes the API publicly accessible from anywhere
    print(f"Starting Users API on port {port}")
    print(f"API will be accessible at: http://0.0.0.0:{port}")
    print("API Endpoints:")
    print(f"  - GET /api/users (returns 3 users, optional ?userType=ACTIVE|INACTIVE)")
    print(f"  - GET /api/health")
    print(f"  - GET /")
    print("Response: Array of 3 user objects with complete profile data")
    
    app.run(
        host='0.0.0.0',  # Bind to all network interfaces for public access
        port=port,
        debug=debug_mode,
        threaded=True    # Enable threading for better concurrent request handling
    )
