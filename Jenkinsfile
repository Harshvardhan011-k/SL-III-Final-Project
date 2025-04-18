pipeline {
    agent any
    stages {
        stage('Build Django') {
            steps {
                sh 'docker build -t kediaharsh/djangoappfinal ./bookstore'
            }
        }
        stage('Build Flask') {
            steps {
                sh 'docker build -t kediaharsh/flaskappfinal ./flask_app'
            }
        }
        stage('Push Images') {
            steps {
                withCredentials([string(credentialsId: 'dockerhub-token', variable: 'DOCKERHUB_TOKEN')]) {
                    sh 'echo $DOCKERHUB_TOKEN | docker login -u kediaharsh --password-stdin'
                    sh 'docker push kediaharsh/djangoappfinal'
                    sh 'docker push kediaharsh/flaskappfinal'
                }
            }
        }
    }
}
