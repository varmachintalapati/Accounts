# Public API Deployment Guide

This guide explains how to deploy the Transactions API to make it publicly accessible from anywhere.

## 🚀 Quick Start (Local Public Access)

### Method 1: Simple Python Deployment
```bash
# Install dependencies
pip install -r requirements.txt

# Run with public access
python deploy.py [optional_port]
```

### Method 2: Production with Gunicorn
```bash
# Install dependencies including Gunicorn
pip install -r requirements.txt

# Run with Gunicorn (recommended for production)
gunicorn -c gunicorn.conf.py app:app
```

### Method 3: Docker Deployment
```bash
# Build and run with Docker
docker-compose up --build

# Or build and run manually
docker build -t transactions-api .
docker run -p 5000:5000 transactions-api
```

## 🌐 Making the API Publicly Accessible

### 1. **Local Network Access**
The API runs on `0.0.0.0:5000`, making it accessible from:
- `http://localhost:5000` (local machine)
- `http://YOUR_LOCAL_IP:5000` (local network)

### 2. **Internet Access (Public Deployment)**

#### Option A: Cloud Platform Deployment

**Heroku:**
```bash
# Install Heroku CLI and login
heroku create your-transactions-api
git add .
git commit -m "Deploy transactions API"
git push heroku main
```

**AWS EC2:**
```bash
# On your EC2 instance
git clone <your-repo>
cd codeSamples
pip install -r requirements.txt
gunicorn -c gunicorn.conf.py app:app
```

**Google Cloud Platform:**
```bash
# Deploy to Google Cloud Run
gcloud run deploy transactions-api --source . --port 5000 --allow-unauthenticated
```

**DigitalOcean:**
```bash
# Use DigitalOcean App Platform or Droplet
# Upload files and run gunicorn
```

#### Option B: VPS/Dedicated Server
1. Rent a VPS (DigitalOcean, Linode, Vultr, etc.)
2. Install Python and dependencies
3. Upload your code
4. Run with Gunicorn
5. Configure firewall to allow port 5000

#### Option C: Home Server with Port Forwarding
1. Run the API on your home computer
2. Configure router port forwarding (port 5000)
3. Find your public IP
4. Access via `http://YOUR_PUBLIC_IP:5000`

### 3. **Firewall Configuration**

**Windows Firewall:**
```powershell
# Allow inbound traffic on port 5000
New-NetFirewallRule -DisplayName "Transactions API" -Direction Inbound -Port 5000 -Protocol TCP -Action Allow
```

**Linux (UFW):**
```bash
sudo ufw allow 5000
```

**Linux (iptables):**
```bash
sudo iptables -A INPUT -p tcp --dport 5000 -j ACCEPT
```

## 🔗 API Endpoints (Public Access)

Once deployed publicly, your API will be accessible at:

```
Base URL: http://YOUR_PUBLIC_IP:5000
or
Base URL: https://your-domain.com (if using custom domain)
```

### Endpoints:
- `GET /api/transactions` - Get all transactions
- `GET /api/transactions?transactionType=CREDIT` - Get credit transactions
- `GET /api/transactions?transactionType=DEBIT` - Get debit transactions
- `GET /api/health` - Health check
- `GET /` - API documentation

## 🛡️ Security Considerations

### Current Security Features:
- CORS enabled for all origins
- Security headers added
- Input validation
- Error handling

### For Production Use, Consider Adding:
1. **API Key Authentication:**
```python
# Add to app.py
@app.before_request
def require_api_key():
    if request.endpoint != 'health_check':
        api_key = request.headers.get('X-API-Key')
        if api_key != os.environ.get('API_KEY'):
            return jsonify({"error": "Invalid API key"}), 401
```

2. **Rate Limiting:**
```bash
pip install Flask-Limiter
```

3. **HTTPS/SSL:**
- Use a reverse proxy (Nginx) with SSL certificate
- Or deploy to a platform that provides HTTPS (Heroku, etc.)

4. **Database Integration:**
- Replace in-memory data with a proper database
- Add connection pooling and error handling

## 📊 Monitoring and Logging

### Health Check:
```bash
curl http://YOUR_API_URL/api/health
```

### API Testing:
```bash
# Test all transactions
curl http://YOUR_API_URL/api/transactions

# Test credit transactions only
curl "http://YOUR_API_URL/api/transactions?transactionType=CREDIT"

# Test debit transactions only
curl "http://YOUR_API_URL/api/transactions?transactionType=DEBIT"
```

### Production Monitoring:
- Monitor the `/api/health` endpoint
- Set up log aggregation
- Use application performance monitoring (APM) tools

## 🔧 Troubleshooting

### Common Issues:

1. **Connection Refused:**
   - Check if the API is running
   - Verify firewall settings
   - Ensure correct IP and port

2. **CORS Errors:**
   - Already configured to allow all origins
   - If issues persist, check browser console

3. **Performance Issues:**
   - Increase Gunicorn workers
   - Use a load balancer for high traffic
   - Implement caching

4. **Memory Issues:**
   - Monitor memory usage
   - Restart workers periodically
   - Use a database instead of in-memory data

## 🌍 Example Public URLs

After deployment, your API will be accessible like:
- `http://203.0.113.1:5000/api/transactions`
- `https://my-transactions-api.herokuapp.com/api/transactions`
- `https://api.mydomain.com/transactions`

## 📱 Client Integration Examples

### JavaScript (Web):
```javascript
fetch('http://YOUR_API_URL/api/transactions?transactionType=CREDIT')
  .then(response => response.json())
  .then(data => console.log(data));
```

### Python:
```python
import requests
response = requests.get('http://YOUR_API_URL/api/transactions')
data = response.json()
```

### cURL:
```bash
curl -X GET "http://YOUR_API_URL/api/transactions?transactionType=DEBIT"
```

## 📞 Support

For issues or questions about deployment, check:
1. Application logs
2. Network connectivity
3. Firewall settings
4. Cloud platform documentation
