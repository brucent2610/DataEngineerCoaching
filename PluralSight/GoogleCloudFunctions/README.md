# Introducing Event-driven Microservices

## Why use Cloud Functions?
- Reduce Maintance
- Securing Your Code
- Easy to integrate with Services

## Google Cloud Compute Spectrum
- Compute Engine
- Kubernetes Engine
- App Engine
- Cloud Functions

# Breaking Down a Function

## Function Types
- HTTP Trigger
- Pub/Sub Trigger
- Storage Trigger

## Event Object
- eventId: String
- timestamp: String (ISO 8601)
- eventType: String
- resource: String
- data: Object

## Data Property
- HTTP: ExpressJS Request
- Pub/Sub Message: 
+ data: String (bytes)
+ attributes: Map (key: String, value: String)
+ messageId: String
+ publishTime: String
- Cloud Storage Object
+ Id, Name and Bucket
+ Time Created, Updated, and Deleted
+ Content Type and Metadata
+ Access Control Lists
+ Encryption

## Ending the Function
- HTTP: ExpressJS Response
- Pub/Sub and Cloud Storage Object: Callback