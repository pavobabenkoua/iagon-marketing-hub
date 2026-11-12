---
title: "Decentralized Web Hosting"
# Sidebar/nav label is set in docs/.vitepress/sidebar.ts
---
# Decentralized Web Hosting


## Overview

Our decentralized web hosting system utilizes Iagon’s cutting-edge decentralized storage to offer a reliable and scalable solution for hosting websites. By distributing data across a network of nodes rather than relying on centralized servers, Iagon ensures redundancy and security. The Iagon Identifier seamlessly links domain names to specific folders in the Iagon Storage network, while data caching optimizes performance and encryption safeguards data integrity. Whether you're hosting personal blogs, business websites, or decentralized applications (dApps), Iagon's approach embodies the principles of trustless and transparent web hosting.
And this is just the beginning - there are more innovations and enhancements yet to come in the realm of decentralized web hosting.


## Key Features

### Decentralized Cloud Infrastructure
- Iagon operates on a decentralized model, distributing data across a network of nodes.
- Redundancy and fault tolerance ensure high availability.

### Trustless and Permissionless
- Users can host websites without relying on centralized providers.
- No need for intermediaries or third-party trust.

### Efficient Retrieval
- The Iagon Identifier validates requests and links domain names to specific folders in the Iagon Storage network.
- Users can access content seamlessly.

### Data Caching and Performance Optimization
- Frequently accessed data is cached, reducing latency.
- Caching mechanisms enhance performance for web content delivery.

### Cost-Effective and Transparent
- Users pay only for the resources they use.
- Transparent pricing and resource allocation.


## How does it work?

![Web hosting Architecture](/img/webhostnew1.1.png)

### User Interaction
- The process begins when a user interacts with their web browser (labeled as Browser).
- The user initiates a request to access a specific resource, such as a webpage or file.

### Iagon DNS Identifier
The Iagon DNS Identifier acts as a crucial link between our custom Iagon DNS (Domain Name System) and the files stored within the Iagon Storage network. When a user requests a resource, such as a webpage or file, the Iagon DNS directs the request to the appropriate files within our network.

#### Here’s how it works:
- Frequently accessed data (such as files, shards, or metadata) is temporarily stored in a cache.
- The cache acts as a buffer between the user’s requests and the Iagon Storage network.
- When a user requests a file, the system first checks the cache.
- If the file is found in the cache (a cache hit), it is served directly to the user.
- If the file is not in the cache (a cache miss), the system retrieves it from the Iagon Storage network and adds it to the cache for future use.
- Cached data remains available until it is replaced by other data or invalidated due to updates.

### Data Caching
Data caching within the Iagon ecosystem is a critical component enhancing data retrieval speed and efficiency.

#### Here's how it works:
- The Iagon cache stores Iagon-specific data, optimizing data retrieval and access.
- Frequently accessed data, including files, shards, or metadata, is temporarily stored in the cache.
- The cache acts as a buffer between the user’s requests and the Iagon Storage network.
- When a user requests a file, the system checks the cache first.
- If the file is found in the cache (a cache hit), it is directly served to the user.
- If the file is not in the cache (a cache miss), the system retrieves it from the Iagon Storage and adds it to the cache for future access.
- Cached data remains available until it's replaced or invalidated due to updates,

### Iagon API
- The user’s request is forwarded to the Iagon API.
- The Iagon API acts as an interface for communication with various Iagon services.
- The Iagon API communicates with the Iagon Storage network.
- It retrieves the requested resource (e.g., an HTML file).

### Serving Iagon Files
- The Iagon DNS serves the requested files from the Iagon Storage.
- The user’s browser receives the requested resource (e.g., an index.html file).

<br/>
