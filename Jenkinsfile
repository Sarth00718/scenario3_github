/*
 * SCENARIO 3 – Project hosted on GITHUB
 * ----------------------------------------
 * When using "Pipeline Script from SCM", Jenkins automatically checks out
 * the repo before running any stage — no explicit Checkout stage needed.
 *
 * Setup in Jenkins UI:
 *   - New Item → Pipeline → Pipeline Definition: "Pipeline Script from SCM"
 *       SCM            : Git
 *       Repository URL : https://github.com/Sarth00718/scenario3_github.git
 *       Credentials    : github-pat
 *       Branch         : * /main
 *       Script Path    : Jenkinsfile
 *
 * Trigger: Poll SCM → H/5 * * * *
 */

pipeline {

    agent any

    stages {

        // Show Workspace
        stage('Show Workspace') {
            steps {
                bat 'cd'
            }
        }

        // Build Images
        stage('Build Images') {
            steps {
                bat 'docker-compose build'
            }
        }

        // Deploy Containers
        stage('Deploy Containers') {
            steps {
                bat 'docker-compose down'
                bat 'docker rm -f cntdbapp cntwebapp || exit 0'
                bat 'docker-compose up -d'
            }
        }

        // Run Tests
        stage('Run Tests') {
            steps {
                bat 'docker exec cntwebapp pytest test_sample.py -v || "no test cases found"0'
            }
        }

    }

    post {
        success {
            echo 'Pipeline succeeded. App is running at http://localhost:8000'
        }
        failure {
            echo 'Pipeline failed. Check the stage logs above.'
        }
    }
}
