It is a [[CLI]] program that support [[cisco IOS command]]s to manage network devices, it essentially offers many utilities to make [[network configuration]] easier.

The tool can be used in two modes:
- [[user EXEC mode]]: limited mode that allows for most monitoring command but no possibility to perform changes, the prompt has the symbol ">"
- [[privileged EXEC mode]]: allow to execute all commands, prompt has the symbol "#". You can switch to this mode from [[user EXEC mode]] typing 'enable'. From here you can use the 'configure' command to enter a specific [[configuration mode]].


command:
- [[enable]]: switch to [[privileged EXEC mode]]
- [[disable]]: switch to [[user EXEC mode]]
- [[configure terminal]]: switch to [[global config mode]]
- [[exit]]: move back to the previous mode, if already in [[user EXEC mode]] closes the terminal
- [[line console 0]]: [[configuration management mode]] for the management interface of console port 0
- [[line vty 0 15]]: [[configuration management mode]] for the virtual terminal management, used for remote access to a [[switch]]
- [[interface fastethernet 0/1]]: open [[configuration mode]] for the desired [[network interface]]
- [[end]]: exit every [[configuration mode]]
- [[show running-config]]: show configuration on current device
- [[show interfaces]]
- [[show ip interface]]: [[network layer|layer 3]] info regarding the [[interface]]
- [[show arp]]
- [[show ip route]]: show the routing table on the [[router]]
- [[show protocol]]: extra information for [[layer 3]] interfaces ([[network layer]])
- [[show version]]: software and hardware information of the [[router]]

