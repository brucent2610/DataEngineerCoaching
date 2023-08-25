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
**Open source Connectors**
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
- Spark Application is a set of processes
- Has Driver and Executor processes
- Driver takes input from user, determines how to execute job, analyzes job and distributes work to executors
- Executors are responsible for executing the work (or code)
- Spark Session is the entry point to all functionality of Spark
- Use Spark Session to read file, create objects, run queries etc

**To improve Parallelization**
- Increase number of Executors
- Add more cores to each executor
- But provisioning too many resources results in under utilization (wastage)

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

How it works?
- Driver and Executors on same JVM
Cluster Managers
- Local
Development Tools
- Spark Shell Notebooks IDEs
Purpose
- Run locally for dev/testing

**Client Execution Mode**
- Driver runs on client machine
- Each executor runs as a separate JVM process in cluster

How it works?
- Driver on client, executors on cluster
Cluster Managers
- YARN [client] Standalone
Development Tools
- Spark Shell Notebooks Spark-submit
Purpose
- Interactive querying, Data analysis

**Cluster Execution Mode**
- Driver and Executors run on cluster
- Each process consumes resources on cluster
- Used to run production workloads

How it works?
- Driver and executors in separate JVMs on cluster
Cluster Managers
- YARN [cluster] Standalone Kubernetes Mesos
Development Tools
- Spark-submit Cloud notebooks
Purpose
- Long running jobs in production