WITH product_with_cat AS (
    SELECT 
        p.PRODUCT_ID, 
        pc.CATEGORY_NAME
    FROM PRODUCTS as p
    INNER JOIN PRODUCT_CATEGORIES as pc
), customer_with_contacts AS (
    SELECT 
        c.CUSTOMER_ID, 
        c.CUSTOMER_NAME, 
        contact.PHONE
    FROM CUSTOMERS as c
    INNER JOIN CONTACTS as contact ON c.CUSTOMER_ID = o.CUSTOMER_ID
), order_with_customer AS (
    SELECT 
        c.ORDER_ID, 
        c.CUSTOMER_NAME
    FROM ORDERS as o
    INNER JOIN customer_with_contacts as cwc ON cwc.CUSTOMER_ID = o.CUSTOMER_ID
)

SELECT 
    pwc.CATEGORY_NAME as 'Nhóm sản phẩm', 
    owc.CUSTOMER_NAME as 'Khách Hàng', 
    SUM(oi.UNIT_PRICE * oi.QUANTITY) as 'Doanh Thu', 
    owc.PHONE as 'Phone'
FROM ORDER_ITEMS as oi
INNER JOIN product_with_cat as pwc ON oi.PRODUCT_ID = pwc.PRODUCT_ID
INNER JOIN order_with_customer as owc ON oi.ORDER_ID = owc.ORDER_ID
GROUP BY pwc.CATEGORY_NAME, owc.CUSTOMER_NAME
ORDER BY 'Doanh Thu' DESC;