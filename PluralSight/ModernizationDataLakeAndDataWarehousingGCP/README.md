# Building Data Warehouse
## Data Warehouse
- Consolidate data from many sources
- The data in a warehouse should have quantity, consistency and accuracy
- A data warehouse should be optimized for simplicity of access and high-speed query performance

**A modern data warehouse**
- Gigabytes to petabytes
- Serverless and no-ops including ad hoc queries
- Ecosystem of visualization and reporting tools
- Ecosystem of ETL and data processing tools
- Up-to-the-minute data
- Machine learning
- Security and collaboration

## Intro to BigQuery
**BigQuery has many capabilities that make it an ideal data warehouse**
- Gigabytes to petabytes
- Serverless and no-ops including ad hoc queries
- Ecosystem of visualization and reporting tools
- Ecosystem of ETL and data processing tools
- Up-to-the-minute data
- Machine learning
- Security and collaboration

## Getting Started
- BigQuery organizes data tables into units called datasets
- BigQuery datasets belong to project
- Access control to run a query is via Cloud IAM
- BigQuery datasets can be regional or multi-regional
- The table schema provides structure to the data
- Security, encryption and auditing for BigQuery
- BigQuery provides predifined roles for controlling access to resources
- Views add another degree of access control
- With the BigQuery Data Transfer Service, you can copy large datasets from different projects to yours in seconds

## Loading Data
**Batch load supports different file formats**
- CSV
- NEWLINE_DELIMITED_JSON
- AVRO
- DATASTORE_BACKUP
- PARQUET
- ORC

**Most common is loading data into BigQuery tables**
- Batch
- Periodic

**BigQuery address backup and disaster recovery at the service level (time travel)**

**BigQuery Data Transfer Service helps you build and manage your data warehouse**
- Managed service
- Automatic transfers
- Scheduled
- Data staging
- Data processing
- Data backfills

**Data Transfer Service provides SaaS connectors**

**BigQuery supports user-defined functions in SQL, Javascript, and scripting**

## Exploreing Schemas
- Designing schemas that scale is a core job of data engineers

## Schema Design
- Normalize for efficiency in transactional databases (only if table has <1M rows or 10GB)
- Denormalize before loading into a data warehouse
- Grouping on a 1-to-many field in flattened data can cause shuffling of data over the network
- Nested and repreated columns improve the efficiency of BigQuery with relational source data

## Nested and Repeated Fields
- STRUCTS (RECORD)
- ARRAYS (REPEATED)
- ARRAYS can be part of regular fields or STRUCTS
- A single table can have many STRUCTS

## Optimizing with Partitioning and Clustering
- Reduce cost and amount of data read by partitioning your tables
- BigQuery supports three ways of partitioning tables
+ Ingestion time
+ Any column that is of type DATE or TIMESTAMP
+ Integer-typed column
- Partitioning can improve query cost and performance by reducing data being queried
- BigQuery automatically sorts the data based on values in the clustering columns
- In streaming tables, the sorting fails over time and so BigQuery has to recluster
- BigQuery will automatically recluster your data

### Organize data through managed tables
**Partitioning**
- Filter storage before query execution begins to reduce costs
- Reduces a full table scan to the partitions specified
- A single column results in lower cardinality (e.g thousands of partitions)
+ Time partitioning (Pseudocolumn)
+ Time partitioning (User Date/Time column)
+ Integer range partitioning
**Clustering**
- Storage optimization within columnar segments to improve filtering and record colocation
- Clustering performance and cost savings can't be accessed before query begins
- Prioritized clustering of up to 4 columns, on more diverse types (but no nested columns)

## Transforming Batch and Streaming Data
- Data Processing: Data is processed in an intermidiate system before it is loaded into the analytics warehouse.
+ Cloud Dataproc
+ Cloud Dataflow
- Streaming Data Processing: Data flows are buffered and processed rapidly in pipelines
+ Cloud Pub/Sub
+ Cloud Dataflow
+ BigQuery












