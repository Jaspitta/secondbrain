A [[router]] is a device that normally operates at [[network layer|layer 3]], tasked with interconnecting different [[network]]s.

Unlike a [[switch]], a [[router]] is a more complex device [[hardware]] wise, it requires an [[operating system]], [[CPU]], [[RAM]], [[ROM]] and [[NVRAM]].

On a cisco router the [[cisco IOS]] is the [[operating system]] normally used.

Every [[router]] is different but in general you have:
- [[console port]]: usually two for initial configuration and [[CLI]] access with [[RJ-45]] connector or [[USB]]
- [[LAN interface]]: usually two that support the standard connector or the [[fiber optic]] one
- [[network interface modules]]: slots that are extensible with various attachments

Just like a [[switch]], there are different way to access the [[router configuration]]:
- [[console port]]: [[USB]] or [[serial]]
- [[ssh]]: require at least one [[network interface card]] configured
- [[aux port]]: remote connection using [[dial up telephone]] or [[modem]], legacy

The [[router boot up process]] is similar to a [[switch]]:
- from [[ROM]] the [[power on self test]] is loaded and ran for error checks
- from [[ROM]] the [[bootstrap]] program is loaded, it locate and start the [[operating system]]
- from [[flash memory]] the [[cisco IOS]] is loaded and ran, if not found it will look for it via [[TFTP]]
- from [[NVRAM]], [[TFTP]] or [[console]], the [[configuration file]] is loaded, now setup mode is started

