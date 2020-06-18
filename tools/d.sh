#!/bin/bash

set -e

openssl enc -d -aes256 -in crun.sh | tar xz