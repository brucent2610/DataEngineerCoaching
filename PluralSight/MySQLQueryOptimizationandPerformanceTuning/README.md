# Optimizing Data Access

## Overhead
- More data does not hurt but if we get less we might have to re-write queries to get them in the future
- It is just an extra column in the result set, it does not hurt
- We are going to implement paging in application, let us get the entire result set now
- We are just retrieving one extra row, so do not worry about it

## Understanding Data Needs
- Retrieve rows which are required in the application
-- Using WHERE clause properly
- Retrieve columns which are required in the application
-- Avoid Using SELECT * and list Column Names in SELECT clause
- Avoid retrieving the same data multiple times
-- Use CACHE of applications to store data for the moment
- Order the data only if you are not ordering them in application
-- Use ORDER By in the SELECT clause rather than application

## Summary
- Do not retrieve the data which is not useful to the application
- Avoid using * (Star) in SELECT statement
- It is always a good idea to write new queries as well modify the existing ones instead of writing query which retrieve more than required now

## MySQL Query Optimization

# Execution Path of a Query
- Client -> Query Cache -> Parser -> Preprocessor -> Query Optimizer -> Query Execution Engine (Storage Engines -> Data) -> Client

# Client Protocols
- Fetch only the queries which are required by the application. Client request to MySQL Server
- MySQL Server will respond back only the rows which client wants to consume

# Query Cache
- First, MySQL engine checks for Query Text in Query Cache
- If Query Cache contains exactly the same query sent by Client
- Query Cache will return the result back to the client from cache without execute query
- When MySQL Engine does not find exact Query Text in Query Cache, It goes to Parser and Preprocessor

# Parser
- Take a single query 
- Divide into multiple tokens or operators 
- Build the parse tree
- The Parse tree is validated against MySQL's language grammar

# Preprocessor
- Check various privileges
- Check additional semintic

# Query Optimizer
- Evaluate various execution plans
- Find the best option to execute the query
**Responsibilities**
- Converts sub-optimal join types to efficient logic
- Reorder join tables
- Reducing constant expressions
- Optimizing algebraic rules
- Logic short circuit
- Optimal index usage
- Sort optimization
- Optimizing aggregate functions
**Limitations**
- No parallel query execution
- No consideration to parallel running query
- Dependency on storage engine statistics
- Fastest executing query vs Most resource optimized query
- Cost of stored routines (SP, Function) are not often considered in the cost of operation

## Query Executuin and Storage
- Execute the plan
- Every execution plan will have its own instance of a handler API
- Handler API will interface with Storage Engine (InnoDB or MyIsam)
- Get necessary data back to Query Executution Engine

## Return Result to Client
- Return data to Client
- If Query text cacheable, return cache result

## Query Optimizer
- Query Optimizer is a Cost Based Optimizer
-- Selects the path using least resources
- MySQL execution plan is tree of instructions
-- Use EXPLAIN EXTENDED
- Static Optimization
-- Inspection of parse tree
- Dynamic Optimization
-- Contextual inspection of various factors of query

## Maximizing Query Optimizer Performance
- Optimizing Data Access
- Understanding Query Optimization
- Query Re-write

## Understanding Query States
- SHOW FULL PROCESSLIST
-- Sleep
-- Query
-- Locked
-- Analyzing and statistics
-- Copying to tmp table
-- Sorting result
-- Sending data

## Understanding EXPLAIN Command
- EXPLAIN SELECT Query
-- id: 
-- select_type: SIMPLE
-- table: which table query
-- type: ALL (current table), ref (referenced from another table)
-- possible_keys: Possible Index can be used
-- key: Index key used
-- key_len: 
-- ref:
-- rows: how many rows go through
-- Extra: additional information

## Explain Extended Command
- Additional information of filtered column - we have not used any filtered or rare condition over here
- After EXPLAIN EXTENDED
- Execute SHOW WARNINGS command
- Showing new statement MySQL reconstructed our select query into Execution PLan
- Return different query but same result
- SHOW WARNING can see what actually MySQL is going to execute, the wat MySQL works, will reduce the burden on MySQL Optimizer works

## Summary
- MySQL Optimizer uses Cost Based Algorithm to find the most optimal plan for any query
- You can use command EXPLAIN to see details about Query Plans
- MySQL Storage Engine plays a key role in performance of query as the optimizer depends on it for various crucial information

# Performance Optimization by Practical Query Turning

## Index used for SELECT clause
- If you use * and if your data set is relatively larger -> MySQL will not use index which you have created on your WHERE condition

## One Complex Query and Multiple Simple Queries
- Messure Query cost
- SHOW STATUS LIKE 'Last_Query_Cost';
- There is no right or wrong answer
- If Multiple queries is better than one complex query but in reality we have more cost like building execution plan, building parse tree,  additional traffic between Client and MySQL Engine -> Multi Queries may not be that advantage to complex queries
- Try our various combination and see result
- If the query is not using the index, can re-write this query little bit and union them together

## Table Order in Join Clause - INNER JOIN
- In case of INNER JOIN, it does not matter what order we use tables in our join condition
- The result set is the same
- The cost of query also same

## Table Order in Join Clause - OUTER JOIN
- Joins are order may get different results sometimes
- Different performance if we are using OUTER JOINs

## Most Optimal Choice - Subquery vs Exist vs Joins
- Base on particular case, base on 
-- result set
-- the workload
- Good Idea to do performance test
```
delimiter //

```

## Tuning Aggregate Function
- If the using Aggregation MIN MAX in Index column indexed, ORDER that column and find min max value is optimal way, if not index maybe worse
- Only way figure out is to do performance test

## Tuning GROUP BY Clause
- In case one-to-one relationship between primary key and link columns together, choose the primary key

## Optimizing Paging with LIMIT Clause
- Strong suggest use power of database to do paging instead of bringing entire result set in application

## Impact on Performance of UNION and UNION ALL
- UNION: distinct result
- UNION ALL: not distinct result
- Strong suggest use UNION ALL but your business requirment is remove duplicate rows must use UNION

## Summary
- You can use EXPLAIN key words to check the execution plan of query
- Avoid using <> operator in query as it ignores index created on table
- Use UNION ALL in place of UNION if do not care about duplicate data
- Always test query with real data on your development server before deploying on production

# BEST PRACTICES
- Use EXPLAIN keyword to see the execution plan for the query
-- Check the index usage
-- Check rows scanned
- Use LIMIT 1 clause when retrieving Unique Row
-- Helps aggregate functions like MIN or MAX
- Try to Convert <> operator to = operator
-- = operator increases chances of index usage
- Avoid using SELECT *
-- Forces full table scan
-- Wastes network bandwidth
- Split big DELETE, UPDATE or INSERT into multiple smaller queries
- Use appropriate data types for columns
-- Smaller columns are faster performance
- MySQL query cache is case and space sensitive
-- Use same query case for repeat queries
- Index columns in the WHERE clause
- Index columns used in JOIN
- Use UNION ALL instead of UNION if duplicate data is permissible in result set
- Table order does not matter INNER JOIN clause is used
- If column used in ORDER BY clause are indexed they help with performance
- Use LIMIT clause to implemant pagination logic