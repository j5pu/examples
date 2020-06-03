#!/usr/bin/env bash
# https://pawelgrzybek.com/change-macos-user-preferences-via-command-line/

# Let's take it apart to get familiar with the terminology used throughout this article:

# defaults - interface
# write - method
# comapple.finder - domain
# AppleShowAllFiles - key
# -string - type descriptor
# YES - new value
defaults domains | tr ',' '\n'

# Methods
# read - prints current user settings
# read-type - prints the type of given key
# write - writes new settings
# delete - deletes a key or a full domain
# domains - prints the full list of domains
# find - searches all domain and keys for a given name
# help - I'm sure you know what this does



defaults read com.apple.Notes
defaults read-type com.apple.Notes NotesContinuousSpellCheckingEnabled
defaults write com.apple.Notes NotesContinuousSpellCheckingEnabled -bool true


# visual code for diffs
defaults read > before
defaults read > after
code --diff before after

https://github.com/kevinSuttle/macOS-Defaults/blob/master/REFERENCE.md

system_profiler

/usr/libexec/PlistBuddy $HOME/Library/Preferences/com.apple.Safari.SafeBrowsing.plist
print