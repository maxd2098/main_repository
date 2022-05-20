USE Northwind

--ex1 количество записей в базе sysobjects?
/*SELECT count(*)
FROM sysobjects*/

--ex2 количество объектов с типом U?
/*SELECT count(*)
FROM sysobjects
WHERE type='U'*/

--ex3 количество объектов, относящихся к объектам с типом U?
/*SELECT count(*)
FROM sysobjects sys1, sysobjects sys2
WHERE sys2.id = sys1.parent_obj and sys2.xtype='U'*/

--ex4 количество объектов, не относящися к типу U и не являющихся объектами с типом U?
/*SELECT count(*)
FROM sysobjects sys1
WHERE sys1.type != 'U' and NOT EXISTS
	(SELECT *
	FROM sysobjects sys2
	WHERE sys2.id = sys1.parent_obj and sys2.type='U')*/

--ex5 Количество типов? Количество объектов каждого типа?
--SELECT count(distinct(type)) FROM sysobjects

/*SELECT distinct type, count(type)
FROM sysobjects
GROUP BY type*/


--ex6 количество объектов каждого типа, не относящися к типу U 
--и не являющихся объектами с типом U? 
/*SELECT type, count(type)
FROM sysobjects sys1
WHERE type != 'U' and NOT EXISTS
	(SELECT *
	FROM sysobjects sys2
	WHERE sys2.id = sys1.parent_obj and sys2.type='U')
GROUP BY type*/

--ex7 количество объектов, чье имя начинается с символов sys?
/*SELECT count (*)
FROM sysobjects
WHERE name LIKE 'sys%'*/

--ex8
/*SELECT count(*) 
FROM sysobjects s1, sysobjects s2
WHERE s1.type = 'U' AND s1.id=s2.parent_obj
	AND s2.name LIKE '%rs'*/

/*SELECT count(*)
FROM sysobjects
GROUP BY type*/



