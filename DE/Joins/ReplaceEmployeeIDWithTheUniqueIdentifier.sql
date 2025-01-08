select unique_id, name from employees left join EmployeeUNI 
on employees.id=EmployeeUNI.id

-- Beats 59.03% of users with MySQL in runtime