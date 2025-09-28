It is a [[networking design]] that has the goal of separating the devices in a [[network]] based on some decided logic, that could be importance, geographical or more.
In the case of a small [[network]] this might simply means splitting in two with a [[router]] in the middle, however in a bigger network this process is repeated multiple times and all this smaller networks are than joined in a hierarchical structure. This structure is though in a way such that two different networks that are likely to communicate with each other are places close, this way the traffic between them does not need to go thorough any other [[network]], improving [[scalability]] and [[security]].

This structure creates also some layers:
- [[access layer]]: devices that interact with the users or with the devices that do (pc, [[access point]], [[switch]]...)
- [[distribution layer]]: interconnect devices at the [[access layer]] keeping the smaller [[network]]s separate
- [[core layer]]: responsible for high speed processing of traffic