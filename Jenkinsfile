pipeline {
  agent any
  stages {
    stage('python') {
      steps {
        sh 'python --version'
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