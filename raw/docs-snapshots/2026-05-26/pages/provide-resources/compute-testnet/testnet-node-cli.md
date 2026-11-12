---
title: "Testnet Node CLI"
search: false
# Sidebar/nav label is set in docs/.vitepress/sidebar.ts
---
# Compute Mainnet Guide 

## Registering Iagon Compute Node using Compute Node CLI
Iagon Compute Node CLI is a CLI application which allows users to share their computational power on the Iagon network to earn rewards.

This document provides step-by-step instructions to help you install and set up Iagon Compute Node CLI on your system. Currently only Linux based OS are supported.

## Running Cardano Node CLI commands as a Compute task
Users can execute cardano-cli commands by specifying the arguments in the textarea and then clicking the "Run Command" button. For commands that require a file as input, there is an input form field available for specifying the filename in the command and providing the contents for that file.

## Installation
You can download the Official Compute Node CLI binary from the [Iagon's Github Release page](https://github.com/Iagonorg/Testnet-Compute-Node/releases).
Once downloaded, navigate to the CLI binary and mark it as executable:

```bash
chmod +rwx ./iag-cli-linux
```

Iagon Compute Node depends on 3rd party trusted packages to perform various benchmarks. These benchmarks help track the current performance and availability of the node in the Iagon Network for use.
These packages don't come bundled with the Iagon Compute Node CLI binary and have to be installed by the user.

### Minimum System Requirements

- OS: Linux (Ubuntu 22.04)
- CPU Cores Count = 4
- Memory = 8 GB
- CPU base ClockSpeed = 2 Ghz
- Storage = 100 GB
- Sequential Read Speed = 5000 Mbps
- Sequential Write Speed = 5000 Mbps
- Random Read Speed = 300 Mbps
- Random Write Speed = 300 Mbps
- Maximum Ping = 100 
- Maximum latency = 100
- Upload Speed = 150 Mbps
- Download Speed = 150 Mbps
- Memory Read Speed = 45000 Mbps
- Memory Write Speed = 40000 Mbps
- CPU EPS (Sysbench) Value = 20

:::info
These minimum system requirements are specifically for Previewnet.
:::
 
### Prerequisites
Before installing the Compute Node CLI, ensure the following prerequisites are met:

#### Port Forwarding
Enable port forwarding for both ssh server and the compute node binary on a static ip. These ports are to be provided during registration process and should be accessible from the internet.

#### Openssh Server
OpenSSH Server is required for remote access of Compute Nodes. If not already installed, you can install it via apt:
```bash
sudo apt install openssh-server
```
After the installation, ensure that openssh server is running. The user is prompted to provide the ssh port and user credential duing the registration process from the CLI. For testing it is recommended to create a separate ssh user with minimum/restricted permissions.

#### FIO
FIO is a powerful tool for testing I/O performance. Follow the installation instructions from [FIO's Github repository](https://github.com/axboe/fio), or install it via apt:

```bash
sudo apt install fio
```

<br/>

#### sysbench
Sysbench is a versatile benchmarking tool for evaluating system CPU and memory performances. Installation instructions can be found on [sysbench's Github repository](https://github.com/akopytov/sysbench), or you can install it via apt:
```bash
sudo apt install sysbench
```


## Usage
Once the binary and the necessary dependencies are installed, you can use the Compute Node CLI. There are various commands available in the CLI to make the on-boarding/registration process easier. The user can start the node and execute various test commands to check the hardware status of the node.

## Commands
Execute the following commands, as: `./iag-compute-cli some-command`
1. **start**

    Evaluate/Register the host machine as compute node or start compute node if already evaluated.
2. **stop**

    Stop compute node (if already running)
3. **status**
    
    Check running status of compute node
4. **check**
    
    Check if the system adhere to prerequisite criteria
5. **info**

    Extract basic information about the system
6. **test-node**
    
    Test if the node is accessible from the internet
7. **clear-config**
    
    Clear the configurations
8. **benchmark-memory**
    
    Run memory tests and benchmark for the host machine
9. **benchmark-cpu**
    
    Run cpu tests and benchmark for the host machine
10. **benchmark-storage**
    
    Run storage i/o tests and benchmark for the host machine
11. **benchmark-network**
    
    Run network tests and benchmark for the host machine
12. **help**

    Display help for command


## Node Integration

### Adding Node

- Navigate to the 'Provider' section to begin.
- In the Provider dashboard, find 'Compute' on the left-hand menu bar.
- Click on 'Compute node' to reach the page with the 'Add Node' button.
- Click the 'Add Node' button to proceed to the screen displayed in the screenshot.
- As shown in the UI, we have to add Auth key
 
 ![Add-Auth-Key](/img/addnode.png)

- After we add Auth key, we can view the details of the node

![nodedetails](/img/node-details.png)

- In the next step, we have to add "Node name" as shown in the picture.

![nodedetails](/img/node-naming.png)

- In our next step, IAG balance and IAG amount to stake is displayed

:::info
Please note that the "Find Delegators" button is disabled in Previewnet. This feature is available only in Mainnet.
:::

![balancestake](/img/balance-stake.png)

### Compute Provider Dashboard

- In our Compute Provider dashboard, we can see the list of pre-set tasks defined by Iagon, such as "Run Cardano Node". These global tasks are displayed in a list view, as shown in the screenshot.

![compute-provider-dashboard](/img/compute-provider-dashboard.png)

### Install Cardano CLI

- As a provider, to install Cardano nodes, navigate to the 'Provider' section. In the Provider section, locate 'Compute' on the left-hand menu bar. From there, we can choose to "Install Cardano Node". <br/>

For reference: [Installing Cardano Node CLI](https://developers.cardano.org/docs/get-started/installing-cardano-node) <br/>
![install-cardano-node](/img/install-cardano.png)

### Run Cardano CLI

- As a provider, to run Cardano nodes, navigate to the 'Provider' section. In the Provider section, locate 'Compute' on the left-hand menu bar. From there, we can choose to "Run Cardano Node". <br/>
For reference: [Running Cardano CLI](https://developers.cardano.org/docs/get-started/running-cardano)

![run-node](/img/run-cardano-node.png)

### Storage Compute Dashboard

- In the Storage Compute dashboard, we can see the list of running commands, as displayed in the screenshot. To access this, navigate to the 'Storage' section and then locate 'Compute' on the left-hand menu bar.

![storage-compute-dashboard](/img/storage-compute-dashboard.png)

### Storage Compute Run Command

- To run any commands, click on the "Run commands" button. A pop-up dialogue box will appear, allowing us to add commands, arguments, and an optional section for inputs, as shown in the screenshot.

![run-command-dashboard](/img/run-command-dashboard.png)

### Storage Compute Result

- We can also view the results of each command we run, as displayed in the screenshot. Simply click on "Pull Result," which opens a dialogue box showing the result, as shown in the screenshot.

![task-result](/img/task-result.png)

## Metrics Collection Process

- Ping stamp -> 3 min
-  Performance matrices: <br/>
  -- All: once a day <br/>
  -- Memory: every 2 hr <br/>
  -- CPU: every 3 hr <br/>
  -- Storage:  once a day <br/>
  -- Network: every 5 hr <br/>