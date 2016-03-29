#!/usr/bin/env bash

set -e

# First things first, use the python virtual env
cd /python/bin
. activate

# This will run the tests from the /tests folder.

if [[ $RUN_VNC_SERVER -eq 1 ]]; then
    echo -e "$VNC_PASSWORD\n$VNC_PASSWORD\n" | vnc4server -geometry 800x600 -depth 16
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
