---
title: "Compute Overview"
# Sidebar/nav label is set in docs/.vitepress/sidebar.ts
---
# Iagon Compute


## Overview
:::tip Iagon Compute is Coming Soon
Iagon Compute is an integral part of the Iagon blockchain ecosystem, designed to augment our decentralized storage solutions. This documentation provides an in-depth exploration of the architecture, functionalities, and tasks associated with Iagon Compute.
:::

Compute, a pivotal feature within the Iagon network, empowers users to harness the potential of their devices as nodes, thus contributing their computational resources to the network. In exchange, users receive rewards commensurate with their contributions. This document delineates the essential functionalities and prerequisites for the Compute feature.

### Objectives
- **Enhance Scalability**: Utilize idle computational resources to expand network capacity by utilizing users' devices as nodes to meet increasing demand.
- **Incentivize Participation**: Reward users for contributing resources and staking devices within the network.
- **Promote Decentralization**: Empower individual users to actively participate in computational tasks, mitigating centralization risks.
- **Enable Integration**: Facilitate easy integration with existing infrastructure and technologies to leverage Iagon Compute effectively.

### Features
- **Device Utilization**: Users can use their devices with good specifications as part of the Iagon network, turning them into nodes.
- **Node Contribution**: Users can contribute their device's resources to the Iagon network and earn rewards.
- **Staking Rewards**: Users can earn staking rewards by staking their devices within the Iagon network.

### Functionalities
- **Device Performance Calculation**: Iagon Compute assesses device performance metrics such as read/write speed and network throughput to determine optimal resource utilization.
- **Node Selection**: When accessing files for download, Iagon Compute utilizes a tracker to identify available nodes and selects the most suitable ones based on performance and availability.
- **Reputation Scoring**: The system calculates reputation scores for nodes based on historical performance records, facilitating efficient resource allocation.
- **Compute Node Management**: Powerful compute nodes are requested to execute compute tasks. Static IPs are assigned to compute nodes for consistent accessibility.
- **Virtual Machine Configuration**: Clone the provided Git repository and run the application in an isolated virtual machine environment.
- **Metrics Tracking**: Various metrics including read/write operations, CPU usage, disk IO, network bandwidth, and resource consumption are tracked for both virtual machines and host systems.
- **VM Runtime Initialization**: Lightweight operating systems are pre-configured and virtualized to execute compute tasks efficiently.
- **Online Compiler**: Users can access a web console to write configurations and execute compute tasks. Subscribers have a CLI interface, which is bound to compute nodes for script execution and file manipulation.


## Basic System Overview

![System Architecture](/img/ComputeArchitecture.png)

### Iagon Compute Node
The Compute Node serves as the host device for computational processes within the Iagon network. Providers register their systems as Compute Nodes, which comprises of three key components:

- **Node CLI application**: This interface enables providers to register their nodes to Iagon Compute. It conducts benchmarking, verifies device eligibility, and requests hardware commitments from the provider. Upon meeting requirements, it provides an authentication key for registration and initiates the internal monitor server.

- **Internal monitoring Server**: It is the communication point for the central monitoring server and node. It is responsible to update the central server about the status of the node. The communication is established only after the node is registered in the provider dashboard.

- **Task Manager**: The computing process is done here. It takes the user's task details, computes the task, encrypts the result and sends it back to the central server to pass it back to the user.

### Compute Backend Server
It is a check server or the central management server (It can be a Hive Server*). It acts as a managing point between the user browsers and the computing nodes.

- **Node Monitor**: Compute backend server is responsible for keeping track of compute nodes connected to it. It constantly communicates with the internal monitoring server in the CLI application to monitor the node availability through heart beat, computational power status through different benchmarking checks, and keep the record of data received.

- **Security Guard**: It acts as a security guard for compute task requests from the subscribers, and filters and validates the requests for authenticity. Only valid requests pass through for processing, ensuring a layer of protection before reaching computing nodes.

- **Task Distributor**: It is responsible for determining the optimal node for user compute requests, ensuring that the node meets all the requirements as per the user's subscription.

### Provider Dashboard
It is a web interface for node providers to access general node overview, status, and performance data. It is created evaluating the data received by the central server from the internal monitoring server. Providers register their nodes using an authentication key from the CLI app and stake an amount for node activation. They can also view stake and reward information on the dashboard.

### Subscription Manager 
It offers various subscription packages for users to choose from based on their computing requirements. It ensures users’ subscription validity and provides renewal options for users.


## Stake IAG
To start receiving tasks from the network and get rewards, the node provider first enabled the node by staking IAG token. The authorization key received during registration is required to bind the node to the provider’s wallet so the rewards are provided to the provider.


## Receive Rewards
Once the staking is completed and the node gets enabled, the compute node starts receiving the task and the rewards get accumulated on the provider's account. Providers can collect rewards from the provider dashboard. 
To calculate the reward for the providers, Iagon uses an internal algorithm that uses data from the central server that contains information of different matrices of the compute node like uptime, performance, usage and evaluates it to give the reward value of their stake amount.


## Monitoring and Metrics

The system will continuously monitor hosts, virtual machines (VMs), and tasks running within the VMs to ensure proper utilization and isolation.
Metrics monitored include:
- **Host**: Memory usage, CPU usage
- **VM**: Memory usage, CPU usage, Read/write speed, Bandwidth of internet
- **Tasks within VMs**: Memory and CPU usage, Read/write speed, Internet bandwidth


## Accurate Measurement of Compute Data
Ensure accurate measurement and tracking of compute-related data, including:
- Read/write operations
- CPU usage
- Disk IO
- Network bandwidth

The Compute feature within the Iagon network provides users with the opportunity to contribute their device's computational resources and earn rewards. By monitoring system metrics, ensuring accurate measurement of compute data, and developing a robust VM runtime component, we aim to create a reliable and efficient compute solution for our users.

:::info
Work on compute is in the early stages. Documentation may change and will be updated as we progress with the next features.
:::

<br/>
