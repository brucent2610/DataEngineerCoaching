# MySQL Indexing for Performance
## Types of Indexes
**InnoDB**
- ACID* Compliant 
- Transactional (Rollback, Commit)
- Row Level Locking
- Row data stored in pages as per Primary Key order
- Supports Foreign Keys
- No Full Text Search
**MyISAM**
- Not ACID* Compliant
- Non-Transactional
- Table Level Locking
- No Particular order for data stored
- Does not support relationship constraint
- Full Text Search
**Note**
ACID (Atomicity, Consistency, Isolation, Durability)

## B-Tree Index
- B-Tree index is often referred as an index
- Most storage engines support B+Tree Index
-- Each Leaf node contains a link to next node for the fast range traversals
-- Values are stored in order
-- Each leaf page is at same distance from root level
-- InnoDB storage uses B+Tree
**Advantages**
- B-Tree Index speeds up data access
-- Storage engine traveres from root node to leaf node with the help of pointers
- Increase performance of following query patterns
-- Full Value (e.g 'Pluralsight', 'Pinal Dave')
-- Leftmost Value of Column Prefix (eg 'Plural' from 'Pluralsight', 'Pinal' from 'Pinal Dave')
-- Range of Value (e.g 1 to 99, Aaron to Fritz, Aaron to Kei%)
- B-Tree stucture helps ORDER BY clause to increase the performance

## Clustered Index
- Clustered Index is just a different approach of data storage
-- Not really different of index
-- Not all storage engines support it
- Rows with adjacent (kế cận) key values are stored close to each other
- One clustered index per table

**Advantages**
- Related data is stored close to each other leading less disk I/O while retriveving or range data
- Faster data access as data and index are stored together at leaf node

**Disadvantages**
- Data insertion speed is dependent on the order of the Primary Key
-- Table needs to optimize if inserted data is not ordered by Primary Key
- Clustered index have minimal impact for in memory data
- Updating the clusted index column is expensive as data is moved based on its size to different location
- Page split occurs when new data is inserted leading to fragmentation
- Secondary index contains the location of the clusted index instead of row pointer, hence the size is larger 

## Secondary Index
- An index which is not clustered index is called as a secondary index
- Secondary Index in InnoDB does not store actual data but only contains the pointer to the data
- If there is a clusterd index on the table
-- Secondary Index will contain the pointer to clusterd index
- If there is no clusted on the table 
-- Secondary Index will contain the row pointer

## Visual Clustered B-Tree
- https://www.youtube.com/watch?v=Z-yFjC_qMQo

## Visual Secondary Index B-Tree

## Hash Index
- Hash Index is built on a hash table
- Increase performance for exact lookups
- For each row a hash code is generated
-- Generally different keys generate different hash code
-- Stores hash codes in index with pointer to each row in a hash table
-- If multiple values have same hash code, it will contain their row pointers in linked list
- Memory storage engine in MySQL supports explicit hash tables
- Very fast and effective as it resides in Memory

**Limitation of Hash Index**
- As Hash Index does not contain original data it is not effective in
-- Sorting
-- No Partial Matching (e.g first name starting with A)
- Only support Equal To ("=") operator
- Multiple values with same hash code, it will result in slow performance
-- Storage engine will follow each row pointers in the linked list and compare
-- Slow maintenance

**Adaptive (Bộ điều hòa) Hash Index**
- InnoDB storage engine supports adaptive hash index
- This is automatic process and no control/configuration
-- Possible to disable
- Hash indexes are built in memory on the top of frequently used B-Tree indexes
- **Adaptive Hash Index gives B-Tree indexes very fast hashed lookups for improved performance**
- Note: You can simulate Hash Indexes on the unsupported storage engine

## Other Indexs
- Spatial Indexes
-- MyISAM supports spatial indexes
-- MySQL GIS support is not exhaustive (mọi khía cạnh)
- Full Text Indexes
-- Just like search engines
-- Finds keywords in the text
-- They are MATCH AGAINST operations (not WHERE operation)
- Other Types
-- TokuDB - Fracial Tree Indexes
-- ScaleDB - Patricia tries
-- InfiniDB - Special Logic

## Summary
- Indexes improve query performance greatly in most of the cases
- Indexes reduce the random I/O of the storage system by converting it to sequential I/O whenever possible
- Indexes improve performance by avoiding sorting, using temporary tables and reducing additional network traffic

# Indexing Strategies for High Performance
## Effectiveness of Index
- Find rows matching a WHERE clause
- Eliminate rows by opting for MOST selective Index
- Retrieve rows from other table while joining multiple tables
- Finding MIN() or MAX() value
- Sort or Group Table
- Reducing I/O bottleneck by using Covering Index
## List Indexes
```
SHOW INDEX FROM ${table} FROM ${database};
SHOW INDEX FROM ${table};

SELECT *
FROM INFORMATION_SCHEMA.STATISTICS
WHERE TABLE_NAME = '${table}'
```
## Basic of Indexes

## Summary
- In most of the cases MySQL Engine knows the best indexes for optimal query performance
- Duplicate Indexes are allowed but they negatively impact performance
- Use keyword EXPLAIN with queries to get data related to query execution
- Use query hints rarely and sparingly

# Index Maintenance
## MySQL Query Optimizer
- MySQL Query Optimizer follows cost based algorithm
- The main cost metric is data accessed by the query
- Two different API calls to decide the selection of index for queries
- records_in_range() - returns number of records in range end points
- info() - returns various types of data and statistics

## Statistics
- Statistics are used when the storage engine does not provide accurate information to the query optimizer
- If statistics are very old or does not exist
- Query Optimizer can make sub-optiomal decisions
- Execuating ANALYZE TABLE will regenerate statistics

## InnoDB Statistics
- InnoDB stores statistics in memory rather than disk
- Statistics are generated by sampling a few random pages in the index
- The default sampled pages are 8
- Configured by innodb_stats_sample_pages variable
- Higher the sample pages more accuracy in statistics
- InnoDB statistics are updated when
- Table first opened (accessed)
- Table size changes significantly
- A size change of 1/16th OR
- Upon running ANALYZE TABLE

## Data and Index Fragmentation
- Fragmentation in B-Tree Indexes can lead to heavy I/O and nonsequential reads on disk, leading to poor query performance
- For optional performance it is essential for data to be organized in ordered sequance and closely placed in the leaf page
- To Reduce data Fragmentation run OPTIMIZE TABLE command on fragmented table
- Workaround: ALTER TABLE TableName Engine=EngineName
- To reduce index fragmentation drop and recreate the indexes
- Run at intervals based on your transactional operations

## Other Index Maintenance Tops
- Frequently review your indexes with help of
-- INFORMATION_SCHEMA
-- SHOW TABLE STATUS
-- SHOW INDEX
- Remove Duplicate Indexes
- Drop indexes which are not frequently used

## Summary
- With the help of the statistics MySQL Optimizer selects an optimal index for any query
- Statistics can be updated manually with the help of ANALYZE TABLE command
- Data and Index fragmentation can lead to poor performance of the query
- Command OPTIMIZE TABLE will reduce fragmentation in data tables
- Recreate Indexes to remove index fragmentation

# Checklists

## Slow Running Query
- Check for exessive indexing on the table
- Create new appropriate indexes
- Check index maintenance jobs
- Additional tuning tricks

## Drop Indexes
- Drop unused and duplicate indexes on the tables
- Drop least used indexes

## Create Indexes
- Create clustered index on table if neccessary
- Do not create indexes on every columns of table
- Create indexes for most critical queries for performance
- Narrow width indexes are preferred
- Careful with column order in indexes

## Index Maintenance
- Rebuild indexes at well defined intervals
- Update statistics before statistics become stale (ANALYSE TABLE)
- Reduce Fragmentation by optimizing table (OPTIMIZE TABLE)
