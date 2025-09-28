---
aliases:
- IPV6 global unicast
---

like a [[public IPV4 address]], globally unique, for now only those starting with $001$ are being actively used, made of:
	- [[routing prefix]]: normally given from [[ISP]]s to customer, it is a /48 prefix that represent the [[network prefix]]
	- [[subnet id]]:  the remaining part from the [[routing prefix]] that is needed to get to a [[network prefix]] of /64, reserved for organizations to create their [[subnets]]
	- [[interface id]]: [[host components]]

The configuration is equal to ipv4 but you use the prefix ipv6 where you would use ip, for example `ipv6 address ipv6-address/prefix-length`

```
R1(config)# **interface gigabitethernet 0/0/0**
R1(config-if)# **ipv6 address 2001:db8:acad:1::1/64**
R1(config-if)# **no shutdown**
R1(config-if)# **exit**
R1(config)# **interface gigabitethernet 0/0/1**
R1(config-if)# **ipv6 address 2001:db8:acad:2::1/64**
R1(config-if)# **no shutdown**
R1(config-if)# **exit**
R1(config)# **interface serial 0/1/0**
R1(config-if)# **ipv6 address 2001:db8:acad:3::1/64**
R1(config-if)# **no shutdown**
```

of course, static configuration has it's limitations, the most common practice is to use [[DHCPv6]] or [[StateLess Address AutoConfiguration]]
