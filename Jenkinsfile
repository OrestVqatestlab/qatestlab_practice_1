pipeline {
  agent any
  stages {
    stage('venv') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('hello') {
      steps {
        sh 'pytest -v -s tests/'
      }
    }
  }
}