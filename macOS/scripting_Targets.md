# (Scriptable targets)[https://www.jessesquires.com/blog/executing-applescript-in-mac-app-on-macos-mojave/]
Scripting access groups are provided by applications that support scripting via AppleScript. Access groups define groups of scriptable operations, which you can learn more about in this WWDC talk. There are a couple of ways to discover what is scriptable in an app. You can open the Script Editor, select File > Open Dictionary..., then select the application you want to automate and explore what is possible. This is great for simply writing AppleScript scripts, but I could not find anything that specified which actions were part of an access group. For that, you need to use the sdef tool, the scripting definition extractor.

sdef /Applications/Mail.app
This will dump the specified application’s scripting definition to stdout. I’d recommend tossing the output into a file, so you can open it in an editor.

sdef /Applications/Mail.app > ~/Desktop/mail_sdef.xml
Once you have this, you can search for access-group in the definition file. For the Mail app, you will eventually find:

<access-group identifier="com.apple.mail.compose" access="rw"/>
Cool. Now I have a much better understanding of scripting targets and access groups. What’s left is finding out the access groups I need to specify for System Events, so that I can use the approved com.apple.security.scripting-targets entitlement.

sdef /System/Library/CoreServices/System\ Events.app > ~/Desktop/system_events_sdef.xml
And disappointment ensues. The access groups I need are not there. In fact, the only one available is com.apple.systemevents.window.position, which looks like it was added because of this radar from Craig Hockenberry. About four years later, and no additional access groups have been added.

sudo find -d / -not -path "*/.Trash/* " -type f -name "*.sdef" -exec cp "{}" "${HOME}/Library/Application_Support" \; 
