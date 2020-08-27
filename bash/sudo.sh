#!/usr/bin/env bash
python -c "import getpass; print(getpass.getuser())"
python -c "import os; print(os.getlogin())"
python -c "import os; print(os.uname().sysname)"
python3 -c "import os; print(os.uname().nodename)"
python3 -c "import socket; print(socket.gethostname())"
python3 -c "import socket; print(socket.getfqdn())"
python3 -c "import os; print(os.uname().nodename.split('.')[0])"

python3 -c "import distro; print(distro._distro.info()['like'])"
python3 -c "import distro; print(distro._distro.info()['id'])"

if [[ "$(id -u)" != "0" ]] && [[ ! "${SUDO_UID-}" ]] && [[ "$(uname -s)" == "Darwin" ]]; then
  export INTERNET_PASSWD="$(security find-internet-password -s github.com -w)"
fi

for i in SUDO_UID USER LOGNAME SUDO_USER SUDO_COMMAND SHELL SUDO_GID HOME; do
echo "${i}: ${!i}"
done

$ stat -f "%Su" /dev/console
jose

$ logname
root

$ sudo logname
root

$ sudo --login logname
root

$ sudo --login su -l
# logname
root

# last -1

- sudo su
SUDO_UID=501
USER=root
LOGNAME=root
SUDO_USER=jose
SUDO_COMMAND=/usr/bin/su
SHELL=/usr/local/bin/bash
SUDO_GID=20

- sudo su -l
SUDO_UID:
USER: root
LOGNAME:
SUDO_USER:
SUDO_COMMAND:
SHELL: /usr/local/bin/bash
SUDO_GID:
HOME: /var/root

- sudo --login su
SUDO_UID: 501
USER: root
LOGNAME: root
SUDO_USER: jose
SUDO_COMMAND: /usr/local/bin/bash -c su
SHELL: /usr/local/bin/bash
SUDO_GID: 20
HOME: /var/root


- sudo --login su -l
SUDO_UID:
USER: root
LOGNAME:
SUDO_USER:
SUDO_COMMAND:
SHELL: /usr/local/bin/bash
SUDO_GID:
HOME: /var/root

"""
