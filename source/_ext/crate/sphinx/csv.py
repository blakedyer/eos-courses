"""Minimal fallback for ``crate.sphinx.csv`` when the external package is unavailable."""


def setup(app):
    """Register a no-op extension.

    The course docs no longer rely on custom CSV directives, but the import remains in
    ``conf.py`` for compatibility with existing environments.
    """

    return {"parallel_read_safe": True, "parallel_write_safe": True}
