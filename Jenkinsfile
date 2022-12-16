pipeline {
  agent any
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