# Write your MySQL query statement below
SELECT Name as Customers From Customers
Where Customers.Id not in 
(SELECT CustomerId as Id From Orders)
