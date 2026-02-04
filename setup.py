"""
Setup configuration for btbricks package.

This package is designed for MicroPython environments. While it's distributed
via PyPI for reference and documentation, actual deployment to MicroPython
devices uses one of these methods:

1. **Using micropip (MicroPython's package manager):**
   On the MicroPython device:
   ```python
   import micropip
   await micropip.install("btbricks")
   ```

2. **Using mpremote (for ESP32, SPIKE, etc.):**
   ```bash
   mpremote cp -r btbricks :btbricks
   ```

3. **Manual upload via WebREPL or Thonny:**
   Copy the btbricks/ folder to the device's filesystem.

For development/documentation on regular Python, you can install normally:
```bash
pip install btbricks
```
"""

from setuptools import setup, find_packages
import pathlib

# Read long description from README
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read metadata from pyproject.toml so we only need to update one file
pyproject_path = pathlib.Path("pyproject.toml")
pyproject_data = {}
if pyproject_path.exists():
    try:
        # Python 3.11+
        import tomllib as _toml

        pyproject_data = _toml.loads(pyproject_path.read_text(encoding="utf-8"))
    except Exception:
        try:
            import toml as _toml  # type: ignore

            pyproject_data = _toml.loads(pyproject_path.read_text(encoding="utf-8"))
        except Exception:
            pyproject_data = {}

project_meta = pyproject_data.get("project", {}) if isinstance(pyproject_data, dict) else {}


def _first_author(meta):
    authors = meta.get("authors") or []
    if authors and isinstance(authors, list):
        first = authors[0]
        return first.get("name"), first.get("email")
    return (None, None)


author_name, author_email = _first_author(project_meta)

# Extract version from btbricks.__init__.py for single source of truth
try:
    import re

    init_file = pathlib.Path("btbricks/__init__.py").read_text(encoding="utf-8")
    version_match = re.search(r'^__version__\s*=\s*["\']([^"\'\']+)["\']', init_file, re.MULTILINE)
    version = version_match.group(1) if version_match else "0.0.0"
except Exception:
    version = project_meta.get("version", "0.0.0")


# Update package.json with version from __init__.py
def _sync_package_json(version_str):
    try:
        import json

        package_json_path = pathlib.Path("package.json")
        if package_json_path.exists():
            data = json.loads(package_json_path.read_text(encoding="utf-8"))
            if data.get("version") != version_str:
                data["version"] = version_str
                package_json_path.write_text(
                    json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
                )
    except Exception:
        pass


_sync_package_json(version)

# Fallbacks for commonly used fields
name = project_meta.get("name", "btbricks")
description = project_meta.get("description", "")
keywords = ", ".join(project_meta.get("keywords", []))
classifiers = project_meta.get("classifiers", [])
python_requires = project_meta.get("requires-python", project_meta.get("python_requires", ">=3.7"))
install_requires = project_meta.get("dependencies", [])
extras_require = project_meta.get("optional-dependencies", {})
project_urls = project_meta.get("urls", {})
url = (project_urls or {}).get("Homepage", project_meta.get("homepage", ""))

setup(
    name=name,
    version=version,
    author=author_name or "",
    author_email=author_email or "",
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=url,
    packages=find_packages(),
    classifiers=classifiers,
    python_requires=python_requires,
    install_requires=install_requires,
    extras_require=extras_require,
    keywords=keywords,
    project_urls=project_urls,
)
