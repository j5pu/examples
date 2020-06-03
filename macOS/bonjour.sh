#!/usr/bin/env bash

# Browse all discoverable dns-sd  -B  _services._dns-sd._udp  local.
dns-sd  -B  _services._dns-sd._udp  local.

# Printers
dns-sd  -B  _ipp._tcp  local.

# Instance
dns-sd  -L HP _ipp._tcp  local.

# ssh
dns-sd -B _ssh._tcp .

# impresoras
uri="$( lpinfo -v | grep "\/\/HP" | awk '{print $2}' )"
lpadmin -p HP -v "${uri}"

lpstat -p

lpstat -v

# Borrar
lpstat -p | awk '{print $2}' | while read printer
do
    echo "Deleting Printer:" $printer
    lpadmin -x $printer
done

# Agregar
/usr/sbin/lpadmin -p QUEUENAME -o printer-is-shared="False" -E -v lpd://10.x.x.x -P /Library/Printers/PPDs/Contents/Resources/HP\ LaserJet\ 2420.gz -D "Room Number"
