USE Northwind

--1 ���������� ������� 3, 4, 5 �� �� 2 ��������� �������� JOIN
/*SELECT CategoryName as '��� ���������', avg(prod.UnitPrice) as '������� ���� �� ��.'
FROM categories cat JOIN products prod ON cat.categoryid=prod.categoryid
GROUP BY cat.categoryname*/

/*SELECT count(*)
FROM (SELECT categoryid, avg(unitprice) as aver FROM products GROUP BY categoryid) as p1
JOIN products p2 ON p1.categoryid=p2.categoryid AND p2.unitprice>p1.aver*/

/*SELECT c.categoryname, count(unitprice) as average
FROM (SELECT categoryid, avg(unitprice) as aver FROM products GROUP BY categoryid) as p1
    JOIN products as p2
	ON p1.categoryid=p2.categoryid 
	AND p2.unitprice>p1.aver
    JOIN categories as c
	ON p2.categoryid = c.categoryid
GROUP BY c.categoryname
ORDER BY average*/

--2 ��������� ������� �� �����������, ������������ �������� JOIN
/*SELECT customerid, sum((unitprice-discount)*quantity) as turnover
FROM orders o JOIN "Order Details" d ON o.orderid=d.orderid
GROUP BY customerid*/

--3 ������� 10 ����������� � ������������� ���������
/*SELECT TOP 10 customerid, sum((unitprice-discount)*quantity) as turnover
FROM orders o JOIN "Order Details" d ON o.orderid=d.orderid
GROUP BY customerid
ORDER BY turnover DESC*/

--4 ����� ����������� � ��������� ���� �������
/*SELECT customerid, sum((unitprice-discount)*quantity) as turnover
FROM orders o JOIN "Order Details" d ON o.orderid=d.orderid
GROUP BY customerid
HAVING sum((unitprice-discount)*quantity)>
	(SELECT avg(summ)
	FROM (SELECT sum((unitprice-discount)*quantity) as summ
		FROM orders o JOIN "Order Details" d ON o.orderid=d.orderid
		GROUP BY customerid) as p)*/

SELECT *
FROM orders o JOIN "Order Details" d ON o.orderid=d.orderid





