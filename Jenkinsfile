pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
      }
    }
    stage('hello') {
      steps {
        sh 'pytest -v -s --alluredir=/Users/user/PycharmProjects/pythonProject5/reports tests/main_page_tests.py'
      }
    }
  }
}