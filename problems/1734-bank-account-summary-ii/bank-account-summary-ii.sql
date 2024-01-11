# Write your MySQL query statement below
select c.name, c.balance from (select a.name, a.account, sum(t.amount) as balance from users a left join transactions t on a.account=t.account group by a.account) c where c.balance>10000;