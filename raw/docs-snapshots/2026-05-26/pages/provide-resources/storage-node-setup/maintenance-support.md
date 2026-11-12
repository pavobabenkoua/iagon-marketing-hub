---
---

Storage Node
# Maintenance and Support


## Maintenance

### Change Storage Device
Example cases include changing from HDD to SSD or to a larger HDD/SSD. When changing storage devices, please ensure that the new device has at least as much storage as the old device.

The steps to change the storage device are as follows:

1. Stop the storage node

2. Back up all data on the old storage device

3. Unmount the old storage device

4. Change the storage device

5. Mount the new storage device in the same directory as the old storage device

6. Restore all data from the backup

7. Restart the node


### Increase Storage Commitment
If your storage device has more storage capacity than your current storage commitment, you can increase your storage commitment:

1. Navigate to the node's details page on the [Iagon web dashboard](https://dashboard.iagon.com/node)

2. Select the 3-dot menu <img src="/img/3-dot-menu-light.png" alt="" class="only-light iagon-menu-icon-inline" /> <img src="/img/3-dot-menu-dark.png" alt="" class="only-dark iagon-menu-icon-inline" /> at the top right and select **Resize Commitment**

3. a) If the node is an Independent Node, use the slider or input field to set the amount of storage you want to add to your node's commitment

    b) If the node is a Delegated Node, select either **Stake Yourself** or **Request Delegation** then select **Next**

4. Click **Next** to continue to stake the amount of IAG required to commit the additional storage capacity

5. After staking, the additional storage commitment will be applied to your node


### Migrate Node
Move the node to a different server or host system.

1. Locate the auth key of the node you'd like to migrate, or regenerate it if it was lost. To regenerate the node's auth key, navigate to the node's details page on the [Iagon web dashboard](https://dashboard.iagon.com/node), select the 3-dot menu <img src="/img/3-dot-menu-light.png" alt="" class="only-light iagon-menu-icon-inline" /> <img src="/img/3-dot-menu-dark.png" alt="" class="only-dark iagon-menu-icon-inline" /> at the top right and select **Regenerate Auth Key**

2. Install the storage node on the new server, and use the `--auth-key` flag with the `register` command to specify the existing auth key
   ::: code-group
   ```bash [Linux]
   iagon-node register --auth-key <AUTH_KEY>
   ```
   ```zsh [Mac]
   Coming soon...
   ```
   ```cmd [Windows]
   Coming soon...
   ```
   :::


### Retire Node
When a node is retired, it will be removed from the network and any data on the node will be deleted. This process takes 3 months to complete and is irreversible. This means you will not be able to withdraw your staked IAG until 3 months after retirement is initiated.

1. Navigate to the node's details page on the [Iagon web dashboard](https://dashboard.iagon.com/node)

2. Select the 3-dot menu <img src="/img/3-dot-menu-light.png" alt="" class="only-light iagon-menu-icon-inline" /> <img src="/img/3-dot-menu-dark.png" alt="" class="only-dark iagon-menu-icon-inline" /> at the top right and select **Retire Node**

3. Follow the on-screen prompts to complete the retirement process


## Known Issues

### `A JavaScript error occurred in the main process`
- Issue: Usually a corrupted configuration file issue seen with Windows nodes.

- Fix: Kill the node process in the Details tab of Task Manager, delete the iagon-node folder in your user directory, then restart the node.


## Get Support

If you encounter any issues or have any questions, our support team is available on Discord. Join our [Discord server](https://discord.gg/TCS23VWuWm) to connect with our team or contact us through our [support](mail:support@iagon.com) email. We're committed to providing excellent support to ensure you have a smooth experience.

<br/>
