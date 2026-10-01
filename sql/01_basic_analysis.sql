-- Basic order-status analysis
SELECT
    order_status,
    COUNT(*) AS order_count,
    ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 2) AS order_pct
FROM orders
GROUP BY order_status
ORDER BY order_count DESC;

-- Delivered orders available for delivery analysis
SELECT COUNT(*) AS delivered_orders
FROM orders
WHERE order_status = 'delivered';
