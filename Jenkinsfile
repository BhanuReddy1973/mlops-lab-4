pipeline {
    agent any
    
    environment {
        // DockerHub credentials (setup in Jenkins)
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-token')
        DOCKERHUB_USERNAME = 'bhanureddy1973'  // Update this
        IMAGE_NAME = '2022bcd0026-wine-quality'
        IMAGE_TAG = "${BUILD_NUMBER}"
    }
    
    stages {
        stage('Checkout Code') {
            steps {
                echo '📥 Checking out code from repository...'
                checkout scm
            }
        }
        
        stage('Setup Python Environment') {
            steps {
                echo '🔧 Setting up Python virtual environment...'
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }
        
        stage('Train Model') {
            steps {
                echo '🎯 Training the ML model...'
                sh '''
                    . venv/bin/activate
                    cd scripts
                    python train.py
                    cd ..
                '''
            }
        }
        
        stage('Validate Model') {
            steps {
                echo '✅ Validating model metrics...'
                sh '''
                    # Check if model file exists
                    if [ ! -f "model.pkl" ]; then
                        echo "❌ Model file not found!"
                        exit 1
                    fi
                    
                    # Check if metrics file exists
                    if [ ! -f "metrics.json" ]; then
                        echo "❌ Metrics file not found!"
                        exit 1
                    fi
                    
                    # Extract and validate accuracy
                    accuracy=$(jq -r '.accuracy' metrics.json)
                    echo "📊 Model Accuracy: $accuracy"
                    
                    # Check if accuracy meets threshold (e.g., > 0.50)
                    threshold=0.50
                    if (( $(echo "$accuracy > $threshold" | bc -l) )); then
                        echo "✅ Model meets accuracy threshold!"
                    else
                        echo "❌ Model accuracy below threshold!"
                        exit 1
                    fi
                '''
            }
        }
        
        stage('Build Docker Image') {
            steps {
                echo '🐳 Building Docker image...'
                sh '''
                    docker build -t ${DOCKERHUB_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG} .
                    docker tag ${DOCKERHUB_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG} \
                               ${DOCKERHUB_USERNAME}/${IMAGE_NAME}:latest
                '''
            }
        }
        
        stage('Push to DockerHub') {
            steps {
                echo '📤 Pushing image to DockerHub...'
                sh '''
                    echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_USERNAME --password-stdin
                    docker push ${DOCKERHUB_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG}
                    docker push ${DOCKERHUB_USERNAME}/${IMAGE_NAME}:latest
                '''
            }
        }
        
        stage('Cleanup') {
            steps {
                echo '🧹 Cleaning up local Docker images...'
                sh '''
                    docker rmi ${DOCKERHUB_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG} || true
                    docker rmi ${DOCKERHUB_USERNAME}/${IMAGE_NAME}:latest || true
                '''
            }
        }
    }
    
    post {
        success {
            echo '✅ Pipeline completed successfully!'
            echo "🚀 Image: ${DOCKERHUB_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG}"
        }
        failure {
            echo '❌ Pipeline failed! Check logs for details.'
        }
        always {
            echo '🧹 Cleaning up workspace...'
            cleanWs()
        }
    }
}

