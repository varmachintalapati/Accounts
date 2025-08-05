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

class TransactionType(Enum):
    CREDIT = "CREDIT"
    DEBIT = "DEBIT"

# Sample transaction data
SAMPLE_TRANSACTIONS = [
    {
        "accountNumber": "12312",
        "type": "New Account Deposit",
        "checkNumber": 123,
        "typeCd": "DEP",
        "amount": 1232.11,
        "postedDate": [2012, 9, 20],
        "effectiveDate": [2012, 9, 20],
        "debitCredit": "C",
        "status": "Completed",
        "runningBalance": "1234.56",
        "internalTransactionDescription": "Internal Transaction Description",
        "ExternalTransactionDescription": "External Transaction Description",
        "referenceNumber": "12345 - 111",
        "parentTransactionReferenceNumber": "12323 - 123",
        "reversed": False
    },
    {
        "accountNumber": "1232322",
        "type": "Credit Card Payment",
        "amount": 1234,
        "postedDate": [2012, 9, 20],
        "effectiveDate": [2012, 9, 20],
        "debitCredit": "D",
        "status": "Completed",
        "internalTransactionDescription": "internalTransactionDescription",
        "ExternalTransactionDescription": "enternalTransactionDescription",
        "referenceNumber": "90167149 - 316",
        "reversed": True
    },
    {
        "accountNumber": "54321",
        "type": "ATM Withdrawal",
        "amount": 200.00,
        "postedDate": [2012, 9, 21],
        "effectiveDate": [2012, 9, 21],
        "debitCredit": "D",
        "status": "Completed",
        "runningBalance": "1034.56",
        "internalTransactionDescription": "ATM Withdrawal",
        "ExternalTransactionDescription": "ATM Cash Withdrawal",
        "referenceNumber": "ATM001 - 789",
        "reversed": False
    },
    {
        "accountNumber": "12312",
        "type": "Direct Deposit",
        "amount": 2500.00,
        "postedDate": [2012, 9, 22],
        "effectiveDate": [2012, 9, 22],
        "debitCredit": "C",
        "status": "Completed",
        "runningBalance": "3534.56",
        "internalTransactionDescription": "Payroll Deposit",
        "ExternalTransactionDescription": "Direct Deposit - Salary",
        "referenceNumber": "DD001 - 456",
        "reversed": False
    }
]

def filter_transactions_by_type(transactions: List[Dict], transaction_type: Optional[str]) -> List[Dict]:
    """
    Filter transactions based on the transaction type (CREDIT or DEBIT)
    
    Args:
        transactions: List of transaction dictionaries
        transaction_type: Optional transaction type filter ('CREDIT' or 'DEBIT')
        
    Returns:
        Filtered list of transactions
    """
    if not transaction_type:
        return transactions
    
    # Map transaction type to debitCredit field values
    type_mapping = {
        TransactionType.CREDIT.value: "C",
        TransactionType.DEBIT.value: "D"
    }
    
    if transaction_type.upper() not in type_mapping:
        return transactions
    
    debit_credit_value = type_mapping[transaction_type.upper()]
    return [tx for tx in transactions if tx.get("debitCredit") == debit_credit_value]

@app.route('/api/transactions', methods=['GET'])
def get_transactions():
    """
    Get transactions with optional filtering by transaction type
    
    Query Parameters:
        transactionType (optional): Filter by CREDIT or DEBIT transactions
        
    Returns:
        JSON array of transactions
    """
    try:
        # Get the optional transactionType query parameter
        transaction_type = request.args.get('transactionType', None)
        
        # Validate transaction type if provided
        if transaction_type and transaction_type.upper() not in [e.value for e in TransactionType]:
            return jsonify({
                "error": "Invalid transaction type. Valid values are: CREDIT, DEBIT"
            }), 400
        
        # Filter transactions based on the transaction type
        filtered_transactions = filter_transactions_by_type(SAMPLE_TRANSACTIONS, transaction_type)
        
        return jsonify(filtered_transactions), 200
        
    except Exception as e:
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "message": "Transactions API is running"}), 200

@app.route('/', methods=['GET'])
def home():
    """Root endpoint with API documentation"""
    documentation = {
        "message": "Transactions API",
        "version": "1.0.0",
        "endpoints": {
            "/api/transactions": {
                "method": "GET",
                "description": "Get transactions with optional filtering",
                "parameters": {
                    "transactionType": {
                        "type": "string",
                        "required": False,
                        "description": "Filter by transaction type",
                        "enum": ["CREDIT", "DEBIT"]
                    }
                },
                "examples": {
                    "all_transactions": "/api/transactions",
                    "credit_only": "/api/transactions?transactionType=CREDIT",
                    "debit_only": "/api/transactions?transactionType=DEBIT"
                }
            },
            "/api/health": {
                "method": "GET",
                "description": "Health check endpoint"
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
    print(f"Starting Transactions API on port {port}")
    print(f"API will be accessible at: http://0.0.0.0:{port}")
    print("API Endpoints:")
    print(f"  - GET /api/transactions (with optional ?transactionType=CREDIT|DEBIT)")
    print(f"  - GET /api/health")
    print(f"  - GET /")
    
    app.run(
        host='0.0.0.0',  # Bind to all network interfaces for public access
        port=port,
        debug=debug_mode,
        threaded=True    # Enable threading for better concurrent request handling
    )
