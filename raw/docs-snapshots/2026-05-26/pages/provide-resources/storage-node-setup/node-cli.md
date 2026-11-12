---
title: "Node CLI"
# Sidebar/nav label is set in docs/.vitepress/sidebar.ts
---
Storage Node
# Command-Line Interface Setup


## Overview

### How to interact with CLI

The Command-Line Interface (CLI) allows users to interact with a system or application by issuing text-based commands. This interaction enables users to execute specific tasks, view system information, or modify settings, with the system providing feedback in the form of text-based responses.

To use CLI, open **Terminal** (Linux/Mac) or **Command Prompt** (Windows) and paste in the commands from the instructions on this page.


## System Requirements

### Minimum System Requirements:

- Storage Capacity: 900 GB
- Upload Speed: 20 Mbps or 2.5 MB/s
- Download Speed: 20 Mbps or 2.5 MB/s
- Read Speed: 20 Mbps or 2.5 MB/s
- Write Speed: 20 Mbps or 2.5 MB/s
- Uptime Percent: 90%

## IAG Stake Required

Following the setup of your device as a node, the network requires storage providers to demonstrate their commitment to the network and stake a balance of IAG tokens that is proportionate to the storage they wish to provide. The number of tokens required is dynamic and changes based on the current value of IAG tokens and how much storage a user wishes to provide. The calculation is as follows:

**Current Base USD Staked per GB:** ```0.5```<br/>
*Initially set at \$0.5 per gigabyte (GB) committed. Represents the minimum staking requirement in USD for each GB of storage.*

**Current Alpha Coefficient:** ```0.9```<br/>
*Determines how sensitive the staking requirement is to the IAG token price. Subject to adjustment based on market research.*

**Formula:**
```
IAG to be staked = Storage (in GBs) * (Base USD Staked per GB + Alpha * (Base USD Staked per GB / IAG Value))
```

:::info
IAG stake cannot be withdrawn until the node is [retired](./maintenance-support.md#retire-node) and a 3 month retirement period has passed.
:::


## Node Installation and Setup

### 1. Download and Install The Node
In the directory you'd like to store the node application in, run this command to download and install it:

   ::: code-group
   ```bash [Linux]
   curl -fsSL https://skywalker.luke.iagon.com/iagon-node/linux/install | sudo bash
   ```
   ```zsh [Mac (ARM64)]
   curl -fsSL https://skywalker.luke.iagon.com/iagon-node/macos/install | sudo bash
   ```
   ```cmd [Windows]
   Coming soon...
   ```
   :::

### 2. Register The Node
Choose your approach depending on whether you're converting an existing legacy node on the same server; migrating a node from another server; or setting up a new node:

   ::: tabs
   ::: tab Convert Legacy Node
   :::warning
   Before starting the new node application, make sure the legacy node application is no longer running. Do not forget to disable any services or scheduled scripts that would auto-start the old node application. It is recommended to completely remove the old node application from the server.
   :::
   Run the following command and accept the prompt to convert your **existing legacy node**'s config and continue running that node on the **same server**. The original config will be copied and converted for use by the new node, and the same storage directory will be used:
   ::: code-group
   ```bash [Linux]
   iagon-node register
   ```
   ```zsh [Mac (ARM64)]
   iagon-node register
   ```
   ```cmd [Windows]
   Coming soon...
   ```
   :::
   ::: tip
   If an existing config is not in the default location, use the `--data-dir` flag to specify its directory.
   Example: `iagon-node register --data-dir /configs/iagon-node/`
   :::
   :::

   :::tab Migrate From Different Server
   :::warning
   Before migrating the node to a new server, make sure the node application is no longer running on the original server. Do not forget to disable any services or scheduled scripts that would auto-start the node application on the old server. It is recommended to completely remove the node application from the old server.
   :::
   Run the following command to migrate an **existing node** from a **different server**, using the same auth key and specifying the new storage path:
   ::: code-group
   ```bash [Linux]
   iagon-node register --auth-key <AUTH_KEY> --data-dir <STORAGE_PATH>
   ```
   ```zsh [Mac (ARM64)]
   iagon-node register --auth-key <AUTH_KEY> --data-dir <STORAGE_PATH>
   ```
   ```cmd [Windows]
   Coming soon...
   ```
   :::
   :::
   
   ::: tab New Node
   Run the following command to set up a **new node**, specifying where the node should store data shards:
   ::: code-group
   ```bash [Linux]
   iagon-node register --data-dir <STORAGE_PATH>
   ```
   ```zsh [Mac (ARM64)]
   iagon-node register --data-dir <STORAGE_PATH>
   ```
   ```cmd [Windows]
   Coming soon...
   ```
   :::
   :::
   :::

### 3. Set Up System Service (Optional)
Add the node as a system service for automatic startup on system boot (highly recommended if the system supports it):

   ::: code-group
   ```bash [Linux]
   sudo iagon-node service install && sudo iagon-node service start
   ```
   ```zsh [Mac (ARM64)]
   sudo iagon-node service install
   ```
   ```cmd [Windows]
   Coming soon...
   ```
   :::

The node service will be started.

### 4. Start The Node (Skip if step 3 was completed)
This runs the node in the foreground, meaning it stays attached to your current terminal, and log output appears in that session. Closing the terminal or interrupting the process (for example with `Ctrl+C`) would then stop the node. To run the node in the background, use the system service from step 3 when you can. If you are unable to use system services, other usual approaches are `tmux` or `screen`, `nohup` or `disown`, or any process manager that keeps the session alive outside a single interactive shell - this page does not document those setups as they are up to your preference as a systems administrator.
:::warning
Only run this command if you did not complete step 3!
:::

   ::: code-group
   ```bash [Linux]
   iagon-node start
   ```
   ```zsh [Mac (ARM64)]
   iagon-node start
   ```
   ```cmd [Windows]
   Coming soon...
   ```
   :::

## Node Registration

1. Visit https://dashboard.iagon.com/node on your mobile Cardano wallet’s dapp browser, or your desktop web browser that has a Cardano wallet browser extension set up, and log in with your wallet

2. Select <img src="/img/add-storage-node.png" class="iagon-inline-icon" alt="Storage Node +"/>

3. Follow the on-screen prompts to input your auth key and evaluate your device

<img src="/img/launch-storage-node-auth-key-light.png" class="only-light iagon-theme-screenshot" />
<img src="/img/launch-storage-node-auth-key-dark.png" class="only-dark iagon-theme-screenshot" />

<br/>

4. You will need to decide if you want to run this node as an independent node or a delegated node. An independent node will be staked only by you, and you will keep all of the node’s earnings. A delegated node will be staked partially by you (at least the minimum requirement) and partially by other IAG token holders, with whom you will share the node’s earnings with. If you have any questions about these differences, please reach out to our team or refer to the [Staking Platform](https://docs.iagon.com/products/staking-platform) documentation

<img src="/img/launch-storage-node-node-type-light.png" class="only-light iagon-theme-screenshot" />
<img src="/img/launch-storage-node-node-type-dark.png" class="only-dark iagon-theme-screenshot" />

<br/>

5. Continue to follow on-screen prompts to set any further node parameters and to stake your IAG tokens

:::tip
You may resize your node's commitment and stake more IAG any time.
:::

## Full Command list

   ::: tabs

   ::: tab Linux
   `start` Start the node in the foreground (current terminal session):
   ```bash [Linux]
   iagon-node start
   ```
   `service` Manage the service:
   ```bash [Linux]
   iagon-node service

   # Usage: iagon-node service [OPTIONS] <COMMAND>

   #  Commands:
   #  start      Start the service
   #  stop       Stop the service
   #  restart    Restart the service
   #  status     Check service status
   #  install    Install as an OS service
   #  uninstall  Uninstall the OS service
   #  help       Print this message or the help of the given subcommand(s)
   #  Options:
   #  -l, --log <LEVEL>  Set the logging level [possible values: error, warn, info, debug, trace]
   #  -h, --help         Print help
   ```
   `register` Register the node in the Iagon network:
   ```bash [Linux]
   iagon-node register

   # Optional flags:
   # --auth-key <AUTH_KEY> to specify an existing node's auth key to migrate that node.
   # --data-dir <DATA_DIR> to specify either the directory where an existing legacy config is stored; or where a new node should store its hosted data.
   ```
   `update` Manually update the node to the latest version:
   ```bash [Linux]
   iagon-node update
   ```
   `migrate` Migrate configuration from a legacy node:
   ```bash [Linux]
   iagon-node migrate
   ```
   `benchmark` Run performance benchmarks:
   ```bash [Linux]
   iagon-node benchmark
   ```
   `info` Check node info:
   ```bash [Linux]
   iagon-node info
   ```
   `key` Manage node keys:
   ```bash [Linux]
   iagon-node key
   ```
   `reset` Reset the node and clear data and configuration:
   ```bash [Linux]
   iagon-node reset
   ```
   `help` Print command list or the help of the given subcommand(s):
   ```bash [Linux]
   iagon-node help
   ```
   :::

   ::: tab Mac (ARM64)
   `start` Start the node in the foreground (current terminal session):
   ```zsh [Mac]
   iagon-node start
   ```
   `service` Manage the service:
   ```zsh [Mac]
   iagon-node service

   # Usage: iagon-node service [OPTIONS] <COMMAND>

   #  Commands:
   #  start      Start the service
   #  stop       Stop the service
   #  restart    Restart the service
   #  status     Check service status
   #  install    Install as an OS service
   #  uninstall  Uninstall the OS service
   #  help       Print this message or the help of the given subcommand(s)
   #  Options:
   #  -l, --log <LEVEL>  Set the logging level [possible values: error, warn, info, debug, trace]
   #  -h, --help         Print help
   ```
   `register` Register the node in the Iagon network:
   ```zsh [Mac]
   iagon-node register

   # Optional flags:
   # --auth-key <AUTH_KEY> to specify an existing node's auth key to migrate that node.
   # --data-dir <DATA_DIR> to specify either the directory where an existing legacy config is stored; or where a new node should store its hosted data.
   ```
   `update` Manually update the node to the latest version:
   ```zsh [Mac]
   iagon-node update
   ```
   `migrate` Migrate configuration from a legacy node:
   ```zsh [Mac]
   iagon-node migrate
   ```
   `benchmark` Run performance benchmarks:
   ```zsh [Mac]
   iagon-node benchmark
   ```
   `info` Check node info:
   ```zsh [Mac]
   iagon-node info
   ```
   `key` Manage node keys:
   ```zsh [Mac]
   iagon-node key
   ```
   `reset` Reset the node and clear data and configuration:
   ```zsh [Mac]
   iagon-node reset
   ```
   `help` Print command list or the help of the given subcommand(s):
   ```zsh [Mac]
   iagon-node help
   ```
   :::

   :::tab Windows
   `start` Start the node in the foreground (current terminal session):
   ```cmd [Windows]
   iagon-node start
   ```
   `service` Manage the service:
   ```cmd [Windows]
   iagon-node service

   # Usage: iagon-node service [OPTIONS] <COMMAND>

   #  Commands:
   #  start      Start the service
   #  stop       Stop the service
   #  restart    Restart the service
   #  status     Check service status
   #  install    Install as an OS service
   #  uninstall  Uninstall the OS service
   #  help       Print this message or the help of the given subcommand(s)
   #  Options:
   #  -l, --log <LEVEL>  Set the logging level [possible values: error, warn, info, debug, trace]
   #  -h, --help         Print help
   ```
   `register` Register the node in the Iagon network:
   ```cmd [Windows]
   iagon-node register

   # Optional flags:
   # --auth-key <AUTH_KEY> to specify an existing node's auth key to migrate that node.
   # --data-dir <DATA_DIR> to specify either the directory where an existing legacy config is stored; or where a new node should store its hosted data.
   ```
   `update` Manually update the node to the latest version:
   ```cmd [Windows]
   iagon-node update
   ```
   `migrate` Migrate configuration from a legacy node:
   ```cmd [Windows]
   iagon-node migrate
   ```
   `benchmark` Run performance benchmarks:
   ```cmd [Windows]
   iagon-node benchmark
   ```
   `info` Check node info:
   ```cmd [Windows]
   iagon-node info
   ```
   `key` Manage node keys:
   ```cmd [Windows]
   iagon-node key
   ```
   `reset` Reset the node and clear data and configuration:
   ```cmd [Windows]
   iagon-node reset
   ```
   `help` Print command list or the help of the given subcommand(s):
   ```cmd [Windows]
   iagon-node help
   ```

   :::
   :::

<br/>
