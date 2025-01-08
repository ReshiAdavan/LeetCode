select customer_id, COUNT(*) as count_no_trans from 
    (select Visits.customer_id, Transactions.transaction_id from Visits
    left join Transactions on Visits.visit_id = Transactions.visit_id) as T
where transaction_id is null
group by customer_id

-- Beats 41.02% of users with MySQL in runtime

select v.customer_id, COUNT(v.visit_id) as count_no_trans 
from Visits v 
left join Transactions t 
on v.visit_id = t.visit_id
where transaction_id is null
group by customer_id

-- Beats 70.27% of users with MySQL in runtime