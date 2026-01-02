# Write your MySQL query statement below
SELECT s.seller_name
FROM Orders o
RIGHT JOIN Seller s on o.seller_id = s.seller_id
WHERE s.seller_id not in (select seller_id from Orders where YEAR(sale_date) = 2020) or o.order_id is Null
ORDER BY s.seller_name ASC