"""SQLAlchemy models for the External Tickets plugin."""

from __future__ import annotations

from sqlalchemy import Column, DateTime, Index, Integer, String, Text

from airflow.sdk import timezone
from airflow.models.base import _get_schema, naming_convention
from sqlalchemy import MetaData
from sqlalchemy.orm import registry


metadata = MetaData(schema=_get_schema(), naming_convention=naming_convention)

mapper_registry = registry(metadata=metadata)
Base = mapper_registry.generate_base()
Base.metadata = metadata


class DagRunTicket(Base):
    """Persisted ticket metadata for a DagRun."""

    __tablename__ = "dag_run_ticket"

    id = Column(Integer, primary_key=True)
    dag_id = Column(String(250), nullable=False)
    run_id = Column(String(250), nullable=False)
    system = Column(String(50), nullable=False)
    key = Column(String(250), nullable=False)
    status = Column(String(50), nullable=True)
    url = Column(Text, nullable=True)
    created_at = Column(DateTime, default=timezone.utcnow, nullable=False)
    updated_at = Column(DateTime, default=timezone.utcnow, onupdate=timezone.utcnow)

    __table_args__ = (Index("idx_drt_dag_run", "dag_id", "run_id"),)
