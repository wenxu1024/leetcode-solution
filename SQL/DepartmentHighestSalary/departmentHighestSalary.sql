# Write your MySQL query statement below
Select Department.Name as Department, employeemax.Name as Employee, Salary From
Department 
Join
(Select Name, Salary, Employee.DepartmentId as Id From
Employee
inner Join
(Select MAX(Salary) as maxSal, DepartmentId From Employee
Group by DepartmentId) maxSalary
Where Employee.Salary = maxSal and Employee.DepartmentId = maxSalary.DepartmentId) employeemax
on Department.Id = employeemax.Id
