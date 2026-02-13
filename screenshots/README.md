# Screenshots Guide

Place your screenshots in this folder with the following naming convention:

## Required Screenshots (30 total)

### Part 1: Jenkins Setup (1-6)
- `1_docker_build.png` - Docker build output
- `2_container_running.png` - Jenkins container running (docker ps)
- `3_jenkins_unlock.png` - Jenkins unlock screen
- `4_admin_password.png` - Admin password retrieval
- `5_plugin_installation.png` - Plugin installation progress
- `6_admin_user.png` - Admin user creation

### Part 2: Credentials (7-8)
- `7_dockerhub_token.png` - DockerHub token creation
- `8_jenkins_credentials.png` - Jenkins credentials page

### Part 3: Pipeline Config (9-11)
- `9_code_updates.png` - Updated Jenkinsfile and app.py
- `10_pipeline_creation.png` - New pipeline creation
- `11_pipeline_config.png` - Pipeline configuration

### Part 4: Pipeline Execution (12-20)
- `12_build_triggered.png` - Build started
- `13_pipeline_stages.png` - All stages green
- `14_checkout_stage.png` - Checkout code output
- `15_setup_environment.png` - Python setup output
- `16_train_model.png` - Model training output
- `17_validate_model.png` - Model validation with metrics
- `18_build_image.png` - Docker build output
- `19_push_image.png` - Docker push to DockerHub
- `20_pipeline_success.png` - Success message

### Part 5: DockerHub & History (21-22)
- `21_build_history.png` - Jenkins build history
- `22_dockerhub_repo.png` - DockerHub repository

### Part 6: Testing (23-28)
- `23_container_running_local.png` - Local container running
- `24_health_check.png` - Health endpoint response
- `25_metrics_api.png` - Metrics endpoint response
- `26_swagger_ui.png` - Swagger UI documentation
- `27_prediction.png` - Prediction via curl
- `28_swagger_prediction.png` - Prediction via Swagger UI

### Part 7: Dashboard (29-30)
- `29_dashboard.png` - Complete Jenkins dashboard
- `30_pipeline_view.png` - Pipeline visualization

## Tips for Good Screenshots

- Use full screen or maximize window
- Ensure text is readable
- Capture entire output/response
- Include timestamps where available
- Highlight important sections if needed
- Use PNG format for clarity

## Screenshot Tools

**Windows:**
- Snipping Tool (built-in)
- Windows + Shift + S (screenshot snip)
- Snagit (optional)

**Mac:**
- Command + Shift + 4 (region capture)
- Command + Shift + 3 (full screen)

**Browser:**
- Browser developer tools (F12)
- Full page screenshot extensions

---

Once all screenshots are captured, verify:
- [ ] All 30 screenshots are present
- [ ] Names match exactly as listed above
- [ ] Images are clear and readable
- [ ] No sensitive information (passwords) visible
- [ ] All screenshots are in PNG format
