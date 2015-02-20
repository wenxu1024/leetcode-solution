# Write your MySQL query statement below
Select FirstName, LastName, City, State From
Person
left join Address
On Person.PersonId = Address.PersonId
