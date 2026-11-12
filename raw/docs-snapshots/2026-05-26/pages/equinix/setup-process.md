---
title: "Equinix Setup Process"
# Sidebar/nav label is set in docs/.vitepress/sidebar.ts
---

# Setup Process for Equinix Server

## Setup:

- Setup your equinix SSH keys.
- Create a bare metal server with desired configuration.
- Once the server is deployed, SSH into the server.
- Create a directory where you will want to store incoming files, in your desired partition.

## Downloading the Installation Package

Visit [Iagon GitHub](https://github.com/Iagonorg/mainnet-node-cli/releases/latest) to download the installation package for your equinix server.

## Installation Steps

## Windows

- Download the application from this link:
  - `wget https://github.com/Iagonorg/mainnet-node-CLI/releases/latest/download/iag-cli-windows.exe`
- Follow the on-screen instructions to complete the installation process.
- Once the installation is complete, the Iagon Node CLI is ready to use.

### Command Set for Interacting with the Node CLI

- **Start Node Evaluation**:
  - Command: `./iag-cli-windows start`
  - Description: This command evaluates or starts the node if already evaluated.
- **Stop Node**:
  - Command: `./iag-cli-windows stop`
  - Description: Stops the running node.
- **Regenerate Authorization Key**:
  - Command: `./iag-cli-windows key:regenerate`
  - Description: Regenerates the authorization key for the node.
- **Get Node Information**:
  - Command: `./iag-cli-windows get:info`
  - Description: Retrieves information about the node.
- **Check Node Status**:
  - Command: `./iag-cli-windows get:status`
  - Description: Checks the status of the node.
- **Get Node Verification Status**:
  - Command: `./iag-cli-windows get:verification`
  - Description: Obtains the verification status of the node.
- **Display Command Help**:
  - Command: `./iag-cli-windows help`
  - Description: Displays help for commands.

## Linux

- Download the application from this link:
  - `wget https://github.com/Iagonorg/mainnet-node-CLI/releases/latest/download/iag-cli-linux`
- Open a terminal window.
- Navigate to the directory where the installation package is located.
- Make the file executable:
  - `chmod +rwx ./iag-cli-linux`
- Follow the on-screen instructions to complete the installation process.
- Once the installation is complete, the Iagon Node CLI is ready to use.

### Command Set for Interacting with the Node CLI

- **Start Node Evaluation**:
  - Command: `./iag-cli-linux start`
  - Description: Evaluates or starts the node if already evaluated.
- **Stop Node**:
  - Command: `./iag-cli-linux stop`
  - Description: Stops the running node.
- **Regenerate Authorization Key**:
  - Command: `./iag-cli-linux key:regenerate`
  - Description: Regenerates the authorization key for the node.
- **Get Node Information**:
  - Command: `./iag-cli-linux get:info`
  - Description: Retrieves information about the node.
- **Check Node Status**:
  - Command: `./iag-cli-linux get:status`
  - Description: Checks the status of the node.
- **Get Node Verification Status**:
  - Command: `./iag-cli-linux get:verification`
  - Description: Obtains the verification status of the node.
- **Display Command Help**:
  - Command: `./iag-cli-linux help`
  - Description: Displays help for commands.

## macOS

- Download application from this link.
  - wget https://github.com/Iagonorg/mainnet-node-CLI/releases/latest/download/iag-cli-macos
- Open a terminal window.
- Navigate to the directory where the installation package is located.
- Enter the following command to make it executable
  - chmod +rwx ./iag-cli-macos
- Follow the on-screen instructions to complete the installation process.
- Once the installation is complete, Iagon Node CLI is ready to use.

### Command Set for Interacting with the Node CLI.

- Start Node Evaluation:
  - Command: ./iag-cli-macos start
  - Description: This command is used to evaluate the node or start the node if it has already been evaluated.
- Stop Node:
  - Command: ./iag-cli-macos stop
  - Description: Use this command to stop your node if it is already running.
- Regenerate Authorization Key:
  - Command: ./iag-cli-macos key:regenerate
  - Description: Regenerate the authorization key for your node.
- Get Node Information:
  - Command: ./iag-cli-macos  get:info
  - Description: Retrieve information about your node.
- Check Node Status:
  - Command: ./iag-cli-macos get:status
  - Description: Check the status of your node.
- Get Node Verification Status:
  - Command: ./iag-cli-macos get:verification
  - Description: Obtain the verification status of your node.
- Display Command Help:
  - Command: ./iag-cli-macos help
  - Description: Display help for commands.

## For FreeBSD

- Download application from this link
  - wget https://github.com/Iagonorg/mainnet-node-CLI/releases/latest/download/iag-cli-freebsd
- Open a terminal window.
- Navigate to the directory where the installation package is located.
- Enter the following command to make it executable
  - chmod +rwx ./iag-cli-freebsd
- Follow the on-screen instructions to complete the installation process.
- Once the installation is complete, Iagon Node CLI is ready to use.
- Command Set for Interacting with the Node CLI.
- Start Node Evaluation:
  - Command: ./iag-cli-freebsd  start
  - Description: This command is used to evaluate the node or start the node if it has already been evaluated.
- Stop Node:
  - Command: ./iag-cli-freebsd stop
  - Description: Use this command to stop your node if it is already running.
- Regenerate Authorization Key:
  - Command: ./iag-cli-freebsd key:regenerate
  - Description: Regenerate the authorization key for your node.
- Get Node Information:
  - Command: ./iag-cli-freebsd  get:info
  - Description: Retrieve information about your node.
- Check Node Status:
  - Command: ./iag-cli-freebsd get:status
  - Description: Check the status of your node.
- Get Node Verification Status:
  - Command: ./iag-cli-freebsd get:verification
  - Description: Obtain the verification status of your node.
- Display Command Help:
  - Command: ./iag-cli-freebsd help
  - Description: Display help for commands.

### Post-Installation Steps

Upon completion of the node CLI application installation, users are required to register their device's node by following these steps:

- Launch  Application:
  - Open the  Iagon Node CLI application on your device.
- Configure API Port:
  - Specify the port for the Node  to operate. The default port is randomly generated. Optionally, users may choose an available alternative port.
- Select File Storage Path:
  - Choose a file path for  Iagon Node CLI to store files. Ensure that the selected path has adequate free storage space and hit Evaluate.
- Testing Phase:
  - The application will conduct a thorough test to validate the functionality of file uploads and downloads in the chosen storage path. This process may take a few minutes.
- Authorization Key Retrieval:
- Upon successful testing, users will be provided with an authorization key. Copy this key and securely store it for future use.
- To activate the node add this auth key to Provider Dashboard https://app.iagon.com/provider.
- You can monitor your node's performance in this dashboard.

### Steps to migrate to higher version

- Install the latest version of Iagon Node from above installation steps.
- Stop the older version of your Iagon Node CLI.
- After installation, start the latest version of the node.

### Demonstrating the setup of the Equinix server and the installation of the Node CLI.

<iframe src="https://drive.google.com/file/d/1hHJVy1cinucvPEtsQz-7ohsVehg3kmOZ/preview" allow="autoplay"></iframe>

### Demonstration the usability of Iagon Storage.

<iframe src="https://drive.google.com/file/d/15vW0jw0Q0Hqnur7owyGyL70mNiDFYKYB/preview" allow="autoplay"></iframe>

### Demonstration GDPR compliance.

<iframe src="https://drive.google.com/file/d/1FGpWAjN6YY7onLRmk9MK_9GeSe6nNELO/preview" allow="autoplay"></iframe>

