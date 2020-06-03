#!/usrbin/env bash
scutil
> list
> n.list
> show com.apple.smb
> show State:/Users/ConsoleUser
echo "show State:/Users/ConsoleUser" | scutil
echo "show com.apple.opendirectoryd.node:/Contacts" | scutil
echo "show Setup:/System" | scutil
echo "show com.apple.sharing" | scutil
echo "show key /Network/HostNames" | scutil

# https://support.apple.com/pl-pl/HT204021
## smb
scutil
> list
> show com.apple.smb
##
<dictionary> {
  AclsEnabled : FALSE
  AllowDropboxShare : TRUE
  AllowGuestAccess : FALSE

  DirectoryLeasingEnabled : TRUE
  FileLeasingEnabled : TRUE

  SMB1SigningEnabled : TRUE

  SharingEnabled : TRUE
  SigningEnabled : TRUE
  SigningRequired : TRUE

}
> get com.apple.smb  ## igual a sudo scutil --prefs com.apple.smb.server.plist; > get /
> d.show  ## ya estamos en ese dictionary.
> get SharingEnabled
echo "show com.apple.smb" | scutil
sudo scutil --prefs com.apple.smb.server.plist


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
