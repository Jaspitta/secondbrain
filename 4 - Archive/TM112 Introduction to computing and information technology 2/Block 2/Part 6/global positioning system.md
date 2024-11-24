---
aliases:
  - GPS
---
It is a technology originally developed for military use and now employed also for regular consumers that employ a [[line-of-sight technology]].
Since the use of [[global positioning system|GPS]] in [[consumer technology]] and the growth of [[location-based services]], more and more concerns started to raise regarding the breach of privacy in peoples locations and data that is often also made publicly available.

The [[GPS]] system is composed of [[receiver]] and [[satellite]], however, [[satellites]] do not reply individually to each [[receiver]] but rather broadcasts information and the [[receiver]] has to figure out its position. To understand the position of the receiver a code run continuously and synchronously at every receiver and satellite, the signal sent from satellite to receiver will appear delayed by the time it took to travel.
Since the signal travel at the speed of light, we can measure the time by the delay in the code, and we know `speed = distance / time` we can calculate the distance as a consequence.
Once we have a distance we can draw an imaginary sphere around the satellite, if we do that for 2 more satellites we can use [[trilateration]], the intersection of the spheres will results in 2 points, one in space and one on earth.

Synchronizing clocks with such precision require very expensive clocks which are not usable in every day devices, the solution is to use a 4th satellite to improve the precision of the measurements. If there are imprecisions the sphere drawn by the fourth [[satellite]] will not match the point of the other 3 and therefore the [[receiver]] clock needs to be adjusted. The [[receiver]] therefore finds an adjustment that would make the all the four spheres meet in the right point and apply it.

In order for the [[receiver]] to know where the [[satellite]] is in the sky [[satellites]] themselves broadcast [[ephemeris data]] which describe the orbit of each satellite and [[almanac data]] which roughly describe where each satellite is in the sky. Waiting and processing [[ephemeris data]] can take time so it is not done all the times.
