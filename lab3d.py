#!/usr/bin/env python3
# Author ID: mdfernando3
import subprocess

def free_space():
    p = subprocess.Popen("df -h | grep '/$' | awk '{print $4}'", stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = p.communicate()

    if error:
        return error.decode('utf-8').strip()
   
    output_str = output.decode('utf-8').strip()
    return output_str
if __name__ == '__main__':
    print(free_space())
