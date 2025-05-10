pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                echo '✅ Repo cloned by Jenkins automatically'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("bbc-text-api")
                }
            }
        }

        stage('Run Docker') {
            steps {
                sh "docker run -d -p 8000:8000 bbc-text-api"
            }
        }
    }
}
