from airflow.utils.db_manager import BaseDBManager
from ticketing.models import Base
from pathlib import Path

PACKAGE_DIR = Path(__file__).parent

_REVISION_HEADS_MAP: dict[str, str] = {
    "0.1.0": "d759c6d30f5a",
}


class DRTDBManager(BaseDBManager):
    """Database manager for DagRunTicket model."""

    metadata = Base.metadata
    version_table_name = "alembic_version_drt"
    migration_dir = (PACKAGE_DIR / "migrations").as_posix()
    alembic_file = (PACKAGE_DIR / "alembic.ini").as_posix()
    supports_table_dropping = True
    revision_heads_map = _REVISION_HEADS_MAP
