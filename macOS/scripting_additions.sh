#!/bin/bash
# https://developer.apple.com/download/more/
# https://download.developer.apple.com/Developer_Tools/xcode_3.2.1_developer_tools/xcode321_10m2003_developerdvd.dmg
# https://scriptingosx.com/2018/08/user-interaction-from-bash-scripts/
# https://scriptingosx.com/bash/

https://developer.apple.com/design/downloads/SF-Symbols.dmg

export PATH=/usr/bin:/bin:/usr/sbin:/sbin

consoleUser() {
	echo "show State:/Users/ConsoleUser" | scutil | awk '/Name :/ && ! /loginwindow/ { print $3 }'
}

displaydialog() { # $1: message
	message=${1:-"Message"}
	user=$(consoleUser)
    if [[ $user != "" ]]; then
        uid=$(id -u "$user")
		launchctl asuser $uid /usr/bin/osascript <<-EndOfScript
			button returned of ¬
			    (display dialog "$message" ¬
				buttons {"OK"} ¬
				default button "OK")
		EndOfScript
	fi
}

displaynotification() { # $1: message $2: title
	message=${1:-"Message"}
	title=${2:-"Script Notification"}
	user=$(consoleUser)
    if [[ $user != "" ]]; then
        uid=$(id -u "$user")
		launchctl asuser $uid /usr/bin/osascript <<-EndOfScript
			display notification "$message" with title "$title"
		EndOfScript
	fi
}


displayfortext() { # $1: message $2: default text
	message=${1:-"Message"}
	defaultvalue=${2:-"default value"}
	user=$(consoleUser)
    if [[ $user != "" ]]; then
        uid=$(id -u "$user")

	    launchctl asuser $uid /usr/bin/osascript <<-EndOfScript
			text returned of ¬
				(display dialog "$message" ¬
					default answer "$defaultvalue" ¬
					buttons {"OK"} ¬
					default button "OK")
			EndOfScript
	else
	    exit 1
	fi
}

# run all functions

displaydialog "Hello"
name=$(displayfortext "Enter your name:" "$(consoleUser)")
displaynotification "Hello, $name"