---
title: "Compute Metrics"
search: false
# Sidebar/nav label is set in docs/.vitepress/sidebar.ts
---
# Compute Metrics


## Overview

This guide outlines the performance score calculation for devices contributing compute resources to our network. Each performance type is calculated using specific formulas, and this guide details each formula and its components.


## CPU EPS (Events Per Second)

In the evaluation of device performance, the CPU EPS (Events Per Second) score plays a crucial role. This metric quantifies the processing capability of the central processing unit in handling events within a specific timeframe. The calculation of CPU EPS involves a straightforward formula that considers various factors to determine the efficiency of the CPU. <br/>
The sigmoid function is used so that it has slow growth before and after the optimal range. Likewise, subtraction causes the origin point to be 0, 0 and have a good curve. <br/>
The CPU EPS performance score is calculated using the sigmoid function:

![CPU EPS](/img/computemetrics/1.CPUEPS(EventsPerSecond).png)

![CPU Graph](/img/computemetrics/cpsgraph.png)


## Uptime

When evaluating the reliability and availability of computing devices, one crucial metric to consider is the uptime score. The uptime score calculation provides valuable insights into the device's ability to remain operational and accessible over a specific period. This metric is particularly important for systems that require continuous operation and minimal downtime, such as servers, network devices, and critical infrastructure components. <br/>
The formula for calculating uptime is straightforward and involves determining the percentage of time during which the device was operational. <br/>
The Uptime performance score is calculated using the exponential decay formula:

![Uptime Score](/img/computemetrics/uptimescore.png)

The uptime score is a critical indicator of a device's reliability and availability. A higher uptime percentage signifies that the device experienced minimal downtime and was operational for the majority of the total time period. Conversely, a lower uptime percentage indicates frequent outages or periods of inoperability, highlighting potential reliability issues that may impact system performance and user experience.


## Memory Read/Write

### Read Score

Memory Read Score is a key measure that evaluates the efficiency of memory operations, specifically focusing on read operations. Understanding how the Memory Read Score is calculated provides valuable insights into the memory subsystem's performance and its impact on overall system responsiveness.

![Memory Read Score](/img/computemetrics/3.1_Memory_Read_Score.png)

The Memory Read Score calculation offers insights into how effectively the memory subsystem can retrieve data for processing within a given time period. A higher Memory Read Score indicates that the memory can quickly read and deliver data to the processor, enhancing overall system performance and responsiveness.

### Write Score

![Memory Write Score](/img/computemetrics/3.2_Memory_Write_Score.png)

### Memory Total Score

![Memory Total Score](/img/computemetrics/3.3_Memory_Total_Score.png)


## Network Read/Write

Network Throughput Score plays a pivotal role in evaluating the efficiency and capacity of data transmission across a network infrastructure. This metric quantifies the rate at which data is successfully transmitted between network devices within a specific timeframe, providing essential insights into network reliability and performance optimization. <br/>
The calculation of Network Throughput Score involves analyzing the volume of data transferred and the time taken to complete the transmission process.

### Network Download Score

![Network Download Score](/img/computemetrics/4.1_Network_Download_Score.png)

### Network Upload Score

![Network Upload Score](/img/computemetrics/4.2_Network_Upload_Score.png)

### Network Total Score

![Network Total Score](/img/computemetrics/4.3_Network_Total_Score.png)


## Storage Sequential Read/Write
Disk I/O (Input/Output) Performance Score serves as a critical metric for assessing the efficiency and speed of data storage and retrieval operations on disk drives. The calculation of the Disk I/O Performance Score involves analyzing the throughput and latency of read and write operations, providing valuable insights into the disk subsystem's performance and its impact on overall system responsiveness. <br/>
The formula for calculating the Disk I/O Performance Score encompasses the consideration of both read and write operations, taking into account the data transfer rate and access times.

### Sequential Read Score

![Sequential Read Score](/img/computemetrics/5.1_Sequential_Read_Score.png)

### Sequential Write Score

![Sequential Read Score](/img/computemetrics/5.2_Sequential_Write_Score.png)

### Sequential Total Score

![Sequential Total Score](/img/computemetrics/5.3_Sequential_Total_Score.png)


## Storage Random Read/Write

### Random Read Score

![Random Read Score](/img/computemetrics/6.1_Random_Read_Score.png)

### Random Write Score

![Random Write Score](/img/computemetrics/6.2_Random_Write_Score.png)

### Random Total Score

![Random Total Score](/img/computemetrics/6.3_Random_Total_Score.png)

### Disk Total Score

![Disk Total Score](/img/computemetrics/6.4_Disk_Total_Score.png)


## Total Score Calculation
The total performance score is calculated using the weighted sum of the individual scores:

![Total Score Calculation](/img/computemetrics/7_Total_Score_Calculation.png)