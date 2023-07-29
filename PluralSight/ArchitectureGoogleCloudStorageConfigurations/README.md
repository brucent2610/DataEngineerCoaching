# Understanding Cloud Storage in the GCP Service Taxonomy

## Overview
- Google Cloud Storage is a service for elastic object storage
- Ideal for unstructured data
- Four storage classes
- Coldline, nearline, regional, multiregional
- Many powerful features
- Many quirks too

## Computing Choice

### Cloud Computing
- The practice of using a network of remote servers hosted on the Internet to store, manage, and process data, rather than a local server or a personal computer.

### Choices in (Any) Computing
**Compute:** Where and how does code run
**Storage:** Where and how is the data stored
**Other choices - Networking, logging etc - are less important**

### GCP Compute Choices
- Google Compute Engine
- Google Kubernetes Engine
- Google App Engine
- Google Cloud Functions

## GCP Storage Technologies
**Unstructured Data**
- OLTP (Cloud SQL, Cloud Spanner)
- OLAP (BigQuery, BigTable)
**Structured Data**
- Block Storage (Persistent Disks - HDD,SSD, Local SSD)
- Object Storage (GCS Buckets)

## Persistent Disks and GCS Buckets
**Persistent Disks**
- Block storage
- Max 64TB in size
- Pay what you allocate
- Tied to GCE VMs
- Zonal (or regional) access
**Buckets**
- Object storage
- Infinitely scalable
- Pay what you use
- Independent of GCE VMs
- Regional or global access

## Working with GCS
- Web console
- gsutil command line utility (different from gcloud)

# Cloud Storage in the Taxonomy of GCP Storage Technologies
- Cloud Storage Buckets - Binary object storage
- BigQuery - Data warehousing (OLAP use cases)
- BigTable - NoSQL similar to HBase
- Datastore - NoSQL document database
- Cloud SQL, Spanner - Relational databases (OLTP use cases)

# GCP Storage Classes
**How often is a data item accessed?**
- Very rarely -> Cold Data -> Coldline
- Not that often -> Cool Data -> Nearline 
- All the time -> Hot Data -> Where is the data accessed from? -> Regional or Multi-regional 

**Note**
- Different storage classes represent different trade-offs
- Several parameters along which to compare

**Use cases**
- Multi-regional: Serving websites, interactive workloads, mobile and gaming applications
- Regional: Access from Compute Engine VMs or Dataproc cluster
- Nearline: Data backup, disaster recovery, archival storage
- Coldline: Legal or regulatory needs: also disaster recovery where recovery time is important

## Pricing of GCS Bucket
**Free tier**
- No charges below a limit
**Beyond that, charges for**
- Data storage
- Retrieval and early deletion
- Operations performed
- Network usage

## Summary
- Google Cloud Storage is a service for elastic object storage
- Ideal for unstructured data
- Coldline, nearline, regional, multi-regional
- Choose based on access pattern

# Creating and Using Cloud Storage Buckets

## Overview
- Object storage, not file storage
- GCS buckets contain objects
- Most important attribute is storage class
- Coldline, nearline, regional, multi-regional based on access pattern
- Key-value pairs associated with objects as metadata
- Object versioning for archival
- Lifecycle management of objects

## Uploading and Downloading Data

### GCS for Object Storage
**File Storage**
- Hierarchical structure
- Support for nesting and directories
- File-level locks
- File and directory headers
**Object Storage**
- Flat, non-nested structure
- Nested structure merely simulated
- No distributed lock - last write wins
- Unstructured series of bytes

**Note**
- Object deletion is permanent, GCP support can't undo

## Modifying the Storage Class of a Bucket and Object

### Object Storage Class
- Every bucket has an associated storage class
- Every object also has an associated storage class
- On creation, object inherits storage class of bucket

### Changing Storage Class of a Bucket
- Every bucket has a default storage class
- Default storage class specified during creation
- Default storage class can be changed subsequently
- Can not change multi-regional to regional (or vice versa)
- Other changes are fine

**When storage class of a bucket is changed**
- new objects subsequently added to bucket pick up change
- but existing objects in bucket keep their storage class

**Can change storage class of object**
- without changing storage class of bucket
- without moving object to different bucket
- without affecting URL of object

## Accessing and Modifying Object Metadata

### Object Metadata
- Objects have associated metadata - storage class
- Key-value pairs - fixed key metadata system creates keys

### Fixed-key Metadata
- Storage Class
- Access Control
- Cache Control
- Content Disposition
- Content Language
- Content Type

## Object Versioning
- Need to be enabled for bucket
- Once enabled, bucket creates archived versions of each object
- Whenever live object is overwritten or deleted version with unique generation number is created
- Each copy charged separately

**Can perform following additional operations if versioning enabled**
- List archived versions
- restore live version to previous
- permanently delete archived version

**Note**
- Versioning changes can take some time to propagate
- After enabling versioning
- Wait at least 30 seconds before deleting or overwriting

## Lifecycle Management
**Can automatically specify changes to object storage class**
- Change from regional to nearline after seven days
- Delete all data created before 1/1/2017
- Delete all but 3 most recent versions

**Supported conditions**
- Age
- CreatedBefore
- IsLive
- MatchesStorageClass
- NumberOfNewerVersions

**Supported actions**
- Delete

**Note**
- Eache rule consists of one or more condition and exactly one action
- If rule contains multiple conditions
- Action will be executed only of all conditions are met

## Summary
- Object storage, not file storage
- GCS buckets contain objects
- Most important attribute is storage class
- Coldline, nearline, regional, multi-regional based on access pattern
- Key-value pairs associated with objects as metadata
- Object versioning for archival
- Lifecycle management of objects

# Regulating Access and Using from Other GCP Services

## Overview
- GCS has powerful features
- Customer Supplied Encryption Keys (CSEKs)
- IAM and ACLs to restrict access
- Signed URLs for time-restricted access

## Using Customer Supplied Encrypted Keys

### Encryption
- Encrypted even at rest
- Default: Google generates keys
- Can use CSEK (Customer Supplied Encryption Key)

## Making Data Public

### GCS and Load Balancers
- Load Balancers to distribute incomming traffic - Usually, compute engine VMs as backend instances
- GCS bucket can be backend instances too - Great for serving static data

## IAM and ACLs

### Cloud IAM
- Identity and Access Management
- Used for all GCP resources
- Role-based Access Control (RBAC)
- Preferred to ACL-based access control

### Access Control Lists
- Each entry in an ACL includes
- Permission: What action can be performed
- Scope: Who can perform the specified action

### Restricting Access
**Cloud IAM**
- project level
- bucket level
**Access Control Lists**
- for individual objects
- e.g PII (Personally Identifiable Information)

## Time-limited Access Using Signed URLs
- Time Limited, signed URL
- Provide access without further authentication
- Specific operations can be specified

## Syncing Local Folders to GCS Buckets

## Summary
- GCS has powerful features
- Customer Supplied Encryption Keys
- IAM and ACLs to restrict access
- Signed URLs for time-restricted access


