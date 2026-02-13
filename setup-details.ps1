# Lab 6 Setup Script - Auto-fill Student Details
# This script updates all necessary files with your information

Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host "  Lab 6: Jenkins CI/CD Pipeline - Setup Script" -ForegroundColor Yellow
Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host ""

# Collect user information
Write-Host "Please provide your details:" -ForegroundColor Green
Write-Host ""

$studentName = Read-Host "Enter your full name"
$dockerUsername = Read-Host "Enter your DockerHub username"

Write-Host ""
Write-Host "Confirming your details:" -ForegroundColor Yellow
Write-Host "  Name: $studentName" -ForegroundColor White
Write-Host "  Roll Number: 2022BCD0026" -ForegroundColor White
Write-Host "  DockerHub Username: $dockerUsername" -ForegroundColor White
Write-Host ""

$confirm = Read-Host "Is this correct? (Y/N)"

if ($confirm -ne 'Y' -and $confirm -ne 'y') {
    Write-Host "Setup cancelled. Please run the script again." -ForegroundColor Red
    exit
}

Write-Host ""
Write-Host "Updating files..." -ForegroundColor Cyan

# Update Jenkinsfile
Write-Host "  [1/3] Updating Jenkinsfile..." -ForegroundColor Gray
$jenkinsfile = Get-Content "Jenkinsfile" -Raw
$jenkinsfile = $jenkinsfile -replace "DOCKERHUB_USERNAME = 'your-dockerhub-username'", "DOCKERHUB_USERNAME = '$dockerUsername'"
Set-Content "Jenkinsfile" $jenkinsfile
Write-Host "  ✓ Jenkinsfile updated" -ForegroundColor Green

# Update app.py  
Write-Host "  [2/3] Updating app.py..." -ForegroundColor Gray
$appFile = Get-Content "app.py" -Raw
$appFile = $appFile -replace '"Your Name"', "`"$studentName`""
Set-Content "app.py" $appFile
Write-Host "  ✓ app.py updated" -ForegroundColor Green

# Update LAB6_SUBMISSION.md
Write-Host "  [3/3] Updating LAB6_SUBMISSION.md..." -ForegroundColor Gray
$submissionFile = Get-Content "LAB6_SUBMISSION.md" -Raw
$submissionFile = $submissionFile -replace '\[Your Full Name\]', $studentName
$submissionFile = $submissionFile -replace '\[Your Roll Number\]', '2022BCD0026'
$submissionFile = $submissionFile -replace '\[your-dockerhub-username\]', $dockerUsername
$submissionFile = $submissionFile -replace '\[your-username\]', $dockerUsername
Set-Content "LAB6_SUBMISSION.md" $submissionFile
Write-Host "  ✓ LAB6_SUBMISSION.md updated" -ForegroundColor Green

Write-Host ""
Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host "  Setup Complete! ✓" -ForegroundColor Green
Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Your details have been updated in:" -ForegroundColor Yellow
Write-Host "  • Jenkinsfile (DockerHub username)" -ForegroundColor White
Write-Host "  • app.py (Student name and roll number)" -ForegroundColor White
Write-Host "  • LAB6_SUBMISSION.md (All details)" -ForegroundColor White
Write-Host ""
Write-Host "Next Steps:" -ForegroundColor Yellow
Write-Host "  1. Get Jenkins password:" -ForegroundColor White
Write-Host "     docker exec jenkins-2022bcd0026 cat /var/jenkins_home/secrets/initialAdminPassword" -ForegroundColor Cyan
Write-Host ""
Write-Host "  2. Access Jenkins:" -ForegroundColor White
Write-Host "     http://localhost:8080" -ForegroundColor Cyan
Write-Host ""
Write-Host "  3. Follow the QUICKSTART.md guide" -ForegroundColor White
Write-Host ""
Write-Host "Good luck! 🚀" -ForegroundColor Green
Write-Host ""
