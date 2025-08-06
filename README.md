# Users API

A public REST API endpoint that provides user data with optional filtering capabilities. **This API is configured for public access and can be accessed from any system or location.**

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
- Example: `https://abc123.ngrok.io/api/users`

**☁️ Cloud Platforms:**
- **Render:** `https://yourapp.onrender.com/api/users`
- **Railway:** `https://yourapp.railway.app/api/users`
- **Heroku:** `https://yourapp.herokuapp.com/api/users`

**🏠 Local:**
- `http://localhost:5000/api/users`

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

### GET /api/users

Returns a list of 3 users with optional filtering.

**Query Parameters:**
- `userType` (optional): Filter users by type
  - Valid values: `ACTIVE`, `INACTIVE`
  - If not provided, all 3 users are returned

**Examples:**

1. Get all users (3 users):
```
GET /api/users
```

2. Get only active users:
```
GET /api/users?userType=ACTIVE
```

3. Get only inactive users:
```
GET /api/users?userType=INACTIVE
```

**Response Format (3 users):**
```json
[
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
```

### GET /api/health

Health check endpoint to verify the API is running.

**Response:**
```json
{
  "status": "healthy",
  "message": "Users API is running"
}
```

### GET /

Root endpoint that provides API documentation.

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| id | number | Unique user identifier |
| name | string | Full name of the user |
| username | string | Username for the account |
| email | string | Email address |
| address | object | Address information |
| address.street | string | Street address |
| address.suite | string | Suite/apartment number |
| address.city | string | City name |
| address.zipcode | string | ZIP/postal code |
| address.geo | object | Geographic coordinates |
| address.geo.lat | string | Latitude |
| address.geo.lng | string | Longitude |
| phone | string | Phone number |
| website | string | Personal/company website |
| company | object | Company information |
| company.name | string | Company name |
| company.catchPhrase | string | Company catchphrase |
| company.bs | string | Company business strategy |

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
