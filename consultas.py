SELECT categoria, AVG(precio) AS precio_promedio
FROM tiendas
GROUP BY categoria;

SELECT categoria, SUM(precio * cantidad_stock) AS valor_total_stock
FROM tiendas
GROUP BY categoria;


SELECT sucursal, SUM(total_venta) AS total_ventas
FROM ventas
GROUP BY sucursal;


SELECT cliente_id, SUM(monto_compra) AS total_compras
FROM compras
GROUP BY cliente_id
ORDER BY total_compras DESC
LIMIT 1;
