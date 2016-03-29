
def buildSingleVersion(version) {
    node {
        sh """
        rm -fr $version
        git clone /home/raptor/projects/germanium $version
        cd $version
        git checkout remotes/origin/$version
        bin/build-docker-instance.sh
        """
    }
}

stage "Build Instances"

parallel python27: {
    buildSingleVersion("python2.7")
}, python34: {
    buildSingleVersion("python3.4")
}, python35: {
    buildSingleVersion("python3.5")
}, failFast: true

stage "Run Tests"

parallel python27: {
    parallel python27Firefox: {
        node {
            sh '''
                docker run --rm \\
                       -e TEST_REUSE_BROWSER=1 \\
                       germanium/germanium-python2.7-tests
            '''
        }
    }, python27Chrome: {
        node {
            sh '''
                docker run --rm \\
                       -e TEST_REUSE_BROWSER=1 \\
                       -e TEST_BROWSER=chrome \\
                       germanium/germanium-python2.7-tests
            '''
        }
    }, failFast: true
}, python34: {
    parallel python34Firefox: {
        node {
            sh '''
                docker run --rm \\
                       -e TEST_REUSE_BROWSER=1 \\
                       germanium/germanium-python3.4-tests
            '''
        }
    }, python34Chrome: {
        node {
            sh '''
                docker run --rm \\
                       -e TEST_REUSE_BROWSER=1 \\
                       -e TEST_BROWSER=chrome \\
                       germanium/germanium-python3.4-tests
            '''
        }
    }, failFast: true
}, python35: {
    parallel python35Firefox: {
        node {
            sh '''
                docker run --rm \\
                       -e TEST_REUSE_BROWSER=1 \\
                       germanium/germanium-python3.5-tests
            '''
        }
    }, python35Chrome: {
        node {
            sh '''
                docker run --rm \\
                       -e TEST_REUSE_BROWSER=1 \\
                       -e TEST_BROWSER=chrome \\
                       germanium/germanium-python3.5-tests
            '''
        }
    }, failFast: true
}, failFast: true

stage "Publish on PyPI"

node {
    sh '''
        ls
    '''
}
