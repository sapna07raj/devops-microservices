pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Getting code from GitHub...'
                checkout scm
            }
        }

        stage('Build Order Service Docker Image') {
            steps {
                echo 'Building Order Service Docker Image...'
                sh 'docker build -t order-service:1.0 ./order-service'
            }
        }

        stage('Build Payment Service Docker Image') {
            steps {
                echo 'Building Payment Service Docker Image...'
                sh 'docker build -t payment-service:1.0 ./payment-service'
            }
        }

        stage('Check Docker Images') {
            steps {
                echo 'Checking Docker Images...'
                sh 'docker images'
            }
        }
    }

    post {
        success {
            echo 'Build completed successfully!'
        }

        failure {
            echo 'Build failed. Check the console output.'
        }
    }
}