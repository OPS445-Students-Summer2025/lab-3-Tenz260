#!/usr/bin/env python3
'''Lab 3 Inv 2 function free_space'''
# Author ID: 134207232

import subprocess

def free_space():
    p = subprocess.Popen(
        "df -h | grep '/$' | awk '{print $4}'",
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True
    )
    stdout, stderr = p.communicate()
    return stdout.decode('utf-8').strip()

if __name__ == '__main__':
    print(free_space())
