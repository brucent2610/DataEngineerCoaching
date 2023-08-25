# Introducing
- How to create data pipelines
- Make your pipelines more resislient
- Advanced techniques
- Scale our pipelines

# Introducing Apache Airflow

## What is Apache Airflow?
- Open source platform to programmatically develop, schedule and orchestrate workflows.
- Write a Python file that describes the tasks to run and ensure execution and retries
- Workflows are defined as code, they become more maintainable, versionable, testable and collavorative

## Benefis Of Airflow
- Extensibility
- Reliability
- Scalable

## Getting A most of this course
**Required:**
- Proficiency in a programing language
- ETL
- Statistics
- Docker
**Course suggestions**
- Interpreting Data with Statistical Models
- Building Data Pipelines with Luigi and Python
- Core Python: Getting Started
- Docker: The Big Picture
**Not needed**
- Apache Airflow

## Outline
- Fundamentals: Architecture and core concepts
- Scheduling: Backfill and Catchup
- Decouple Pipelines: SubDAGs, Branching, and XComs
- Scaling Airflow: LocalExecutor and CeleryExecutor
- More Resources: Where to continue your journey?

# Dissecting (Phân tích) the Components of a Pipeline

## Architecture of Apache Airflow

**Example Workflow**
1. Download
2. Transform
3. Save
4. Notify and Report

**Scheduler**
- Trigger when Expected
- Trigger when Previous Failed
- Retry Tasks
- Alert if Failure Is Permanent

**Webserver**
- The way of graphically seeing workflow and status
- Easy operability and management

**Meta Database**
- Workflow executions
- Tasks success and length
- Users and Roles
- Connections outside of Airflow
- Communication layer between components

**Executor**
- Gets Tasks from Scheduler
- Executes Tasks
- Reports back the state of the Task

## How Do We Represent the Pipeline in Airflow

**Permitted Worflows**
- Workflows must not have loops
- Those will always end
- They are called **Direct Acyclic Graphs (DAG)**

**DAG Parameters**
- dag_id: Who are you?
- start_date: When should it start?
- schedule_interval: How often should it run?
- catchup: When should I rerun?

## Dissecting DAGs: Tasks and Operators

**Operators**
- Are Python objects that represent Tasks
- Can execute Airflow has many pre-made Operators
- To instantiate a Task we need to instantiate its Operator Object

**Operator Examples**
- BashOperator
- PythonOperator
- PostgresOperator
- SlackWebhookOperator

**Definition**
- DAG: Actual Pipeline to run
- Task: Actual instruction we need to perform
- A DAG is composed of Tasks in an order defined by dependencies
- Operator: Representation of a Task in code
- Each DAG execution is a DAGRun
- Each box is a TaskInstance (refers to an instantiation of Task to a given DAGRun)
- TaskInstance = Task + Point of execution

**Connections**
- A database connections
- A file path
- A Token to authenticate
- AWS Credentials

## Summary
- Check Task dependencies for loops
- Always define a start_date and schedule_interval
- Always define an ID for the DAG and each Task
- Test each Task separately

# Demystifying Common DAG Pitfalls

## Understand start_date and schedule_interval

**What happened in the DEMO?**
- When the date is before the start_date the DAG isn't triggered
- When the date is exactly at the start_date the DAG still isn't triggered
- When the DAG is triggered, the DAGRun execution date is different from the DAGRun triggered date

**Definition**
- start_date: Defines when the DAG will start
- schedule_interval: Interval between any two DAG executions

**Schedule Explained**
- Because the Date was set before the DAG's start_dae
- The DAGRun will execute after schedule_interval has passed
- If a DAG is scheduled to run at a given time, Airflow will wait for the schedule_interval to pass before triggering it

**Summary**
start_date: 1/11/2020 at 8AM and schedule_interval: @daily
- The DAGRun with execution_date 1/11/2020 at 8AM is actually triggered on 2/11/2020 at 8AM
- The DAGRun with execution_date 2/11/2020 at 8AM is actually triggered on 3/11/2020 at 8AM
- ...so on.

**Explanation**
- Because the date was set before the DAG's start_date
- Because the date was before the scheduled_interval has passed
- Because the execution_date is the date the DAGRun is scheduled, but triggering date is when it is triggered

## Summary
- The start_date represents the Date from which your DAG starts being scheduled.
- The schedule_interval represents the time the Scheduer waits from an execute_date to trigger a DAG
- For any date before the start_date of a TASK, The Task won't run and set as success
- If catchup is set to True, beware of setting the start_date in the future

## Tips
- Check the start_date is correctly set to the point in time you expect
- Rememeber any triggering happens after the schedule_interval has passed
- If the scheduler dies, check if any DAG has catchup set to True with a start_date way back
- You can debug when Airflow will trigger your DAGs changing local Date

# Abstract Functionality
- Macro
- Template

## Advanced DAG flow with Braching
**Templating in Python Functions**
- Accessing the execution_date in python functions is simple

**Note**
- If we have a BranchOperator on the end of a DAG, we must add a DummyTask as a default

**Summary**
- The Branch Operator enables perform conditionals
- The Branch Operator can be combined with Templating
- The Branch Operator must not be final within a DAG

**Condition task two options**
- PythonBranchOperator
- Trigger Rules

**Trigger Rules In Detail**
- all_success
- all_failed
- one_success
- one_failed
- all_done
- none_failed

## Summary
- We can access Variables and Macros with {{}}
- The BranchOperator enables conditionals, but can not be final Task of DAG
- We can leverage Trigger Rules to execute depending on parents result
- Extending BaseOperator creates custom Operators
- Airflow Plugins enable easy sharing of Operators

## Tips
- Check within the documentation the templated_fields of the Operator you use
- Check if the BranchOperator is being the final Task in some Branch of your DAG
- Remember to define custom Operators within the custom Plugin and put the plugin in the plugins folder

# Scaling Airflow

## Sequential, Local and Celery Executors
**Airflow Executors**
- SequentialExecutor: runs a single task instance at a time, no parallelism
- LocalExecutor: runs each task instance in a separate process in the same machine that the scheduler runs
- CeleryExecutor: runs each task instance in a specific worker node within a multi-node architecture. The scheduler will send a message to a queue (Redis, Celery broker) will redirect that to a given free worker that can execute it

**Comparing Executors**
- Sequential: setup easy, parallelism no, cost cheapest, use case Debug and developing DAGs
- Local: setup easy, parallelism yes depending on machine, cost cheap, use case small production environments, maintenance low
- Celery: setup complex, parallelism yes, cost expensive, use case large production environments, maintenance high

**Summary**
- Developing DAGs -> SequentialExecutor
- Starting in Production -> LocalExecutor
- High Airflow usage -> CeleryExecutor
- High spikes in Task usage -> CeleryExecutor in Kubernetes

# Summary
- To add parallelism switch from SequentialExecutor
- LocalExecutor runs each Task in its own process
- For more scalability use CeleryExecutor
- There are 4 concurrency parameters for each level: Task, DAG, Worker, and Airflow

# Tips
- Check Redis URL in Broker configuration if workers don't connect
- Check the Executor if you have parallelism
- Develop and Debug DAGs in SequentialExecutor
- Check concurrency parameters to increase parallerl TaskInstances

# Final Thoughts

## How Does Airflow fit into the future of ML?
**Machine Learning Stages**
- Data Ingestion and Preprocessing
- Model Training
- Model Validation and Deployment

**The Model Traing Pipeline**
- Download Data Script
- Train Model Script
- Validate and Deploy Script

**Problems Arise**
- Different model versions
- Data Models are variable
- Failover strategy

**Apache Airflow to the Rescue**
- Handles retries
- One DAG per Data Model
- Scheduling in the future
- Handles Model versioning