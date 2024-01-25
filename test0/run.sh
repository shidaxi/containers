#!/bin/sh
while true; do
  echo -ne "The time is now $(date +%T), apk install hi, version ${VERSION}\\r"
  sleep 1
done