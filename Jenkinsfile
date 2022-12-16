pipeline {
  agent {
      docker { image '3.10.9-slim-buster' }
  }
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