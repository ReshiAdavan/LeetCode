select E.name from Employee E
inner join Employee F
on E.id = F.managerId
group by F.managerId
having count(F.managerId) >= 5;
-- Beats 51.24 %of users with MySQL in runtime