#!/bin/bash


# First take eth0 down, then bring it up with IP 0.0.0.0
ifconfig eth0 down
ifconfig eth0 0.0.0.0 promisc up


# create the bridge br0
brctl addbr br0
brctl addif br0 eth0
brctl stp br0 off

dhclient br0
ifconfig br0 up


