#!/usr/bin/env bash

client=com.apple.ScriptEditor2
service=kTCCServiceAccessibility

sudo sqlite3 '/Library/Application Support/com.apple.TCC/TCC.db' '.tables'
# access            active_policy     expired
# access_overrides  admin             policies

sudo sqlite3 '/Library/Application Support/com.apple.TCC/TCC.db' '.dump access'
sudo sqlite3 '/Library/Application Support/com.apple.TCC/TCC.db' '.schema access'
sudo sqlite3 '/Library/Application Support/com.apple.TCC/TCC.db' 'PRAGMA table_info(access)'
sudo sqlite3 '/Library/Application Support/com.apple.TCC/TCC.db' 'select * from access'

sudo sqlite3 '/Library/Application Support/com.apple.TCC/TCC.db' "select allowed from access where ( service = '${service}' and client = '${client}' );"
# 0
sudo sqlite3 '/Library/Application Support/com.apple.TCC/TCC.db' "update access set allowed=1 where ( service = '${service}' and client = '${client}' );"
# 1
sudo sqlite3 '/Library/Application Support/com.apple.TCC/TCC.db' "select client from access where service = '${service}';"
# com.apple.ScriptEditor2
# com.jetbrains.pycharm
sudo sqlite3 '/Library/Application Support/com.apple.TCC/TCC.db' "select client from access;" | sort -u
# /usr/sbin/smbd
# /usr/sbin/sshd
# com.apple.ScriptEditor2
# com.apple.Terminal
# com.jetbrains.pycharm
# org.virtualbox.app.VirtualBox
sudo sqlite3 '/Library/Application Support/com.apple.TCC/TCC.db' "select service from access;" | sort -u
# kTCCServiceAccessibility
# kTCCServiceDeveloperTool
# kTCCServiceListenEvent
# kTCCServicePostEvent
# kTCCServiceSystemPolicyAllFiles
sudo sqlite3 '/Library/Application Support/com.apple.TCC/TCC.db' "select allowed from access;"
# 1
# 1
# 1
# 0
# 0
# 1
# 1
sudo sqlite3 '/Library/Application Support/com.apple.TCC/TCC.db' "update access set allowed=1;"
# 1
# 1
# 1
# 1
# 1
# 1
# 1
