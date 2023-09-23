# Getting Started with Apache Kafka

## Overview

**High volume (số lượng):**
- Over 1.4 trillion messages per day
- 175 terabytes per day
- 650 terabytes of messages consumed per day
- Over 433 million users
**High Velocity (Tốc độ):**
- Peak 13 million messages per second
- 2.75 gigabytes per second
**High Variety:**
- Multiple RDBMS (Oracle, MySQL, etc)
- Multiple NoSQL (Espresso, Voldemort)

**Use Cases**
- Distributed systems design
- Cover each component
- Scenarious and walkthroughs
=> Big Data solutions with Apache Kafka

## Why Apache Kafka?
- What? **High-throughput** and **fault tolerant** distributed messaging system.

## Enterprise challenge with Data

**Data replication & Log shipping**
- RDBMS to RDBMS only
- Database-specific
- Tight coupling (schema)
- Performance challenges (log shipping)
- Cumbersome (subscriptions)

**Extract, Transform, and Load (ETL)**
- Typically proprietary and costly
- Lots of custom development
- Scalability challenged
- Performance challenged

**Messaging**
- Limited scalability (collect and distribute data as messages)
- Smaller messages (Larger messages can put severe strain on message brokers)
- Requires rapid consumption
- Not fault-tolerant (application)
- Perils of Messaging Under High Volume
- Perils of Messaging With Application Faults 

**Custom middleware magic**
- Increasing complex (Application changes, schema changes)
- Deceiving
- Consistency concerns
- Potentially expensive

## Isn't There a Better Way?
- Cleanly
- Reliably
- Quickly
- Autonomously

## Next-generation Messaging Goals
- High throughput
- Horizontally scalable
- Reliable and durable
- Loosely coupled Producers and Consumers
- Flexble publish-subscribe semantics

## Summary
- Kafka is a distributed messaging system
- Designed to move data at **high volumes**
- Addresses shortcomings of tranditional data movement tools and approaches
- Invented by LinkedIn to address data growth issues common to many enterprises
- Open-sourced under Apache Software Foundation in 2012
- First-choice adoption for data movement for hundreds of enterprise and internet-scale companies

# Getting to know Apache Kafka's Architecture

## Apache Kafka as a Messaging System

![Messaging System](https://imgur.com/MdM5IfS)

- Producers: Publish message to broker
- Consumers: Subcribe message from broker
- Topics: Collection or Group messages, consumers retreive messages in specific topic
- Brokers: Software process referred to as an executable or daemon service that runs on a machine (physical or virtual machine). Access resources on the machine (file system)

## Apache Kafka Cluster
- Grouping multiple Kafka brokers (Single Broker or multiple Broker on a single machine or brokers on different machines)

## Principles of Distributed Systems

**Distributed Systems**
- Collection of resources that are instructed to achieve a specific goal or function
- Consist of multiple workers or nodes
- The system of nodes require coordination to ensure consistency and progress towards a common goal
- Each node communicates with each other though messages

**Distributed Systems: Controller Election**
- Controller responsibility: Attendance (what worker available to work), Work items (has been committed and assign to worker), Status of the staff and progress of the tasks
- When tasks come in Kafka cluster, controller has to make a decision which workers should take it

## Reliable Work Distribution
- Worker availability and health
- Task redundancy

**Distributed Systems: Getting Work Done (Reliably)**
- Ensure work is assigned to a worker
- Each task given to a worker must also be given to at least one of the worker's peers in the event of unexpected catastrophe (thảm họa)
=> Relicas

## Distributed Consensus (Đồng thuận) with Apache Zookeeper

**Distrivbuted Systems: Communication and Consensus**
- Worker node membership and naming
- Configuration management
- Leader election
- Health status

**Apache Zookeeper**
- Centralized service for maintaining metadata about a cluster of distributed nodes
- Configuration information
- Heath status
- Group membership
- Some system depend on Zookeeper like Hadoop, Hbase, Mesos, Solr, Redis, and Neo4j
- Distributed system consisting of multiple nodes in an "ensemble"

## Summary
**Apache Kafka is Pub-Sub messaging system, consisting of:**
- Producers and Consumers
- Brokers within a Cluster
**Characteristics of distributed systems**
- Worker node roles: Controllers, Leaders, and Followers
- Reliability through replication
- Consensus-based communication
**Role of Apache Zookepper**

# Understanding Topics, Partitions and Brokers

## Apache Kafka Topics
**Central Kafka abstraction**
**Named feed or category of messages**
- Producers produce to a topic
- Consumers consume from a topic
**Logical entity** (only care topic to work with)
**Physical represented as a log**

## Event Sourcing
- An architectural style or approach to maintaining an application's state by capturing all changes as a sequence of time-ordered, immutable events

## Message Content
- Timestamp
- Referenceable identifier
- Payload (binary)

## The consumer offset and message retention policy

### The Offset
Use to maintain their autonomy as far as message consumption from a common topic
**A Placeholder**
- Last read message position
- Maintained by the Kafka Consumer
- Corresponds to the message identifier

### Message Retention Policy
- Apache Kafka retain all published messages regardless of consumption
- Retention period is configurable (Default is 168 hours or seven days)
- Retention period is defined on a per-topic basis
- Physical storage resource can constrain (ràng buộc) message retention

## Apache Kafka as a Distributed Commit Log

### Transaction or Commit Logs
- Source of truth
- Physically stored and maintained
- Higher-order data structures derive from the log (Tables, indexes, views, etc)
- Point of recovery
- Basis for replication and distribution

### Apache Kafka is
- Publish-subscribe messaging rethough as a distributed commit log
- Highly distributed raw database that brokers reads and writes using publish and subscribe

## Apache Kafka Partition in Detail

### Kafka Partitions
- Each topic has one or more partitions
- A partition is the basis for which Kafka can: Scale, Become fault-tolerant, Achive higher levels of throughput
- Each partition is maintained on at least one or more Brokers

**In general, the scalabilityy of Apache Kafka is determined by the number of partitions being managed by multiple broker nodes**

## Distributed Partition Management in Apache Kafka

### Partitioning Trade-offs
**The more partitions the greater the Zookeeper overhead**
- With large partition numbers ensure proper ZK capacity
**Message ordering can become complex**
- Single partition for global ordering
- Consumer-handling for ordering
**The more partitions the longer the leader fail-over time**

## Achiving Reliability with Apache Kafka Replication

### Something is Missing (What about fault-tolerance?)
- Broker failure
- Network issue
- Disk failure

### Replication Factor
**Reliable work distribution**
- Redundancy of messages
- Cluster resiliency
- Fault-tolerance
**Guarantees**
- N-1 broker failure tolerance
- 2 or 3 minimum
**Configured on a per-topic basis**

## Summary
**Detailed explanation of**
- Topics and Partitions
- Broker partition management and behavior
**Aligned with distributed systems principles**
- Broker leader election for partitions
- Work distribution and failover

# Producing Messages with Kafka Producers

## Basic create Kafka Producer

**Kafka Producer: Required Properties**
- boostrap.servers: Cluster membership: partition leaders, etc
- key and value serializers: Classes used for message serialization and deserialization

**Kafka Producer Record: Required Properties**
- topic: Topic to which the ProducerRecord will be sent
- value: The message content (matching the serializer type for value)
- partition: specific partition within the topic to send ProducerRecord
- timestamp: the Unix timestamp applied to the record
- key: a value to be used as the basis of determining the partitioning strategy to be employed by the Kafka Producer

### Best Practice: Define a Key**
**Two useful purpose:**
- Additional information in the message
- Can determine what partitions the message will be written to
**Downside:**
- Additional overhead
- Depends on serializer type used

**KafkaProducer instances can only send ProducerRecords that match the key and value serializers types it is configured with**

### Micro-batching in Apache Kafka
**At scale, efficiency is everything**
**Small, fast batches of messages:**
- Sending (Producer)
- Writing (Broker)
- Reading (Consumer)
**Modern operating system functions:**
- Pagecache
- Linux sendfile() system call (kernel)
**Amortization of constant cost**

**The RecordAccumulator gives the producer its ability to micro-batch records intented to be sent at high volumes and high frequencies**
**When a producer record has been assigned to a partition through the partitioner, It will get handed over to a RecordAccumulator, where it will be added to a collection of record batch objects for each topic partiton combination needed by producer instance**

## Message Buffering and Micro-Batching
- "batch.size"
- "buffer.memory"
- "max.block.ms"
- "linger.ms"

## Delivery Guarantees
**Broker acknowledgement ("acks")**
- 0: fire and forget
- 1: leader acknowledged
- 2: replication quorum acknowledged
**Broker responds with error**
- "retries"
- "retry.backoff.ms"

## Ordering Guarantees
**Message order by partition**
- No global order across partitions
**Can get complicated with errors**
- retries, retry.backoff.ms
- max.in.flight.request.per.connection
**Delivery semantics**
- At-most-once, at-least-once, only-once

## Advanced Topics Not Covered
- Custom Serializers
- Custom Partitoners
- Asynchronous Send
- Compression
- Advanced Settings

## Summary
**Kafka Producer Internals**
- Properties -> ProducerConfig
- Message -> ProducerRecord
- Processing Pipeline: Serializers and Partitioners
- Micro-batching -> Record Accumulator and RecordBuffer
**Delivery and Ordering Guarantees**
**Java-based Producer**

# Consuming Messages with Kafka Consumers and Consumer Groups

## Introduction and Apache Kafka Consumer Overview
**Kafka Consumer: Required Properties**
- bootstrap.servers: Cluster membership: partition leaders, etc
- key and value deserializers: Classes used for message deserialization

## Subscribing and Unsubscribing topics
**Subscribing** subscribe topics
**Un-subscribling:** unsubscribe for all topics

## Compare subscribe and assign APIs
**subscribe()**
- For topics (dynamic/automatic)
- One topic, one-to-many partitions
- Many topics, many more partitions
**assign()**
- For partitions
- One or more partitions, regardless of topic
- Manual, self-administering mode

## Single Consumer Topic Subscriptions
- Pull any and all partitions within the topic for new messages to consumer
- Depending on the number of topics and number of partitions within each of those topics

**=> Could be a lot of message polling by a single consumer**

## Single Consumer Partition Assignments
- A single consumer instance may want complete control over what partitions it want to poll messages from

## The Poll Loop
- Primary function of the Kafka Consumer - poll()
- Continuously polling the brokers for data
- Single API for handling all Consumer-Broker interactions - A lot of interactions beyond message retrieval

## Walkthrough: Consumer Polling
- SubscriptionState: When the subscriber assign method to invoked, the content of collections they were passed to are used to set fields within the SubscriptionState object
- ConsumerCoordinator: manage the offsets
- The fetcher servers as the reponsible object for most of the communication between the consumer and the cluster. It not actually communicate with the cluster
- Consumer Network Client: communicate with the cluster with client open and sending TCP packets
- Metadata: inital request is sent and received, the response is used to instantiate its internal metadata object

## Walkthrough: Message Processing
- The poll() process is a single-threaded operation
- Careful consideration should be made to how each record should be processed
- The more the consumer signs up for, the more it has to process and all within a single polling loop
- Single consumer may not be a feasible or rational idea

## The Consumer Offset in Detail
- The last committed offset: has confirmed to have processed depending on the configured offset/reset behavior, from partition viewpoint
- Consumer reads records from the last committed offset, it tracks its current position
- Log-end offset
- Un-committed offsets: between current position and the last committed offset

**enable.auto.commit**
**auto.commit.interval**

## Offset Behavior and Management

### Offset Behavior
**Read != Committed**
**Offset commit behavior is configurable**
- enable.auto.commit = true (default)
- auto.commit.interval.ms = 5000 (default): upper bound your record processing will be finished but it could also create an offset gap positions
- auto.offset.reset = "latest|earliest|none" (default): when consumer starts reading from a new partition
**Single Consumer vs Consumer Group**

**Kafka stores the committed offsets in a special topic called __consumer_offsets**

### Offset Managment
**Automatic vs Manual**
- enable.auto.commit = false
**Full control of offset commits**

### CommitSync and CommitAsync for Manual Offset Management
- commitSync: Synchronous - blocks until receives response from cluster. Retries until succeeds or unrecoverable error - retry.backoff.ms (default: 100)
- commitAsync: Asynchronous - non-blocking but non-deterministic. No retries. Callback option

## When to Manager Your Own Offsets Altogether

### Committing Offsets
- The commit process will take batch of records and ask the consumer coordinatr to commit them to Kafka cluster via the consumer network client which it does immediately
- When the offsets have been confirmed to be committed
- The consumer coordinator updates so the fetcher can always know what offsets have been committed and what next records it should be retrieving

### Going It Alone
- Consistency control - when is "done"
- Atomicity (nguyên vẹn) - exactly one vs At-least-once

## Scaling out with Consumer Groups

### Scaling-out Consumers
- A lot for a single consumer to manage retrieving and processing messages
- Isn't realistic to expect a single consumer application to take on the entire burden of message processing from potential large Kafka cluster environment
**=> The solution is to be able to scale out the number of consumers consuming messages**

### Consumer Groups
- Kafka's solution to Consumer-side scale-ut
- Independent Consumers working as a team ("group.id" setting)
- Sharing the message consumption and processing load (Parallelism and throughput, Redundancy, Performance)
- heartbeat.interval.ms = 3000: sending regular heartbeats at an interval. The group coordinator relies on this heartbeat to determine whether an individual consumer is alive and able to participate in group
- session.timeout.ms: group coordinator will wait after not receiving any heartbeats before it will consider the consumer failed and take corrective action

## Consumer Group Coordinator
**Evenly balances available Consumers to partitions**
- 1:1 Consumer-to-partition ratio
- Can't avoid over-provisioning
**Initiates the rebalancing protocol**
- Topic changes (partition added)
- Consumer failure

## Configuration and Advanced Topics

### Consumer Configuration
**Consumer performance and efficiency** 
- fetch.min.bytes
- max.fetch.wait.ms
- max.partition.fetch.bytes
- max.poll.records

### Advanced Topics Not Covered
**Consumer position control**
- seek()
- seekToBeginning()
- seekToEnd()
**Flow control**
- pause()
- resume()
**Rebalance Listeners**

## Summary
**Kafka Consumer Internals**
- Properties -> ConsumerConfig
- Message -> ConsumerRecord
- Subsciptions and assignments
- Message polling and consumption
- Offset management
**Consumer Groups**
**Consumer Configuration**
**Java-based Consumer**

# Exploring the Kafka Ecosystem and Its Future

## APache Kafka's Success and Challenges

### Primary Use Cases for Apache Kafka
- Connection disparate (khác nhau tạp nham) source of data
- Large-scale data movement pipelines
- "Big Data" integration

### Challenges Remain
- Governannce and Data Evolution
- Consistency and Productivity
- Big and Fast Data

## Challenges in Governance and Evolution 
- More data diversity is introduced from different systems
- Each producer publising massive amount of data into Kafka
- Consumbers recived any kind of value from data being produced
- The challenge is the lack of some common means of cataloging registering and reconciling the disparate message specifications and compatibility mappings between serializing producers and deserializing consumers

**Solution: Kafka Schema Registry**
- Apache Avro serialization format
- First-class Avro serializers and deserializers
- Schema registry and version management
- RESTful service discovery
- Compatibility broker
- Open source with Apache license

## Challenges in Consistency and Productivity
- A lot of duplication of effort in terms of writing producer and consumer applications connect the source and target together
- Working to integrate data stores, they are all more or less the same as relational database and nosql
- Lack of consistency in providing a common framework for integrating data sources and targets

**Solution: Apache Kafka Connect**
- Common framework for integration (Standardization of common approaches, Producers and Consumers)
- Platform Connectors (Oracle, HP, 50+ and growing)
- Connector Hub

## Challenges in Big and Fast Data
- With Kafka generally being positioned between these it would be need an army of producers and consumers to keep the steaming pipes flowing

**Solution: Kafka Streams**
- Leverages existing Kafka machinery
- Single infrastructure solution (at least for streaming-based processing)
- Embeddable within existing applications

## Summary
- Apache Kafka's unquestionable success
- Continued challenges in an everchanging industry
- Kafka is evolving (Schema Registry, Kafka Connect and Hub, Kafka Streams)
- Lots of technology, little time
- Apache Kafka is a solid bet






