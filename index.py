def notifyLINE(status) {
    def token = "bZKmxmEvpymT9nndjCg5caa3lLkN7iY7UNGV7dwP8u0"
    def jobName = env.JOB_NAME
    def buildNo = env.BUILD_NUMBER
    def url= 'https://notify-api.line.me/api/notify'
    def message = "${jobName} Build #${buildNo} ${status} \r\n"
    sh"curl ${url} -H 'Authorization: Bearer ${token}' -F 'message=${message}'"
}
pipeline {
    agent any
 
    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
                }
            }
        }
    post{
        success{
        notifyLINE("success")
    }
    failure{
        notifyLINE("failde")
        }
    }
}
