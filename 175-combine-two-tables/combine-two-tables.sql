# Write your MySQL query statement below
SELECT firstName, lastName, city, state
from Person p
left join Address a On a.personId = p.personID
