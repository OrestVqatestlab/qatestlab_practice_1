pipeline {
  agent any
  stages {
    stage('venv') {
      steps {
        sh 'source venv/bin/activate'
      }
    }
    stage('hello') {
      steps {
        sh 'pytest -v -s tests/'
      }
    }
  }
}