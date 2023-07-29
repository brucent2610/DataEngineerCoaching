# Understanding BigQuery in the GCP Service Taxonomy

## Overview
- Big Query is a cloud data warehouse
- Standard SQL and ODBC/JDBC drivers
- No clusters, no servers
- "No-ops" - not even indices (Chỉ mục)
- Autoscaling right to Petabytes
- Streaming and real-time analytics

## Transactional and Analytical Processing

**Transactional Processing**
- Analyzes individual entries
- Access to recent data, from the last few hours or days
- Updates data
- Fast real-time access
- Usually a single data source
**Analytical Processing**
- Analyzers large batches of data
- Access to older data going back months, or even years
- Mostly reads data
- Long running jobs
- Multiple data sources

**Small Data:** Both these objectives could be achieved using same database system
**Big Data:** Very hard to meet all requirements with the same database system
- Data distributed on a cluster with multiple machines
- Semi-structured or unstructured data
- No random access to data
- Data replicated, propagation (phát tán) of updates take time

### 3 Vs of Big Data
- Volume: Amount of data
- Variety: Number and type of sources
- Velocity: Batch and streaming

## Big Query

### Big Query and Tranditional Data Warehouse
**Big Query**
- Complex analytical queries
- Scales to Petabytes
- Both reads and updates
- Fast real-time or batch access
- Multiple data source
- Streaming as well as batch
**Traditional Data Warehouse**
- Complex analytical queries
- Scales to Petabytes
- Mostly reads
- Long running jobs
- Multiple data sources
- Often more focus on batch
### Big Query and Tranditional RDBMS

**Big Query**
- Access using SQL
- Scales to Petabytes
- No ACID or transaction support
- Serverless
- No indices, no provisioning
**Tranditional RDBMS**
- Access using SQL
- Usually top out (ra đi) at Terabytes
- Strong emphasis on ACID and transation support
- Classic example of server
- Heavy administrative overhead

### BigQuery Features
- Serverless: No cluster, no provisioning
- Autoscaling
- Automatic high availability

### Support for the 3Vs
**Volume:** Scales to Petabytes
**Variety** Federated data sources
- Cloud Storage
- BigTable
- Google Drive spreadsheets
**Velocity**
- Streaming ingestion
- Real-time queries

### SQL Support
**Standard SQL**
- ANSI:2011 compliant
- Extenstions for nested/repeated fields
**Legacy SQL**

### Data Locality
- Some support for specific locations
- US, Japan, EU

### BigQuery ML
- Currently in Beta
- Simple model building and use
- All in SQL from within BigQuery
- Not covered in this course

## GCP Storage Options

### BigQuery vs Cloud SQL
**BigQuery**
- Scale to Petabytes
- Serverless
- No-ops e.g no indices
- Automatic high-availability
- No ACID or transaction support
- SQL access
- Weak schema enforcement
**Cloud SQL**
- Top out at 20TB
- Requires cluster provisioning
- Manually design schemas, build indices
- High availability needs configuration
- Strong ACID and transaction support
- SQL access
- Strong schema enforcement

### BigQuery vs BigTable
**BigQuery**
- Scales to Petabytes
- Serverless
- Autoscaling - no need to design cluster
- Two-dimensional relational data
- SQL access
- Latency order of seconds
- Writes relatively slower than reads
- Relatively inexpensive
**BigTable**
- Scales to Petabytes
- Requires cluster provisioning
- Design cluster size, disk type and more
- Four-dimensional columnar data model
- NoSQL technology
- Latency order of milliseconds
- Extremely fast reads and writes
- Relatively expensive

### BigQuery and DataStore
**BigQuery**
- Scale to Petabytes
- Serverless
- Relational data
- SQL access
- Analytical queries
- OLAP
**Datastore**
- More effective at Terabyte scale
- Serverless
- Document-oriented
- NoSQL technology
- Hierarchical queries e.g in XML
- OLAP but has transaction support too

### BigQuery and AWS Redshift
**BigQuery**
- GCP data warehousing solution
- Serverless - no provisioning needed
- Autoscaling - no control over compute
- No operations needed
**AWS Redshift**
- AWS data warehousing solution
- Provisioning needed - more like BigTable
- Scale up by adding nodes
- Some operations and cluster maintenance indeed needed

## BigQuery Pricing

### Storage costs
**Active**
- Data in tables modified in last 90 days
- Currently approximately 2 cents/GB/month
- First 10 GB is free
- When table is edited, pricing reverts to active
**Long-term**
- Data in tables not modified in last 90 days
- About 50% lower, currently about 1 cent/GB/month
- First 10GB is free
- When table is not edited, pricing automatically drops to long-term

### Query Costs
**On-demand**
- Based solely on usage
- 5$ per TB/month, First 1TB/month free

**Flat-rate**
- Predictable, fixed monthly costs
- $40000/month for 2000 slots*; $10,000 per 500 additional slots

### BigQuery Slot
- Unit of computational capacity required to execute SQL queries. BigQuery automatically calculates how many slots are required by each query, depending on query size and complexity

### Free Operations
- Loading data - streaming inserts not free
- Copying data
- Exporting data
- Deleting datasets
- Deleting tables, views, partitions
- Metadata operations

### Minimizing Costs
**Query only columns you need**
- Under the hood, BigQuery is columnar
- Each column stored separately in encrypted, replicated file
**Use table preview to explore data**
- Don't run queries just to explore
**Calculate query price before running**
- dry_run flag in CLI
- query validator in UI
- GCP pricing calculator

## Summary
- BigQuery is a cloud data warehouse
- Standard SQL and ODBC/JDBC drivers
- No clusters, no servers
- "No-ops" - not even indices
- Autoscaling right to Petabytes
- Streaming and real-time analytics

# Using Datasets, Tables and Views in BigQuery

## Overview
- Datasets are containers
- Similar to databases in RDBMS
- Tables contain records
- Views are defined by query
- Non-materialized views

## BigQuery Data Model
**Datasets**
- Top level container used to organize the control access to tables and views. A table or view must belong to a dataset.
**Tables**
- Contains individual records organized in rows. Each record is composed of columns (also called fields)
**Views**
- Virtual table defined by a SQL query. Whenever a user queries the view, the underlying view-query is executed

### Data Location
- Geographic location can be specified at create-time
- After creation, location becomes immutable
- US, EU, Asia (Japan)

### Data features
- Access control at dataset level
- Labels can be assigned

### Public Datasets
- Stored in BigQuery
- Google pays for storage
- Available for general usage via a project
- User pays for queries

### Advantages of Views
- Reduce query complexity
- Restrict access to data
- Construct different logical tables from the same physical table

### Authorized Views
- Pattern to control access
- Leverage views and dataset-level access control

## Summary
- Datasets are containers
- Similar to databases in RDBMS
- Tables contain records
- Views are defined by query
- Non-materialized views

# Getting Data in and out of BigQuery

## Overview
- Inter-operability with cloud storage
- CSV, JSON and AVRO formats
- Partitioned tables

## Partitioned in BigQuery

### Paritioned Table
- A partitioned table is a special kind of table that is divided into segments, called partitions, that make it easier to manage and query your data

### Types of Partitioning
**Only 2 types in BigQuery**
- Based on ingestion-time
- Based on column

### Ingestion-time Partitioning
- BigQuery automatically loads
- Daily, date-based partitions
- _PARTITIONTIME pseudo-column

### Column-based Partitioning
- Partition on specific column
- Must be of type DATE or TIMESTAMP
- No _PARTITIONTIME pseudo-column
- Two special partitons (__NULL__,__UNPARTITIONED__)

### Partitioning and Sharding

**Partitioning**
- Data split logical horizontal groups
- Managed by BigQuery
- Metadata and access control automatically applied
- More efficient
- Less flexible

**Sharding**
- Data split logical horizontal groups
- Manually performed by user
- Metadata and access control must be individually applied to shards
- Less efficient
- More flexible

**Note:** Partitioned tables perform better in BigQuery as compared with sharded tables

# Performing Advanced Analytical Queries in BigQuery

## Overview
- BigQuery supports both nested and repeated fields
- Nested fields are effectively structs
- Repeated fields are affectively arrays
- Subqueries allow you to perform complex analysis
- Has support for windowing functions

## Normalized Storage in a Tranditional Databases

### Normalized Data
- Data is stored in a granular form to minimize redundancy
- Minimizes redundancy, optimizes storage
- Foreign keys to ensure valid joins
- Updates in one location, no duplication of data

### Denomorlized data
- Data is compressed into one table to be read in a single operation
- Disk space is very cheap
- No foreign key constraints
- Optimize the number of disk seeks
- Store data for an entity in one location
- Ignore redundancy, minimize joins

### Fields supporting
**Struct**
- Logical grouping of data
- Can hold fields of different types and values
- Each field within the nested field has its own name
**Array**
- Collection of values
- No fixed size
- Entities of the same type
- Can be primitive types or a collection of nested fields

## BigQuery Operators
**UNNEST**
- Splits an array field into individual rows
**ARRAY_AGG**
- Aggregates individual rows into an array field
**STRUCT**
- Aggregates individual columns into a struct

## Aggregations
- ANY_VALUE
- AVG
- COUNTIF
- STRING_AGG
- FORMATi

## Window Operation
- PARTITION BY
- ORDER BY

## Summary
- BigQuery supports both nested and repeated fields
- Nested fields are effectively structs
- Repeated fields are effectively arrays
- Subqueries allow you to perform complex analysis
- Has support for windowing functions

# Architecting Data Warehousing Solution Using Google BigQuery

## Overview
- Integation with visualization tools
- Datalab notebooks from within GCP
- Programatic access using Pythong library

## Google DataStudio
- Interactive dashboards and reports
- Connectors to GCP services and data stores
- Easy to share with team in your organization

## Google Cloud Datalab
- Datalab is a powerful interactive tool to build ML models on the GCP
- Data exploration and visualization tools
- Runs on a special VM which runs jupyter notebooks

## Summary
- Visualize data in BigQuery using DataStudio
- Programatically access BigQuery APIs from within Datalab

## Other Cloud Computing Platforms
- Building your first Amazon Redshift
- Introduction to the Azure Data Lake and U-SQL

## Other GCP Technologies
- Creating and Administering Google Cloud SQL Instances
- Architecting Google Cloud Storage configurarion

