# Write your MySQL query statement below
select a.name, sum(t.amount) as balance from users a left join transactions t on a.account=t.account group by a.account having balance>10000;