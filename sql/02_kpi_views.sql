-- 1. Total Revenue per Order
CREATE OR REPLACE VIEW total_order_revenue AS
SELECT 
    o.order_id,
    SUM(oi.quantity * p.unit_price) AS total_revenue
FROM order_items oi
JOIN orders o ON oi.order_id = o.order_id
JOIN products p ON oi.product_id = p.product_id
GROUP BY o.order_id;

-- 2. Total Revenue by Month
CREATE OR REPLACE VIEW revenue_by_month AS
SELECT 
    DATE_TRUNC('month', o.order_date) AS month,
    SUM(oi.quantity * p.unit_price) AS revenue
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
GROUP BY month
ORDER BY month;

-- 3. Revenue by Product
CREATE OR REPLACE VIEW revenue_by_product AS
SELECT 
    p.product_id,
    p.product_name,
    SUM(oi.quantity * p.unit_price) AS revenue
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY p.product_id, p.product_name
ORDER BY revenue DESC;

-- 4. Revenue by Region
CREATE OR REPLACE VIEW revenue_by_region AS
SELECT 
    c.region,
    SUM(oi.quantity * p.unit_price) AS revenue
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
GROUP BY c.region
ORDER BY revenue DESC;

-- 5. Top Customers by Revenue
CREATE OR REPLACE VIEW top_customers AS
SELECT 
    c.customer_id,
    c.customer_name,
    SUM(oi.quantity * p.unit_price) AS revenue
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
GROUP BY c.customer_id, c.customer_name
ORDER BY revenue DESC;
