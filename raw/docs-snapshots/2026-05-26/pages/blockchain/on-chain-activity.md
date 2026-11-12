---
title: "On-Chain Activity"
# Sidebar/nav label is set in docs/.vitepress/sidebar.ts
---

# Iagon's On-Chain Activity

## Overview

Iagon runs its on-chain operations on Cardano, a blockchain built for long-term reliability and verifiable transparency: every transaction and script interaction is recorded on a public ledger that anyone can audit. That openness, together with Cardano’s research-driven design and strong security properties, gives Iagon a foundation where state and value movements are clear, predictable, and hard to tamper with - supporting secure, efficient coordination across tokens, smart contracts, and staking flows.

As a protocol active on Cardano, we aim to use the chain for as much of our workflow as practically possible - settling logic, assets, and commitments where they can be verified by the network rather than offloaded elsewhere. That focus keeps Iagon’s activity tied to the same proof-of-stake economy that rewards stake pool operators and ADA delegators for running infrastructure and delegating stake to secure the ledger. In practice, the more the protocol relies on Cardano, the more those participants can benefit from the fees, rewards, and decentralization that come from a busy, well-supported network.

The sections below collect the on-chain identifiers of Iagon's activities on Cardano.

## IAG Token

The Iagon token (ticker: IAG) is the key store of value that backs the resources available on Iagon's network:

**IAG Token Policy**:
<br/>
`5d16cc1a177b5d9ba9cfa9793b07e60f1fb70fea1f8aef064415d114`

**IAG Token Hex Name**:
<br/>
`494147`

**IAG Asset Fingerprint**:
<br/>
`asset1z62wksuv4sjkl24kjgr2sm8tfr4p0cf9p32rca`

## Nodes

The parameters of every node are recorded on-chain as a token, accompanying the node's IAG token stake in a UTxO:

**Node Token Policy**:
<br/>
`ac35ee89c26b1e582771ed05af54b67fd7717bbaebd7f722fbf430d6`

**Node Script Payment Address**:
<br/>
`addr1zxkrtm5fcf43ukp8w8kstt65kelawutmht4a0aezl06rp43y2c4s7gthspjk2c4557c9zltqcssl4qz7x5syzf7yknhqma7zxx`

[**Borrow Stake**](/products/borrow-stake) **Payment Address**:
<br/>
`addr1qxd47yse7y8aagtw2nrcx2ymclvjvjf5hj8tacp8knuysl4g500utfac3r6wvsygpnvt57a5ht0edjs0n6ejlwvuytns24cetc`

**Legacy Script Payment Address**:
<br/>
`addr1w9k25wa83tyfk5d26tgx4w99e5yhxd86hg33yl7x7ej7yusggvmu3`

**Node Contract Upgrade Intermediary Payment Address**\*:
<br/>
`addr1v8ckrqqrj4u34sxt45vdu8s8nqq3lm3lc8s7su5nyzaq9tcqy2n8j`

<p class="note-small">* This address is used to temporarily store a node's staked IAG tokens in the middle of the process of the node upgrading from the legacy node contract to the new node contract, preventing the need for node retirement in the process.</p>

## Node Delegations

The parameters of every delegated position are recorded on-chain as a token, accompanying the delegated IAG token stake in a UTxO:

**Delegation Token Policy**:
<br/>
`faecb80eee6cadf9dac5184263ed4d164b38fe71d4f6f55e8f6b0da0`

**Delegation Script Payment Address**:
<br/>
`addr1z8awewqwaek2m7w6c5vyycldf5tykw87w820da273a4smgpy2c4s7gthspjk2c4557c9zltqcssl4qz7x5syzf7yknhq6uv6j0`

## Staking Rewards

When IAG staking rewards are claimed, a multi-signature transaction is built by the rewards batcher and transferred from the rewards batcher address to the address that claimed its rewards:

**Rewards Payment Address**:
<br/>
`addr1v8ckrqqrj4u34sxt45vdu8s8nqq3lm3lc8s7su5nyzaq9tcqy2n8j`

## Staking Market

The marketplace that allows IAG token delegators to sell their delegated positions to new owners in exchange for ADA is powered by a transaction batcher. The batcher address is also tracked with an identification token which travels intra-address in every staking market batching transaction:

**Market Payment Address**:
<br/>
`addr1v8ckrqqrj4u34sxt45vdu8s8nqq3lm3lc8s7su5nyzaq9tcqy2n8j`

**Market Batcher Token Policy**:
<br/>
`3ec3f628639c989da3302724c61c90ced45571d611563d98cd528616`

**Market Batcher Token Hex Name**:
<br/>
`4961676f6e62617463686572`

**Market Batcher Asset Fingerprint**:
<br/>
`asset18cjvk5rck9l3gfy7flnguha45rte6rw5uhlku3`

## Service Users

### Subscription Payments

User subscriptions can be paid in cryptocurrencies:

**Subscription Payment Address**:
<br/>
`addr1q84jyp334avpyc324jhhhpq7ect58dhs9snqxj52ncfc5cj4kyyq3nn28eplyq5vx78jq6xledxldfjm4ua4z5ggsrpqel0wm4`

## Cyclone Pre-Sales

Cyclone pre-sales have the option to pay with ADA or stablecoins:

**Cyclone Purchase Payment Address**:
<br/>
`addr1q8suf0puuzuesugyag23vqgraldvkrp7lp8krup39ufmj58gvtj2ayhp0wtrwwqqpc6ux4vhzmt0xwhetxrmavf2tugsw8caqs`

## ADA Stake Pools

Iagon's stake pools generate ADA to contribute to the IAG-ADA liquidity pairs on decentralized token exchanges (DEX):

**IAGL1**:

Hex: `12eda6e24a9e221fcf924c736d481342cc7be064e2454d7c9cde77fc`

Bech32: `pool1ztk6dcj2nc3plnujf3ek6jqngtx8hcryufz56lyumemlcy2xxn0`

**IAGL2**:

Hex: `cd0b7a6e8c22110113a9cffc266270e916a6e7ce2189917c70deebdd`

Bech32: `pool1e59h5m5vyggszyafel7zvcnsayt2de7wyxyezlrsmm4a679q3zr`

<br/>
