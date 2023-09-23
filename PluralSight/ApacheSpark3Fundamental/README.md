# Overview
- Understand how Apache Spark works
- Processing data wit RDDs and DataFrames
- Optimizing Spark applications
- Working with new features of Spark 3
- Delta Lake, for Streaming and Cloud

# Apache Sparks 3 Fundamentals

## Overview
- Understand what is Apache Spark and how it works
- Setup Apache Spark environment
- Work with RDDs
- Clean & transform data with DataFrames
- Work with Spark SQL, UDF and common operations
- Perform optimizations in Spark
- New features in Spark 3
- Build reliable Data Lake with Delta Lake
- Handle streaming data with Structured Streaming
- Work with Spark in cloud

**What we'll be using**
- Python with Spark (called PySpark)
- SQL language
- Jupyter notebooks on local machine
- PyCharm IDE
- Azure subscription to work in cloud

**Summary**
- Need for Apache Spark
- Spark architecture and ecosystem
- How execution happens in Spark
- Spark supported API

## Need for Apache Spark
- Extremely powerful analytics engine for large scale distributed data processing, whether structured or unstructured
- In-memory engine can run workloads up to 100x faster than Hadoop
- Simplified code and multiple language support
- Unifies variety of use cases - batch processing, stream processing, machine learning and advanced analytics

# Understanding Spark Architecture and Ecosystem

## Spark Architecture

**Spark Cluster:** as your computer, install with single nodes or multiple nodes
**Cluster manager:** For efficient resource allocation on Spark cluster
**Distributed File System:** like HTFS store data
**Spark Engine:** actual distributed processing engine
**Spark Core:** core library, set of core APIs

**Spark engine and core provide in-memory processing capabilities that allow Spark to run massive speeds and all other basic functionality like memory management, fault tolerance, task scheduling, monitoring and vv**

**Spark SQL:** Batch processing - module allows fỏ structured data processing, not only SQL, ETL pipeline can be built using this library
**Streaming:** Streaming processing
**MLLib:** Machine learning
**GraphX:** Graph computation

## Spark Ecosystem

**Cluster Managers**
- YARN, Kubernetes, Mesos etc
**Distributed File System options**
- HDFS, Azure Data Lake Store, Amazon S3 or Google Cloud Storage
**Multiple language support**
- Scala, Python, SQL, R and Java
- Open-source support for C#
**Development options**
- Console, IDEs (PyCharm, VS Code), Notebooks (Jupyter, Zeppelin) etc.
**Available in Cloud Platforms**
- Databricks, Cloudera, Azure Synapse Analytics, Azure HDInsight, Amazon EMR etc

## Open source Connectors

- Relational databases - SQL Server, Oracle
- NoSQL - MongoDB, Cassandra, Azure Cosmos DB
- Apache Hadoop, HBase, Hive
- Cloud storage
- MPP engines - AWS Redshift, Azure Dedicated SQL
- Visualuzation tools - Power BI, Tableau
- Streaming - Kafka, Azure Event Hubs, AWS Kinesis
- ...and much more

## How Execution Happens in Spark?

- Cluster is a group of machines / nodes
- Cluster Manager allocates resources to Spark Applications on Cluster
- Spark Application is a set of processes, has Driver and Executor processes
- Driver takes input from user, determines how to execute job, not actually execute it, only analyzes job and distributes work to executors
- Executors are responsible for executing the work (or code) and returns result back to Driver

**Driver Process**
- Spark Session is the entry point to all functionality of Spark
- Use Spark Session to read file, create objects, run queries etc

**NOTE**
- each core run one task
- how many task base on how many partitions split the file
- output not combine to one file, it will be output files of each tasks

**To improve Parallelization**
- Increase number of Executors
- Add more cores to each executor
**But provisioning too many resources results in under utilization (wastage)**

**Spark Application**
**Job**
- Job is created when you need to execute code and take action (getting back results)
**Partitions**
- A partition is a chunk of data
- Driver decides how many partitions to be created
- Number of tasks = number of partitions
- Each task processes only one partition
**Cores/Threads/Slots**
- Each core can execute only one task at a time
- Number of parallel tasks = Number of cores

## Spark APIs

**Resilient Distributed Datasets**
- Introduced with inception of Spark
- Native data structure (Spark Core library)
- RDD represents collection of data in memory. Ex - When file is loaded in memory, it is call RDD
- All processing in Spark happens on RDDs
- Write code using low-level RDD APIs
* APIs load data in memory as RDDs and process them
* All languages supportes - Scala, Java, R and Python
- Spark does not apply any optimization to RDD code

**DataFrames**
- Introduced with Spark 1.3
- Based on RDDs
- Collection of data, but in tabular format
- No compile-time safety
- Spark applies optimizations to code
- Supported in all languages

**Datasets**
- Introduced with Spark 1.6
- Based on RDDs
- Combination of RDDs and DataFrames
- Provides compile-time safety
- Spark applies optimizations to code
- Supported in Java and Scala

## Summary

**Apache Spark handles modern data processing needs**

**In-memory analytics engine that runs on a cluster**
- Spark Core and Engine performs distributed processing
- Built-in libraries for various uses cases - batch processing, streaming, ML, graph computations
- Uses cluster manager and HDFS

**Distributed execution architecture**
- Spark application creates Driver and Executors
- Driver creates a Spark Session
- Data is divided into Partitions
- Task is allocated to a core to process a data partition

**RDDs are native data structure (uses RDD APIs)**

**DataFrames have tabular form (uses DataFrame API)**

**Structured API = DataFrame API + Dataset API**
- Typed APIs - Scala and Java
- Untyped APIs - Python and R


# Setting up Spark Environment

## Overview

**Understand Spark Environments**
- Development options, cluster managers, execution modes etc
**Install Spark and configure environment**
**Monitor Spark applications**
**Development options**
- Command line / Spark shell
- Jupyter notebooks
- PyCharm IDE
- Spark-submit command
**Setup multi-node cluster**

## Understanding Spark Environments

**Spark Development Options**
- Command line / Spark shell
- Notebooks 
* Jupyter, Zeppelin
* Can run locally or in cloud platforms like Azure HDInsight and Google Dataproc
- IDEs to build projects
* IntelliJ, PyCharm, VS Code
* Run code locally, or build and run in Spark cluster
- Spark Submit command to run jobs
- Cloud platform notebooks
* Offered by Databricks, Azure Synapse Analyrics, etc

**Cluster Managers**
Manage and allocatates resources to applications on the cluster
- Local
- Standalone
- YARN
- Mesos
- Kubernetes

**Application Execution Modes**
- Local Mode
- Client Mode
- Cluster Mode

**Local Execution Mode**
local[1]
- Single thread is used
- Driver runs all the jobs
- No executors are created
local[3]
- Three thread are created in same JVM
- Executors run tasks
- Simulation of production cluster environment

**Note**
- How it works?: Driver and Executors on same JVM
- Cluster Managers: Local
- Development Tools: Spark Shell Notebooks IDEs
- Purpose: Run locally for dev/testing

**Client Execution Mode**
- Driver runs on client machine
- Each executor runs as a separate JVM process in cluster

**Note**
How it works?: Driver on client, executors on cluster
Cluster Managers: YARN [client] Standalone
Development Tools: Spark Shell Notebooks Spark-submit
Purpose: Interactive querying, Data analysis

**Cluster Execution Mode**
- Driver and Executors run on cluster
- Each process consumes resources on cluster
- Used to run production workloads

**Note**
How it works?: Driver and executors in separate JVMs on cluster
Cluster Managers: YARN [cluster] Standalone Kubernetes Mesos
Development Tools: Spark-submit Cloud notebooks
Purpose: Long running jobs in production

## Spark-submit
**Utility to submit a Spark Application / Job to a cluster**
**Code can be in any language**
- Scala, Python or Java
**Can be submitted to any supported Cluster Manager**
- Local, Standalone, YARN, Mesos, Kubernetes
**Provide configuration and dependencies**
**Both Spark Shell and Spark Submit are command line**
- Spark Shell is typically used for interactive queriying
- Spark-Submit is typically used to submit long running jobs

## Summary
**Can work with Spark in various ways**
- Several development options and cluster managers
**Understood application execution modes**
- Local mode - Single JVM to run driver and executors
- Client mode - Driver on client and executors on cluster
- Cluster mode = Driver and executors run on cluster
**Spark can be installed on local machine or on cluster**
**Development Options**
- Command Line can be used for dev/testing
- Jupyter for interactive analysis or development
- PyCharm IDE for project development
- Spark-submit to run long running production jobs
**WebUI can be used for monitoring**

# Working with RDDs - Resilient Distributed Datasets

## Overview
- Understand RDDs
- Create RDDs
- Working with Pair RDDs
- Apply operations on RDDs
- Use narrow transformations
- Use wide transformations and data shuffling
- Spark application concepts

## Undestanding RDDs

Resilient Distributed Dataset (RDD) is the native Data Structure of Spark
- In-memory objects
- Do not have schema
- Distributed collection of elements
- All processing in Spark happens on RDDs

**Features of RDDs**
- In-memory: Resides in the memory of cluster
- Partitioned: Split into partitions, processed by tasks
- Read-only: Transformed into another RDD or result
- Resilient: auto recover in case of failure

**Note**
- Spark will re-execute failed Tasks using their Lineage Graph
- Only if the failure is transient, and not permanent (like divide by zero)

## Options to create RDD
- Parallelize a collection
- Read a File
- From another RDD

## Working with Pair RDDs
**RDDs with Key-Value pairs**
- Two items are linked together
- Key is identifier. Value is corresponding data
**Key need not be unique**
**Spark has special operations for Pair RDDs**
- reducebyKey, sortByKey, countByKey etc
- Some operations are costly

## RDD Operations

**Transformation Operation**
- Function that produces new RDD from existing RDDs
- Transformation operations help in building a Lineage Graph
- Example: Read a file, Convert sales amount from INR to USD, Filter records with sales amount greater than 1000 

**Action**
- Returns result of RDD computations
- Triggers execution of transformations using Lineage Graph
- Examples: Write the output to storage

**Note**
- Transformations are Lazy operations, which are only executed when an Action operation is applied
- Action operation is applied

## Narrow Dependency Transformation
- A transformation where each input partition is used at-most once to produce output partitions
- Each input partition is used at-most once to produce output partitions
- Extremely fast
- No data movement between partitons / No shuffling
- Example: Filter, Map, FlatMap, MapPartition, Sample, Union, etc

## Wide Dependency Transformation and Data Shuffling
- One output might be used multiple times to produce output partitions
- Requires shuffling of data between partitions
- Expensive operation
- Shuffle Read can only start when all data is written out as Shuffle Blocks

## Spark Execution Components
**Spark Application is a set of resources**
- Contains driver and executor processes
**Multiple jobs can run in an Application**
- Number of jobs = Action operations applied
**Each job is divided into Stages**
- Number of stages = Wide transformations + 1
**Stages are typically executed in sequence**
- When one stage finishes, then only next can start
- Exceptions - Join where 2 datasets can be read parallelly as separate stages
**Each Stage has its own set of Tasks**
- Number of Tasks = Number of partitions

## Summary
**RDD is native data structure of SPark**
- In-memory, Partitioned, Read-only and Resilient
**RDD can be created in many ways**
- Parallelize a collection, read a file or convert an RDD
**Pair RDD is an RDD with Key-Value pairs**
**Apply transformation and action operations on RDDs**
- Transformation gives new RDD. Action gives result
- Transformation are lazy operations.
**Transforamtion are of two types**
- Narrow - Each input partition is used at-most once
- Wide - An input partition may be used multiple times
**Data shuffling is a two step process**
**Application -> Jobs -> Stages -> Tasks**

# Cleaning and Transforming Data with DataFrames

## Overview
- Understand DataFrames and its optimiztion
- Create DataFrames
- Apply schema
- Analyze and clean data
- Apply transformations
- Handle corrupt data
- Save processed data to files

## Understanding DataFrames

**DataFrames**
- Part of Spark SQL library
- Built on top of RDDs (In memory, partitioned, read-only and resilient)
- Imposes a tabular structure on the data
- Spark engine can apply optimizations
- Less development effort
- Allows for structured data processing
- Supports variety of Data Types
-- Simple - String, Integer, Double, Boolean etc.
-- Complex - Array, Timestamp, Binary etc

**Spark Optimization Engines**
- Catalyst Optimizer: Query Optimizer to produce optimized query plan
- Tungsten Engine: Improve efficiency of memory and CPU for Spark applications

**Catalyst Optimization Phases**
- Analysis
- Logical Optimization
- Physical Planning
- Code Generation

## Create DataFrames

**Options to Create DataFrames**
- From RDD or Collection
- Read from Data Source (file, database etc)
- From another DataFrame

## Data Quality Checks
**Completeness**
- Remove null or missing data
- Fill missing values with placeholder
**Uniqueness**
- Remove duplicate records
**Timeliness**
- Appropriate date range
**Accuracy**
- Remove inaccurate data

## Options to Handle Corrupt Data
**Text formats (CSV and JSON) have built-in support for handling corrupt records**
**Support 3 Parse Modes while reading data**
- Permissive
- DropMalformed
- FailFast

## Apache Parquet
- Columnar storage format
- Support complex nested data strutures
- Stores schema in the file itself
- Supports efficient compression and encoding
- Binary files
- Querying is much faster than CSV/JSON

## Summary
**DataFrame APIs are higher-level Spark API**
**DataFrame have tabular structure - columns and rows**
**DataFrame API code undergoes optimization**
- Done using Catalyst optimizer's 4-stage process
- Tungsten engine improves memory and CPU efficiency
**Build optimized ETL pipeline**
- Create DataFrames by reading file or converting RDD
- Manually define schema or infer it
- Apply data quality checks like drop duplicates, fill missing data, remove nulls, remove invalid rows etc
- Tranform data by selecting, filtering, creating derived columns etc
- Handle corrupt data in textual files with ParseModes
- Save output to storage as Parquet files

# Working with Spark SQL, UDFs and Common DataFrame Operations

## Overview
- Run SQL queries on DataFrames
- Work with Spark databases and tables
- Work with user-defined functions (UDFs)
- Perform operations on multiple datasets
- Perform window operations

# Performing Optimization in Spark

## Overview
- Working with Spark partitions
- Change DataFrame partitions
- Memory management
- Persist data
- Spark join strategies and broadcast join
- Optimize join with bucketing
- Dynamic resource allocation
- Resource allocation using fair scheduling

## Workking with Spark partitions
















