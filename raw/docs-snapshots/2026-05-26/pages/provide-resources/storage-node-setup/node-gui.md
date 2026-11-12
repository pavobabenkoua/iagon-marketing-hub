---
title: "Node GUI"
# Sidebar/nav label is set in docs/.vitepress/sidebar.ts
---
Storage Node
# Graphical User Interface Setup


## Overview

A GUI simplifies node operation by providing an intuitive visual interface that allows operators to easily navigate settings and monitor performance without extensive technical knowledge.


## System Requirements

### Minimum System Requirements:

- Storage Capacity: 900 GB
- Upload Speed: 20 Mbps or 2.5 MB/s
- Download Speed: 20 Mbps or 2.5 MB/s
- Read Speed: 20 Mbps or 2.5 MB/s
- Write Speed: 20 Mbps or 2.5 MB/s
- Uptime Percent: 90%
- Storage Used: no minimum set, depends upon the usage
- Demand percent: no minimum set, depends upon demand


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


## Installation and Setup

### Windows GUI
- Download the .exe file [here](https://github.com/Iagonorg/mainnet-node-GUI/releases/latest)
- Double-click the downloaded installer to begin the installation.
- Follow the on-screen instructions to complete the installation process.
- Once the installation is complete, Iagon Storage Node is online and ready to register.

### Linux GUI
- Download the AppImage file [here](https://github.com/Iagonorg/mainnet-node-GUI/releases/latest)
- Open a terminal window.
- Call the directory where the installation package is located with:
```
cd /your/directory/
```
- Enter the following command with the appropriate version number to make it executable:
```
chmod +rwx ./ Iagon-Storage-Node_x.x.x
```
- Double-click on it to run it.
- Follow the on-screen instructions to complete the installation process:
    - Specify the port for the Node to operate. The default port is randomly generated. Optionally, users may choose an available alternative port.
    - Choose a file path for Iagon Node GUI to store files. Ensure that the selected path has adequate free storage space and hit Evaluate.
    - Enter the storage size in GB that you want to provide.
    - After all the configuration is setup, you will receive an authorization key.
- Once the installation is complete, Iagon Storage Node is online and ready to register.

### MacOS GUI
- Download the .dmg file [here](https://github.com/Iagonorg/mainnet-node-GUI/releases/latest)
- Double-click the downloaded DMG file to mount the disk image.
- Drag the Iagon Storage Node application icon to your Applications folder.
- Eject the Iagon Storage Node disk image.
- Open the Applications folder and locate Iagon Storage Node.
- Double-click to launch the application.
- Follow the on-screen instructions to complete the installation process.
- Once the installation is complete, Iagon Storage Node is online and ready to register.


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

<br/>
