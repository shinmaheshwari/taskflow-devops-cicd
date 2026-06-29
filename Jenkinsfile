pipeline {

    agent any

    environment {
        VENV = "venv"
    }

    stages {

        stage('Build') {

            steps {

                sh '''
                    python3 -m venv $VENV
                    . $VENV/bin/activate

                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {

            steps {

                sh '''
                    . $VENV/bin/activate

                    pytest
                '''
            }
        }

        stage('Deploy') {

            steps {

                sh '''
                    echo "Deploying Application"

                    pkill -f app.py || true

                    nohup python app.py > app.log 2>&1 &

                    echo "Deployment Complete"
                '''
            }
        }
    }

    post {

        success {

            emailext(
                subject: "SUCCESS Build ${BUILD_NUMBER}",
                body: "TaskFlow deployment succeeded",
                to: "shagunmaheshwariitmec@gmail.com"
            )
        }

        failure {

            emailext(
                subject: "FAILED Build ${BUILD_NUMBER}",
                body: "Pipeline failed",
                to: "shagunmaheshwariitmec@gmail.com"
            )
        }
    }
}
