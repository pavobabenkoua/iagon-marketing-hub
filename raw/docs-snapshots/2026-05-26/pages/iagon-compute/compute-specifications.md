---
title: "Compute Specifications"
search: false
# Sidebar/nav label is set in docs/.vitepress/sidebar.ts
---
# Technical Details


## Installation and System Requirements

Users need to install the Iagon compute CLI application on their devices to participate in the Compute feature.

**System requirements include:**

- Available Storage
- CPU cores
- Available memory
- Virtualization support
- Internet bandwidth
- Publicly accessible IP

<!-- ## IAGON Compute Node as a Cardano Node
When node providers register their device for compute nodes, they can choose the ‘Run Cardano Node’ as a global task. When a global task is defined, the task manager immediately initiates the Cardano Node on the provided node.

**Minimum Requirements for Running Cardano Node**
- OS: Linux (Ubuntu 22.04)
- CPU: 4 Core, 2 GHz (Clockspeed), 3000 Multi Core EPS
- Memory: 32 GB
- Storage: 400 GB (SSD), 500 Mbps (Read), 400 Mbps (Write)
- Network: 150 Mbps Stable
- Storage Type: NVMe -->

### Evaluation Pass Criteria
*Values are the minimum requirements.*<br/>
*For how values are calculated see benchmarking process described below.*

- CPU: 60 IPS (EPS)
- Memory Bandwidth: 45000 Mbps (Read), 40000 Mbps (Write)\*
- Storage Bandwidth:
    - Sequential: 5000 Mbps (Read), 5000 Mbps (Write)
    - Random: 300 Mbps (Read), 300 Mbps (Write)
- Network:
    - Ping: 100 ms (max)
    -	Bandwidth: 150 Mbps (Download/Read), 150 Mbps (Upload/Write)
    -	Latency: 100 ms (max)

\* *Please note that these are not final evaluation criteria, and may change.*


## Evaluation Process

### CPU
Sysbench is employed to calculate events per second (EPS) as IPS metrics for the CPU. Sysbench CPU stress test is run to calculate 200000 max primes in single-threaded mode for a maximum of 10 seconds.

### Memory
Sysbench is used to measure read and write bandwidth. Sysbench memory test is run to test for both read and write of 20 GB data in 1 KB blocks for a maximum of 10 seconds in single-threaded mode.

### Storage
Fio is used to calculate sequential and random read/write bandwidth. Two fio jobs are executed for sequential and random read/write respectively with 1 GB data in 4 KB blocks for max 5 seconds.

### Network
It is similar to the calculation for storage nodes. 
For ping, we ping the nearest Cloudflare server for a minimum of 5 replies and take the average value. 
For bandwidth, we perform upload and download for 4 iterations; in each iteration we upload/download presets values of different byte sizes and calculate the average.
For latency, we use average latency while performing upload/download for bandwidth calculation.


## Running Tasks on the Iagon Compute network (Subscriber)

Users can use Iagon Compute Service to run their compute task on compute nodes.

Process to run a task on Iagon Compute:
- Subscription: Users subscribe to the Compute service.
- Task Submission: Users define and send tasks through the Compute App.
- Security Check: Tasks are filtered by the Security Guard to discard malicious ones, then encrypted and forwarded to the Task Distributor.
- Node Selection: Task Distributor selects a node based on user subscription, task requirements, and network availability, then sends the task.
- Task Execution: Compute node acknowledges the request and Task Manager decrypts and executes the task.
Result Delivery: Upon completion, task result is encrypted and sent back to the backend, then provided to the user.


## Running an Iagon Compute Node (Provider)

Anyone with the compute resource can join the Iagon Compute Service, given that the compute resource matches the minimum requirements set for running the node. One can follow the instructions to download and run node cli to evaluate the system performance for eligibility to run a Compute node.

**Register the Node**
First, the node provider should register the node. This can be done in two ways :

<!-- (decision pending) -->
- Using Node CLI: Node CLI binary is released, that the node providers can download on their system. Using this binary, they can evaluate and register.

<!-- - Booting Preconfigured IAGON Compute ISO: Preconfigured Ubuntu ISO is released, that the user installs and boot into. All the user permissions are preconfigured so that the node provider cannot access the system in high privileged mode to examine the task running. Disk encryption can also be preconfigured. All the required packages can also be preinstalled. -->

During registration:
- The system is evaluated by running different benchmarks. The Node Monitor service on the backend also tests if the node is accessible for an external network. 
- Once all the tests and evaluations are completed and the node has passed the criteria, the node gets registered and the provider gets the authorization key which is required at the next step and should be stored safely by the node provider. The provider needs to go to the provider section in the Iagon web app, add the auth key from the node, and stake the required amount to complete the registration.


## VM Runtime Component

Develop the VM runtime component responsible for:
- Initializing lightweight operating systems
- Virtualizing compute tasks
<!-- - Ensuring proper isolation and resource utilization within VMs -->

The Compute feature within the Iagon network provides users with the opportunity to contribute their device's computational resources and earn rewards. By monitoring system metrics, ensuring accurate measurement of compute data, and developing a robust VM runtime component, we aim to create a reliable and efficient compute solution for our users.

:::info
Work on Compute is in the early stages. Documentation may change and will be updated as we progress with the upcoming new features.
:::