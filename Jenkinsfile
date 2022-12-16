pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'pytest --version'
      }
    }
    stage('hello') {
      steps {
        sh 'pytest -v -s tests/'
      }
    }
  }
}