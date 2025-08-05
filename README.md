# Transactions API

A public REST API endpoint that provides transaction data with optional filtering capabilities. **This API is configured for public access and can be accessed from any system or location.**

## 🌐 Public Access Features

- ✅ **Publicly accessible** from any system or network
- ✅ **CORS enabled** for cross-origin requests
- ✅ **No authentication required** (configurable)
- ✅ **Multiple deployment options** (local, cloud, Docker)
- ✅ **Production-ready** with Gunicorn support
- ✅ **Security headers** included
- ✅ **Health monitoring** endpoint

## 🚀 Quick Public Deployment

### Option 1: 🔥 Instant Public Access (Recommended for Testing)
**Windows:**
```powershell
.\make_public.ps1
```
**Or:**
```bash
python public_deploy.py
```
*This uses ngrok to create an instant public tunnel. Perfect for demos and testing!*

### Option 2: ☁️ Permanent Cloud Deployment (Recommended for Production)
**Render (FREE):**
1. Create account at [render.com](https://render.com)
2. Connect GitHub repo
3. Deploy automatically with `render.yaml`

**Railway (FREE):**
```bash
# Install Railway CLI
npm install -g @railway/cli
# Deploy
railway login
railway deploy
```

### Option 3: 🐳 Docker Deployment
```bash
docker-compose up --build
```

### Option 4: 🏠 Local Development
```bash
python app.py
```

## 🌐 Access URLs

After deployment, your API will be accessible at:

**🔥 Ngrok (Instant):**
- Public URL provided after running `public_deploy.py`
- Example: `https://abc123.ngrok.io/api/transactions`

**☁️ Cloud Platforms:**
- **Render:** `https://yourapp.onrender.com/api/transactions`
- **Railway:** `https://yourapp.railway.app/api/transactions`
- **Heroku:** `https://yourapp.herokuapp.com/api/transactions`

**🏠 Local:**
- `http://localhost:5000/api/transactions`

## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

The API will be available at `http://localhost:5000`

## API Endpoints

### GET /api/transactions

Returns a list of transactions with optional filtering.

**Query Parameters:**
- `transactionType` (optional): Filter transactions by type
  - Valid values: `CREDIT`, `DEBIT`
  - If not provided, all transactions are returned

**Examples:**

1. Get all transactions:
```
GET /api/transactions
```

2. Get only credit transactions:
```
GET /api/transactions?transactionType=CREDIT
```

3. Get only debit transactions:
```
GET /api/transactions?transactionType=DEBIT
```

**Response Format:**
```json
[
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
    "reversed": false
  }
]
```

### GET /api/health

Health check endpoint to verify the API is running.

**Response:**
```json
{
  "status": "healthy",
  "message": "Transactions API is running"
}
```

### GET /

Root endpoint that provides API documentation.

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| accountNumber | string | Account identifier |
| type | string | Transaction type description |
| checkNumber | number | Check number (optional) |
| typeCd | string | Transaction type code (optional) |
| amount | number | Transaction amount |
| postedDate | array | Posted date as [year, month, day] |
| effectiveDate | array | Effective date as [year, month, day] |
| debitCredit | string | "C" for Credit, "D" for Debit |
| status | string | Transaction status |
| runningBalance | string | Account balance after transaction (optional) |
| internalTransactionDescription | string | Internal description |
| ExternalTransactionDescription | string | External description |
| referenceNumber | string | Transaction reference number |
| parentTransactionReferenceNumber | string | Parent transaction reference (optional) |
| reversed | boolean | Whether the transaction was reversed |

## Error Handling

The API returns appropriate HTTP status codes:

- `200 OK`: Successful request
- `400 Bad Request`: Invalid query parameters
- `500 Internal Server Error`: Server error

Error responses include a JSON object with an `error` field describing the issue.

## CORS Support

The API includes CORS (Cross-Origin Resource Sharing) support, allowing it to be accessed from web applications running on different domains.

## Production Deployment

For production use, consider:

1. Use a production WSGI server like Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

2. Set up proper environment variables for configuration
3. Use a reverse proxy like Nginx
4. Implement proper logging and monitoring
5. Use a database instead of in-memory data
