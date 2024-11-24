---
aliases:
  - latitude/longitude coordinate scheme
---
In the beginning when you wanted to move around you had to use an atlas where the map was built as a grid system and page index scheme to represent a specific location. This meant that unless someone had the exact same atlas such information could only be useful to you.

The [[lat-long coordinate scheme]] therefore is born as a global, standardized and agreed upon system that everyone can use to reference a specific place on earth.
In this system earth is split by a grid of horizontal and vertical lines. Horizontals are called [[latitudes]] where the [[equator]] is defined as 0 degrees, while verticals are called [[longitudes]] where the one that passes through the observatory of [[Greenwich]] is considered the 0 degrees one. The cross of the 0 degree [[latitude]] and [[longitude]] is called the [[reference point]].
When moving on this grid, since the earth is round, the direction is expressed in degrees of rotation, moving to W of the [[Greenwich]] meridian implies negative longitudes and moving to S of the [[equator]] implies negative latitudes.

You need to be careful of the representation of the way you represent data using the [[lat-long coordinate scheme]] when it comes to negative numbers. Keep in mind that for negative longitudes you could also say a positive one but prepend it with the W to imply that we are moving W compared to the [[Greenwich]] meridian.

This system of representing [[geolocation]] used by [[global positioning system|GPS]] is called [[WGS 84]] or also [[WGS 84|EPSG:4326]].