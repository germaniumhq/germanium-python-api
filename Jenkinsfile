properties([
    parameters([
        booleanParam(name: 'PYTHON_27', defaultValue: true,
                description: 'Run Python 2.7 tests.'),
        booleanParam(name: 'PYTHON_34', defaultValue: true,
                description: 'Run Python 3.4 tests'),
        booleanParam(name: 'PYTHON_35', defaultValue: true,
                description: 'Run Python 3.5 tests'),

        booleanParam(name: 'RUN_FIREFOX_TESTS', defaultValue: true,
                description: 'Run the tests against Firefox'),
        booleanParam(name: 'RUN_CHROME_TESTS', defaultValue: true,
                description: 'Run the tests against Chrome'),
        booleanParam(name: 'RUN_IE8_TESTS', defaultValue: true,
                description: 'Run the tests against IE8'),
        booleanParam(name: 'RUN_IE9_TESTS', defaultValue: true,
                description: 'Run the tests against IE9'),
        booleanParam(name: 'RUN_IE11_TESTS', defaultValue: true,
                description: 'Run the tests against IE11'),
        booleanParam(name: 'RUN_EDGE_TESTS', defaultValue: true,
                description: 'Run the tests against Edge'),

        booleanParam(name: 'RUN_CHROME_LOCAL_TESTS', defaultValue: true,
                description: 'Run the tests on a local Chrome instance.'),
        booleanParam(name: 'RUN_FIREFOX_LOCAL_TESTS', defaultValue: true,
                description: 'Run the tests on a local Firefox instance.'),

        string(name: 'GIT_SERVER', defaultValue: 'http://192.168.0.2:10080/germanium/germanium.git',
                description: 'Git Server location for the project.'),

        string(name: 'GERMANIUM_HUB_URL', defaultValue: 'http://192.168.0.2:4444/wd/hub',
                description: 'Where is the Germanium HUB running.'),

        string(name: 'PYPI_URL', defaultValue: 'http://192.168.0.2:8081/repository/pypi-local/pypi',
                description: 'PyPI Location'),
        string(name: 'PYPI_INDEX_URL', defaultValue: 'http://192.168.0.2:8081/repository/pypi-local/simple',
                description: 'Squid proxy to use for fetching resources'),

        string(name: 'TEST_HOST', defaultValue: '192.168.0.2',
                description: 'On what host are the tests exposed.')
    ])
])

PYTHON_27 = Boolean.valueOf(PYTHON_27)
PYTHON_34 = Boolean.valueOf(PYTHON_34)
PYTHON_35 = Boolean.valueOf(PYTHON_35)

RUN_FIREFOX_TESTS = Boolean.valueOf(RUN_FIREFOX_TESTS)
RUN_CHROME_TESTS = Boolean.valueOf(RUN_CHROME_TESTS)
RUN_IE8_TESTS = Boolean.valueOf(RUN_IE8_TESTS)
RUN_IE9_TESTS = Boolean.valueOf(RUN_IE9_TESTS)
RUN_IE11_TESTS = Boolean.valueOf(RUN_IE11_TESTS)
RUN_EDGE_TESTS = Boolean.valueOf(RUN_EDGE_TESTS)

RUN_CHROME_LOCAL_TESTS = Boolean.valueOf(RUN_CHROME_LOCAL_TESTS)
RUN_FIREFOX_LOCAL_TESTS = Boolean.valueOf(RUN_FIREFOX_LOCAL_TESTS)

CHROME_GERMANIUM_URL = "chrome:${GERMANIUM_HUB_URL}"
FIREFOX_GERMANIUM_URL = "firefox:${GERMANIUM_HUB_URL}"
//IE_GERMANIUM_URL = "ie:${GERMANIUM_HUB_URL}"
IE8_GERMANIUM_URL = "ie?wdurl=${GERMANIUM_HUB_URL}&version=8"
IE9_GERMANIUM_URL = "ie?wdurl=${GERMANIUM_HUB_URL}&version=9"
IE11_GERMANIUM_URL = "ie?wdurl=${GERMANIUM_HUB_URL}&version=11"
EDGE_GERMANIUM_URL = "'edge:${GERMANIUM_HUB_URL}'"

// Ports that will be used in parallel, since we have the same
// test host (the docker instance)

TEST_HOST_IE8_PORT=8008     // 8008:8000 -> IE 8
TEST_HOST_IE9_PORT=8009     // 8009:8000 -> IE 9
TEST_HOST_IE11_PORT=8011     // 8011:8000 -> IE 11
TEST_HOST_EDGE_PORT=8012     // 8012:8000 -> Edge
TEST_HOST_CHROME_PORT=8020   // 8011:8000 -> Chrome
TEST_HOST_FIREFOX_PORT=8021  // 8011:8000 -> Firefox

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

stage('Build Instances') {
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
}

stage('Run Python 3.5 Tests') {
    if (PYTHON_35) {
        def parallelPython35 = [:]

        if (RUN_FIREFOX_TESTS) {
            parallelPython35."Firefox (GRID)" = {
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
        }

        if (RUN_CHROME_TESTS) {
            parallelPython35."Chrome (GRID)" = {
                node {
                    dockerRun image: 'germanium/germanium-python3.5-tests',
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
        }

        if (RUN_IE8_TESTS) {
            parallelPython35."IE8 (GRID)" = {
                node {
                    dockerRun image: 'germanium/germanium-python3.5-tests',
                        remove: true,
                        env: [
                            'TEST_REUSE_BROWSER=1',
                            'RUN_VNC_SERVER=0',
                            "TEST_HOST=$TEST_HOST:$TEST_HOST_IE8_PORT",
                            "TEST_BROWSER=$IE8_GERMANIUM_URL",
                            "EXTRA_BEHAVE_ARGUMENTS=--tags ~noie8"
                        ],
                        ports: [
                            "$TEST_HOST_IE8_PORT:8000"
                        ]
                }
            }
        }

        if (RUN_IE9_TESTS) {
            parallelPython35."IE9 (GRID)" = {
                node {
                    dockerRun image: 'germanium/germanium-python3.5-tests',
                        remove: true,
                        env: [
                            'TEST_REUSE_BROWSER=1',
                            'RUN_VNC_SERVER=0',
                            "TEST_HOST=$TEST_HOST:$TEST_HOST_IE9_PORT",
                            "TEST_BROWSER=$IE9_GERMANIUM_URL",
                            "EXTRA_BEHAVE_ARGUMENTS=--tags ~noie9"
                        ],
                        ports: [
                            "$TEST_HOST_IE9_PORT:8000"
                        ]
                }
            }
        }

        if (RUN_IE11_TESTS) {
            parallelPython35."IE11 (GRID)" = {
                node {
                    dockerRun image: 'germanium/germanium-python3.5-tests',
                        remove: true,
                        env: [
                            'TEST_REUSE_BROWSER=1',
                            'RUN_VNC_SERVER=0',
                            "TEST_HOST=$TEST_HOST:$TEST_HOST_IE11_PORT",
                            "TEST_BROWSER=$IE11_GERMANIUM_URL"
                        ],
                        ports: [
                            "$TEST_HOST_IE11_PORT:8000"
                        ]
                }
            }
        }

        if (RUN_EDGE_TESTS) {
            parallelPython35."Edge (GRID)" = {
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
        }

        if (RUN_CHROME_LOCAL_TESTS) {
            parallelPython35."Chrome (Local)" = {
                node {
                    dockerRun image: 'germanium/germanium-python3.5-tests',
                        remove: true,
                        privileged: true,
                        env: [
                            'TEST_REUSE_BROWSER=1',
                            'RUN_VNC_SERVER=1',
                            'TEST_BROWSER=chrome'
                        ],
                        ports: [
                            "25901:5901"
                        ]
                }
            }
        }

        if (RUN_FIREFOX_LOCAL_TESTS) {
            parallelPython35."Firefox (Local)" = {
                node {
                    dockerRun image: 'germanium/germanium-python3.5-tests',
                        remove: true,
                        env: [
                            'TEST_REUSE_BROWSER=1',
                            'RUN_VNC_SERVER=1',
                            'TEST_BROWSER=firefox'
                        ],
                        ports: [
                            "25902:5901"
                        ]
                }
            }
        }

        parallel(parallelPython35)
    }
}

stage('Run Python 2.7 Tests') {
    if (PYTHON_27) {
        def parallelPython27 = [:]

        if (RUN_FIREFOX_TESTS) {
            parallelPython27."Firefox (GRID)" = {
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
        }

        if (RUN_CHROME_TESTS) {
            parallelPython27."Chrome (GRID)" = {
                node {
                    dockerRun image: 'germanium/germanium-python2.7-tests',
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
        }

        if (RUN_IE8_TESTS) {
            parallelPython27."IE8 (GRID)" = {
                node {
                    dockerRun image: 'germanium/germanium-python2.7-tests',
                        remove: true,
                        env: [
                            'TEST_REUSE_BROWSER=1',
                            'RUN_VNC_SERVER=0',
                            "TEST_HOST=$TEST_HOST:$TEST_HOST_IE8_PORT",
                            "TEST_BROWSER=$IE8_GERMANIUM_URL",
                            "EXTRA_BEHAVE_ARGUMENTS=--tags ~noie8"
                        ],
                        ports: [
                            "$TEST_HOST_IE8_PORT:8000"
                        ]
                }
            }
        }

        if (RUN_IE9_TESTS) {
            parallelPython27."IE9 (GRID)" = {
                node {
                    dockerRun image: 'germanium/germanium-python2.7-tests',
                        remove: true,
                        env: [
                            'TEST_REUSE_BROWSER=1',
                            'RUN_VNC_SERVER=0',
                            "TEST_HOST=$TEST_HOST:$TEST_HOST_IE9_PORT",
                            "TEST_BROWSER=$IE9_GERMANIUM_URL",
                            "EXTRA_BEHAVE_ARGUMENTS=--tags ~noie9"
                        ],
                        ports: [
                            "$TEST_HOST_IE9_PORT:8000"
                        ]
                }
            }
        }

        if (RUN_IE11_TESTS) {
            parallelPython27."IE11 (GRID)" = {
                node {
                    dockerRun image: 'germanium/germanium-python2.7-tests',
                        remove: true,
                        env: [
                            'TEST_REUSE_BROWSER=1',
                            'RUN_VNC_SERVER=0',
                            "TEST_HOST=$TEST_HOST:$TEST_HOST_IE11_PORT",
                            "TEST_BROWSER=$IE11_GERMANIUM_URL"
                        ],
                        ports: [
                            "$TEST_HOST_IE11_PORT:8000"
                        ]
                }
            }
        }

        if (RUN_EDGE_TESTS) {
            parallelPython27."Edge (GRID)" = {
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
        }

        if (RUN_CHROME_LOCAL_TESTS) {
            parallelPython27."Chrome (Local)" = {
                node {
                    dockerRun image: 'germanium/germanium-python2.7-tests',
                        remove: true,
                        privileged: true,
                        env: [
                            'TEST_REUSE_BROWSER=1',
                            'RUN_VNC_SERVER=1',
                            'TEST_BROWSER=chrome'
                        ],
                        ports: [
                            "25901:5901"
                        ]
                }
            }
        }

        if (RUN_FIREFOX_LOCAL_TESTS) {
            parallelPython27."Firefox (Local)" = {
                node {
                    dockerRun image: 'germanium/germanium-python2.7-tests',
                        remove: true,
                        env: [
                            'TEST_REUSE_BROWSER=1',
                            'RUN_VNC_SERVER=1',
                            'TEST_BROWSER=firefox'
                        ],
                        ports: [
                            "25902:5901"
                        ]
                }
            }
        }

        parallel(parallelPython27)
    }
}

stage('Run Python 3.4 Tests') {
    if (PYTHON_34) {
        def parallelPython34 = [:]

        if (RUN_FIREFOX_TESTS) {
            parallelPython34."Firefox (GRID)" = {
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
        }

        if (RUN_CHROME_TESTS) {
            parallelPython34."Chrome (GRID)" = {
                node {
                    dockerRun image: 'germanium/germanium-python3.4-tests',
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
        }

        if (RUN_IE8_TESTS) {
            parallelPython34."IE8 (GRID)" = {
                node {
                    dockerRun image: 'germanium/germanium-python3.4-tests',
                        remove: true,
                        env: [
                            'TEST_REUSE_BROWSER=1',
                            'RUN_VNC_SERVER=0',
                            "TEST_HOST=$TEST_HOST:$TEST_HOST_IE8_PORT",
                            "TEST_BROWSER=$IE8_GERMANIUM_URL",
                            "EXTRA_BEHAVE_ARGUMENTS=--tags ~noie8"
                        ],
                        ports: [
                            "$TEST_HOST_IE8_PORT:8000"
                        ]
                }
            }
        }

        if (RUN_IE9_TESTS) {
            parallelPython34."IE9 (GRID)" = {
                node {
                    dockerRun image: 'germanium/germanium-python3.4-tests',
                        remove: true,
                        env: [
                            'TEST_REUSE_BROWSER=1',
                            'RUN_VNC_SERVER=0',
                            "TEST_HOST=$TEST_HOST:$TEST_HOST_IE9_PORT",
                            "TEST_BROWSER=$IE9_GERMANIUM_URL",
                            "EXTRA_BEHAVE_ARGUMENTS=--tags ~noie9"
                        ],
                        ports: [
                            "$TEST_HOST_IE9_PORT:8000"
                        ]
                }
            }
        }

        if (RUN_IE11_TESTS) {
            parallelPython34."IE11 (GRID)" = {
                node {
                    dockerRun image: 'germanium/germanium-python3.4-tests',
                        remove: true,
                        env: [
                            'TEST_REUSE_BROWSER=1',
                            'RUN_VNC_SERVER=0',
                            "TEST_HOST=$TEST_HOST:$TEST_HOST_IE11_PORT",
                            "TEST_BROWSER=$IE11_GERMANIUM_URL"
                        ],
                        ports: [
                            "$TEST_HOST_IE11_PORT:8000"
                        ]
                }
            }
        }

        if (RUN_EDGE_TESTS) {
            parallelPython34."Edge (GRID)" = {
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
        }

        if (RUN_CHROME_LOCAL_TESTS) {
            parallelPython34."Chrome (Local)" = {
                node {
                    dockerRun image: 'germanium/germanium-python3.4-tests',
                        remove: true,
                        privileged: true,
                        env: [
                            'TEST_REUSE_BROWSER=1',
                            'RUN_VNC_SERVER=1',
                            'TEST_BROWSER=chrome'
                        ],
                        ports: [
                            "25901:5901"
                        ]
                }
            }
        }

        if (RUN_FIREFOX_LOCAL_TESTS) {
            parallelPython34."Firefox (Local)" = {
                node {
                    dockerRun image: 'germanium/germanium-python3.4-tests',
                        remove: true,
                        env: [
                            'TEST_REUSE_BROWSER=1',
                            'RUN_VNC_SERVER=1',
                            'TEST_BROWSER=firefox'
                        ],
                        ports: [
                            "25902:5901"
                        ]
                }
            }
        }

        parallel(parallelPython34)
    }
}
