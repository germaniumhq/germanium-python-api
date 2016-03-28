
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
    node {
        sh "docker run --rm -e TEST_REUSE_BROWSER=1 germanium/germanium-python2.7-tests"
    }
}, python34: {
    node {
        sh "docker run --rm -e TEST_REUSE_BROWSER=1 germanium/germanium-python3.4-tests"
    }
}, python35: {
    node {
        sh "docker run --rm -e TEST_REUSE_BROWSER=1 germanium/germanium-python3.5-tests"
    }
}, failFast: true

stage "Publish on PyPI"

node {
    sh '''
        ls
    '''
}

