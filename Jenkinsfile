
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

stage "Run Python 3.5 Tests"

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
}, python35Ie8: {
   node {
       sh '''
           docker run --rm \\
                  -e TEST_REUSE_BROWSER=1 \\
                  -e RUN_VNC_SERVER=0 \\
                  -p 8008:8000 \\
                  -e TEST_HOST=192.168.0.6:8008 \\
                  -e TEST_BROWSER=ie:http://192.168.0.22:5555/ \\
                  germanium/germanium-python3.5-tests
       '''
   }
}, failFast: true

stage "Run Python 2.7 Tests"

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

stage "Run Python 3.4 Tests"

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
