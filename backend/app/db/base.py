from typing import Any

from sqlalchemy.orm import as_declarative

# It's used to create tables "normalized".
# Future apply to inflect from models to plural tables name.


@as_declarative()
class Base:
    id: Any
    __name__: str
