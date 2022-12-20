pipeline {
  agent { docker { image 'python:3.10.7-alpine' } }
  stages {
    stage('python') {
      steps {
        sh 'python3 -m venv .venv'
        sh 'source .venv/bin/activate'
      }
    }
    stage('requirements') {
      steps {
        sh 'pip install -r requirements.txt'
        sh 'pytest -v -s tests/'
      }
    }
  }
}