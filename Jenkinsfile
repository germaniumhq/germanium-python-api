properties([
    parameters([
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

        string(name: 'PYPI_URL', defaultValue: 'http://nexus:8081/repository/pypi-local/pypi',
                description: 'PyPI Location'),
        string(name: 'PYPI_INDEX_URL', defaultValue: 'http://nexus:8081/repository/pypi-local/simple',
                description: 'Pypi index URL'),

        string(name: 'GERMANIUM_HUB_URL', defaultValue: 'http://germanium-hub:4444/wd/hub',
                description: 'Where is the Germanium HUB running.'),

        string(name: 'TEST_HOST', defaultValue: '192.168.0.51',
                description: 'On what host are the tests exposed.')
    ])
])

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
IE8_GERMANIUM_URL = "ie?wdurl=${GERMANIUM_HUB_URL}&version=8"
IE9_GERMANIUM_URL = "ie?wdurl=${GERMANIUM_HUB_URL}&version=9"
IE11_GERMANIUM_URL = "ie?wdurl=${GERMANIUM_HUB_URL}&version=11"
EDGE_GERMANIUM_URL = "'edge:${GERMANIUM_HUB_URL}'"

def image_name

stage('Build Germanium Image') {
    node {
        deleteDir()
        checkout scm

        image_name = "germanium_${gitHash()}"

        docker.build(image_name)
    }
}

stage('Test Germanium') {
    def tests = [:]

    if (RUN_CHROME_LOCAL_TESTS) {
        tests."Chrome (Local)" = {
            dockerInside image: image_name,
                privileged: true,
                links: [
                    'vnc-server:vnc'
                ],
                volumes: [
                    '/dev/shm:/dev/shm:rw'
                ],
                env: [
                    'DISPLAY=vnc:0',
                    'TEST_REUSE_BROWSER=1',
                    'RUN_VNC_SERVER=1',
                    'TEST_BROWSER=chrome'
                ],
                code: {
                    sh """
                        cd /src
                        behave -t ~@nochrome --no-color --junit
                    """
                }
        }
    }

    parallel(tests)
}

