USE Northwind

--1 сколько имеется категорий товаров с таблицу Categories?
/*SELECT COUNT(DISTINCT CategoryName)
FROM Categories*/

--2 сколько видов товаров в каждой категории?
/*SELECT CategoryName, count(*) AS Count
FROM Categories cat, Products prod
WHERE cat.CategoryID=prod.CategoryID
GROUP BY cat.CategoryName*/

--3 вычислите среднюю стоимость единицы продукции по каждой категории
/*SELECT CategoryName as 'Имя категории', avg(prod.UnitPrice) as 'Средняя цена за ед.'
FROM categories cat, products prod
WHERE cat.CategoryID=prod.CategoryID
GROUP BY cat.categoryname*/

--4 сколько имеется товаров, чья стоимость единицы продукции превышает среднюю стоимость
--единицы в соответствующей группе?
/*SELECT count(unitprice) as average
FROM products p1
WHERE unitprice >
	(SELECT avg(unitprice)
	FROM products p2
	GROUP BY categoryid
	HAVING p1.categoryid=p2.categoryid)*/

--5 вычислите П.4 для каждой категории товаров, отсортируйте результат по количеству
/*SELECT categoryname, count(unitprice) as average
FROM categories cat, products p1
WHERE p1.categoryid = cat.categoryid and p1.unitprice >
	(SELECT avg(p2.unitprice)
	FROM products p2
	WHERE p1.categoryid=p2.categoryid)
GROUP BY categoryname
ORDER BY average*/

--6 в скольких странах располагаются поставщики товаров?
/*SELECT count(distinct country)
FROM suppliers*/

--7 сколько наименований товаров поступает из каждой страны? отсортируйте результат по
--убыванию количества товаров
/*SELECT Country, count(productname) as count_PN
FROM suppliers s, products p
WHERE p.supplierid=s.supplierid
GROUP BY country
ORDER BY count_PN DESC*/


/*CREATE VIEW aver
as
SELECT categoryid, avg(unitprice) as average
FROM products
GROUP by categoryid*/

/*SELECT c.categoryname, count(unitprice) as aver
FROM categories c, products p, aver a
WHERE a.categoryid=p.categoryid AND unitprice>average AND c.categoryid=p.categoryid
GROUP BY c.categoryname
ORDER BY aver*/






 
