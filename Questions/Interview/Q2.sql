WITH order_with_customer AS (
    SELECT 
        c.ORDER_ID, 
        c.CUSTOMER_NAME
    FROM ORDERS as o
    INNER JOIN CUSTOMERS as c ON c.CUSTOMER_ID = o.CUSTOMER_ID
)

SELECT 
    owc.CUSTOMER_NAME as 'Khách Hàng',
    pwc.PRODUCT_NAME as 'Nhóm sản phẩm',
    owc.WEBSITE as 'Website',
    SUM(oi.UNIT_PRICE * oi.QUANTITY) as 'Doanh Thu'
FROM ORDER_ITEMS as oi
INNER JOIN order_with_customer as owc ON oi.ORDER_ID = owc.ORDER_ID
INNER JOIN PRODUCTS as p ON p.PRODUCT_ID = oi.PRODUCT_ID
GROUP BY pwc.CUSTOMER_NAME, owc.WEBSITE, p.PRODUCT_NAME
ORDER BY 'Doanh Thu' DESC;

