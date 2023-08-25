# Overview
- Where Composer fits in
- How Composer focuses on pipelines of system tasks
- Explore what a Composer environment is
- Understand the powerful suite of operators

# Introducing Google Composer
## Overview
- Workflow orchestration service on GCP
- Define pipeline as DAG
- Simple Python code
- Great visualization support
- Runs on Kubernetes
- Host of useful operators

## Composer for Pipeline Orchestration
**Definition**
- Composer is a pipeline orchestration technology similar to Oozie or Azkaban

**Using Composer**
- Write code for pipeline
- Copy into GCS bucket
- Airflow picks up and schedules
- Pipeline parallelized and executed

**Important Composer Concepts**
- Airflow 
- Composer
- Environment
- DAG
- Operator
- Trigger

### Airflow
- Apache Airflow (incubating)
- Create workflows as DAGs
- Airflow schedules and executes
- Ensures dependencies satisfied
- Simple Python API
- Scalable architecture
- Powerful operators
- Jinja templates
- Airflow workers
- Web server to managed pipelines
- Scheduler tracks and executes DAGs
- Celery task queue to scale workers
- Redis as message broker for Celery

### Composer
- GCP managed service for Airflow
- Airflow workers on GKE cluster
- Airflow metadata on Cloud SQL
- Airflow web server on App Engine Flex
- GCS bucket for DAGs

## Dataflow vs Composer

**Dataflow**
- Data processing pipelines
- Focus on windowing and streaming
- Complex to implement
- Cumbersome (cồng kềnh) to trigger
- Visualization UI exists but not central
- Few specialized operators
- Serverless, no clusters provisioned
- No access to compute nodes
- Apache Beam API

**Composer**
- General purpose pipelines
- Focus on scripting and Python
- SImple to implement
- Trivial to trigger
- Fundamentially UI-based
- Many helpful specialized operators
- Run on KUbernetes cluster
- Compute nodes in GKE cluster
- Apache Airflow API

**Using Dataflow**
1. Write code for Pipeline
2. Submit job for execution
3. Dataflow assigns workers to execute
4. Pipeline parallelized and executed

**Using Composer**
1. Write code for pipeline
2. Copy into GCS bucket
3. Airflow picks up and schedules
4. Pipeline parallelized and executed

## Apache Airflow

**Environment**
- Self-cointained Airflow deployment
- Google-managed tenant project
- Hosted entirely within a region

**DAG**
- Directed-Acyclic-Graph
- Defined in Airflow Python script
- Must execute instantaneously
- Merely DAG definition file
- Contains operators and dependencies
- Different tasks run on different workers
- DAG defined in global namespace
- Uses context manager
- Contains dependencies
- Copied to environment GCS bucket
- Scheduled and executed periodically

**Operator**
- Corresponds to one step in pipeline
- Each instantiation of an operator is one task instance
- Each task in intance exists inside pipeline
- BashOperator
- PythonOperator
- BranchPythonOperator
- SendGrid
- BigQuery
- Dataproc
- Cloud Storage buckets

**BashOperator**
- Cloud composer runs the provided commands in a Bash script on a worker
- Worker is a Debian-based Docker container and includes several packages (gcloud, bq, gsutil, kubectl)

**GCP Operator**
- Cloud Composer automatically configures an Airflow connection to the environment's project
- BigQuery operators query and process data in BigQuery
- Cloud Dataflow operators run Apache Beam jobs in Cloud Dataflow

**Email Operator**
- Use the EmailOperator to send email from a DAG. To send email from a Cloud Composer environment, you must configure your environment to use SendGrid

**Branching**
- BranchingPythonOperator expects a python_callable that return a task_id; The task_id returned is followed, and all of the other paths are skipped
- Never leav an empty path after branch - use dummpy task instead

**Trigger**
- Airflow scheduler monitors DAGs
- Triggers task instances whose dependencies have been met
- Runs each DAG one schedule_interval after start date
- Several trigger rules
- all_success
- all_failed
- one_failed
- one_success
- dummy

## Pricing
- Based on the size of Cloud Composer environment
- Per-minute billing
- In addition to charges for (Google Kubernetes Engine, Cloud Storage)

## Summary
- Workflow orchestration service on GCP
- Simple Python code
- Easy to visualize
- Runs on Kubernetes
- Host of useful operators

# Creating, Configuring and Accessing Environments
- Creating a Directed Acyclic Graph (DAG)
- Configuring trigger rules
- BashOperator
- PythonOperator
- BranchPythonOperator
- DummyOperator

# Managing and Monitoring Workflows

## Overview
- Setting Airflow and environment variables
- Copying files with GCS operators
- Sending emails with SendGrid
- SQL queries and CURD operations with BigQuery
- Dataproc Hadoop operators