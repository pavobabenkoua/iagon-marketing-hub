---
title: "Compute Subscription"
search: false
# Sidebar/nav label is set in docs/.vitepress/sidebar.ts
---
# Compute Subscription


## Overview

The prices are based on the cost per GB of storage, the amount of RAM in GB, and the number of CPU cores.

### Pricing Formula

The pricing is calculated using the following formula:

```
Price = 4 * (CPU_cores + (RAM / 2) + (Storage / 100))
```
Where:
- `CPU_cores` is the number of CPU cores.
- `RAM` is the amount of RAM in GB.
- `Storage` is the storage amount in GB.


<!-- ```
Price per tier = Cost per GB * total GB offered + charges of services offered on each tiers

Per GB dollar value to be held = 0.2USD
```
<br/> -->

<!-- ## Pricing and Storage Comparison

| SNo | Name                  | Price Monthly ($) | Price Annually ($) | Total Storage GB | Base Storage Costs per year | Extra Features costs ($) | Extra Features(%) | 
|-----|-----------------------|-------------------|--------------------|------------------|-----------------------------|--------------------------|-------------------| 
| 1   | Iagonauts Basic       | 2.20              | 24                 | 1000             | 24                          | 0.00                     | 0.00%             | 
| 2   | Iagonauts Standard    | 11.00             | 120                | 4000             | 96                          | 24.00                    | 25.00%            | 
| 3   | Iagonauts Business    | 33.00             | 360                | 10000            | 240                         | 120.00                   | 50.00%            | 
| 4   | Iagonauts Enterprise  | 115.50            | 1260               | 30000            | 720                         | 540.00                   | 75.00%            | 
| 5   | New Users Basic       | 2.20              | 24                 | 500              | 12                          | 12.00                    | 100.00%           | 
| 6   | New Users Standard    | 11.00             | 120                | 2000             | 48                          | 72.00                    | 150.00%           | 
| 7   | New Users Business    | 33.00             | 360                | 5000             | 120                         | 240.00                   | 200.00%           | 
| 8   | New Users Enterprise  | 115.50            | 1260               | 15000            | 360                         | 900.00                   | 250.00%           |



## Iagonauts Subscription Tiers Overview

### Iagonauts Basic

| **Category**            | **Cost & Details**       |
|-------------------------|--------------------------|
| **Subscription Type**   |                          |
| Price Monthly           | $2.20                    |
| Price Annually          | $24                      |
| **Storage**             |                          |
| Total Storage GB        | 1000                     |
| Base Storage Costs/year | $24                      |
| **Extra Features**      |                          |
| Extra Features Costs    | $0.00                    |
| Extra Features (%)      | 0.00%                    |
| **Tokens & API**        |                          |
| \$ held                  | \$200                     |
| Tokens to be held       | 740.7407407              |
| API calls per day       | 20,000                   |
| **Website & Shards**    |                          |
| Website count           | 2                        |
| Total Shards count      | 7                        |
| Recovery Shards count   | 4                        |


### Iagonauts Standard

| **Category**                  | **Cost & Details**       |
|-------------------------------|--------------------------|
| **Subscription Type**         |                          |
| Price Monthly                 | $11.00                   |
| Price Annually                | $120                     |
| **Storage**                   |                          |
| Total Storage GB              | 4000                     |
| Base Storage Costs/year       | $96                      |
| **Extra Features**            |                          |
| Extra Features Costs          | $24.00                   |
| Extra Features (%)            | 25.00%                   |
| **Tokens & API**              |                          |
| \$ held                        | \$800                     |
| Tokens to be held             | 2962.962963              |
| **Website & Shards**          |                          |
| Website count                 | 5                        |
| Total Shards count            | 9                        |
| Recovery Shards count         | 4                        |


### Iagonauts Business

| **Category**                  | **Cost & Details**       |
|-------------------------------|--------------------------|
| **Subscription Type**         |                          |
| Price Monthly                 | $33.00                   |
| Price Annually                | $360                     |
| **Storage**                   |                          |
| Total Storage GB              | 10000                    |
| Base Storage Costs/year       | $240                     |
| **Extra Features**            |                          |
| Extra Features (%)            | 50.00%                   |
| **Tokens & API**              |                          |
| \$ held                        | \$2000                    |
| Tokens to be held             | 7407.407407              |
| API calls per day             | 70,000                   |
| **Website & Shards**          |                          |
| Website count                 | 7                        |
| Total Shards count            | 12                       |
| Recovery Shards count         | 5                        |


### Iagonauts Enterprise

| **Category**                  | **Cost & Details**       |
|-------------------------------|--------------------------|
| **Subscription Type**         |                          |
| Price Monthly                 | $115.50                  |
| Price Annually                | $1260                    |
| **Storage**                   |                          |
| Total Storage GB              | 30000                    |
| Base Storage Costs/year       | $720                     |
| **Extra Features**            |                          |
| Extra Features Costs          | $540.00                  |
| Extra Features (%)            | 75.00%                   |
| **Tokens & API**              |                          |
| \$ held                        | \$6000                    |
| Tokens to be held             | 22222.22222              |
| API calls per day             | 100,000                  |
| **Website & Shards**          |                          |
| Website count                 | 10                       |
| Total Shards count            | 14                       |
| Recovery Shards count         | 5                        |



### New Users Basic

| **Category**                  | **Cost & Details**       |
|-------------------------------|--------------------------|
| **Subscription Type**         |                          |
| Price Monthly                 | $2.20                    |
| Price Annually                | $24                      |
| **Storage**                   |                          |
| Total Storage GB              | 500                      |
| Base Storage Costs/year       | $12                      |
| **Extra Features**            |                          |
| Extra Features Costs          | $12.00                   |
| Extra Features (%)            | 100.00%                  |
| **Tokens & API**              |                          |
| $ held                        | -                        |
| Tokens to be held             | -                        |
| API calls per day             | 10,000                   |
| **Website & Shards**          |                          |
| Website count                 | 1                        |
| Total Shards count            | 6                        |
| Recovery Shards count         | 4                        |


### New Users Standard

| **Category**                  | **Cost & Details**       |
|-------------------------------|--------------------------|
| **Subscription Type**         |                          |
| Price Monthly                 | $11.00                   |
| Price Annually                | $120                     |
| **Storage**                   |                          |
| Total Storage GB              | 2000                     |
| Base Storage Costs/year       | $48                      |
| **Extra Features**            |                          |
| Extra Features Costs          | $72.00                   |
| Extra Features (%)            | 150.00%                  |
| **Tokens & API**              |                          |
| $ held                        | -                        |
| Tokens to be held             | -                        |
| API calls per day             | 20,000                   |
| **Website & Shards**          |                          |
| Website count                 | 2                        |
| Total Shards count            | 8                        |
| Recovery Shards count         | 4                        |


### New Users Business

| **Category**                  | **Cost & Details**       |
|-------------------------------|--------------------------|
| **Subscription Type**         |                          |
| Price Monthly                 | $33.00                   |
| Price Annually                | $360                     |
| **Storage**                   |                          |
| Total Storage GB              | 5000                     |
| Base Storage Costs/year       | $120                     |
| **Extra Features**            |                          |
| Extra Features Costs          | $240.00                  |
| Extra Features (%)            | 200.00%                  |
| **Tokens & API**              |                          |
| $ held                        | -                        |
| Tokens to be held             | -                        |
| API calls per day             | 30,000                   |
| **Website & Shards**          |                          |
| Website count                 | 3                        |
| Total Shards count            | 9                        |
| Recovery Shards count         | 4                        |


### New Users Enterprise

| **Category**                  | **Cost & Details**       |
|-------------------------------|--------------------------|
| **Subscription Type**         |                          |
| Price Monthly                 | $115.50                  |
| Price Annually                | $1260                    |
| **Storage**                   |                          |
| Total Storage GB              | 15000                    |
| Base Storage Costs/year       | $360                     |
| **Extra Features**            |                          |
| Extra Features Costs          | $900.00                  |
| Extra Features Costs          | $900.00                  |
| **Tokens & API**              |                          |
| $ held                        | -                        |
| Tokens to be held             | -                        |
| API calls per day             | 50,000                   |
| **Website & Shards**          |                          |
| Website count                 | 5                        |
| Total Shards count            | 10                       |
| Recovery Shards count         | 4                        |

<br/>
The Iagonauts tiers will be available to those who hold IAG tokens.

If the users haven't paid for the last 3 months the data will be deleted from Iagon storage.

:::info
The tiers will be defined according to compliances, app access level, quality of service(will update the parameters as we add them).
::: -->