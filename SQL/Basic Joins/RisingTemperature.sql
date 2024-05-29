select w1.id from Weather w1, Weather w2
where DATEDIFF(w1.recordDate, w2.recordDate) = 1 AND 
w1.temperature > w2.temperature

-- Beats 23.25% of users with MySQL in runtime