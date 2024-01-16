# Write your MySQL query statement below
select contest_id, round(count(r.user_id)*100/(select count(*) from users),2) percentage from Register r left join Users u on r.user_id=u.user_id group by contest_id order by percentage desc,contest_id;