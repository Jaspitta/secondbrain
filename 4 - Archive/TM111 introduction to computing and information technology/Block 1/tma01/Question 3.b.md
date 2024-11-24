
Customers_Table

| Customer_Number | Firstname   | Surname   |
| --------------- | ---------- | --------- |
| 00001           | Margaret   | Chen      |
| 00002           | Kofi       | Kayga     |
| 00003           | Barrington | Watson    |
| 00004           | Ebony      | Patterson |
| 00005           | Leonard    | Chen      |
| 00006           | Guy        | Harvey    |
| 00007           | Armet      | Francis   |

Cruises_Table

| Cruise_Number | Ship      | Month     |
| ------------- | --------- | --------- |
| 00001         | Lauretic  | January   |
| 00002         | Britannic | January   |
| 00003         | Oceanic   | March     |
| 00004         | Albertic  | May       |
| 00005         | Laurentic | January   |
| 00006         | Homeric   | September |
| 00007         | Delphic   | June      |
| 00008         | Delphic   | February  |
| 00009         | Britannic | March     |
| 00010         | Britannic | December  |
| 00011         | Oceanic   | October   |


I separated the tables into the two entities which are Customers and Cruises, now each entity is represented in its own table.
At this point it is easy to notice that the relation between Customers and Cruises is lost and therefore we need a new way to represent it, this is where joining tables, the core of relational databases, come into play.
In each Table I added an attribute which identify each instance uniquely in the form of a progressive integer number, respectively I added Customer_Number for the Customer Table and Cruise_Number for the Cruises Table. This number will allow us to reference every single entity via their Id and recreate the relationship between the entities without sacrificing the ease of adding new instances or editing them that we have by having the 2 entities represented as separate tables