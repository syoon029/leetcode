# Write your MySQL query statement below
with full as (select s.name as sname, s.sales_id, o.com_id, c.name as cname
from SalesPerson s
LEFT JOIN Orders o on s.sales_id = o.sales_id
LEFT JOIN Company c on c.com_id = o.com_id)

SELECT distinct sname as name
from full
where sales_id not in (select sales_id from full where cname = 'RED')


