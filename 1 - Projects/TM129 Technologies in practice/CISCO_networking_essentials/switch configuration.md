Usually only needs: 
- [[hostname]]: possibly descriptive with info of the physical location, `hostname name`
- [[management IP info]]: for remote access `[[configure terminal]]` `interface vlan 1` `ip address <address> <[[subnet mask]]>` `no shutdown` `exit` `ip default-gateway <[[default gateway]]>`
- [[password]]
- [[descriptive info]]

```Switch> enable
Switch# configure terminal
Switch(config)# hostname S1
S1(config)# enable secret class
S1(config)# line console 0
S1(config-line)# password cisco
S1(config-line)# login
S1(config-line)# line vty 0 15
S1(config-line)# password cisco
S1(config-line)# login
S1(config-line)# exit
S1(config)# service password-encryption
S1(config)# banner motd #No unauthorized access allowed!#
S1(config)# interface vlan1
S1(config-if)# ip address 192.168.1.20 255.255.255.0
S1(config-if)# no shutdown
S1(config-if)# end
S1# copy running-config startup-config
Destination filename [startup-config]?
Building configuration...
[OK]
S1#
```

Even if a [[switch]] is a [[layer 2]] device it can still have an ip configuration, simply because of the necessity of connecting to it remotely for example. To do this the switch must have a [[switch virtual interface]], `ip default-gateway <ip-address>`
