#!/usr/bin/env python3
"""
Public Internet Deployment Script for Users API
This script provides multiple options to make your API accessible over the internet
"""

import os
import sys
import subprocess
import platform
import webbrowser
import time
import json

def check_ngrok_installed():
    """Check if ngrok is installed"""
    try:
        subprocess.run(["ngrok", "version"], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def install_ngrok_instructions():
    """Provide instructions to install ngrok"""
    print("\n🔧 NGROK INSTALLATION REQUIRED")
    print("=" * 50)
    print("📥 Download from: https://ngrok.com/download")
    print("\n💡 Or use package managers:")
    if platform.system() == "Windows":
        print("   • Chocolatey: choco install ngrok")
        print("   • Scoop: scoop install ngrok")
        print("   • Winget: winget install ngrok.ngrok")
    elif platform.system() == "Darwin":
        print("   • Homebrew: brew install ngrok")
    else:
        print("   • Snap: sudo snap install ngrok")
    
    print("\n🔑 After installation, authenticate with:")
    print("   1. Create free account at https://dashboard.ngrok.com/signup")
    print("   2. Get your authtoken from https://dashboard.ngrok.com/auth")
    print("   3. Run: ngrok authtoken YOUR_TOKEN")
    return False

def start_api_with_ngrok():
    """Start the API and expose it publicly using ngrok"""
    print("🚀 STARTING PUBLIC API WITH NGROK")
    print("=" * 50)
    
    # Check if ngrok is available
    if not check_ngrok_installed():
        install_ngrok_instructions()
        return False
    
    try:
        print("📡 Starting Flask API server...")
        
        # Start the Flask app in background
        api_process = subprocess.Popen([
            sys.executable, "app.py"
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Wait for server to start
        time.sleep(3)
        
        print("🌐 Creating public tunnel with ngrok...")
        
        # Start ngrok tunnel
        ngrok_process = subprocess.Popen([
            "ngrok", "http", "5000"
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        # Wait for ngrok to establish tunnel
        time.sleep(5)
        
        # Get the public URL from ngrok API
        try:
            import requests
            response = requests.get("http://localhost:4040/api/tunnels", timeout=10)
            tunnels_data = response.json()
            
            if tunnels_data.get("tunnels"):
                public_url = tunnels_data["tunnels"][0]["public_url"]
                
                print("\n✅ SUCCESS! Your API is now PUBLIC on the internet!")
                print("=" * 60)
                print(f"🔗 Public URL: {public_url}")
                print("=" * 60)
                print("📋 Test these endpoints from anywhere in the world:")
                print(f"   • All users: {public_url}/api/users")
                print(f"   • Active users: {public_url}/api/users?userType=ACTIVE")
                print(f"   • Inactive users: {public_url}/api/users?userType=INACTIVE")
                print(f"   • Health check: {public_url}/api/health")
                print(f"   • API docs: {public_url}/")
                print("=" * 60)
                print("🌍 Share this URL with anyone - it works globally!")
                print("📱 Opening in browser...")
                
                # Open in browser
                webbrowser.open(public_url)
                
                print("\n⚠️  IMPORTANT:")
                print("   • This URL is PUBLIC - anyone can access it")
                print("   • The tunnel stays active while this script runs")
                print("   • Press Ctrl+C to stop and close the tunnel")
                print("\n🔄 Running... (Press Ctrl+C to stop)")
                
                try:
                    # Keep running until interrupted
                    while True:
                        time.sleep(1)
                except KeyboardInterrupt:
                    print("\n\n🛑 Stopping servers...")
                    api_process.terminate()
                    ngrok_process.terminate()
                    print("✅ All services stopped. API is no longer public.")
                    return True
            else:
                print("❌ Could not get ngrok tunnel information")
                return False
                
        except ImportError:
            print("⚠️  Installing requests library...")
            subprocess.run([sys.executable, "-m", "pip", "install", "requests"])
            print("🔄 Please run the script again")
            return False
        except Exception as e:
            print(f"❌ Error getting tunnel info: {e}")
            print("💡 Try checking ngrok dashboard at: http://localhost:4040")
            return False
            
    except Exception as e:
        print(f"❌ Error starting services: {e}")
        return False

def cloud_deployment_guide():
    """Provide detailed cloud deployment instructions"""
    print("\n☁️  PERMANENT CLOUD DEPLOYMENT OPTIONS")
    print("=" * 60)
    
    print("\n🎯 1. RENDER (Recommended - FREE)")
    print("   • Website: https://render.com")
    print("   • Steps:")
    print("     1. Create free account")
    print("     2. Connect your GitHub repository")
    print("     3. Create new Web Service")
    print("     4. Use these settings:")
    print("        - Build Command: pip install -r requirements.txt")
    print("        - Start Command: gunicorn --bind 0.0.0.0:$PORT app:app")
    print("     5. Deploy!")
    print("   • Your API will get a permanent public URL")
    
    print("\n🎯 2. RAILWAY (FREE tier)")
    print("   • Website: https://railway.app")
    print("   • Steps:")
    print("     1. Create account and connect GitHub")
    print("     2. Deploy from repo")
    print("     3. Railway auto-detects Python and uses railway.json")
    
    print("\n🎯 3. GOOGLE CLOUD RUN (FREE tier)")
    print("   • Website: https://cloud.google.com/run")
    print("   • Steps:")
    print("     1. Install Google Cloud CLI")
    print("     2. Run: gcloud run deploy --source .")
    print("     3. Follow prompts")
    
    print("\n🎯 4. FLY.IO (FREE tier)")
    print("   • Website: https://fly.io")
    print("   • Steps:")
    print("     1. Install flyctl")
    print("     2. Run: fly launch")
    print("     3. Follow setup")
    
    print("\n💡 All these options give you a permanent public URL that works 24/7!")

def local_network_only():
    """Run API on local network only"""
    print("🏠 STARTING API - LOCAL NETWORK ACCESS")
    print("=" * 50)
    print("⚠️  This will only work on your local network")
    print("🔗 Find your local IP and use: http://YOUR_LOCAL_IP:5000")
    print("=" * 50)
    
    subprocess.run([sys.executable, "app.py"])

def main():
    """Main deployment function"""
    print("🌍 TRANSACTIONS API - INTERNET DEPLOYMENT")
    print("=" * 60)
    print("Make your API accessible from anywhere on the internet!")
    print("=" * 60)
    
    if len(sys.argv) > 1 and sys.argv[1] == "--cloud":
        cloud_deployment_guide()
        return
    
    print("\n🚀 Choose your deployment option:")
    print("1. 🔥 Instant Public Access (using ngrok)")
    print("2. ☁️  Permanent Cloud Deployment (free options)")
    print("3. 🏠 Local Network Only")
    print("4. ❓ Help & Information")
    
    choice = input("\nEnter your choice (1-4): ").strip()
    
    if choice == "1":
        success = start_api_with_ngrok()
        if success:
            print("✅ Public deployment completed!")
        else:
            print("❌ Ngrok deployment failed.")
            print("💡 Try option 2 for cloud deployment instead.")
    elif choice == "2":
        cloud_deployment_guide()
    elif choice == "3":
        local_network_only()
    elif choice == "4":
        print("\n📖 HELP & INFORMATION")
        print("=" * 40)
        print("🔥 Option 1 (ngrok): Instant but temporary")
        print("   • Works immediately")
        print("   • Public URL changes each time")
        print("   • Free tier has some limitations")
        print("   • Perfect for testing/demos")
        print("\n☁️  Option 2 (Cloud): Permanent and professional")
        print("   • Permanent public URL")
        print("   • Works 24/7 even when your computer is off")
        print("   • Free tiers available")
        print("   • Professional solution")
        print("\n🏠 Option 3 (Local): Testing only")
        print("   • Only works on your local network")
        print("   • Not accessible from internet")
        print("   • Good for development")
    else:
        print("❌ Invalid choice. Please run the script again.")

if __name__ == "__main__":
    main()
