SELECT
	d.year,
	co.country,
	AVG(s.amount) AS average_sales
FROM "FactSales" s
INNER JOIN 
	"DimDate" d ON s.dateid = d.dateid
INNER JOIN
	"DimCountry" co ON s.countryid = co.countryid
GROUP BY 
	CUBE (1, 2)
ORDER BY
	1,
	2;