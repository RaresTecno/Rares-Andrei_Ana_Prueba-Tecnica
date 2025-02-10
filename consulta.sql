SELECT producto, SUM(cantidad) FROM ventas
WHERE fecha >= date_trunc('month', CURRENT_DATE) - INTERVAL '1 month'
AND fecha < date_trunc('month', CURRENT_DATE)
GROUP BY producto
ORDER BY SUM(cantidad) DESC
LIMIT 3;