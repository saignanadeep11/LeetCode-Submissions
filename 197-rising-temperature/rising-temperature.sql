# Write your MySQL query statement below
select w1.id as Id from Weather w1 inner join Weather w2 on w1.recordDate=date_add(w2.recordDate,interval 1 day) and w1.temperature>w2.temperature;