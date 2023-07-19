# What is NoSQL?
- NoSQL - non relational database technology
- CAP Theorem
-- Consistency
-- Availability
-- Partition Tolerance

## Consistency and Comprimise
**Consistency**
**Comprimise**

## NoSQL Product Categories
- Key-Value Stores (eg: Redis)
- Document Stores (eg: CoachDB, MongoDB)
- Wide Column Stores (eg: ApacheHBase, Cassandra)
- Graph Databases (eg: Neo4j)

## NoSQL Do's and Don'ts
# Performance
- For certain types of queries, performance on NoSQL databases can be unacceptably slow
- For Line of Business application loads, relational databases will be just as fast, and far more robust/reliable
- But if you have just a few bits of information to fetch and enormous traffic and concurrency, NoSQL may be best
# Appropriateness
- Using relational databases for the following may be imprudent (Thiếu thận trọng)
-- Configuration data
-- Environment data, settings, etc
-- Log file, event data
- Using NoSQL for these would be extreme (Quá sức)
-- Stock trades
-- Accounting debits and credits
-- Credit card transactions
- Don't be a partisan (người ủng hộ), use the right tool for the job

## NoSQL vs Relational Databases

# Reason for NoSQL
- Financial
-- Open Source
-- Attacting VCs (Venture Capitalists - funding -> seems old fashioned)
- Demand
-- Web Scale
- Workload
-- Simple store and retrieve

# Reason for Relational Database
- Financial
-- Licenses acquired or irrelevant
-- Training and productivity
- Demand
-- Enterprise
-- Business to business
- Workload
-- Guaranteed consistency
-- Varied reporting and query

## Business Intellegence and Big Data

# NoSQL + BI
- NoSQL databases are not designed for query and data warehousing
- BI applications inolve models, models rely on schema
- Extract, transform and load (ETL) may be your friend
- Wide-column stores, however are good for "Big Data"
- Wide-column stores and column-oriented databases are similar technologically

# NoSQL + Big Data
- NoSQL and BIg Data are interrelated
- Typically Wide-Column stores used in Big Data scenarious
- Example: HBase and Hadoop
- Why?
-- Lack of indexing not a problem
-- Consistency not an issue
-- Fast reads very important
-- Distributed files systems important too
-- Commodity hardware and disk assumptions also important

## Is NoSQL right for your organization?

# Training
- Do your people already have strong relational database skills?
- What is the cost of cross-training them?
- How long will it take them to accumulate the same aggregate YOE?
- What benefit are you getting?

# Do you need OLTP?
- Is your data transaction-based?
- Is it complex in structure?
- How varied are your queries?
- Do you do a lot of reporting?
- Is lost data (due to abortive sessions) tolerable?

# Recruiting
- Are you hiring startup-ambitious people?
- Can you impose good tech screenings?
- Will your recruits know the same NoSQL database that you are using?

# Economics
- Most NoSQL databases are open source - There are still costs, but they increase with personnel, rather than number of customers
- Open source relational databases exists as well - MySQL and PostgreSQL
- In the cloud, it may not matter - PaaS databases eliminate server costs, Data sizes most impactful on cost
- Labor and productivity costs can be hidden

# Funding
- Venture-funded business may do well with NoSQL
- Perception of its scalability may help convince investors of your trajectory and readiness
- It's a hot buzz-phrase
- Many NoSQL companies are venture-funded too.

# Summing Up
- Line of Business -> Relational
- Large, public (consumer) - facing sites -> NoSQL

- Complex data structures -> Relational
- Big Data -> NoSQL

- Transactional -> Relational
- Content Management -> NoSQL

- Enterprise -> Relational
- Consumer Web -> NoSQL