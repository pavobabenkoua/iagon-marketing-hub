---
title: "Running Apps (Testnet)"
search: false
# Sidebar/nav label is set in docs/.vitepress/sidebar.ts
---
# Run dApps on Iagon Compute Testnet

## dApps on Compute Node
Introducing Iagon Compute, a platform tailored to support applications deployed by compute subscribers on the Iagon decentralized compute network. Presently, our platform specifically caters to NodeJS applications.

## Requirements for Running dApps {#requirements-for-running-iagon-apps}
- Must be an Iagon app user
- The app must be a Node.js application (Tested for all LTS versions of Node.js: 16, 18, and 20.)
- The app must have a public Git repository
- You should specify the port your app will be listening on.<br/>
Usually, you can find this information in the index.js file of your application, resembling: <br/>
```app.listen(3000, '0.0.0.0', function ()``` <br/>
:::info
Here, ***'3000'*** represents the port number, and **'0.0.0.0'** stands for the host. <br/>
Please input the same values from your code into the form. <br/>
:::
- The app should include build and start commands in the package.json file. <br/>
Build command: ```npm run (build command you provided```) (leave blank if no build is required) <br/>
Start command: ```npm run (start command you provided)``` <br/>

Please ensure your code resembles the following structure in your package.josn: <br/>
:::info
\{ <br/>
  "scripts": \{ <br/>
    "start": "node index.js" <br/>
  \} <br/>
\}
::: 
- You should provide any environment variables used by the app

:::info
<!-- - Currently, there is no SSL support for the site -->
- Only public repositories are supported
<!-- - The app must explicitly listen on the '0.0.0.0' host -->
- Only Node.js apps are supported (Tested for all LTS versions of Node.js: 16, 18, and 20.)
<!-- - There is no current support for viewing logs of the app -->
:::

### Technical Details
- Each Iagon app runs inside its own isolated environment. Isolation is achieved by creating a new VM for each app using the KVM hypervisor.

<!-- #### VM Specifications
- OS: Minimal Alpine Linux
- CPU Cores: 1
- Memory: 1 GB
- Storage: 8 GB

:::info
Nginx is used as a reverse proxy for apps running on a node. All traffic to the nodes is forwarded to the specific apps by Nginx.
::: -->

## How to run dApps
To run an dApps, navigate to [app.stage.iagon.com](https://app.iagon.com/) and go to the [web host](https://app.iagon.com/webhost) section. In the "dApps" menu, click the "Add dApp" button to deploy your app to the Iagon network. Upon deployment, you will receive a domain URL for your app.

## Additional Instructions
Follow these steps for deploying your dApp with screenshots for guidance:

### Click Webhost, view dApps
- Click on Webhost, dApps menu should be displayed

:::info
If we haven't subscribed to storage, we can only view the dApp hosting option.
:::

![running-apps](/img/running-apps/1compute.png)

### Click dApp (Launch page if no dApp)
- Click on dApps menu (Launch page should be displayed if dApp has not been added yet)

![running-apps](/img/running-apps/2.png)

### Click Run App (List of dApps)
- Click on dApp menu (List of added dApp should be displayed with its proper data and status with button to add dApp)

![running-apps](/img/running-apps/3.png)

### Click Add dApp (Clear node status)
- Click on the Add dApp button (All the nodes status should be deleted before adding new one)

![running-apps](/img/running-apps/4.png)

### Choose subscription plan
- Form should be displayed to enter details to choose subscription plan

### Subscription payment
- Sign the transaction to pay for the subscription.

![Subscription](/img/running-apps/sign-transaction.png)

### Choose paid available plans
- Choose from the available paid plans to host your dApp.

![Subscription](/img/running-apps/paid-available-plans.png)

### Enter app details
- Form should be displayed to enter details of the dApp

![running-apps](/img/running-apps/app-details.png)

#### Fill required fields
- Enter valid data in all the required fields as per necessity. For reference, please refer to [requirements](#requirements-for-running-iagon-apps)

![running-apps](/img/running-apps/app-details-fill.png)

- **For the GitHub link**, please navigate to your repository's code page. Locate the "Code" button, which may be accompanied by a dropdown menu, as shown in the screenshot. Copy the GitHub repository link from there. 
:::info
Please refrain from copying the URL shown in the browser's address bar.
:::
- Paste the copied GitHub repository link into the form.

- **Regarding the branch** <br/>
Referencing the screenshot, identify the name of the branch you are currently working on. This branch name should be added to the form accordingly. If it is the default branch, please include its name in the form.

![github](/img/running-apps/github.png)

### Click Next
- Click on the Next button after entering valid data in all required field

![running-apps](/img/running-apps/7.png)

### View deployment page
- Another  page should be displayed indicating app is being deployed

![running-apps](/img/running-apps/deploying.png)

### Visit button enabled
- Visit button should be enabled after deployed is completed

![running-apps](/img/running-apps/deployed.png)

### App list shows Running
- After added, app list should be displayed at top with Running status

![running-apps](/img/running-apps/app-list.png)

### Delete dApp (Click three dots)
- After adding the dApp, we can delete it. Click on 3 dot button on the web

![running-apps](/img/running-apps/11.png)

### View delete success message
- Successfully deleted message to be displayed

![running-apps](/img/running-apps/12.png)