---
title: Iagon Documentation
titleTemplate: false
description: Explore our detailed documentation for the Iagon Protocol and products. Find user guides, FAQs, and resources to navigate our AI-driven storage and compute solutions effectively.
layout: doc
---
<script setup>
import { cardLinks, highlightCards, participateCards } from './.vitepress/theme/data/homeCards'
import HomeCardGrid from './.vitepress/theme/components/HomeCardGrid.vue'
</script>

<div class="home-landing">
  <h1>Iagon Documentation</h1>
  <br/>
  <p class="home-intro">
    <strong>Welcome to Iagon</strong>, where we're pioneering a
    <strong>decentralized marketplace</strong> for storage and computing resources. Our platform aims to
    <strong>simplify and democratize</strong> access to the shared storage economy for
    <strong>everyone</strong>. Initially, our focus lies in creating a transparent
    <strong>storage marketplace</strong>, empowering providers to trade their surplus storage to consumers at fair prices, all while ensuring
    <strong>data privacy and security</strong>.
  </p>
  <h2>Get to Know Us</h2>
  <HomeCardGrid :items="cardLinks" />
  <h2>Highlights</h2>
  <HomeCardGrid :items="highlightCards" />
  <h2>Participate in the Network</h2>
  <HomeCardGrid :items="participateCards" />
</div>
