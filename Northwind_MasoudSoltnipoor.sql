-- 1) چند سفارش در مجموع ثبت شدهاست ؟

use northwind;
select count(*) as total_orders from orders;


-- ================================================== --
-- 2) درآمد حاصل از این سفارشها چقدر بوده است؟

use northwind;
select od.OrderID, od.Quantity, p.Price, (od.Quantity * p.Price) total_price
from orderdetails od
join products p 
on od.ProductID = p.ProductID


-- ================================================== --
-- 3) 5مشتری برتر را بر اساس مقداری که خرج کهاند پیدا کنید 
											
with custumerOrder as (
	select o.OrderID, c.CustomerID, c.ContactName 
	from customers c
	join orders o
	on c.CustomerID = o.CustomerID
), orderdetails_products as (
	select od.OrderID, od.Quantity, p.Price, (od.Quantity * p.Price) total_price
	from orderdetails od
	join products p 
	on od.ProductID = p.ProductID
)
select CustomerID, ContactName, sum(total_price) sum_total_price  from custumerOrder co 
join orderdetails_products odp
on co.OrderID = odp.OrderID
group by CustomerID, ContactName
order by total_price desc
limit 5


-- ================================================== --
-- 4) میانگین هزین هی سفارشات هر مشتری را به همراه ID و نام او گزارش کنید.

with custumerOrder as (
	select o.OrderID, c.CustomerID, c.ContactName 
	from customers c
	join orders o
	on c.CustomerID = o.CustomerID
), orderdetails_products as (
	select od.OrderID, od.Quantity, p.Price, (od.Quantity * p.Price) total_price
	from orderdetails od
	join products p 
	on od.ProductID = p.ProductID
)
select CustomerID, ContactName, avg(total_price) avg_total_price  from custumerOrder co 
join orderdetails_products odp
on co.OrderID = odp.OrderID
group by CustomerID, ContactName
order by avg_total_price desc


-- ================================================== --
-- 5) مشتر یان را بر اساس مقدار کل هزینهی سفارشات رتبهبندی کنید،

with custumerOrder as (
	select o.OrderID, c.CustomerID, c.CustomerName 
	from customers c
	join orders o
	on c.CustomerID = o.CustomerID
), orderdetails_products as (
	select od.OrderID, od.Quantity, p.Price, (od.Quantity * p.Price) total_price
	from orderdetails od
	join products p 
	on od.ProductID = p.ProductID
)
select co.CustomerID, co.CustomerName, sum(total_price)  sum_total_price
from custumerOrder co 
join orderdetails_products odp
on co.OrderID = odp.OrderID
group by CustomerID, CustomerName
having  count(co.OrderID) > 5    
                  

-- ================================================== --
-- 6) کدام محصول در کل سفارشات ثبت شده بیشترین درآمد را ایجاد کرده است؟

select od.ProductID, p.ProductName, sum(od.Quantity * p.Price) total_price
from orderdetails od
join products p 
on od.ProductID = p.ProductID
group by p.ProductName, od.ProductID
order by total_price desc


-- ================================================== --
-- 7) هر دسته  چند محصول دارد؟

select c.CategoryName, count(p.CategoryID) cnt
from categories c
join products p 
on c.CategoryID = p.CategoryID
group by CategoryName
order by cnt desc


-- ================================================== --
-- 8) محصول پرفروش در هر دسته بر اساس درآمد را تعیین کنید

with highcost as
(select c.CategoryName, p.ProductName, sum(od.Quantity * p.Price) total_price
from orderdetails od
join products p 
on od.ProductID = p.ProductID
join categories c
on c.CategoryID = p.CategoryID
group by c.CategoryName, p.ProductName
order by total_price desc
)
select CategoryName, max(total_price) HighCost from highcost
group by CategoryName


-- ================================================== --
-- 9) 5 کارمند برتر که بالاترین درآمد را ایجاد کردند به همراه ID و نام + ‘ ‘ + نام خانوادگی گزارش کنید .

create view orderdetails_products as (
	select od.OrderID, (od.Quantity * p.Price) total_price
	from orderdetails od
	join products p 
	on od.ProductID = p.ProductID
)
select o.EmployeeID, concat(FirstName, " ", LastName) as FullName, sum(total_price) sum_total_cost 
from orderdetails_products odp
join orders o 
on odp.OrderID = o.OrderID
join employees e
on e.EmployeeID = o.EmployeeID
group by EmployeeID
order by sum_total_cost desc
limit 5


-- ================================================== --
-- 10) میانگین درآمد هر کارمند به ازای هر سفارش چقدر بودهاست؟

select o.orderID, concat(e.FirstName, " ", e.LastName) as FullName, avg(total_price) avg_salary
from orders o
join employees e
on o.EmployeeID = e.EmployeeID
join orderdetails_products odp
on o.orderID = odp.orderID
group by o.orderID, FullName
order by avg_salary desc


-- ================================================== --
-- 11) کدام کشور بیشترین تعداد سفارشات را ثبت کرد هاست؟

select distinct Country,
count(SupplierID) over (partition by Country) as cnt
from suppliers 
order by cnt desc


-- ================================================== --
-- 12) مجموع درآمد از سفارشات هر کشور چقدر بوده؟

with totalquntity as
(select distinct ProductID, 
		sum(Quantity) over (partition by ProductID) as TotalQuntity
from orderdetails
), totalsuppliercost as 
(select tq.ProductID,
		TotalQuntity, 
		SupplierID, 
		(price * TotalQuntity) as TotalCost,
		sum(price * TotalQuntity) over (partition by SupplierID) as TotalSupplierCost
from totalquntity tq
join products p
on tq.ProductID = p.ProductID
)
select  Country,
        sum(distinct TotalSupplierCost) TotalSupplierCost_Country
from totalsuppliercost ts
join suppliers s
on ts.SupplierID = s.SupplierID
group by Country


-- ================================================== --
-- 13) میانگین قیمت هر دسته چقدر است؟

select p.CategoryID, CategoryName, avg(Price) AvgPrice from products p
join categories c
on p.CategoryID = c.CategoryID
group by CategoryID
order by AvgPrice desc


-- ================================================== --
-- 14) ) گران ترین دسته بندی کدام است؟

select p.CategoryID, CategoryName, sum(Price) MaxPrice from products p
join categories c
on p.CategoryID = c.CategoryID
group by CategoryID
order by MaxPrice desc


-- ================================================== --
-- 15) طی سال 1996 هر ماه چند سفارش ثبت شد هاست؟

select distinct month(OrderDate) Month_ ,
count(OrderID) over (partition by month(OrderDate)) as TotalOrder
from orders


-- ================================================== --
-- 16) میانگین فاصل هی زمانی بین سفارشات هر مشتری چقدر بوده؟

with diffdate as (
select CustomerID,  
DateOrder, 
datediff(leadd, DateOrder) DiffDate
from (
	select CustomerID,
    date(OrderDate) as DateOrder,
	lead(date(OrderDate)) over (partition by CustomerID) as leadd
	from orders) as leadtable
)
select d.CustomerID, CustomerName, round(avg(DiffDate), 0) AvgDiffDate
from diffdate d
join customers c
on d.CustomerID = c.CustomerID
group by CustomerID, CustomerName
order by AvgDiffDate desc


-- ================================================== --
-- 17) در هر فصل جمع سفارشات چقدر بودهاست؟

select YearOrderDate, QuarterOrderDate, count(QuarterOrderDate) TotalOrders from (
select year(OrderDate) YearOrderDate, quarter(OrderDate) QuarterOrderDate from orders) as cte
group by YearOrderDate, QuarterOrderDate


-- ================================================== --
-- 18) کدام تامین کننده بیشترین تعداد کالا را تامین کرد هاست؟
with cte as(
select SupplierID, count(SupplierID) CountSupplier from products 
group by SupplierID
order by CountSupplier desc
)
select c.SupplierID, SupplierName, CountSupplier from cte c
join suppliers s
on c.SupplierID = s.SupplierID


-- ================================================== --
-- 19) میانگین قیمت کالای تامین شده توسط هر تامیکننده چقدر بوده؟ 

select p.SupplierID, SupplierName, round(avg(Price), 1) AvgPrice 
from products p
join suppliers s
on p.SupplierID = s.SupplierID
group by SupplierID, SupplierName
order by AvgPrice desc