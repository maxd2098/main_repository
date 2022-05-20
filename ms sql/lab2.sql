USE Northwind

--1 ������� ������� ��������� ������� � ������� Categories?
/*SELECT COUNT(DISTINCT CategoryName)
FROM Categories*/

--2 ������� ����� ������� � ������ ���������?
/*SELECT CategoryName, count(*) AS Count
FROM Categories cat, Products prod
WHERE cat.CategoryID=prod.CategoryID
GROUP BY cat.CategoryName*/

--3 ��������� ������� ��������� ������� ��������� �� ������ ���������
/*SELECT CategoryName as '��� ���������', avg(prod.UnitPrice) as '������� ���� �� ��.'
FROM categories cat, products prod
WHERE cat.CategoryID=prod.CategoryID
GROUP BY cat.categoryname*/

--4 ������� ������� �������, ��� ��������� ������� ��������� ��������� ������� ���������
--������� � ��������������� ������?
/*SELECT count(unitprice) as average
FROM products p1
WHERE unitprice >
	(SELECT avg(unitprice)
	FROM products p2
	GROUP BY categoryid
	HAVING p1.categoryid=p2.categoryid)*/

--5 ��������� �.4 ��� ������ ��������� �������, ������������ ��������� �� ����������
/*SELECT categoryname, count(unitprice) as average
FROM categories cat, products p1
WHERE p1.categoryid = cat.categoryid and p1.unitprice >
	(SELECT avg(p2.unitprice)
	FROM products p2
	WHERE p1.categoryid=p2.categoryid)
GROUP BY categoryname
ORDER BY average*/

--6 � �������� ������� ������������� ���������� �������?
/*SELECT count(distinct country)
FROM suppliers*/

--7 ������� ������������ ������� ��������� �� ������ ������? ������������ ��������� ��
--�������� ���������� �������
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






 
