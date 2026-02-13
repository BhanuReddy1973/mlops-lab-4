# Lab 6: Jenkins CI/CD Pipeline for MLOps

## 📚 Overview
This lab demonstrates how to build an automated CI/CD pipeline using Jenkins for ML model deployment. The pipeline automatically trains models, validates performance, builds Docker containers, and deploys to DockerHub.

## 🎯 Learning Objectives
- Set up Jenkins server with custom Docker image
- Create automated ML training pipelines
- Implement continuous integration for ML models
- Automate Docker image building and deployment
- Configure credentials and secrets in Jenkins

## 📁 Project Structure
```
lab-6/
├── Dockerfile.jenkins       # Custom Jenkins server image
├── Jenkinsfile             # CI/CD pipeline definition
├── app.py                  # FastAPI inference service
├── Dockerfile              # Application container image
├── requirements.txt        # Python dependencies
├── scripts/
│   └── train.py           # Model training script
└── README.md              # This file
```

## 🔧 Prerequisites
- Docker installed on your machine
- DockerHub account
- GitHub account (optional, for SCM integration)
- Basic understanding of:
  - Docker containers
  - CI/CD concepts
  - Python and scikit-learn

---

## 🚀 Quick Start Guide

### Step 1: Build Jenkins Server

Build the custom Jenkins image with all required tools:

```bash
cd lab-6
docker build -t 2022bcd0026-jenkins -f Dockerfile.jenkins .
```

### Step 2: Run Jenkins Server

Start Jenkins container with Docker socket access:

```bash
docker run -d -u root -p 8080:8080 -p 50000:50000 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v jenkins_home:/var/jenkins_home \
  --name jenkins-2022bcd0026 \
  2022bcd0026-jenkins
```

**Why run as root?** The container needs access to Docker socket for building images.

### Step 3: Access Jenkins

1. Open browser: `http://localhost:8080`
2. Get initial password:
   ```bash
   docker exec jenkins-2022bcd0026 cat /var/jenkins_home/secrets/initialAdminPassword
   ```
3. Copy and paste the password

### Step 4: Initial Setup

1. **Install Plugins:**
   - Choose "Install suggested plugins"
   - Wait for installation to complete

2. **Create Admin User:**
   - Username: (your choice)
   - Password: (your choice)
   - Full Name: Your Name
   - Email: your.email@example.com
   - Click "Save and Continue"

3. **Jenkins URL:**
   - Keep default: `http://localhost:8080/`
   - Click "Save and Finish"

---

## 🔑 Configure Credentials

### A. DockerHub Token

1. **Generate Token on DockerHub:**
   - Go to https://hub.docker.com/
   - Account Settings → Security
   - Click "New Access Token"
   - Description: `jenkins-pipeline`
   - Access: Read, Write, Delete
   - Click "Generate" and **copy the token**

2. **Add to Jenkins:**
   - Jenkins Dashboard → Manage Jenkins → Credentials
   - Click "(global)" → Add Credentials
   - Kind: `Username with password`
   - Username: Your DockerHub username
   - Password: Paste the token you generated
   - ID: `dockerhub-token`
   - Description: `DockerHub Access Token`
   - Click "Create"

### B. GitHub Token (Optional)

If using GitHub for source control:

1. **Generate on GitHub:**
   - GitHub Settings → Developer settings → Personal access tokens
   - Generate new token (classic)
   - Select scopes: `repo` (all)
   - Generate and copy token

2. **Add to Jenkins:**
   - Same process as DockerHub
   - ID: `github-token`

---

## 📝 Configure Pipeline

### Step 1: Update Jenkinsfile

Edit `Jenkinsfile` and update:
```groovy
DOCKERHUB_USERNAME = 'your-dockerhub-username'  // Change this!
IMAGE_NAME = '2022bcd0026-wine-quality'         // Already set
```

### Step 2: Update app.py

Edit `app.py` and update student information:
```python
STUDENT_INFO = {
    "name": "Your Name",           # Your actual name
    "roll_no": "2022BCD0026",     # Your roll number
    "lab": "Lab 6 - Jenkins CI/CD Pipeline"
}
```

### Step 3: Create Jenkins Pipeline

1. **New Item:**
   - Click "New Item" on Jenkins dashboard
   - Name: `wine-quality-pipeline`
   - Select: "Pipeline"
   - Click OK

2. **Configure Pipeline:**
   - Description: `ML Model Training and Deployment Pipeline`
   - Pipeline section:
     - Definition: `Pipeline script from SCM` (if using Git) OR
     - Definition: `Pipeline script` (paste Jenkinsfile content)
   - Click "Save"

---

## ▶️ Run the Pipeline

### Manual Trigger

1. Go to pipeline: `wine-quality-pipeline`
2. Click "Build Now"
3. Watch the build progress

### Pipeline Stages

The pipeline will execute:

1. **Checkout Code** - Get code from repository
2. **Setup Python Environment** - Install dependencies
3. **Train Model** - Train ML model on wine dataset
4. **Validate Model** - Check accuracy meets threshold (>50%)
5. **Build Docker Image** - Create container image
6. **Push to DockerHub** - Upload to registry
7. **Cleanup** - Remove local images

---

## 🧪 Test the Deployment

### Pull and Run Image

```bash
# Pull from DockerHub
docker pull your-dockerhub-username/2022bcd0026-wine-quality:latest

# Run container
docker run -d -p 8000:8000 --name wine-api-2022bcd0026 \
  your-dockerhub-username/2022bcd0026-wine-quality:latest
```

### Test API

1. **Health Check:**
   ```bash
   curl http://localhost:8000/health
   ```

2. **View Metrics:**
   ```bash
   curl http://localhost:8000/metrics
   ```

3. **Make Prediction:**
   ```bash
   curl -X POST http://localhost:8000/predict \
     -H "Content-Type: application/json" \
     -d '{
       "alcohol": 13.2,
       "malic_acid": 2.77,
       "ash": 2.51,
       "alcalinity_of_ash": 18.5,
       "magnesium": 96.0,
       "total_phenols": 2.45,
       "flavanoids": 2.53,
       "nonflavanoid_phenols": 0.29,
       "proanthocyanins": 1.54,
       "color_intensity": 4.6,
       "hue": 1.04,
       "od280_od315": 2.77,
       "proline": 562.0
     }'
   ```

4. **Open Swagger UI:**
   - Browser: `http://localhost:8000/docs`

---

## 📊 Understanding the Pipeline

### Why Jenkins?
- **Automation:** No manual steps needed
- **Consistency:** Same process every time
- **Traceability:** Complete build history
- **Integration:** Works with Git, Docker, etc.

### Pipeline Flow
```
Code Push → Jenkins Trigger → Train Model → Validate → Build Image → Push to Registry → Deploy
```

### Key Components

| Component | Purpose |
|-----------|---------|
| `Dockerfile.jenkins` | Custom Jenkins server with tools |
| `Jenkinsfile` | Pipeline stages definition |
| `train.py` | ML model training logic |
| `app.py` | FastAPI inference service |
| `Dockerfile` | Application container |

---

## 🔍 Common Issues

### Issue 1: Docker socket permission denied
**Solution:** Run Jenkins container with `-u root` flag

### Issue 2: Pipeline fails at Docker build
**Solution:** Ensure Docker socket is mounted: `-v /var/run/docker.sock:/var/run/docker.sock`

### Issue 3: DockerHub push fails
**Solution:** 
- Check credentials ID matches: `dockerhub-token`
- Verify token has write permissions
- Check DockerHub username is correct

### Issue 4: Model accuracy below threshold
**Solution:** This is expected behavior - pipeline validates model quality

---

## 📸 Required Screenshots

For submission, capture:

1. Jenkins dashboard with successful build
2. Pipeline stages view (all green)
3. Pipeline logs showing each stage
4. DockerHub repository showing pushed image
5. API health check response
6. Swagger UI documentation
7. Prediction API response

---

## 🎓 Key Learnings

1. **CI/CD for ML:** Automated model training and deployment
2. **Jenkins Setup:** Custom server configuration
3. **Containerization:** Docker for reproducible environments
4. **Pipeline as Code:** Jenkinsfile defines entire workflow
5. **Model Validation:** Automated quality checks

---

## 📚 Additional Resources

- Jenkins Documentation: https://www.jenkins.io/doc/
- Docker Documentation: https://docs.docker.com/
- FastAPI Documentation: https://fastapi.tiangolo.com/

---

## 👨‍💻 Student Information

**Update in `app.py` before submission:**
```python
STUDENT_INFO = {
    "name": "Your Name",
    "roll_no": "Your Roll Number",
    "lab": "Lab 6 - Jenkins CI/CD Pipeline"
}
```

---

## ✅ Submission Checklist

- [ ] Jenkins server running successfully
- [ ] Pipeline executes all stages
- [ ] Docker image pushed to DockerHub
- [ ] API tested and working
- [ ] All screenshots captured
- [ ] Student info updated in code
- [ ] Submission document completed

---

**Good luck! 🚀**
