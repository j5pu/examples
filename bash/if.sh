#!/bin/bash

a=/ala
[[ "${a}" == /* ]] && echo yes || echo no  # First character is /

# To match this or that in a regex use |, i.e.
# user* means use and zero-or-more occurrences of r, so use and userrrr will match
# user.* means user and zero-or-more occurrences of any character, so user1, userX will match.
# ^user.* means match the pattern user.* at the begin of $HOST.
if [[ "$HOST" =~ ^user.*|^host1 ]]; then
    echo "yes"
fi
# Para math exacto 
[[ "${1}" =~ ^ERROR$|^DEBUG$|^WARN$|^INFO$|^SCRIPT$|^OK$|^PASS$ ]] || { msg ERROR "\$1 must be ERROR|DEBUG|WARN|INFO|SCRIPT|OK|PASS" >&2; exit 1; }

script=mierda
[[ "${script}" == *"path"* ]] && echo si || echo no
script=/Users/wheel/Desktop/macdev/bootstrap/scripts/00-path.sh
[[ "${script}" == *"path"* ]] && echo si || echo no
