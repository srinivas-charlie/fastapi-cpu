pipeline {

    agent any 

    stages {

        stage('Check docker') {
            steps {
                sh 'docker --version'
                sh 'docker compose version'
            }
        }

        stage('stop existing containers') {
            steps {
                sh 'docker compose down || true'
            }
        }
        stage('Bulid Containers') {
            steps {
                sh 'docker compose build'
            }
        }
        stage('start container') {
            steps {
                sh 'docker compose up -d'
            }
        }
        stage('verify running containers') {
            steps {
                sh 'docker ps'
            }
        }
        
    }
    
    post {
        success {
            echo 'deployement successful'
        }
        failure {
            echo 'deployement failed'
        }
    }
}
