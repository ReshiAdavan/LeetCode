select S.user_id, 
    round(
        coalesce(sum(case when C.action = 'confirmed' then 1 else 0 end), 0) /
        case when count(C.user_id) > 0 then count(C.user_id) else 1 end , 2
        ) as confirmation_rate
from Signups S 
left join Confirmations C
on S.user_id = C.user_id
group by S.user_id

-- Beats 46.06% of users with MySQL in runtime