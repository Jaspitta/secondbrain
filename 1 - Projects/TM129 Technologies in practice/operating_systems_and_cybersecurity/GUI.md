---
aliases:
  - graphical user interface
---
A particular component of this type of [[shell]] is the [[file manager]].

In modern [[operating system]]s the [[GUI]] has become a core part of the product, the [[desktop environment]] and the [[windowing system]] are now more important than ever but they can be managed very differently depending on the system.
In [[linux]] the [[GUI]] is less linked to the rest of the system offering much more flexibility.

The [[linux desktop environment]] depend on many components but two main parts:
- [[window manager]]: keeps applications virtually separated, windows can be stacked on top with [[stacking]], they can also be tiled with [[tiling]], or when a [[GPU]] can handle it [[X11]] will delegate to the [[hardware]] the job of transparency, shadows and more, this is called [[composing]]
- [[widget toolkit]]: provide developers with buttons and controls for a unified look
more features are added like a [[clipboard]] but they are less essentials.

Behind almost all the [[linux desktop environment]]s there is the same [[display system]], that is [[X11]] which manages the display, moving windows, display devices, inputs and outputs. X11 could be a [[GUI]] alone but lack lots of features, so with time desktop environments like [[GNOME]] and [[KDE]] became the standard that interacts with a [[window manager]] which talk to X11 to handle keyboard, mouse and screen.
The only in construction alternative is [[Wayland]]

You can run a session of X11 for each user in a linux system but the common approach is to have one running at [[boot]] and letting a [[session manager]] handle the starting and stopping of new applications.

