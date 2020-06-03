#!/usr/local/bin/python3.7
import os
import subprocess

def main():
    if os.path.exists('/root/.virtualenv/my_env'):
        print('my_env already exists')
    else:
        subprocess.run(['bash', 'create_env.sh'])
        print('my_env created')

if __name__ == '__main__':
    main()
