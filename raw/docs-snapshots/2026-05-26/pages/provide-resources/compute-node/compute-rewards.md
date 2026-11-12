---
title: "Compute Rewards"
search: false
# Sidebar/nav label is set in docs/.vitepress/sidebar.ts
---
# Compute Reward Allocation


## Reward Allocation

20,000,000 IAG has been allocated as rewards for this program. The maximum return will be capped at 30% APY until a minimum of 6M IAG has been staked. The maximum rewards emitted per year are defined below; the actual return will be based on the aggregate performance score of the nodes. Leftover rewards from each year will be added to more years after the initial program has concluded, until the 20,000,000 IAG has been entirely distributed.

| Year | Allocations  | Percent of total |
| ---- | ------------ | ---------------- |
| 1    | 1,772,004.963 | 8.86%            |
| 2    | 1,701,124.764 | 8.51%            |
| 3    | 1,633,079.774 | 8.17%            |
| 4    | 1,567,756.583 | 7.84%            |
| 5    | 1,505,046.32 | 7.53%            |
| 6    | 1,444,844.467 | 7.22%            |
| 7    | 1,387,050.688 | 6.94%            |
| 8    | 1,331,568.661 | 6.66%            |
| 9    | 1,278,305.914  | 6.39%            |
| 10   | 1,063,202.978  | 5.32%            |
| 11   | 1,063,202.978  | 5.32%            |
| 12   | 1,063,202.978 | 5.32%            |
| 13   | 1,063,202.978  | 5.32%            |
| 14   | 1,063,202.978  | 5.32%            |
| 15\* | 1,063,202.978  | 5.32%            |
|      | 20,000,000    | 100.00%          |

- \*to be reduced to distribute rewards to initial nodes

:::info
The rewards scheme is not final and may change based on market research.
:::


## Rewards Calendar

Staking Rewards for epoch n are calculated at n+1 epoch but distributed at epoch n+73 epoch. Rewards can be claimed as they are available.

To calculate fees and rewards, node performance metrics calculations are used.


## Calculation of Tokens to be Staked

As a Compute Node provider, staking IAG tokens demonstrates your commitment to the network. The staking amount depends on both your Compute capacity and the current IAG token price. Let's break it down:

1. **Base USD Staked per commitment**:

   - Initially set at Base value per commitment = 80
   - Represents the minimum staking requirement in USD for each commitment unit of Compute.

   :::info
   Commitment unit = CPU cores committed + RAM committed in GB / 2 + (log<sub>10</sub>(Storage committed in GB) - 1 )
   :::

2. **Alpha Coefficient**:

   - Alpha defines the sensitivity of the staking requirement to the price of the IAG token.
   - Currently set at 0.9 (adjustment possible based on market research).

3. **Formula**:

   - Calculate the IAG tokens to be staked:
     ```
     IAG to be staked = Commitment Unit * (Base  Staked per commitment + ((Alpha * Base Value Staked per commitment)/IAG price))
     ```

4. **Advantages**:
   - If the IAG token price drops, staking requirements in terms of tokens increase, reducing circulating supply and potentially supporting price stability.
   - If IAG price rises, staking becomes more accessible for new providers, fostering inclusiveness.

Remember, this dynamic adjustment balances commitment and accessibility within the Iagon network.


## Staking Period

In order to ensure the reliability and availability of Compute services, we've implemented a minimum staking period. For instance, when Compute Node providers stake their tokens, they have the option to request withdrawal (Retire) immediately. However, the withdrawal is only available after a 3-month waiting period following the "Retire" action. This results in a total token lock period of 3 months.

This policy promotes a commitment to the network. This precaution safeguards against abrupt token removal, which could disrupt file availability, inconveniencing users.

<i>Note: Once the retire process has been initiated, it's essential for the node to remain active for a period of time. This allows for the smooth migration of applications currently running on that node to another node, providing ample time for the migration process.</i>


## Compute Metrics
The detailed elaboration of Compute metrics can be checked [here](./compute-metrics.md).