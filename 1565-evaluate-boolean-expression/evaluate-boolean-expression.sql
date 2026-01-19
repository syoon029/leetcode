# Write your MySQL query statement below
SELECT left_operand, operator, right_operand, CASE WHEN operator = "=" THEN IF(V1.value = V2.value, 'true','false')
WHEN operator = ">" THEN IF(V1.value > V2.value, 'true','false')
WHEN operator = "<" THEN IF(V1.value < V2.value, 'true','false')
END AS value 
FROM Expressions E
JOIN variables V1 on E.left_operand = V1.name
JOIN variables V2 on E.right_operand = V2.name