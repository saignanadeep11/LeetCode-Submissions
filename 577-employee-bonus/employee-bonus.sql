# Write your MySQL query statement below
-- select e.name, b.bonus from Employee e left join Bonus b on b.bonus<1000 and e.empId=b.empId ;
select e.name, b.bonus from Employee e left join Bonus b on b.empID=e.empId where  b.bonus<1000 or b.bonus is null ;