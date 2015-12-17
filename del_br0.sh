#/bin/bash
ifconfig br0 down
ifconfig eth0 down
brctl delif br0 eth0
brctl delbr br0
dhclient eth0
ifconfig eth0 up
