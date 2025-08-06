# Gunicorn configuration file for production deployment
# Usage: gunicorn -c gunicorn.conf.py app:app

import os

# Server socket
bind = "0.0.0.0:5000"  # Bind to all interfaces for public access
backlog = 2048

# Worker processes
workers = 4  # Adjust based on CPU cores (2 * cores + 1)
worker_class = "sync"
worker_connections = 1000
timeout = 30
keepalive = 2

# Restart workers after this many requests, to help prevent memory leaks
max_requests = 1000
max_requests_jitter = 100

# Security
limit_request_line = 4094
limit_request_fields = 100
limit_request_field_size = 8190

# Logging
accesslog = "-"  # Log to stdout
errorlog = "-"   # Log to stderr
loglevel = "info"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(D)s'

# Process naming
proc_name = "users_api"

# Server mechanics
daemon = False
pidfile = "/tmp/users_api.pid"
user = None
group = None
tmp_upload_dir = None

# SSL (uncomment and configure if using HTTPS)
# keyfile = "/path/to/keyfile"
# certfile = "/path/to/certfile"

# Environment variables
raw_env = [
    'DEBUG=False',
    'PYTHONPATH=/app'
]

# Preload app for better memory usage
preload_app = True
