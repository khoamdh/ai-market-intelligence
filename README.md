# AI Market Intelligence System

## Overview

This project is a modular **AI-powered market intelligence system** that
analyzes financial time-series data (S&P 500 and Bitcoin) and generates insights
using a **tool-augmented single-agent LLM architecture**.

Instead of a simple script or chatbot, the system is designed as a **structured
data + AI pipeline**, where the LLM acts as a reasoning engine on top of
engineered financial features and tool-based data access.

---

## Key Capabilities

- Fetches real market data (S&P 500, Bitcoin) using Yahoo Finance
- Computes financial indicators:
  - Returns
  - Volatility
  - Correlation between assets
- Uses a **tool-based architecture** for data access and computation
- Applies an LLM as a **reasoning agent**
- Generates natural language market insights
- Interactive dashboard using Streamlit

---

## System Architecture

```text
User Question
      ↓
Streamlit UI
      ↓
Orchestration Layer (pipeline.py)
      ↓
┌──────────────────────────────────────┐
│ Tool Layer                           │
│ - Data Fetching (BTC, S&P 500)       │
│ - Analytics (returns, correlation)   │
└──────────────────────────────────────┘
      ↓
Context Builder (structured input)
      ↓
LLM Agent (OpenAI GPT model)
      ↓
Insight Generation
      ↓
Streamlit Output
```
