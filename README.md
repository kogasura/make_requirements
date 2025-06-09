# my_project

This repository contains a minimal Python project using the src layout.

## Folder Layout

- `src/my_package/` – package source code.
- `requirements/` – YAML requirements organized by date with a schema in `schema/`.
- `tests/` – pytest suite.
- `docs/` – Sphinx documentation.
- `.github/workflows/` – CI pipelines.
- `pyproject.toml` – project metadata.

## Development

Create a virtual environment and install development dependencies:

```bash
pip install -e .[dev,test]
```

### Validate Requirements

Run the following command to validate example requirements against the schema:

```bash
pykwalify -d requirements/2025-06/US-0001.yaml -s requirements/schema/requirements.schema.json
```

### Run Tests

Execute the test suite with:

```bash
pytest
```

