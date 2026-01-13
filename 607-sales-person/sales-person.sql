SELECT name
from SalesPerson
Where sales_id not in (select sales_id from Company c RIGHT JOIN Orders o on c.com_id = o.com_id where c.name = 'RED' )
