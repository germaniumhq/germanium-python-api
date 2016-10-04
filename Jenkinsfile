
PYTHON_27 = Boolean.valueOf(PYTHON_27)
PYTHON_34 = Boolean.valueOf(PYTHON_34)
PYTHON_35 = Boolean.valueOf(PYTHON_35)

RUN_FIREFOX_TESTS = Boolean.valueOf(RUN_FIREFOX_TESTS)
RUN_CHROME_TESTS = Boolean.valueOf(RUN_CHROME_TESTS)
RUN_IE_TESTS = Boolean.valueOf(RUN_IE_TESTS)

// GIT_SERVER

def buildSingleVersion(version) {
    node {
        sh """
        rm -fr $version
        git clone $GIT_SERVER $version
        cd $version
        git checkout remotes/origin/$version
        bin/build-docker-instance.sh
        """
    }
}

stage "Build Instances"

parallel python27: {
    if (PYTHON_27) {
        buildSingleVersion("python2.7")
    }
}, python34: {
    if (PYTHON_34) {
        buildSingleVersion("python3.4")
    }
}, python35: {
    if (PYTHON_35) {
        buildSingleVersion("python3.5")
    }
}, failFast: true

stage "Run Python 3.5 Tests"

if (PYTHON_35) {
    parallel python35Firefox: {
        if (RUN_FIREFOX_TESTS) {
            node {
                sh '''
                    docker run --rm \\
                           -e TEST_REUSE_BROWSER=1 \\
                           germanium/germanium-python3.5-tests
                '''
            }
        }
    }, python35Chrome: {
        if (RUN_CHROME_TESTS) {
            node {
                sh '''
                    docker run --rm \\
                           -e TEST_REUSE_BROWSER=1 \\
                           -e TEST_BROWSER=chrome \\
                           --security-opt seccomp:/home/raptor/projects/germanium/test/docker/chrome.json \\
                           germanium/germanium-python3.5-tests
                '''
            }
        }
    }, python35Ie8: {
        if (RUN_IE_TESTS) {
            node {
                sh '''
                    docker run --rm \\
                           -e TEST_REUSE_BROWSER=1 \\
                           -e RUN_VNC_SERVER=0 \\
                           -p 8008:8000 \\
                           -e TEST_HOST=192.168.0.23:8008 \\
                           -e TEST_BROWSER=ie:http://192.168.0.25:5555/ \\
                           germanium/germanium-python3.5-tests
                '''
            }
        }
    }, failFast: false
}

stage "Run Python 2.7 Tests"

if (PYTHON_27) {
    parallel python27Firefox: {
        if (RUN_FIREFOX_TESTS) {
            node {
                sh '''
                    docker run --rm \\
                           -e TEST_REUSE_BROWSER=1 \\
                           germanium/germanium-python2.7-tests
                '''
            }
        }
    }, python27Chrome: {
        if (RUN_CHROME_TESTS) {
            node {
                sh '''
                    docker run --rm \\
                           -e TEST_REUSE_BROWSER=1 \\
                           -e TEST_BROWSER=chrome \\
                           --security-opt seccomp:/home/raptor/projects/germanium/test/docker/chrome.json \\
                           germanium/germanium-python2.7-tests
                '''
            }
        }
    }, python27Ie8: {
        if (RUN_IE_TESTS) {
            node {
                sh '''
                    docker run --rm \\
                           -e TEST_REUSE_BROWSER=1 \\
                           -e RUN_VNC_SERVER=0 \\
                           -p 8008:8000 \\
                           -e TEST_HOST=192.168.0.23:8008 \\
                           -e TEST_BROWSER=ie:http://192.168.0.25:5555/ \\
                           germanium/germanium-python2.7-tests
                '''
            }
        }
    }, failFast: false
}

stage "Run Python 3.4 Tests"

if (PYTHON_34) {
    parallel python34Firefox: {
        if (RUN_FIREFOX_TESTS) {
            node {
                sh '''
                    docker run --rm \\
                           -e TEST_REUSE_BROWSER=1 \\
                           germanium/germanium-python3.4-tests
                '''
            }
        }
    }, python34Chrome: {
        if (RUN_CHROME_TESTS) {
            node {
                sh '''
                    docker run --rm \\
                           -e TEST_REUSE_BROWSER=1 \\
                           -e TEST_BROWSER=chrome \\
                           --security-opt seccomp:/home/raptor/projects/germanium/test/docker/chrome.json \\
                           germanium/germanium-python3.4-tests
                '''
            }
        }
    }, python34Ie8: {
        if (RUN_IE_TESTS) {
            node {
                sh '''
                    docker run --rm \\
                           -e TEST_REUSE_BROWSER=1 \\
                           -e RUN_VNC_SERVER=0 \\
                           -p 8008:8000 \\
                           -e TEST_HOST=192.168.0.23:8008 \\
                           -e TEST_BROWSER=ie:http://192.168.0.25:5555/ \\
                           germanium/germanium-python3.4-tests
                '''
            }
        }
    }, failFast: false
}
