# EXCEPT
The EXCEPT operator in SQL is used to retrieve the unique records that exist in the first table, not the common records of both tables. This operator acts as the opposite of the SQL UNION operator.

#FILTER
```
SELECT
  COUNT(*) FILTER (WHERE conditional_expression)
FROM table_name;
-----
SELECT 
  COUNT(*) FILTER (WHERE device_type = 'laptop') AS laptop_views,
  COUNT(*) FILTER (WHERE device_type IN ('tablet', 'phone'))  AS mobile_views 
FROM viewership;
```

#DATE_PART and EXTRACT
```
DATE_PART('year', sent_date::DATE)
EXTRACT(MONTH FROM sent_date)
EXTRACT(MONTH FROM sent_date - interval '1 month')
CAST(measurement_time AS DATE)
MAKE_DATE(issue_year, issue_month, 1)
```

#WITH


# ROW_NUMBER and PARTITION BY
```
WITH trans_num AS (
  SELECT 
    user_id, 
    spend, 
    transaction_date, 
    ROW_NUMBER() OVER (
      PARTITION BY user_id ORDER BY transaction_date) AS row_num 
  FROM transactions)
 
SELECT 
  user_id, 
  spend, 
  transaction_date 
FROM trans_num 
WHERE row_num = 3;
```
```
SELECT 
  user_id,
  tweet_date,
  ROUND(AVG(tweet_count) OVER (
    PARTITION BY user_id     
    ORDER BY tweet_date     
    ROWS BETWEEN 2 PRECEDING AND CURRENT ROW)
  ,2) AS rolling_avg_3d
FROM tweets;
```
```
WITH 
yearly_spend AS (
  SELECT 
    EXTRACT(YEAR FROM transaction_date) as year, 
    product_id,
    SUM(spend) as curr_year_spend
    -- SUM(spend) FILTER (WHERE EXTRACT(YEAR FROM transaction_date) = EXTRACT(YEAR FROM transaction_date - interval '1 year')) AS prev_year_spend
  FROM user_transactions
  -- WHERE year = EXTRACT(YEAR FROM transaction_date - interval '1 year')
  GROUP BY EXTRACT(YEAR FROM transaction_date), product_id
  ORDER BY product_id
),
yearly_variance AS (
  SELECT 
    yearly_spend.year,
    yearly_spend.product_id,
    yearly_spend.curr_year_spend,
    LAG(curr_year_spend, 1) OVER (
      PARTITION BY product_id 
      ORDER BY product_id, year
    ) AS prev_year_spend
  FROM yearly_spend
)
SELECT 
  year,
  product_id, 
  curr_year_spend, 
  prev_year_spend, 
  ROUND(100 * (curr_year_spend - prev_year_spend)/ prev_year_spend, 2) AS yoy_rate 
FROM yearly_variance;
```
```
WITH searches_expanded AS (
  SELECT searches
  FROM search_frequency
  GROUP BY 
    searches, 
    GENERATE_SERIES(1, num_users))

SELECT 
  ROUND(PERCENTILE_CONT(0.50) WITHIN GROUP (
    ORDER BY searches)::DECIMAL, 1) AS  median
FROM searches_expanded;
```
```
WITH payments AS (
  SELECT 
    merchant_id, 
    EXTRACT(EPOCH FROM transaction_timestamp - 
      LAG(transaction_timestamp) OVER(
        PARTITION BY merchant_id, credit_card_id, amount 
        ORDER BY transaction_timestamp)
    )/60 AS minute_difference 
  FROM transactions) 

SELECT COUNT(merchant_id) AS payment_count
FROM payments 
WHERE minute_difference <= 10;
```
```
WITH calls AS (
SELECT 
  EXTRACT(YEAR FROM call_received) AS yr,
  EXTRACT(MONTH FROM call_received) AS mth,
  COUNT(case_id) AS curr_mth_call,
  LAG(COUNT(case_id)) OVER (
    ORDER BY EXTRACT(MONTH FROM call_received)) AS prev_mth_call
FROM callers
WHERE call_duration_secs > 300
GROUP BY 
  EXTRACT(YEAR FROM call_received),
  EXTRACT(MONTH FROM call_received)
)

SELECT
  yr,
  mth,
  ROUND(100.0 * 
    (curr_mth_call - prev_mth_call)/prev_mth_call,1) AS growth_pct
FROM calls
ORDER BY yr, mth;
```