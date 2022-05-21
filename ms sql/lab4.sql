USE pubs

--1 выполнить нижеследующие запросы
/*create table tab1(i integer not null);
alter table tab1 add primary key(i);
create table tab2(j integer not null);
alter table tab2 add primary key(j);
alter table tab1 add constraint tab1fk foreign key(i) references tab2(j);
alter table tab2 add constraint tab2fk foreign key(j) references tab1(i);*/

--написать batch для удаления созданных таблиц

--2 выполнить нижеследующие запросы
/*create table nums(i integer not null);
alter table nums add primary key(i);
insert into nums(i) values (1);*/

--alter table nums add new_num integer;

/*update nums
set new_num=i+i*(2*i+1)*/

--select * from nums


--3 выполните следующие запросы, написать запрос, возвращающий таблицу с сортировкой по
--алфавиту
/*create table person(name varchar(160) not null);
alter table person add primary key(name);
insert into person(name) values('Иванов');
insert into person(name) values('Федоров');
insert into person(name) values('Сидоров');
insert into person(name) values('Петров');*/
--select * from person order by name

--DROP TABLE person;


--4 к таблице из предыдущей таблицы добавить еще одну, выполнив нижеследющий запрос
/*create table ocupation(name varchar(160) not null, ocupied varchar(160) not null);
alter table ocupation add primary key(name, ocupied);
alter table ocupation add foreign key (name) references person(name);
insert into ocupation(name, ocupied) values('Иванов', 'Раскапывает');
insert into ocupation(name, ocupied) values('Федоров', 'Закапывает');*/
--select * from ocupation

--alter table ocupation drop name;
--drop table person;

/*select name, ocupied from ocupation
union
select name, null from person where name not in (select name from ocupation)*/


--5 выполнить запрос из п.2 столько раз, чтобы было не менее 2000 записей.
--написать запрос, выбирающий все простые числа из таблицы
/*DECLARE @iter INT
SET @iter = (SELECT count(i) from nums); --2
while @iter <= 2000
	BEGIN
	insert into nums(i) values(@iter);
	SET @iter = @iter + 1
	END;*/

/*update nums
set new_num=i+i*(2*i+1)*/

--DROP TABLE nums;
--выбираем простые числа
/*select i
from nums n1
where not exists
(select n2.i from nums n2
where n2.i < n1.i AND n2.i > 1 AND n1.i % n2.i = 0)*/

--6 написать запрос, удаляющий все созданные в ходе ЛР таблицы
/*alter table tab1 drop tab1fk
alter table tab2 drop tab2fk
DROP TABLE tab1, tab2, nums, ocupation, person;*/