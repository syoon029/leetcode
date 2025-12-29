# Write your MySQL query statement below
with primary_table as (
select employee_id, department_id
from Employee
where primary_flag = 'Y'),

one_table as (select employee_id, department_id
from Employee
where employee_id not in (select employee_id from primary_table)
)

select employee_id, department_id
from primary_table
UNION 
select employee_id, department_id
from one_table

