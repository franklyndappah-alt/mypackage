"""mypackage package initialization.

Expose submodules for package users.
"""

from . import my_module
# re-export for package API (imported for side-effect/visibility)

__all__ = ["my_module"]
