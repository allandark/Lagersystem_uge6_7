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
      DOCKER_HUB_HOST = "docker.io"
    }
    
  
  stages {
    stage('Load Config'){
      steps{        
        sh 'chmod +x ./scripts/*.sh'
        sh './scripts/update_config.sh'              
        script {
          // Read and parse the file line by line
          try {
            def envFilePath = "${env.WORKSPACE}/globals.env"            
            def envVars = readFile(envFilePath).split('\n')             
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
          echo "Version: $VERSION"            
          sh "docker build -t $CONTAINER_NAME:$VERSION ."
      }
    }

    stage('Test') {
      steps {
        echo '--- Testing and generating reports ---'
        sh"docker run --rm -v ./tests/results/ --entrypoint ./scripts/run_tests.sh $CONTAINER_NAME:$VERSION"
        sh"ls -R tests"
        junit 'tests/results/*.xml'

      }
    }

    stage('Deploy'){
      steps {
        echo '--- Deploying docker container to portainer ---'

        sh '''
            set -e            
            echo $DOCKER_CREDENTIALS_PSW | docker login --username="$DOCKER_CREDENTIALS_USR" --password-stdin $DOCKER_HUB_HOST
            docker tag $CONTAINER_NAME:$VERSION $DOCKER_CREDENTIALS_USR/$CONTAINER_NAME:$VERSION
            docker push $DOCKER_HUB_HOST/$DOCKER_CREDENTIALS_USR/$CONTAINER_NAME:$VERSION
        '''

        sh '''
        ./scripts/login_docker.sh
        ./scripts/create_container.sh        
        ./scripts/start_container.sh 
        '''
      }
    }
  }

  post {
    always {
      echo '--- Archiving artifacts ---'
      archiveArtifacts artifacts: 'tests/results/*.xml', fingerprint: true
      
      echo 'Cleaning up test cache...'
      sh 'rm -rf .pytest_cache'

    }
  }
}