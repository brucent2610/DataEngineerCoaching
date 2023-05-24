#Using Linux Help Resources

[Server Fault](https://serverfault.com/questions/tagged/linux)

```
sudo apt install info
info

<!-- Example wget -->
info wget examples simple
```

```
cd /usr/share/doc
<!-- Example wget -->
cd wget
less README
```

```
wget --help | less
type wget
```

#Navigating the Linux File Systems
Note For rm: `Be careful with this by the way because you can end up deleting a lot more than you expected and keep in mind Linux terminal has no trashcan to restore`

#Searching the Linux File System
```
updatedb
```
```
cut -d: -f3 /etc/group | sort -rn
```

#Linux kernal and Peripherals
##Troubleshoot Peripherals
- 1. Is device recognized by the system?
- 2. Is the appropriate kernal module loaded?
```
lsusb
lspci
lshw
```
```
ls /lib/modules
uname -r
ls /lib/modules/`uname -r`
ls /lib/modules/`uname -r`/kernel
lsmod | grep ${module_name}
modprobe ${module_name}
```

#Linux Network Connectivity
- Analyzing network connectivity
- Configuring DNS
- SSH remote sessions

##Network Connectivity
```
ip route show
ip addr
```
##Nerwork Addressing
```
route
ifconfig
netstat -i
netstat -l
ss -i 
```
##Domain Name System (DNS) Configuration
```
host ${domain}
ping ${domain}
cat /etc/resolv.conf
systemd-resolve --status
```
##Remote Connections and Secure Shell (SSH)
- Accessing headless servers
- Accessing virtual machines
- Accessing workloads on distant servers

[Linux-cli](https://bootstrap-it.com/linux-cli)