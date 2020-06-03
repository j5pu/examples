#!/usr/bin/env bash

## Alt 1 - $0 without bash substitution
# echo "\${0}: ${0}"
[[ "${0##*/}" == "bash" ]] && dir="${BASH_SOURCE%/*}" || dir="${0%/*}"
[[ "${dir}" != "${BASH_SOURCE%}" ]] || dir="$( pwd )"
echo "dir: ${dir}"

script_real_path=$( cwd="$(pwd)"; cd "${0%/*}" || exit; pwd; cd "${cwd}" || exit; )
echo "script_real_path: ${script_real_path}"

script_filename_no_bash_substitution="$( basename "${0}" )"
echo "script_filename_no_bash_substitution: ${script_filename_no_bash_substitution}"

script_prefix_path="${0%.*}"  # Todo desde el "principio" hasta "último ."
echo "script_prefix_path: ${script_prefix_path}"

script_suffix="${0##*.}"  # Todo desde el "último ." hasta "final"
echo "script_suffix: ${script_suffix}"

script_path="${0}"
echo "script_path: ${script_path}"

script_parent_path="${0%/*}" # Todo desde el "principio" hasta "último /"
echo "script_parent_path: ${script_parent_path}"

script_filename_bash_substitution="${0##*/}"  # Todo desde el "último /" hasta "final"
echo "script_filename_bash_substitution: ${script_filename_bash_substitution}"

script_prefix="${script_filename_bash_substitution%.*}"  # Todo desde el "principio" hasta "último ."
echo "script_prefix: ${script_prefix}"

# For reading through a symlink1, which is usually not what you want
# (you usually don't want to confuse the user this way), try:

script_filename_symlink="$( basename "$(test -L "$0" && readlink "$0" || echo "$0")" )"
echo "script_filename_symlink: ${script_filename_symlink}"

## $BASE_SOURCE - solo cuando se hace source
# shellcheck disable=SC1090
source "${0%/*}/script-bash_source.sh"

## Script params
# Notice on the next line, the first argument is called within double,
# and single quotes, since it contains two words

"${0%/*}/script-parms.sh" "'hello there'" "'william'"
