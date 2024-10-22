delimiter $ 
drop procedure if exists ageMinMax$
create procedure ageMinMax()
begin 
   select floor(datediff(now(), str_to_date(max(birth_date), '%Y-%m-%d')) / 365) as min_age, floor(datediff(now(), str_to_date(min(birth_date), '%Y-%m-%d')) / 365) as max_age from employees;
end$ 
delimiter ;
call ageMinMax();

delimiter $
drop procedure if exists salaireMaxi$
create procedure salaireMaxi(in gender char(1))
begin
    select e.first_name, e.last_name, max(s.salary) as max_salary from employees e inner join salaries s on e.emp_no = s.emp_no where e.gender = gender group by e.first_name, e.last_name;
end$
delimiter ;
call salaireMaxi('F');
call salaireMaxi('M');

delimiter $
drop procedure if exists salaireMaxiOut$
create procedure salaireMaxiOut(in gender char(1), out salaryOut decimal(10,2))
begin 
    select subquery.max_salary into salaryOut 
    from (
        select max(s.salary) as max_salary 
        from employees e 
        inner join salaries s on e.emp_no = s.emp_no 
        where e.gender = gender
    ) as subquery;
end$
delimiter ;

call salaireMaxiOut('F', @salaryOut);
select @salaryOut;
call salaireMaxiOut('M', @salaryOut); 
select @salaryOut;

delimiter $
drop procedure if exists salaireMaxi2$
create procedure salaireMaxi2(in gender char(1))
begin
    declare maxSalary decimal(10,2);
    declare genderOut varchar(50);

    select max(s.salary) into maxSalary from employees e inner join salaries s on e.emp_no = s.emp_no where e.gender = gender;

    if gender = 'M' then 
        set genderOut = 'pour les hommes';
    elseif  gender = 'F' then 
        set genderOut = 'pour les femmes';
    else 
        set genderOut = 'genre non specifie';
    end if;

    select concat('Le salaire maximum est ', maxSalary, ' ', genderOut) as result;
end$
delimiter ;
call salaireMaxi2('F');
call salaireMaxi2('M');