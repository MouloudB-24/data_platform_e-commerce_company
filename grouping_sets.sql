SELECT 
	co.country,
	ca.category,
	SUM(s.amount) AS Total_sales
FROM "FactSales" s
INNER JOIN 
	"DimCategory" ca ON s.categoryid = ca.categoryid
INNER JOIN
	"DimCountry" co ON s.countryid = co.countryid
GROUP BY 
    GROUPING SETS (
        (1, 2),
        (1),
        (2),
        ()
    )
ORDER BY
	1,
	2;
