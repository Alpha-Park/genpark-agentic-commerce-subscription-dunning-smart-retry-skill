# -*- coding: utf-8 -*-
"""Subscription Dunning Smart-Retry Engine for GenPark Agentic Commerce."""
import json
from typing import Dict, Any

class SubscriptionDunningSmartRetryEngine:
    @staticmethod
    def triage_card_decline_reason_code(decline_code: str, attempt_count: int = 1) -> Dict[str, Any]:
        code = decline_code.lower()
        if code in ["insufficient_funds", "soft_decline", "51"]:
            action = "SCHEDULE_SMART_RETRY"
            delay_hours = 48 if attempt_count == 1 else 96
            terminal = False
        elif code in ["lost_stolen_card", "pickup_card", "04", "14"]:
            action = "HARD_DECLINE_IMMEDIATE_CARD_UPDATE_PROMPT"
            delay_hours = 0
            terminal = True
        elif code in ["expired_card", "54"]:
            action = "QUERY_ACCOUNT_UPDATER_VAULT"
            delay_hours = 24
            terminal = False
        else:
            action = "EXPONENTIAL_BACKOFF_RETRY"
            delay_hours = 72
            terminal = False
            
        return {
            "raw_decline_code": decline_code,
            "attempt_number": attempt_count,
            "dunning_action": action,
            "retry_delay_hours": delay_hours,
            "is_terminal_failure": terminal
        }

    @staticmethod
    def synthesize_payday_aligned_retry_schedule(current_day_of_month: int) -> Dict[str, Any]:
        # Target closest upcoming pay period (1st or 15th)
        if current_day_of_month < 15:
            target_day = 15
        elif current_day_of_month < 30:
            target_day = 1
        else:
            target_day = 15
            
        return {
            "current_day": current_day_of_month,
            "target_payroll_retry_day": target_day,
            "rationale": "Liquidity surges on 1st and 15th increase success rate of insufficient funds retries by up to 41%."
        }
