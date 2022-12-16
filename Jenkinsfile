pipeline {
  agent any
  stages {
    stage('python') {
      steps {
        sh 'apk add python3'
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