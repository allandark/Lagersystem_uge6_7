pipeline {
  
    agent {

        docker {
            image 'docker:latest'
            args '-v /var/run/docker.sock:/var/run/docker.sock --entrypoint=""'
        }

    }

    environment{            
      SQL_DB = credentials('mysql-server')
      // JWT_TOKEN = credentials('jwt_secret_token')
      // DOCKER_HUB = credentials('docker_account')
      // PORTAINER = credentials('portainer_account')
      PORTAINER_HOST = "172.20.88.184"
      PORTAINER_PORT = "9000"
      CONTAINER_PORT = "5000"      
      CONTAINER_NAME = "lagersystem"
    }
    

  stages {
    stage('Build') {

      steps {
          echo '--- Building docker image ---'          

          sh 'ls -la'
          sh 'docker ps'
          sh '''
          echo "$DOCKER_HUB_PSW" | docker login https://registry-1.docker.io/v2/ --username="$DOCKER_HUB_USR" --password-stdin
          docker build -t lagersystem:latest .
          '''
      }
    }

    stage('Test') {
      steps {
        echo '--- Testing and generating reports ---'
        // dir("${env.WORKSPACE}") {
        //   sh 'pytest tests/unit --junitxml="tests/results/unittest_report.xml"'
        // //   sh '''pytest tests/integration --junitxml="tests/results/integrationtest_report.xml"'''
        //   junit 'tests/results/*.xml'
        // }  
      }
    }
    stage('Deploy'){
      steps {
        echo '--- Deploying docker container to portainer ---'
        // sh '''
        // docker tag lagersystem $DOCKER_HUB_USER/lagersystem
        // docker push $DOCKER_HUB_USER/lagersystem
        // ./scripts/create_container.sh
        // '''
      }
    }

  }

  post {
    always {
      echo '--- Archiving artifacts ---'
      // archiveArtifacts artifacts: 'tests/results/*.xml', fingerprint: true
      
      echo 'Cleaning up test cache...'
      // sh 'rm -rf .pytest_cache'

    }
  }
}