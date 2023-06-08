## JOINS, UNIONS, AND SUBQUERIES
**JOIN**
- Combines columns from two or more tables in a single result set
- Major types of Joins
-- Inner Join
-- Outer Join (Left, right, full)
-- Cross join
**Inner Join**
- Inner Joins returns rows when there is at least one match in both tables
- Avoid ambiguity by qualifying each column name with table name
- Join tables based on relationships as well ad-hoc
- Operators for join
**Left Outer Join**
- LEFT OUTER join returns all the rows from the left table with the matching rows from the right table
- If there are no columns matching in the right table, it returns NULL values
**Right Outer Join**
- RIGHT OUTER join returns all the rows from the right table with the matching rows from the left table
- If there are no columns matching in the left table, it returns NULL values
**Full Outer Join**
- FULL OUTER join combines left outer join and right outer join
- This join returns rows from either table when the conditions are met and returns a null value when there is no match
- MySQL does not support FULL OUTER JOIN syntax
-- Simulate FULL OUTER JOIN using LEFT and RIGHT join withn UNION
**Cross Join**
- Cross join is a Cartesian Join that deas not necessitate any condition to join
- The result set contains records that are multiples of the record number of both the tables
**UNION Operators**
- UNION Combines two or more SELECT statements into a single result set
- Each SELECT statement of UNION operator must have the same number of Columns
- Union removes duplicate rows
- UNION ALL does not remove duplicate rows
- Only one ORDER BY clause sorting entire result set
- Simulate FULL OUTER JOIN using LEFT and RIGHT join with UNION
**JOINS vs SUBQUERIES**
Joins
- Can include columns from joining tables in the SELECT clause
- Easy to read and more intuitive
Subqueries
- Can pass the aggregate values to the main query
- Simplifies long and complex queries
**Correlated Subqueries**
- A correlated subquery is a subquery that is executed once for each row
- A correlated subquery returns results based on the column of the main query

## Functions
**Scalar Functions**
- A scalar function operates on a single value and returns a single value
-- String Functions
-- Numberic Functions
-- Date/Time Functions
**Control Flow Functions**
```
SET @Var = 1;
SELECT  CASE @Var
            WHEN 1 THEN 'one'
            WHEN 2 THEN 'two'
            ELSE 'more' END AS Result;

SET @Var = 1;
SELECT CASE WHEN @Var = 1 THEN 'one'
            WHEN @Var = 2 THEN 'two'
            ELSE 'more' END AS Result;

SELECT IF(1>2, 2, 3)
SELECT IF(1<2, 'yes', 'no')
SELECT IFNULL(1,0)
SELECT IFNULL(NULL,0)
SELECT IFNULL(1/0,'Yes')
SELECT NULLIF(1,1)
SELECT NULLIF(1,2)
```
**CAST Functions**
- CAST(): Cast a value as a certain type
- CONVERT(): Cast a value as a certain type
**Information Functions**
```
SELECT CHARSET("${database}");
SELECT COLLATION("${database}");
SELECT CONNECTION_ID();
SELECT CURRENT_USER(), CURRENT_USER;
SELECT DATABASE(), SCHEMA();
SELECT VERSION();
```
**Miscellaneous Functions**
```
SELECT NOW();
SELECT SLEEP(1);
SELECT NOW();
SELECT UUID();
```
**Aggreagte Functions**
- An aggregate function operates on a series of values and returns a single value
- Known as Column Function, as it typically operates on a value in column
- AVG and SUM functions return numeric value
- MIN, MAX, COUNT functions return numeric, date or string value
- Ignores the NULL value in Column (except COUNT function)
- Summary Query is a query with multiple aggregation functions
- Requires Group By in query if SELECT clause includes non-aggregate columns along with aggregation function

## Views
**Introduction**
- Technically views do not store any data. The data are retrieved at run time from the base tables
- MySQL supports nested view - a view that is based on another view
- MySQL doesnot support materialized view (a pre-computed data set derived from a query specification (the SELECT in the view definition) and stored for later use)
**Advantages of views**
Simplified Queries
- Summarize data from various tables and contain complex logic
Data Security
- Restrict access to data by using SELECT statement with WHERE clause
DML Operation Over Data
- Update, insert and delete data from base table (with restriction)
**With Check Option**
- A view created with With Check Option will prevent modifying a row in such a way that it would no longer be part of the view result

## Stored Procedures and Stored Functions
**Stored Procedures**
- A subroutine available to applications that access a relational database system
- Contains one or more SQL statements stored in the database
- Typical used for Data Validation as well Access Control Methods
- Called a sproc or procedure
- Parameters are used to pass one or more values from calling program
**Advantages of Store Procedures**
- Overhead
- Avoidance of Network Traffic - run directly within database engine
- Encapsulation of Business Logic
- Delegation of Access Rights
- Protection from SQL Injection

**Stored Functions**
- A Stored Function is an executable database object with SQL procedural code
- A Stored Function is often called a User Defined Functions (UDF) or just a function
- A function can't modify or change anything in the database by executing INSERT, UPDATE or DELETE statements
- The code to call Stored Functions is similar to built-in functions
- MySQL supports scalar functions, which return a single value

## Triggers and Events
**Triggers**
- A trigger is a block of code that is executed automatically when DML operations like INSERT, UPDATE or DELETE are executed
- Trigger execution is often called trigger firing
- Tiggers must be created with FOR EACH ROW clause as it creates a row level trigger firing for each row
- The OLD keyword gets a value from the rows that is being updated or deleted
- The NEW keyword gets a value from the rows that is being inserted or updated
**Events**
- An envent is a block of code that is executed automatically according to event scheduler
- Event execuation is often called event firing
- An Event can be a one time event as well recurring event
- The primary reasons to use events to do various maintenance taskes related to the table

