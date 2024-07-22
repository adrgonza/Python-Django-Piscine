#!/bin/bash

output=$(curl -s "$1")

echo "$output" | grep 'href=' | cut -d '"' -f 2