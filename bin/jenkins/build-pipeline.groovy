
def buildSingleVersion(version) {
    stage version
    node {
        sh """
        rm -fr $version
        git clone /home/raptor/projects/germanium $version
        cd $version
        git checkout remotes/origin/$version
        bin/run-tests-end-to-end.sh
        #bin/build-docker-instance.sh
        """
    }
}

parallel python27: {
    buildSingleVersion("python2.7")
}, python34: {
    buildSingleVersion("python3.4")
}, python35: {
    buildSingleVersion("python3.5")
}, failFast: true


stage "Publish on PyPI"

node {
    sh '''
        ls
    '''
}

