# Lab 6: Jenkins CI/CD Pipeline - Submission Document

---

## Student Information

| Field | Details |
|-------|---------|
| **Name** | bhanu_reddy |
| **Roll Number** | 2022BCD0026 |
| **Course** | MLOps |
| **Lab Number** | Lab 6 |
| **Date of Submission** | [DD-MM-YYYY] |
| **Lab Title** | Jenkins CI/CD Pipeline for MLOps |

---

## Objective

To implement an automated CI/CD pipeline using Jenkins for training, validating, containerizing, and deploying a machine learning model for wine quality prediction.

---

## Part 1: Jenkins Server Setup

### 1.1 Build Custom Jenkins Image

**Command used:**
```bash
docker build -t 2022bcd0026-jenkins -f Dockerfile.jenkins .
```

**Screenshot 1: Docker build output showing successful image creation**

![Screenshot 1 - Docker Build](screenshots/1_docker_build.png)
> Insert screenshot showing the docker build command and successful completion

---

### 1.2 Run Jenkins Container

**Command used:**
```bash
docker run -d -u root -p 8080:8080 -p 50000:50000 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v jenkins_home:/var/jenkins_home \
  --name jenkins-2022bcd0026 \
  2022bcd0026-jenkins
```

**Screenshot 2: Jenkins container running**

![Screenshot 2 - Container Running](screenshots/2_container_running.png)
> Insert screenshot showing `docker ps` output with Jenkins container

---

### 1.3 Access Jenkins Dashboard

**URL:** `http://localhost:8080`

**Screenshot 3: Jenkins unlock screen**

![Screenshot 3 - Jenkins Unlock](screenshots/3_jenkins_unlock.png)
> Insert screenshot of Jenkins initial setup screen

---

### 1.4 Initial Admin Password

**Command to retrieve password:**
```bash
docker exec jenkins-2022bcd0026 cat /var/jenkins_home/secrets/initialAdminPassword
```

**Password:** `[Paste your actual password here]`

**Screenshot 4: Password retrieval**

![Screenshot 4 - Admin Password](screenshots/4_admin_password.png)
> Insert screenshot showing the password retrieval command and output

---

### 1.5 Plugin Installation

**Plugins installed:** Install suggested plugins

**Screenshot 5: Plugin installation progress**

![Screenshot 5 - Plugin Installation](screenshots/5_plugin_installation.png)
> Insert screenshot of plugin installation screen

---

### 1.6 Admin User Creation

| Field | Value |
|-------|-------|
| Username | [Your username] |
| Password | [Your password] |
| Full Name | bhanu_reddy |
| Email | [Your email] |

**Screenshot 6: Admin user creation**

![Screenshot 6 - Admin User](screenshots/6_admin_user.png)
> Insert screenshot of admin user setup screen

---

## Part 2: Credentials Configuration

### 2.1 DockerHub Access Token

**DockerHub Username:** `[Your DockerHub username]`

**Steps followed:**
1. Logged into DockerHub
2. Navigated to Account Settings → Security
3. Created new access token named "jenkins-pipeline"
4. Granted Read, Write, Delete permissions
5. Copied token

**Screenshot 7: DockerHub token creation**

![Screenshot 7 - DockerHub Token](screenshots/7_dockerhub_token.png)
> Insert screenshot from DockerHub showing token creation

---

### 2.2 Add Credentials to Jenkins

**Credential ID:** `dockerhub-token`

**Screenshot 8: Jenkins credentials configuration**

![Screenshot 8 - Jenkins Credentials](screenshots/8_jenkins_credentials.png)
> Insert screenshot showing DockerHub credentials added in Jenkins

---

## Part 3: Pipeline Configuration

### 3.1 Code Updates

**Updated in Jenkinsfile:**
```groovy
DOCKERHUB_USERNAME = 'bhanureddy1973'
IMAGE_NAME = '2022bcd0026-wine-quality'
```

**Updated in app.py:**
```python
STUDENT_INFO = {
    "name": "[Your Name]",
    "roll_no": "2022BCD0026",
    "lab": "Lab 6 - Jenkins CI/CD Pipeline"
}
```

**Screenshot 9: Code updates**

![Screenshot 9 - Code Updates](screenshots/9_code_updates.png)
> Insert screenshot showing updated code in VS Code or text editor

---

### 3.2 Create Jenkins Pipeline

**Pipeline Name:** `2022bcd0026-wine-quality-pipeline`

**Pipeline Type:** Pipeline

**Screenshot 10: Pipeline creation**

![Screenshot 10 - Pipeline Creation](screenshots/10_pipeline_creation.png)
> Insert screenshot of new pipeline creation screen

---

### 3.3 Pipeline Configuration

**Screenshot 11: Pipeline script configuration**

![Screenshot 11 - Pipeline Config](screenshots/11_pipeline_config.png)
> Insert screenshot showing Jenkinsfile content in pipeline configuration

---

## Part 4: Pipeline Execution

### 4.1 Trigger Build

**Build Number:** `#[Your build number]`

**Screenshot 12: Build triggered**

![Screenshot 12 - Build Triggered](screenshots/12_build_triggered.png)
> Insert screenshot showing "Build Now" clicked and build started

---

### 4.2 Pipeline Stages View

**Screenshot 13: All pipeline stages (green/successful)**

![Screenshot 13 - Pipeline Stages](screenshots/13_pipeline_stages.png)
> Insert screenshot showing all 7 stages completed successfully with green checkmarks

**Stages executed:**
- ✅ Checkout Code
- ✅ Setup Python Environment
- ✅ Train Model
- ✅ Validate Model
- ✅ Build Docker Image
- ✅ Push to DockerHub
- ✅ Cleanup

---

### 4.3 Console Output - Key Sections

**Screenshot 14: Checkout Code stage**

![Screenshot 14 - Checkout Stage](screenshots/14_checkout_stage.png)
> Insert screenshot of console output showing code checkout

---

**Screenshot 15: Setup Python Environment stage**

![Screenshot 15 - Setup Environment](screenshots/15_setup_environment.png)
> Insert screenshot showing Python dependencies installation

---

**Screenshot 16: Train Model stage**

![Screenshot 16 - Train Model](screenshots/16_train_model.png)
> Insert screenshot showing model training output

---

**Screenshot 17: Validate Model stage**

![Screenshot 17 - Validate Model](screenshots/17_validate_model.png)
> Insert screenshot showing model validation with accuracy metrics

**Model Metrics Obtained:**
- Accuracy: `[value]`
- F1 Score: `[value]`
- MSE: `[value]`

---

**Screenshot 18: Build Docker Image stage**

![Screenshot 18 - Build Image](screenshots/18_build_image.png)
> Insert screenshot showing Docker image build process

---

**Screenshot 19: Push to DockerHub stage**

![Screenshot 19 - Push Image](screenshots/19_push_image.png)
> Insert screenshot showing Docker push to DockerHub

---

**Screenshot 20: Pipeline completion message**

![Screenshot 20 - Pipeline Success](screenshots/20_pipeline_success.png)
> Insert screenshot showing "Pipeline completed successfully" message

---

### 4.4 Build History

**Screenshot 21: Jenkins dashboard with build history**

![Screenshot 21 - Build History](screenshots/21_build_history.png)
> Insert screenshot showing multiple builds in history

---

## Part 5: DockerHub Verification

### 5.1 DockerHub Repository

**Image Name:** `bhanureddy1973/2022bcd0026-wine-quality`

**Screenshot 22: DockerHub repository showing pushed image**

![Screenshot 22 - DockerHub Repository](screenshots/22_dockerhub_repo.png)
> Insert screenshot from DockerHub showing the image with tags

---

**Tags present:**
- `latest`
- `[build-number]`

**Image Size:** `[size in MB]`

**Last Updated:** `[timestamp]`

---

## Part 6: Testing Deployment

### 6.1 Pull and Run Container

**Commands used:**
```bash
docker pull bhanureddy1973/2022bcd0026-wine-quality:latest
docker run -d -p 8000:8000 --name wine-api-2022bcd0026 \
  bhanureddy1973/2022bcd0026-wine-quality:latest
```

**Screenshot 23: Container running locally**

![Screenshot 23 - Container Running](screenshots/23_container_running_local.png)
> Insert screenshot showing docker pull and docker run output

---

### 6.2 API Health Check

**Command:**
```bash
curl http://localhost:8000/health
```

**Response:**
```json
[Paste actual response here]
```

**Screenshot 24: Health check response**

![Screenshot 24 - Health Check](screenshots/24_health_check.png)
> Insert screenshot showing health check endpoint response

---

### 6.3 View Model Metrics

**Command:**
```bash
curl http://localhost:8000/metrics
```

**Response:**
```json
[Paste actual response here]
```

**Screenshot 25: Metrics endpoint response**

![Screenshot 25 - Metrics API](screenshots/25_metrics_api.png)
> Insert screenshot showing metrics endpoint response

---

### 6.4 Swagger UI

**URL:** `http://localhost:8000/docs`

**Screenshot 26: Swagger UI documentation**

![Screenshot 26 - Swagger UI](screenshots/26_swagger_ui.png)
> Insert screenshot of the interactive API documentation

---

### 6.5 Make Prediction

**Sample Request:**
```json
{
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
}
```

**Response:**
```json
[Paste actual prediction response here]
```

**Screenshot 27: Prediction API response**

![Screenshot 27 - Prediction Response](screenshots/27_prediction.png)
> Insert screenshot showing prediction request and response

---

**Screenshot 28: Prediction via Swagger UI**

![Screenshot 28 - Swagger Prediction](screenshots/28_swagger_prediction.png)
> Insert screenshot of making prediction through Swagger interface

---

## Part 7: Pipeline Understanding

### 7.1 Pipeline Flow Diagram

```
┌─────────────┐
│ Code Commit │
└──────┬──────┘
       │
       ▼
┌─────────────────┐
│ Jenkins Trigger │
└────────┬────────┘
         │
         ▼
┌────────────────┐
│  Setup Python  │
│  Environment   │
└────────┬───────┘
         │
         ▼
┌────────────────┐
│  Train Model   │
└────────┬───────┘
         │
         ▼
┌────────────────┐
│ Validate Model │
│  (Accuracy >   │
│     50%)       │
└────────┬───────┘
         │
         ▼
┌────────────────┐
│ Build Docker   │
│     Image      │
└────────┬───────┘
         │
         ▼
┌────────────────┐
│ Push to Docker │
│      Hub       │
└────────┬───────┘
         │
         ▼
┌────────────────┐
│    Cleanup     │
└────────────────┘
```

---

### 7.2 Key Components Explanation

| Component | Purpose | Why Important |
|-----------|---------|---------------|
| **Dockerfile.jenkins** | Creates custom Jenkins server with Python, Docker CLI, jq, bc pre-installed | Eliminates need for separate build agents; all tools available in one container |
| **Jenkinsfile** | Defines pipeline stages and steps | Pipeline as code - version controlled and repeatable |
| **train.py** | ML model training script | Trains Random Forest classifier on wine dataset |
| **app.py** | FastAPI inference service | Provides REST API for predictions |
| **Dockerfile** | Application container definition | Packages model and API for deployment |
| **requirements.txt** | Python dependencies | Ensures reproducible environment |

---

### 7.3 Benefits of CI/CD for ML

**List 5 benefits you observed:**

1. **[Benefit 1]**
   - [Your explanation]

2. **[Benefit 2]**
   - [Your explanation]

3. **[Benefit 3]**
   - [Your explanation]

4. **[Benefit 4]**
   - [Your explanation]

5. **[Benefit 5]**
   - [Your explanation]

---

## Part 8: Challenges and Solutions

### 8.1 Challenges Faced

**Challenge 1:**
- **Issue:** [Describe the issue]
- **Solution:** [How you resolved it]

**Challenge 2:**
- **Issue:** [Describe the issue]
- **Solution:** [How you resolved it]

**Challenge 3:**
- **Issue:** [Describe the issue]
- **Solution:** [How you resolved it]

---

## Part 9: Questions and Answers

### Q1: Why do we run Jenkins container as root user?

**Answer:**
[Your answer here - hint: Docker socket access]

---

### Q2: What is the purpose of mounting `/var/run/docker.sock`?

**Answer:**
[Your answer here]

---

### Q3: Why do we need model validation in the pipeline?

**Answer:**
[Your answer here]

---

### Q4: What happens if model accuracy is below the threshold?

**Answer:**
[Your answer here]

---

### Q5: How is this different from manual deployment?

**Answer:**
[Your answer here - compare with Lab 3/4]

---

## Part 10: Learning Outcomes

### What I Learned:

1. **Jenkins Setup:**
   - [What you learned]

2. **CI/CD Pipelines:**
   - [What you learned]

3. **Docker Integration:**
   - [What you learned]

4. **MLOps Best Practices:**
   - [What you learned]

5. **Automation Benefits:**
   - [What you learned]

---

## Part 11: Conclusion

**Summary:**

[Write a brief paragraph summarizing your experience with this lab, what worked well, and how Jenkins CI/CD helps in MLOps]

---

## Part 12: Additional Screenshots

**Screenshot 29: Complete Jenkins dashboard**

![Screenshot 29 - Dashboard](screenshots/29_dashboard.png)
> Insert screenshot of overall Jenkins dashboard

---

**Screenshot 30: Pipeline visualization**

![Screenshot 30 - Pipeline View](screenshots/30_pipeline_view.png)
> Insert screenshot of pipeline stages visualization

---

## Submission Checklist

- [ ] All student information filled correctly
- [ ] All 30 screenshots attached in proper format
- [ ] All commands documented with outputs
- [ ] Code updates done (Jenkinsfile and app.py)
- [ ] Docker image successfully pushed to DockerHub
- [ ] API tested and all endpoints working
- [ ] Questions answered completely
- [ ] Learning outcomes documented
- [ ] Conclusion written
- [ ] Document formatted properly

---

## Declaration

I hereby declare that this lab work is my own and has been completed by me. All screenshots and outputs are from my actual implementation.

**Name:** [Your Name]

**Roll Number:** 2022BCD0026

**Signature:** ________________

**Date:** [DD-MM-YYYY]

---

**End of Submission Document**

