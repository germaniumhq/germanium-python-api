#!/usr/bin/env bash

echo '                                          _'
echo '   ____ ____  _________ ___  ____ _____  (_)_  ______ ___'
echo '  / __ `/ _ \/ ___/ __ `__ \/ __ `/ __ \/ / / / / __ `__ \'
echo ' / /_/ /  __/ /  / / / / / / /_/ / / / / / /_/ / / / / / /'
echo ' \__, /\___/_/  /_/ /_/ /_/\__,_/_/ /_/_/\__,_/_/ /_/ /_/'
echo '/____/ 1.9.3'

set -e

# First things first, use the python virtual env
cd /python/bin
. activate

# This will run the tests from the /tests folder.

if [[ $RUN_VNC_SERVER -eq 1 ]]; then
    echo -e "$VNC_PASSWORD\n$VNC_PASSWORD\n" | vnc4server -geometry ${VNC_SERVER_WIDTH}x${VNC_SERVER_HEIGHT} -depth ${VNC_SERVER_BPP}
    export DISPLAY=:1
    parcellite 1>/dev/null 2>&1 &

    #
    # WebSockify proxying of the port.
    #
    if [[ $RUN_WEB_INTERFACE -eq 1 ]]; then
        websockify --web=/home/germanium/novnc/ 8081 localhost:5901 1>/dev/null 2>&1 &
    fi # [[ $RUN_WEB_INTERFACE -eq 1 ]]
fi # [[ $RUN_VNC_SERVER -eq 1 ]]

cd /tests

if [[ $TEST_BROWSER == *":http"* ]]; then
    TEST_BROWSER_ABBREVIATION=$(echo $TEST_BROWSER | perl -pe 's/^(.*?):.*/$1/')
else
    TEST_BROWSER_ABBREVIATION="$TEST_BROWSER"
fi

behave --tags ~@no${TEST_BROWSER_ABBREVIATION}

# kill potentially remaining processes, but don't fail in case
# stuff can't be killed.
killall -9 $(ps xu | grep -v "grep " | grep -v bash | grep -v "ps " | grep -v "cut " | grep -v "tr " | tr -s " " | cut -f2 -d\ ) || true
