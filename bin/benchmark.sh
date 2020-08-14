#!/bin/bash

REMOTE_IP=$1
OUTPUT_FILE=output/$2

echo "" > $OUTPUT_FILE

echo -n "Benchmark JSON: " >> $OUTPUT_FILE
ab -n 3000 -c 100 $REMOTE_IP/benchmark/json/ | grep "Requests per second" >> $OUTPUT_FILE

echo -n "Benchmark RENDER: " >> $OUTPUT_FILE
ab -n 3000 -c 100 $REMOTE_IP/benchmark/render/ | grep "Requests per second" >> $OUTPUT_FILE

echo -n "Benchmark MODEL: " >> $OUTPUT_FILE
ab -n 3000 -c 100 $REMOTE_IP/benchmark/model/ | grep "Requests per second" >> $OUTPUT_FILE
