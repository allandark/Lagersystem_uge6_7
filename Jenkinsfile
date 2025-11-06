pipeline {
  
    agent {

        docker {
            image 'specialistdj/jenkins-agent:latest'
            args '-u root -v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

    environment{            
      SQL_DB = credentials('mysql-server')
      JWT_TOKEN = credentials('jwt_secret_token')
      DOCKER_CREDENTIALS = credentials('docker_account')
      PORTAINER = credentials('portainer_account')
      PORTAINER_HOST = "172.20.88.184"
      PORTAINER_PORT = "9000"
      CONTAINER_PORT = "5000"      
      CONTAINER_NAME = "lagersystem"          
    }
    
  


  stages {

    stage('Load Config'){
      steps{        
        sh 'chmod +x ./scripts/*.sh'
        sh './scripts/update_config.sh'      
        sh 'ls -la'   
        script {
 
          // Read and parse the file line by line
          try {
            def envVars = readFile('./globals.env').split('\n')
            envVars.each { line ->
                def parts = line.trim().split('=')
                if (parts.length == 2) {
                    env[parts[0].replaceAll('export ', '')] = parts[1].replaceAll('"', '')
                }
            }
          } catch(Exception e){
            error "globals.env not found or unreadable: ${e.message}"
          }
        }
      }
    }

    stage('Build') {

      steps {
          echo '--- Building docker image ---'
          sh "Version: $VERSION"    
          sh "docker build -t lagersystem:$VERSION ."
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
        // withCredentials([usernamePassword(credentialsId: 'docker_account', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
        //     sh '''
        //         echo "$DOCKER_PASS" | docker login https://registry-1.docker.io/v2/ \
        //         --username="$DOCKER_USER" --password-stdin
                
        //     '''
        //   }
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