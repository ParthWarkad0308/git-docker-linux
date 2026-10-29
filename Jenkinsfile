pipeline {
    agent any

    stages {
        stage('Checkout from GitHub') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/ParthWarkad0308/git-docker-linux.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t pbl-app:latest .'
            }
        }

        stage('Ansible Health Check') {
            steps {
                sh 'ansible localhost -i localhost, -c local -m ping'
            }
        }
    }
}
