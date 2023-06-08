# Structed Query Language (SQL) is a special-purpose programing language
## SQL's purpose
- To manipulate sets of data
- Typically from a relational database
- ANSI and ISO standards
## Database
- a container to help organize data. 
- a way to efficiently store and retrive data
## Relational
- a way to describe data and the relationships between data entities
## Basic SQL Commands
**SELECT**
- Retrieves one or more rows from one or more tables
```
SELECT first_name, last_name FROM contacts;
```
**INSERT**
- Add one or more rows into a table
```
INSERT INTO contacts (first_name, last_name) VALUES ("First Name", "Last Name");
```
**BULK INSERT**
- Insert multiple rows with one statement
- Either multiple values list or SELECT statement following table
```
INSERT INTO contacts (first_name, last_name) VALUES ("First Name", "Last Name"), ("First Name 2", "Last Name 2");
```
**UPDATE**
- Modifies one or more rows in a table
```
UPDATE contacts SET last_name = "New Last Name" Where id = 1;
```
**DELETE**
- Remove one or more rows from one table
```
DELETE FROM contacts Where id = 2;
```
## Querying Data with the SELECT Statement
**Way to Constrain the Number of Results**
- DISTINCT or NOT DISTINCT
- WHERE
- AND
- OR
- BETWEEN
- LIKE
- IN
- IS
- IS NOT
- GROUP BY
- ORDER BY
**Set Functions**
- COUNT
- MAX
- MIN
- AVG
- SUM
**HAVING**
- Works like WHERE works against SELECT
## Matching Different Data Tables with JOINs
**CROSS JOIN**
- Simplest JOIN
- All rows from both tables
- No WHERE clause
- Least useful
- Inefficient
- Cartesion Product
- CROSS keyword implied
**INNER JOIN**
- Most typical JOIN
- Emphasizes relational nature of database
- Matches column in first table to second
- Primary key to foreign key is most common
- INNER JOIN doesn't deal with NULL values
**OUTER JOINs**
- OUTER JOIN works event when no match
- NULL columns if no match in second table
- FULL OUTER JOIN returns all joined rows
- NULL when no match in either table
**LEFT OUTER  JOIN**
- Another NULL-related JOIN
- All rows from the left side will be returned
- NULL for non-matching right side table
**RIGHT OUTER JOIN**
- opposite of LEFT OUTER JOIN
- All rows from the right side will be returned
- NULL for non-matching left side table
**FULL OUTER JOIN**
- combine LEFT and RIGHT OUTER JOIN
**SELF JOIN**
- JOIN a table on itself
- Odd but sometimes useful
- No special syntax
- Same table on left and right side of JOIN
- Useful when table contains hierachical data
**DATA DEFINITION LANGUAGE (DDL)**
- SQL subset for creating databases and tables
- Most tools have a visual method
- Good to have an idea of what they are doing
**STANDARD SQL DATA TYPES**
- CHARACTER
- CHARACTER VARYING
- BINARY
- SMALLINT
- INTEGER
- BIGINT
- BOOLEAN
- DATE
- TIME
- TIMESTAMP
**NULL VALUES**
- NULL is a special value in SQL
- Indicates a lack of a value
- Columns can be required or not required
- Required is NOT NULL
- Not Required is NULL
**PRIMARY KEY**
- Must be a unique value per row
- Must be NOT NULL
- Can be a multiple columns (compound key)
**CONSTRAINT**
- Way to add keys in one grouping
- Primary or foreign 
**ALTER TABLE**
- Used to change an existing table
- Add/remove column
- Change column data type
- Change column constraints
- Must comport with current data
**DROP TABLE**
- Removes table and all data from database
- Error if table is a foreign key to another table
