# PowerShell script to make API public using ngrok
Write-Host "🌍 MAKING TRANSACTIONS API PUBLIC" -ForegroundColor Green
Write-Host "=================================" -ForegroundColor Green

# Check if ngrok is installed
$ngrokInstalled = $false
try {
    ngrok version | Out-Null
    $ngrokInstalled = $true
    Write-Host "✅ ngrok is installed" -ForegroundColor Green
} catch {
    Write-Host "❌ ngrok is not installed" -ForegroundColor Red
    Write-Host ""
    Write-Host "📥 INSTALL NGROK:" -ForegroundColor Yellow
    Write-Host "1. Download from: https://ngrok.com/download" -ForegroundColor White
    Write-Host "2. Or use: choco install ngrok" -ForegroundColor White
    Write-Host "3. Or use: winget install ngrok.ngrok" -ForegroundColor White
    Write-Host ""
    Write-Host "🔑 SETUP NGROK:" -ForegroundColor Yellow
    Write-Host "1. Create account: https://dashboard.ngrok.com/signup" -ForegroundColor White
    Write-Host "2. Get token: https://dashboard.ngrok.com/auth" -ForegroundColor White
    Write-Host "3. Run: ngrok authtoken YOUR_TOKEN" -ForegroundColor White
    exit 1
}

if ($ngrokInstalled) {
    Write-Host ""
    Write-Host "🚀 Starting Flask API..." -ForegroundColor Cyan
    
    # Start Flask app in background
    $flaskJob = Start-Job -ScriptBlock {
        Set-Location $using:PSScriptRoot
        python app.py
    }
    
    # Wait for Flask to start
    Start-Sleep -Seconds 3
    
    Write-Host "🌐 Creating public tunnel..." -ForegroundColor Cyan
    
    # Start ngrok tunnel in background
    $ngrokJob = Start-Job -ScriptBlock {
        ngrok http 5000
    }
    
    # Wait for ngrok to start
    Start-Sleep -Seconds 5
    
    # Get public URL
    try {
        $response = Invoke-RestMethod -Uri "http://localhost:4040/api/tunnels" -TimeoutSec 10
        if ($response.tunnels -and $response.tunnels.Count -gt 0) {
            $publicUrl = $response.tunnels[0].public_url
            
            Write-Host ""
            Write-Host "✅ SUCCESS! Your API is now PUBLIC!" -ForegroundColor Green
            Write-Host "=================================" -ForegroundColor Green
            Write-Host "🔗 Public URL: $publicUrl" -ForegroundColor Yellow
            Write-Host ""
            Write-Host "📋 Test these endpoints:" -ForegroundColor Cyan
            Write-Host "   • All transactions: $publicUrl/api/transactions" -ForegroundColor White
            Write-Host "   • Credit only: $publicUrl/api/transactions?transactionType=CREDIT" -ForegroundColor White
            Write-Host "   • Debit only: $publicUrl/api/transactions?transactionType=DEBIT" -ForegroundColor White
            Write-Host "   • Health check: $publicUrl/api/health" -ForegroundColor White
            Write-Host ""
            Write-Host "🌍 This URL works from anywhere in the world!" -ForegroundColor Green
            Write-Host "📱 Opening in browser..." -ForegroundColor Cyan
            
            # Open browser
            Start-Process $publicUrl
            
            Write-Host ""
            Write-Host "⚠️  Press Ctrl+C to stop the public tunnel" -ForegroundColor Yellow
            Write-Host "🔄 Running... (tunnel is active)" -ForegroundColor Green
            
            # Keep running until user stops
            try {
                while ($true) {
                    Start-Sleep -Seconds 1
                }
            } catch {
                Write-Host ""
                Write-Host "🛑 Stopping services..." -ForegroundColor Red
            }
        } else {
            Write-Host "❌ Could not get tunnel information" -ForegroundColor Red
        }
    } catch {
        Write-Host "❌ Error connecting to ngrok: $_" -ForegroundColor Red
        Write-Host "💡 Check ngrok dashboard at: http://localhost:4040" -ForegroundColor Yellow
    }
    
    # Cleanup
    Write-Host "🧹 Cleaning up..." -ForegroundColor Cyan
    Stop-Job $flaskJob -Force
    Stop-Job $ngrokJob -Force
    Remove-Job $flaskJob
    Remove-Job $ngrokJob
    Write-Host "✅ All services stopped" -ForegroundColor Green
}
