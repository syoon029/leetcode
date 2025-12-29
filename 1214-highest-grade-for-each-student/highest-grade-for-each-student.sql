# Write your MySQL query statement below
with highest_table as (
    SELECT student_id, course_id, grade, rank() over (partition by student_id order by grade DESC, course_id ASC) as ranking
    from Enrollments
    order by course_id
)

select student_id, course_id, grade
from highest_table
where ranking = 1
order by student_id