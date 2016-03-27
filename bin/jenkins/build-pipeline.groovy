parallel python27: {
    stage "Python 2.7"
}, python34: {
    stage "Python 3.4"
}, python35: {
    stage "Python 3.5"
}, failFast: true


node {
    sh '''
        ls
    '''
}

