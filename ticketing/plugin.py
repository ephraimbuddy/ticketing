"""Airflow plugin definition for External Tickets."""

from __future__ import annotations

from airflow.plugins_manager import AirflowPlugin


class TicketingPlugin(AirflowPlugin):
    name = "ticketing_fastapi_react"


__all__ = ["TicketingPlugin"]
