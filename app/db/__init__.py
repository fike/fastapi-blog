# Alembic needs to import models and Base another directory that real "db" 
# because it identifies as circular dependency. Needs to looke a 
# better solution
from .base import Base

from ..import models
