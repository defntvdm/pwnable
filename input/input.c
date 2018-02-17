#!/usr/bin/python2

from subprocess import Popen
import os
from time import sleep
from socket import create_connection


os.symlink('/home/input2/input', 'input')
os.symlink('/home/input2/flag', 'flag')

# Stage 1
argv = ['A' for _ in range(99)]
argv[0x40] = ''
argv[0x41] = '\x20\x0a\x0d'
argv[0x42] = '2222'
#####

# Stage 2
stderrr, stderrw = os.pipe()
stdinr, stdinw = os.pipe()
os.write(stdinw, b'\x00\x0a\x00\xff')
os.write(stderrw, b'\x00\x0a\x02\xff')
#####

# Stage 3
my_env = dict(os.environ, **{'\xde\xad\xbe\xef': '\xca\xfe\xba\xbe'})
print("%r -  %r" % ('\xde\xad\xbe\xef', my_env['\xde\xad\xbe\xef']))
#####

# Stage 4
with open('\x0a', 'wb') as f:
    f.write(b'\x00\x00\x00\x00')
#####

proc = Popen(['input'] + argv, env=my_env, stdin=stdinr, stderr=stderrr)

# Sleep for proc could read the file and create server
sleep(0.1)

# Stage 5
sock = create_connection(('localhost', 2222))
sock.send(b'\xde\xad\xbe\xef')
sock.close()
os.remove('\x0a')
