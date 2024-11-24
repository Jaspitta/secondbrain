---
aliases:
  - SQL Injection
---
It is a common vulnerability that exposes websites and technology products in general to potential attacks to its [[Database]] that could result in data being reviled, stolen or more.
Most [[Database]]s use a [[query language]] to communicate that is called [[Simple Query Language]], it is a common practice to receive requests that contains [[query parameters]] in the [[URL]] and use such parameters to than execute [[query]] on the database. This process is the core of most online technology products and almost all websites.

The improper use of [[URL]] [[query parameters]] however exposes the product to potential [[SQLi]] attacks. If a malicious [[hacker]] fidget around with what is passed to such [[query parameters]] he could gain access to data that he should not see and in the worst of cases gain full access to the whole [[Database]].

When using [[query parameters]] that are translated into [[SQL instruction]]s it is mandatory to follow some practices that eliminate the threat of [[SQLi]]. For starters permissions should be restricted to the minimum possible following the [[PoLP]], in a [[production environment]] [[database]] [[error log]]s should be turned off to not give extra information (an attack without such information is called [[blind injection]] and it is much less effective), the number and type of [[query parameters]] should be restricted and [[query parsing]] should be done so sanitize the content of such parameters