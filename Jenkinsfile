properties([
    parameters([
        booleanParam(name: 'PYTHON_27',
                defaultValue: true,
                description: 'Run Python 2.7 tests.'),
        booleanParam(name: 'PYTHON_34',
                defaultValue: true,
                description: 'Run Python 3.4 tests'),
        booleanParam(name: 'PYTHON_35',
                defaultValue: true,
                description: 'Run Python 3.5 tests'),

        booleanParam(name: 'RUN_FIREFOX_TESTS',
                defaultValue: true,
                description: 'Run the tests against Firefox'),
        booleanParam(name: 'RUN_CHROME_TESTS',
                defaultValue: true,
                description: 'Run the tests against Chrome'),
        booleanParam(name: 'RUN_IE_TESTS',
                defaultValue: true,
                description: 'Run the tests against IE'),
        booleanParam(name: 'RUN_EDGE_TESTS',
                defaultValue: true,
                description: 'Run the tests against Edge'),

        string(name: 'GIT_SERVER',
                defaultValue: 'http://192.168.0.2:10080/germanium/germanium.git',
                description: 'Git Server location for the project.'),

        string(name: 'GERMANIUM_HUB_URL',
                defaultValue: 'http://192.168.0.2:4444/wd/hub',
                description: 'Where is the Germanium HUB running.'),

        string(name: 'PYPI_URL',
                defaultValue: 'http://192.168.0.2:8081/repository/pypi-local/pypi',
                description: 'PyPI Location'),
        string(name: 'PYPI_INDEX_URL',
                defaultValue: 'http://192.168.0.2:8081/repository/pypi-local/simple',
                description: 'Squid proxy to use for fetching resources'),

        string(name: 'TEST_HOST',
                defaultValue: '192.168.0.2',
                description: 'On what host are the tests exposed.')
    ])
])

CHROME_GERMANIUM_URL = "chrome:${GERMANIUM_HUB_URL}"
FIREFOX_GERMANIUM_URL = "firefox:${GERMANIUM_HUB_URL}"
IE_GERMANIUM_URL = "ie:${GERMANIUM_HUB_URL}"
EDGE_GERMANIUM_URL = "edge:${GERMANIUM_HUB_URL}"

// Ports that will be used in parallel, since we have the same
// test host (the docker instance)

TEST_HOST_CHROME_PORT=8011   // 8011:8000 -> Chrome
TEST_HOST_FIREFOX_PORT=8012  // 8011:8000 -> Chrome
TEST_HOST_IE11_PORT=8013     // 8011:8000 -> IE 11
TEST_HOST_EDGE_PORT=8014     // 8012:8000 -> Edge

def buildSingleVersion(version) {
    node {
        sh """
        echo "Setting PYPI_URL as $PYPI_URL"
        echo "Setting PYPI_INDEX_URL as $PYPI_INDEX_URL"

        echo "Cloning from $GIT_SERVER"
        rm -fr $version
        git clone "$GIT_SERVER" $version
        pwd
        ls -la
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
                dockerRun image: 'germanium/germanium-python3.5-tests',
                    remove: true,
                    env: [
                        'TEST_REUSE_BROWSER=1',
                        'RUN_VNC_SERVER=0',
                        "TEST_HOST=$TEST_HOST:$TEST_HOST_FIREFOX_PORT",
                        "TEST_BROWSER=$FIREFOX_GERMANIUM_URL"
                    ],
                    ports: [
                        "$TEST_HOST_FIREFOX_PORT:8000"
                    ]
            }
        }
    }, python35Chrome: {
        if (RUN_CHROME_TESTS) {
            node {
                dockerRun image: 'germanium/germanium-pyton3.5-tests',
                    remove: true,
                    env: [
                        'TEST_REUSE_BROWSER=1',
                        'RUN_VNC_SERVER=0',
                        "TEST_HOST=$TEST_HOST:$TEST_HOST_CHROME_PORT",
                        "TEST_BROWSER=$CHROME_GERMANIUM_URL"
                    ],
                    ports: [
                        "$TEST_HOST_CHROME_PORT:8000"
                    ]
            }
        }
    }, python35Ie8: {
        if (RUN_IE_TESTS) {
            node {
                dockerRun image: 'germanium/germanium-python3.5-tests',
                    remove: true,
                    env: [
                        'TEST_REUSE_BROWSER=1',
                        'RUN_VNC_SERVER=0',
                        "TEST_HOST=$TEST_HOST:$TEST_HOST_IE11_PORT",
                        "TEST_BROWSER=$IE_GERMANIUM_URL"
                    ],
                    ports: [
                        "$TEST_HOST_IE11_PORT:8000"
                    ]
            }
        }
    }, python35Edge: {
        if (RUN_EDGE_TESTS) {
            node {
                dockerRun image: 'germanium/germanium-python3.5-tests',
                    remove: true,
                    env: [
                        'TEST_REUSE_BROWSER=1',
                        'RUN_VNC_SERVER=0',
                        "TEST_HOST=$TEST_HOST:$TEST_HOST_EDGE_PORT",
                        "TEST_BROWSER=$EDGE_GERMANIUM_URL"
                    ],
                    ports: [
                        "$TEST_HOST_EDGE_PORT:8000"
                    ]
            }
        }
    }, failFast: false
}

stage "Run Python 2.7 Tests"

if (PYTHON_27) {
    parallel python27Firefox: {
        if (RUN_FIREFOX_TESTS) {
            node {
                dockerRun image: 'germanium/germanium-python2.7-tests',
                    remove: true,
                    env: [
                        'TEST_REUSE_BROWSER=1',
                        'RUN_VNC_SERVER=0',
                        "TEST_HOST=$TEST_HOST:$TEST_HOST_FIREFOX_PORT",
                        "TEST_BROWSER=$FIREFOX_GERMANIUM_URL"
                    ],
                    ports: [
                        "$TEST_HOST_FIREFOX_PORT:8000"
                    ]
            }
        }
    }, python27Chrome: {
        if (RUN_CHROME_TESTS) {
            node {
                dockerRun image: 'germanium/germanium-pyton2.7-tests',
                    remove: true,
                    env: [
                        'TEST_REUSE_BROWSER=1',
                        'RUN_VNC_SERVER=0',
                        "TEST_HOST=$TEST_HOST:$TEST_HOST_CHROME_PORT",
                        "TEST_BROWSER=$CHROME_GERMANIUM_URL"
                    ],
                    ports: [
                        "$TEST_HOST_CHROME_PORT:8000"
                    ]
            }
        }
    }, python27Ie8: {
        if (RUN_IE_TESTS) {
            node {
                dockerRun image: 'germanium/germanium-python2.7-tests',
                    remove: true,
                    env: [
                        'TEST_REUSE_BROWSER=1',
                        'RUN_VNC_SERVER=0',
                        "TEST_HOST=$TEST_HOST:$TEST_HOST_IE11_PORT",
                        "TEST_BROWSER=$IE_GERMANIUM_URL"
                    ],
                    ports: [
                        "$TEST_HOST_IE11_PORT:8000"
                    ]
            }
        }
    }, python27Edge: {
        if (RUN_EDGE_TESTS) {
            node {
                dockerRun image: 'germanium/germanium-python2.7-tests',
                    remove: true,
                    env: [
                        'TEST_REUSE_BROWSER=1',
                        'RUN_VNC_SERVER=0',
                        "TEST_HOST=$TEST_HOST:$TEST_HOST_EDGE_PORT",
                        "TEST_BROWSER=$EDGE_GERMANIUM_URL"
                    ],
                    ports: [
                        "$TEST_HOST_EDGE_PORT:8000"
                    ]
            }
        }
    }, failFast: false
}

stage "Run Python 3.4 Tests"

if (PYTHON_34) {
    parallel python34Firefox: {
        if (RUN_FIREFOX_TESTS) {
            node {
                dockerRun image: 'germanium/germanium-python3.4-tests',
                    remove: true,
                    env: [
                        'TEST_REUSE_BROWSER=1',
                        'RUN_VNC_SERVER=0',
                        "TEST_HOST=$TEST_HOST:$TEST_HOST_FIREFOX_PORT",
                        "TEST_BROWSER=$FIREFOX_GERMANIUM_URL"
                    ],
                    ports: [
                        "$TEST_HOST_FIREFOX_PORT:8000"
                    ]
            }
        }
    }, python34Chrome: {
        if (RUN_CHROME_TESTS) {
            node {
                dockerRun image: 'germanium/germanium-pyton3.4-tests',
                    remove: true,
                    env: [
                        'TEST_REUSE_BROWSER=1',
                        'RUN_VNC_SERVER=0',
                        "TEST_HOST=$TEST_HOST:$TEST_HOST_CHROME_PORT",
                        "TEST_BROWSER=$CHROME_GERMANIUM_URL"
                    ],
                    ports: [
                        "$TEST_HOST_CHROME_PORT:8000"
                    ]
            }
        }
    }, python34Ie8: {
        if (RUN_IE_TESTS) {
            node {
                dockerRun image: 'germanium/germanium-python3.4-tests',
                    remove: true,
                    env: [
                        'TEST_REUSE_BROWSER=1',
                        'RUN_VNC_SERVER=0',
                        "TEST_HOST=$TEST_HOST:$TEST_HOST_IE11_PORT",
                        "TEST_BROWSER=$IE_GERMANIUM_URL"
                    ],
                    ports: [
                        "$TEST_HOST_IE11_PORT:8000"
                    ]
            }
        }
    }, python34Edge: {
        if (RUN_EDGE_TESTS) {
            node {
                dockerRun image: 'germanium/germanium-python3.4-tests',
                    remove: true,
                    env: [
                        'TEST_REUSE_BROWSER=1',
                        'RUN_VNC_SERVER=0',
                        "TEST_HOST=$TEST_HOST:$TEST_HOST_EDGE_PORT",
                        "TEST_BROWSER=$EDGE_GERMANIUM_URL"
                    ],
                    ports: [
                        "$TEST_HOST_EDGE_PORT:8000"
                    ]
            }
        }
    }, failFast: false
}

