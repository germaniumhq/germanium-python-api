
PYTHON_27 = Boolean.valueOf(PYTHON_27)
PYTHON_34 = Boolean.valueOf(PYTHON_34)
PYTHON_35 = Boolean.valueOf(PYTHON_35)

RUN_FIREFOX_TESTS = Boolean.valueOf(RUN_FIREFOX_TESTS)
RUN_CHROME_TESTS = Boolean.valueOf(RUN_CHROME_TESTS)
RUN_IE_TESTS = Boolean.valueOf(RUN_IE_TESTS)
RUN_EDGE_TESTS = Boolean.valueOf(RUN_EDGE_TESTS)

//GERMANIUM_HUB_URL = "http://192.168.0.6:4444/wd/hub
IE_GERMANIUM_URL = "ie:${GERMANIUM_HUB_URL}"
EDGE_GERMANIUM_URL = "edge:${GERMANIUM_HUB_URL}"

// PYPI_URL - the URL to use for PYPI
// PYPI_INDEX_URL - the index URL to use for PYPI

// GIT_SERVER - the URL of the git server

// TEST_HOST = "192.168.0.6"  # where are the tests running.
// Ports that will be used in parallel, since we have the same
// test host (the docker instance)

TEST_HOST_IE11_PORT=8011  // 8011:8000 -> IE 11
TEST_HOST_EDGE_PORT=8012  // 8012:8000 -> Edge

def buildSingleVersion(version) {
    node {
        sh """
        echo "Setting PYPI_URL as $PYPI_URL"
        echo "Setting PYPI_INDEX_URL as $PYPI_INDEX_URL"

        echo "Cloning from $GIT_SERVER"
        rm -fr $version
        git clone "$GIT_SERVER" $version
        cd $version
        git checkout remotes/origin/$version
        bin/build-docker-instance.sh "$PYPI_URL" "$PYPI_INDEX_URL"
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
                           --security-opt seccomp:test/docker/chrome.json \\
                           germanium/germanium-python3.5-tests
                '''
            }
        }
    }, python35Ie8: {
        if (RUN_IE_TESTS) {
            node {
                sh """
                    docker run --rm \\
                           -e TEST_REUSE_BROWSER=1 \\
                           -e RUN_VNC_SERVER=0 \\
                           -p $TEST_HOST_IE11_PORT:8000 \\
                           -e TEST_HOST=$TEST_HOST:$TEST_HOST_IE11_PORT \\
                           -e TEST_BROWSER=$IE_GERMANIUM_URL \\
                           germanium/germanium-python3.5-tests
                """
            }
        }
    }, python35Edge: {
        if (RUN_EDGE_TESTS) {
            node {
                sh """
                    docker run --rm \\
                           -e TEST_REUSE_BROWSER=1 \\
                           -e RUN_VNC_SERVER=0 \\
                           -p $TEST_HOST_EDGE_PORT:8000 \\
                           -e TEST_HOST=$TEST_HOST:$TEST_HOST_EDGE_PORT \\
                           -e TEST_BROWSER=$EDGE_GERMANIUM_URL \\
                           germanium/germanium-python3.5-tests
                """
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
                           --security-opt seccomp:test/docker/chrome.json \\
                           germanium/germanium-python2.7-tests
                '''
            }
        }
    }, python27Ie8: {
        if (RUN_IE_TESTS) {
            node {
                sh """
                    docker run --rm \\
                           -e TEST_REUSE_BROWSER=1 \\
                           -e RUN_VNC_SERVER=0 \\
                           -p $TEST_HOST_IE11_PORT:8000 \\
                           -e TEST_HOST=$TEST_HOST:$TEST_HOST_IE11_PORT \\
                           -e TEST_BROWSER=$IE_GERMANIUM_URL \\
                           germanium/germanium-python2.7-tests
                """
            }
        }
    }, python27Edge: {
        if (RUN_EDGE_TESTS) {
            node {
                sh """
                    docker run --rm \\
                           -e TEST_REUSE_BROWSER=1 \\
                           -e RUN_VNC_SERVER=0 \\
                           -p $TEST_HOST_EDGE_PORT:8000 \\
                           -e TEST_HOST=$TEST_HOST:$TEST_HOST_EDGE_PORT \\
                           -e TEST_BROWSER=$EDGE_GERMANIUM_URL \\
                           germanium/germanium-python2.7-tests
                """
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
                           --security-opt seccomp:test/docker/chrome.json \\
                           germanium/germanium-python3.4-tests
                '''
            }
        }
    }, python34Ie8: {
        if (RUN_IE_TESTS) {
            node {
                sh """
                    docker run --rm \\
                           -e TEST_REUSE_BROWSER=1 \\
                           -e RUN_VNC_SERVER=0 \\
                           -p $TEST_HOST_IE11_PORT:8000 \\
                           -e TEST_HOST=$TEST_HOST:$TEST_HOST_IE11_PORT \\
                           -e TEST_BROWSER=$IE_GERMANIUM_URL \\
                           germanium/germanium-python3.4-tests
                """
            }
        }
    }, python34Edge: {
        if (RUN_EDGE_TESTS) {
            node {
                sh """
                    docker run --rm \\
                           -e TEST_REUSE_BROWSER=1 \\
                           -e RUN_VNC_SERVER=0 \\
                           -p $TEST_HOST_EDGE_PORT:8000 \\
                           -e TEST_HOST=$TEST_HOST:$TEST_HOST_EDGE_PORT \\
                           -e TEST_BROWSER=$EDGE_GERMANIUM_URL \\
                           germanium/germanium-python3.4-tests
                """
            }
        }
    }, failFast: false
}
