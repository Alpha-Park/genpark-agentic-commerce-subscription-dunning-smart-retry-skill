# Subscription Dunning Smart-Retry & Involuntary Churn Reducer Skill

[![GenPark Official](https://img.shields.io/badge/GenPark-Official%20Skill-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-blue)](https://www.linkedin.com/company/92955550)
[![MCP Compliant](https://img.shields.io/badge/MCP-JSON--RPC%202.0-green)](https://modelcontextprotocol.io/)
[![Zero Dependency](https://img.shields.io/badge/Dependencies-Zero%20Stdlib-brightgreen)](https://python.org)

Card network decline code triage (insufficient funds vs do not honor), payday cadence alignment, and dynamic billing recovery schedule. Built for GenPark (https://www.genpark.ai).

## 🌐 Official Channels
- **Official Website**: [https://www.genpark.ai](https://www.genpark.ai)
- **LinkedIn Page**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)

## 🛠️ MCP Tools Exposed
- `triage_card_decline_reason_code`: Map raw ISO 8583 response codes to optimal automated dunning retry schedules.
- `synthesize_payday_aligned_retry_schedule`: Formulate dynamic retry timestamps synchronized with 1st/15th bi-monthly payroll deposits.

## 🚀 Installation & Usage
```bash
python -m genpark_agentic_commerce_subscription_dunning_smart_retry_skill.server --test
```
