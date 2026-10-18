/*
 * SCENARIO 3 – Project hosted on GITHUB
 * ----------------------------------------
 * Pre-requisites:
 *   1. Push this folder to GitHub (replace <your-username> below).
 *   2. Jenkinsfile must be in the root of the GitHub repo.
 *
 * Setup in Jenkins UI:
 *   - Manage Jenkins → Plugins → install: Git plugin, Pipeline plugin
 *   - New Item → Pipeline → Pipeline Definition: "Pipeline Script from SCM"
 *       SCM            : Git
 *       Repository URL : https://github.com/<your-username>/demo_project.git
 *       Credentials    : Add GitHub PAT if repo is private
 *       Branch         : * /main
 *       Script Path    : Jenkinsfile
 *
 * Trigger options (choose one):
 *   A. "GitHub hook trigger for GITScm polling"  → GitHub webhook (instant)
 *        GitHub repo → Settings → Webhooks → Add webhook
 *        Payload URL : http://<your-jenkins-host>:8080/github-webhook/
 *        Content type: application/json
 *        Events      : Just the push event
 *
 *   B. "Poll SCM"  → periodic polling (no public URL needed)
 *        Schedule: H/5 * * * *
 *
 * NOTE:
 *   - "agent any" is safe here because GitHub checkout doesn't rely on
 *     a local drive path.
 */

pipeline {

    agent any

    stages {

        // Checkout Code
        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/SarthNarola/scenario3_github.git'
                    // For a private repo, add:
                    // credentialsId: 'github-pat-credential-id'
            }
        }

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
                bat 'docker-compose up -d'
            }
        }

        // Run Tests
        stage('Run Tests') {
            steps {
                bat 'docker exec cntwebapp pytest test_sample.py -v'
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
