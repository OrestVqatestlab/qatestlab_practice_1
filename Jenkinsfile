pipeline {
  agent {
    docker {
        label 'docker'
        image 'python:3.7'
    }
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