#!/usr/bin/env bash

set -e

# First things first, use the python virtual env
cd /python/bin
. activate

# This will run the tests from the /tests folder.

if [[ $RUN_VNC_SERVER -eq 1 ]]; then
    echo -e "$VNC_PASSWORD\n$VNC_PASSWORD\n" | vnc4server -geometry ${VNC_SERVER_WIDTH}x${VNC_SERVER_HEIGHT} -depth ${VNC_SERVER_BPP}
    export DISPLAY=:1

    #
    # WebSockify proxying of the port.
    #
    if [[ $RUN_WEB_INTERFACE -eq 1 ]]; then
        websockify --web=/home/germanium/novnc/ 8081 localhost:5901 1>/dev/null 2>&1 &
    fi # [[ $RUN_WEB_INTERFACE -eq 1 ]]
fi # [[ $RUN_VNC_SERVER -eq 1 ]]

cd /tests

behave --tags ~@no${TEST_BROWSER}

# kill potentially remaining processes, but don't fail in case
# stuff can't be killed.
killall -9 $(ps xu | grep -v "grep " | grep -v bash | grep -v "ps " | grep -v "cut " | grep -v "tr " | tr -s " " | cut -f2 -d\ ) || true
