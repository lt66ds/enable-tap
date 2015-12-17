qemu-system-i386 -enable-kvm -hda disk.img -cdrom Core-current.iso -boot b -netdev tap,id=t0,ifname=tap0,script=./qemu-ifup,downscript=./qemu-ifdown -device e1000,netdev=t0,id=nic0
