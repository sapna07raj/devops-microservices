pipeline {

    agent any

    environment {
        PATH = "/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Getting code from GitHub...'
                checkout scm
            }
        }

        stage('Install Test Dependencies') {
            steps {
                echo 'Installing Pytest and HTTPX...'
                sh 'python3 -m venv .jenkins-venv'
                sh '.jenkins-venv/bin/pip install --upgrade pip'
                sh '.jenkins-venv/bin/pip install -r requirements-test.txt'
            }
        }

        stage('Run Automated Tests') {
            steps {
                echo 'Running Pytest tests...'
                sh '.jenkins-venv/bin/python -m pytest tests/test_services.py -v'
            }
        }

        stage('Build Order Service Docker Image') {
            steps {
                echo 'Building Order Service Docker Image...'
                sh '/usr/local/bin/docker build -t order-service:1.0 ./order-service'
            }
        }

        stage('Build Payment Service Docker Image') {
            steps {
                echo 'Building Payment Service Docker Image...'
                sh '/usr/local/bin/docker build -t payment-service:1.0 ./payment-service'
            }
        }

        stage('Push Images to Docker Hub') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub',
                        usernameVariable: 'DOCKER_USERNAME',
                        passwordVariable: 'DOCKER_PASSWORD'
                    )
                ]) {
                    sh '''
                        echo "$DOCKER_PASSWORD" | /usr/local/bin/docker login -u "$DOCKER_USERNAME" --password-stdin

                        /usr/local/bin/docker tag order-service:1.0 "$DOCKER_USERNAME/order-service:1.0"
                        /usr/local/bin/docker tag payment-service:1.0 "$DOCKER_USERNAME/payment-service:1.0"

                        /usr/local/bin/docker push "$DOCKER_USERNAME/order-service:1.0"
                        /usr/local/bin/docker push "$DOCKER_USERNAME/payment-service:1.0"

                        /usr/local/bin/docker logout
                    '''
                }
            }
        }

        stage('Check Docker Images') {
            steps {
                echo 'Checking Docker Images...'
                sh '/usr/local/bin/docker images'
            }
        }
    }

    post {
        success {
            echo 'Tests passed, images built and pushed to Docker Hub successfully!'
        }

        failure {
            echo 'Pipeline failed. Check the console output.'
        }
    }
}