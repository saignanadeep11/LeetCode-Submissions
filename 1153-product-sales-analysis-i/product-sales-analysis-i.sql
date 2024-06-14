# Write your MySQL query statement below
select pt.product_name,s.year,s.price from Sales s left join Product pt on pt.product_id = s.product_id;