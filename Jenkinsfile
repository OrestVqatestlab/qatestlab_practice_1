pipeline {
  agent { docker { image 'python:3.7.2' } }
  stages {
    stage('python') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('requirements') {
      steps {
        sh 'pytest -v -s tests/'
      }
    }
  }
}