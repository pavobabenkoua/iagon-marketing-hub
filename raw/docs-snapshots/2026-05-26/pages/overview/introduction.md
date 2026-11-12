---
title: "Introduction"
# Sidebar/nav label is set in docs/.vitepress/sidebar.ts
---
# Introduction


## What is Iagon?

Welcome to Iagon, where we're pioneering a decentralized marketplace for storage and computing resources. Our platform aims to simplify and democratize access to the shared storage economy for everyone. Initially, our focus lies in creating a transparent storage marketplace, empowering providers to trade their surplus storage to consumers at fair prices, all while ensuring data privacy and security.
In the realm of digital infrastructure, Iagon emerges as a game-changer. Our mission is clear: to revolutionize the way storage and computing resources are accessed and utilized. By leveraging blockchain technology, we're building a platform that not only simplifies participation in the shared storage economy but also prioritizes transparency, security, and accessibility. 

In upcoming versions, we'll extend our capabilities to include computational processes, making them secure and user-friendly. We envision a future where Iagon transforms cloud storage and computing markets, offering a decentralized grid for storage and processing. By harnessing untapped computing resources from data centers, computers, and other devices, Iagon will revolutionize the landscape of storage and processing.


## Problem Definition

This section shows how Iagon will help solve the most important limitations of using centralized storage solutions.

### Security
The big data market is characterized by the recent adoption of data lake architectures, such as information systems relying on the Hadoop framework. The data lake architecture is based on the implementation of a NoSQL central database such as MongoDB or HBase, where files of any sort can be stored or retrieved. Companies can virtually define central repositories for their information and data files (regardless of the type or contents of those files). These repositories are generally designed to be user-friendly and accessible.

Nonetheless, once the data lake is hacked, an intruder can “swim” in the database system, inspect the files and gain access to valuable data concerning operations of the organization under attack.

Iagon plans to build a technology named Secure Lake that will be based on decentralization, encryption, random clipping masks, error-correcting codes, compression, and sharding. One of its most important functions will be “freezing” the lake, meaning it will prohibit potential threat actors from navigating within the data lake after gaining access to it. See the Secure Lake Technology section for more details about how Iagon will solve this problem.

### Data Privacy and Compliance
In recent years, several tech companies mishandled consumer data, mined data without users’ consent, or failed to notify authorities about data breaches, resulting in fines amounting to \$1.2 billion in total. For example, Google tracked users online by passively collecting data in the background using cookies. Collected information was then used for target advertising which is the company’s primary source of revenue. Also there is general lack of transparency and user control in how tech companies handle and manage user storage data which is legitimate concern in the realm of data privacy and user rights. With Iagon, storage consumers will have the option to specify where their data should be stored and how it should be transferred or accessed. This allows the protocol to meet region-specific data handling requirements such as GDPR or LGPD. Additionally, once a file is uploaded and sharded, its owner will be able to see the number of shards and an indication of where the storage providers hosting the shards are located. Note that the protocol is designed to ensure that storage providers are following all the compliance requirements, and can provide audibility of the several legal framework compliances to trusted third parties.

### Centralization
On December 8, 2021, an AWS outage had widespread effects on the Internet. As a result, several centralized platforms like Netflix, Disney+, and even centralized crypto exchanges like Coinbase and Binance experienced an outage. Unfortunately, this event showed that even platforms like dYDX, the eleventh biggest DeFi app on the Ethereum network at the time, according to DappRadar, do rely on the centralized cloud infrastructure provided by AWS:

Due to a major AWS outage, dYdX exchange is currently down. We are experiencing greater latency across services and impaired functionality with endpoints not working and the website not loading.

It's worth noting that AWS outages are not infrequent. According to The Complete History of AWS Outages page, AWS had seventeen major outages between July 2008 and January 2021. These outages translated to revenue losses for the companies relying on AWS. For example, the AWS outage in March 2017 continued for several hours and caused damages estimated to be more than 300 million USD2.

Iagon aims to solve this dependence through real decentralization. By connecting data centers, business computers, and private users located all over the globe, the protocol will build decentralized storage for web3 that is not dependent on the centralized web infrastructure, thus allowing better data control.

### Monetization of Data Without Consent or Reward
Centralized platforms such as Google or Facebook have played a key role in the advancement of fast and low-cost applications, but they rely on leveraging the private data of their users. As a result, users don't control the data collected and monetized by these centralized platforms.

In contrast, Iagon relies on a decentralized architecture, meaning that there is no central entity that can store or access the files. Iagon plans to implement an architecture that lets users choose a drive specific to their needs. Then, the protocol mints an NFT on the Cardano blockchain relevant to the subscription that the user chooses. Users can then upload the files to their drive.

Moreover, the common practice on the web is to use cookies to record your browsing activity and save the information that you entered into various form fields, such as your name or address. Then, most websites use this information to serve targeted ads and even sell your personal data to other companies that wish to learn about your online behavior when you aren't on their websites.

Based on Iagon's vision that no one should profit from your data without sharing the profit with you, we decided to implement strict privacy policies, including a zero cookies policy. This means that you are browsing anonymously. Nobody will know what you click on our websites, and all form inputs will be erased when you refresh a page.

Thus, it is impossible for Iagon or any other entity that interacts with the protocol to monetize the private data without the user's consent.

### Costs
The size of the cloud services market providing storage capacity is steadily growing year on year, and the market is dominated by four major players: AWS, Google Cloud, Microsoft, and IBM. It is important to note that all these companies use central and less trusted storage and computation facilities. Due to their oligopolistic dominance, the four providers of cloud services set high pricing levels. These providers are also capable of hampering any competition and preventing new market entrants from competing with them, due to the broad scale of their operations and their substantial investments in data centers, servers, and storage facilities.

Iagonʼs major aim is to revolutionize the storage market by creating a marketplace for storage where everybody can participate and trade storage at a transparent price.

### Environmental Impact
Iagon uses Cardano which is one of the most environmentally sustainable blockchain protocols. Its consensus protocol, named Ouroboros, "solves the greatest challenge faced by existing blockchains: the need for more and more energy to achieve consensus. Using Ouroboros, Cardano can securely, sustainably, and ethically scale, with up to four million times the energy efficiency of bitcoin."


## History

Iagon was formed in 2017 on the basis that people need to be in control of their data. The idea started as an attempt at solving major issues related to how healthcare data is stored, with modern solutions severely lacking transparency for individuals, both at a national and international level. The initial ambition of Iagon was to create a secure way for individuals to hold, and thereby own their health data, and to interact more effectively with health services.

The scope of functionality and the purpose of Iagon have then evolved under the realization that not only health data can benefit from being stored by the owner in a secure and decentralized manner. Instead, this approach might prove valuable to all sorts of companies, such as corporations storing important IP documents, SMEs intending to reduce the loss-of-data risk in ransomware attacks, or organizations operating in environments that require high-level security and control over who shares what with whom.Therefore, Iagon envisioned a future in which security, compliance, and decentralization are seamlessly bridged.

Initially, the IAG token was launched as an ERC token. However, as Ethereum was still facing scaling issues, Iagon decided to deploy the protocol on the Cardano network. For more details about the history of the company, including the reasoning behind the decision to use the Cardano network, see the [Cloud Computing Reinvented - A Quick Overview](https://blog.iagon.com/cloud-computing-reinvented-a-quick-overview/) blog post.


## How It Works?

Iagon aims to make it easy for everyone to contribute to the decentralized cloud storage network and earn from it!

**Iagon's Ambition: The Shared Storage Economy that keeps on giving**


## Node Operators

### Who is a Node Operator?

Anyone is able to run our node software to run nodes on our network. How does Iagon reward Node Operators? Our rewards mechanism distributes 90% of the storage user subscription payments to Node Operators based on the performance of their nodes, as well as additional IAG staking rewards.

### How does Iagon reward Node Operators?

Our rewards mechanism distributes 90% of the storage user subscription payments to Node Operators based on the performance of their nodes, as well as additional IAG staking rewards.


## Node Network

### Who can join the node network?

Anyone with a computer or server that has excess storage and is always online may participate and contribute their storage resources to the network.

### How to connect to the node network?

Simply run our node software and follow the setup steps to get the node running. Then use our online dashboard to connect your node to your Cardano wallet using a unique authorization key and stake the required IAG tokens to finalize the node's registration.


## Rewards Payment

### What currency is used for reward payment?

Subscription fees earned by Node Operators are currently available in Cardano's ADA token, while staking rewards are Iagon's IAG token.

<br/>
