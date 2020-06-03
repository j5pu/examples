#!/usr/bin/env bash

pwd -P

# Follows it, but doesn't let you know the file doesn't actually exist
greadlink -f /var

# Follows it, but file not there
greadlink -e /var

readlink /var

test -d /var && test -L /var && echo link || echo no link

SYSTEM_ROOT="/System"
SYSTEM_APPLICATIONS="/Applications"
SYSTEM_PREFERENCES="/Applications/System Preferences.app"

python -c "import os; print(os.path.realpath('${SYSTEM_ROOT}'))"
python3 -c "from homely.files import symlink; symlink('.Brewfile')"

## Si nohay -name entonces -print
sudo find / -path "*/Volumes/*" -prune -o -print
sudo find / \( -path "/Volumes/*" -path "*/Volumes/*" \) -prune -o -type f -name "*.sdef" -print
sudo find -x  -type f -name "*.sdef" -print

sudo find -L / -path "*/Volumes/*" -prune -o -name "*.sdef" -print

sudo find -x / -fstype local -name "*.sdef"

# SI
sudo find -L / -path "*/Volumes/*" -prune -o -name "*.sdef" -print
sudo find -L / -name "*.sdef"

sudo find -x -L / -path "*/Volumes/*" -prune -o -name "*.sdef" -print

sudo find -x -L / -not -path "*/.Trash/*" -type f -name "*.sdef" -exec cp "{}" "${HOME}/Library/Application_Support/PyCharm/sdef" \;

scutil
> list
> n.list
> show com.apple.smb
> show State:/Users/ConsoleUser
echo "show State:/Users/ConsoleUser" | scutil
echo "show com.apple.smb" | scutil
echo "show com.apple.opendirectoryd.node:/Contacts" | scutil
echo "show Setup:/System" | scutil
echo "show com.apple.sharing" | scutil
echo "show key /Network/HostNames" | scutil
echo "show " | scutil
echo "show " | scutil
echo "show " | scutil
echo "show " | scutil
echo "show " | scutil
echo "show " | scutil
echo "show " | scutil
echo "show " | scutil
echo "show " | scutil
echo "show " | scutil
echo "show " | scutil
echo "show " | scutil
echo "show " | scutil
echo "show " | scutil
echo "show " | scutil
echo "show " | scutil
echo "show " | scutil
echo "show " | scutil
echo "show " | scutil
echo "show " | scutil
echo "show " | scutil
echo "show " | scutil
echo "show " | scutil
echo "show " | scutil
