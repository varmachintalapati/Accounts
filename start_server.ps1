# Start the Transactions API server
Write-Host "Starting Transactions API server..." -ForegroundColor Green
Write-Host "API will be available at: http://localhost:5000" -ForegroundColor Yellow
Write-Host ""
Write-Host "Available endpoints:" -ForegroundColor Cyan
Write-Host "  GET /api/transactions                           - Get all transactions" -ForegroundColor White
Write-Host "  GET /api/transactions?transactionType=CREDIT    - Get credit transactions only" -ForegroundColor White
Write-Host "  GET /api/transactions?transactionType=DEBIT     - Get debit transactions only" -ForegroundColor White
Write-Host "  GET /api/health                                 - Health check" -ForegroundColor White
Write-Host "  GET /                                           - API documentation" -ForegroundColor White
Write-Host ""
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Red
Write-Host ""

& "C:/Program Files/Python313/python.exe" app.py
