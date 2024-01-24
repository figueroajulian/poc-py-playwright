pipeline {
    agent { docker { image 'mcr.microsoft.com/playwright/python:v1.41.0-jammy' } }
    stages {
        stage('Set path') {
            steps {
                sh 'export PYTHONPATH="${PYTHONPATH}:/var/jenkins_home/workspace/playwright"'
            }
        }
        stage('e2e-tests') {
            steps {
                sh 'pip install poetry'
                sh 'poetry install'
                sh 'poetry run pytest'
            }
        }
    }
}