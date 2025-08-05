#!/usr/bin/env python3
"""
Production deployment script for the Transactions API
This script configures the API for public access with production settings
"""

import os
import sys
import subprocess
from app import app

def check_dependencies():
    """Check if all required dependencies are installed"""
    try:
        import flask
        import flask_cors
        print("✓ All dependencies are installed")
        return True
    except ImportError as e:
        print(f"✗ Missing dependency: {e}")
        print("Please run: pip install -r requirements.txt")
        return False

def run_production_server():
    """Run the API server with production configuration"""
    if not check_dependencies():
        sys.exit(1)
    
    # Set environment variables for production
    os.environ['DEBUG'] = 'False'
    
    # Get port from command line argument or environment
    port = 5000
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("Invalid port number. Using default port 5000")
    
    print("=" * 60)
    print("🚀 STARTING TRANSACTIONS API - PUBLIC ACCESS MODE")
    print("=" * 60)
    print(f"🌐 Port: {port}")
    print(f"🔗 Local Access: http://localhost:{port}")
    print(f"🌍 Public Access: http://YOUR_PUBLIC_IP:{port}")
    print("=" * 60)
    print("📋 Available Endpoints:")
    print(f"   GET /api/transactions")
    print(f"   GET /api/transactions?transactionType=CREDIT")
    print(f"   GET /api/transactions?transactionType=DEBIT")
    print(f"   GET /api/health")
    print(f"   GET /")
    print("=" * 60)
    print("🔧 To access from external systems:")
    print("   1. Find your public IP address")
    print("   2. Ensure firewall allows traffic on this port")
    print("   3. Use: http://YOUR_PUBLIC_IP:{port}/api/transactions")
    print("=" * 60)
    print("⚠️  SECURITY NOTE: This is a public API without authentication")
    print("   Consider adding API keys or rate limiting for production use")
    print("=" * 60)
    
    # Start the application
    app.run(
        host='0.0.0.0',  # Bind to all interfaces for public access
        port=port,
        debug=False,     # Disable debug mode for production
        threaded=True,   # Enable threading for concurrent requests
        use_reloader=False  # Disable auto-reloader for production
    )

if __name__ == '__main__':
    run_production_server()
