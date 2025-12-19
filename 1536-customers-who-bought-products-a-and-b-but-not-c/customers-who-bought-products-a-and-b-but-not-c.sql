# Write your MySQL query statement below
with joined as(SELECT c.customer_id, c.customer_name, o.order_id, o.product_name
from customers c 
Join orders o ON c.customer_id = o.customer_id)


select customer_id, customer_name
from joined
where customer_id in (select customer_id  from joined where product_name = 'A') and product_name = 'B' and customer_id not in (select customer_id  from joined where product_name = 'C')