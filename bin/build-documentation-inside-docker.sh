#!/usr/bin/env bash

asciidoctor-pdf -o doc/out/germanium-usage.pdf \
    -d book \
    doc/usage/index.adoc

asciidoctor -o doc/out/index.html\
    -d book \
    doc/usage/index.adoc

chown raptor:raptor doc/out/*

