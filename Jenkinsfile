pipeline {
  agent any
  stages {
    stage('venv') {
      steps {
        sh 'pytest -v -s tests/'
      }
    }

  }
}