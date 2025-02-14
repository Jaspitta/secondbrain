---
aliases:
  - FTP
---
It is a common protocol to exchange files between server and client or manage them remotely.
The protocol actually uses two ports, in the beginning of an [[FTP session]] some control connection requests are sent to the server using [[TCP]] on port 21, once the session is active port 20 is than used for communication.