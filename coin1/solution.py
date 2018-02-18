#!/usr/bin/env python3

from socket import create_connection

def ntvdm():
    s = create_connection(('localhost', 9007))
    print(s.recv(2**16).decode())
    for i in range(100):
        inp = s.recv(2**16).decode()
        n, c = (int(param.split('=')[1]) for param in inp.split(' '))
        print('input n=%r c=%r' % (n, c))
        start, end = 0, n
        array = list(range(n))
        middle = (start + end) // 2
        for j in range(1, c+1):
            query = ' '.join(str(e) for e in array[start:middle]) + '\n'
            s.send(query.encode())
            weight = int(s.recv(2**16).decode())
            if weight % 10 == 0:
                start = middle
            else:
                end = middle + 1
            middle = (start + end) // 2
        print('ANSWER:', array[start])
        s.send(str(array[start]).encode() + b'\x0a')
        print('RESULT:', s.recv(2**16).decode())
    print(s.recv(2**16).decode())
    s.close()

if __name__ == '__main__':
    ntvdm()

