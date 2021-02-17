# Alembic needs to import models and Base another directory that real "db"
# because it identifies as circular dependency. Needs to looking forward a
# better solution
from .. import models
from .base import Base
