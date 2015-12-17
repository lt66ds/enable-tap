qemu-system-i386 -enable-kvm -hda disk.img -cdrom Core-current.iso -boot b -netdev tap,id=t0,ifname=tap0,script=/etc/qemu-ifup,downscript=no -device e1000,netdev=t0,id=nic0
