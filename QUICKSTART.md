# Lab 6: Jenkins CI/CD Pipeline - Quick Start

## 🚀 Quick Commands Reference

### 1. Build Jenkins Server
```bash
cd lab-6
docker build -t 2022bcd0026-jenkins -f Dockerfile.jenkins .
```

### 2. Run Jenkins
```bash
docker run -d -u root -p 8080:8080 -p 50000:50000 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v jenkins_home:/var/jenkins_home \
  --name jenkins-2022bcd0026 \
  2022bcd0026-jenkins
```

### 3. Get Initial Password
```bash
docker exec jenkins-2022bcd0026 cat /var/jenkins_home/secrets/initialAdminPassword
```

### 4. Access Jenkins
- URL: http://localhost:8080
- Paste the password from step 3
- Install suggested plugins
- Create admin user

---

## 🔑 Setup Credentials

### DockerHub Token
1. DockerHub → Account Settings → Security → New Access Token
2. Copy token
3. Jenkins → Manage Jenkins → Credentials → Add Credentials
   - ID: `dockerhub-token`
   - Username: Your DockerHub username
   - Password: Token from step 1

---

## 📝 Before Running Pipeline

### Update Jenkinsfile
```groovy
DOCKERHUB_USERNAME = 'your-dockerhub-username'  // Change this!
IMAGE_NAME = '2022bcd0026-wine-quality'         // Already set
```

### Update app.py
```python
STUDENT_INFO = {
    "name": "Your Name",
    "roll_no": "Your Roll Number",
    "lab": "Lab 6 - Jenkins CI/CD Pipeline"
}
```

---

## ▶️ Run Pipeline

1. Jenkins → New Item
2. Name: `wine-quality-pipeline`
3. Type: Pipeline
4. Pipeline script: Copy content from `Jenkinsfile`
5. Click "Build Now"

---

## 🧪 Test Deployment

### Pull and Run
```bash
docker pull your-username/2022bcd0026-wine-quality:latest
docker run -d -p 8000:8000 --name wine-api-2022bcd0026 \
  your-username/2022bcd0026-wine-quality:latest
```

### Test API
```bash
# Health check
curl http://localhost:8000/health

# View metrics
curl http://localhost:8000/metrics

# Swagger UI
# Open browser: http://localhost:8000/docs

# Run test script
python test_api.py
```

---

## 📸 Screenshots Needed

1. Docker build output
2. Jenkins container running
3. Jenkins unlock screen
4. Admin password retrieval
5. Plugin installation
6. Admin user creation
7. DockerHub token
8. Jenkins credentials
9. Code updates
10. Pipeline creation
11. Pipeline configuration
12. Build triggered
13. Pipeline stages (all green)
14-20. Each pipeline stage output
21. Build history
22. DockerHub repository
23. Container running
24. Health check
25. Metrics API
26. Swagger UI
27. Prediction response (curl)
28. Prediction via Swagger
29. Complete dashboard
30. Pipeline visualization

---

## 🛠️ Troubleshooting

### Jenkins won't start
```bash
docker logs jenkins-2022bcd0026
```

### Pipeline fails
- Check credentials ID: `dockerhub-token`
- Verify DockerHub username in Jenkinsfile
- Check Docker socket is mounted

### Can't access API
```bash
docker ps  # Check if container is running
docker logs wine-api-2022bcd0026  # Check container logs
```

---

## 📋 Submission Files

1. **LAB6_SUBMISSION.md** - Main submission document
2. **README.md** - Detailed guide
3. **All code files** - Jenkinsfile, app.py, train.py, etc.
4. **Screenshots folder** - All 30 screenshots

---

## 🎯 Pipeline Stages

1. ✅ Checkout Code
2. ✅ Setup Python Environment  
3. ✅ Train Model
4. ✅ Validate Model (accuracy > 50%)
5. ✅ Build Docker Image
6. ✅ Push to DockerHub
7. ✅ Cleanup

---

## 💡 Key Points

- Jenkins runs as root for Docker socket access
- Pipeline validates model quality before deployment
- Every build creates a new Docker image tag
- Update student info in app.py before submission
- Capture screenshots at each step

---

## 📞 Quick Help

**Jenkins not accessible?**
- Check if port 8080 is free
- Wait 1-2 minutes for Jenkins to start

**Docker build fails?**
- Check Docker daemon is running
- Verify Dockerfile syntax

**Push to DockerHub fails?**
- Verify credentials
- Check token permissions (Read, Write, Delete)

**API returns 503?**
- Model not loaded (check if model.pkl exists)
- Container didn't start properly

---

**Good luck! 🚀**
