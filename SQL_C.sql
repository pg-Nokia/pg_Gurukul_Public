Retrieve customer details
select * FROM [SalesLT].[Customer];


Retrieve customer name data
select
Title,
FirstName,
MiddleName,
LastName,
Suffix
FROM [SalesLT].[Customer];

Retrieve customer names and phone numbers
select
Title+' '+FirstName AS Customer_Name,
SalesPerson
FROM [SalesLT].[Customer];

Retrieve a list of cities
SELECT
DISTINCT City,
StateProvince
FROM [SalesLT].[Address]
ORDER BY City;

Retrieve the heaviest products

SELECT TOP (10) PERCENT WITH TIES Name, Weight FROM SalesLT.Product ORDER BY Weight DESC;

Retrieve product details for product model 1
SELECT Name, Color, Size FROM SalesLT.Product WHERE ProductModelID = 1 ;

Filter products by color and size
SELECT ProductNumber, Name FROM SalesLT.Product WHERE Color IN ('Black', 'Red', 'White')  AND Size IN ('S', 'M');

Filter products by product number
SELECT ProductNumber, Name, ListPrice FROM SalesLT.Product WHERE ProductNumber LIKE 'BK%';

Retrieve specific products by product number
SELECT ProductNumber, Name, ListPrice FROM SalesLT.Product WHERE ProductNumber LIKE 'BK-[^R]%-__';

Retrieve customer orders
SELECT CompanyName from [SalesLT].[Customer];
SELECT SalesOrderID, TotalDue FROM SalesLT.SalesOrderHeader

Retrieve customer orders with addresses
SELECT c.CompanyName,so.SalesOrderID,so.TotalDue FROM SalesLT.Customer AS c
JOIN SalesLT.SalesOrderHeader AS so ON c.CustomerID = so.CustomerID;

/Retrieve a list of all customers and their orders
SELECT a.AddressType,a.CustomerID,so.AddressLine1,so.City,so.StateProvince,so.Postalcode,so.CountryRegion FROM SalesLT.CustomerAddress AS a
JOIN SalesLT.Address AS so ON a.AddressID = so.AddressID
WHERE a.AddressType = 'Main Office';

Retrieve a list of customers with no address
SELECT CustomerID,CompanyName,FirstName,LastName,Phone FROM SalesLT.Customer
SELECT AddressType,AddressID FROM SalesLT.CustomerAddress
SELECT a.CustomerID,a.CompanyName,a.FirstName,a.LastName,a.Phone,so.AddressID,so.AddressType FROM SalesLT.Customer AS a
JOIN SalesLT.CustomerAddress AS so ON a.CustomerID = so.CustomerID WHERE so.AddressID IS NULL;

Retrieve the order ID and freight cost of each order.
SELECT[SalesOrderID] ,ROUND(Freight, 2) AS FreightCost FROM SalesLT.SalesOrderHeader;

Add the shipping method.
SELECT [SalesOrderID],ROUND(Freight, 2) AS FreightCost,LOWER(ShipMethod) AS ShippingMethod FROM SalesLT.SalesOrderHeader;

Add shipping date details.
SELECT [SalesOrderID], ROUND(Freight, 2) AS FreightCost,LOWER(ShipMethod) AS ShippingMethod,YEAR(ShipDate) AS ShipYear,DATENAME(MONTH, ShipDate) AS ShipMonth,DAY(ShipDate) AS ShipDay FROM SalesLT.SalesOrderHeader;

Retrieve total sales by product
SELECT  p.Name AS ProductName,SUM(sod.LineTotal) AS TotalRevenue
FROM SalesLT.Product AS p
JOIN SalesLT.SalesOrderDetail AS sod ON p.ProductID = sod.ProductID GROUP BY p.Name ORDER BY TotalRevenue DESC;

Filter the product sales list to include only products that cost over 1,000
SELECT p.Name AS ProductName,SUM(sod.LineTotal) AS TotalRevenue FROM SalesLT.Product AS p
JOIN SalesLT.SalesOrderDetail AS sod ON p.ProductID = sod.ProductID WHERE p.ListPrice > 1000 GROUP BY p.Name ORDER BY TotalRevenue DESC;

Filter the product sales groups to include only total sales over 20,000

SELECT p.Name AS ProductName,SUM(sod.LineTotal) AS TotalRevenue FROM SalesLT.Product AS p
JOIN SalesLT.SalesOrderDetail AS sod ON p.ProductID = sod.ProductID WHERE p.ListPrice > 1000 GROUP BY p.Name HAVING SUM(sod.LineTotal) > 20000 ORDER BY
    TotalRevenue DESC;