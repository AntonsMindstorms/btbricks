# Development Guide

## Overview

btbricks is a MicroPython Bluetooth library for controlling LEGO hubs and
creating custom BLE peripherals. Development involves both regular Python (for
documentation, testing stubs, and package distribution) and MicroPython (for
actual deployment).

## Key next steps. Please fork and help us out

1. Right now the BLEHandler has code in the IRQ handler for setting up and
   receiving new connection. Depending on the state, e.g. connecting_uart=True,
   it executes one or the other. This should be refactored such that the
   connect_uart() method sets the correct callbacks in the IRQ and IRQ only
   handles callbacks. It's big change with lots of testing involved.
2. Everything is a monolithic file. For memory purposes it is probably better
   to split it, according to the mciropython-lib guidelines.
3. Not the full LEGO ble protocol is implemented. Especially some mario stuff is missing. See more here: <https://github.com/LEGO/lego-ble-wireless-protocol-docs>

## Setting Up Development Environment

### Prerequisites

- Python 3.7 or higher (for development tools, docs, and testing)
- MicroPython board (ESP32, LEGO SPIKE, etc.) for actual testing
- Git
- Virtual environment (venv)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/antonvh/btbricks.git
    cd btbricks
    ```

2. Create and activate virtual environment:

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3. Install development dependencies:

    ```bash
    pip install -e ".[dev]"
    ```

## Building Documentation

We use Sphinx with autodoc to generate API documentation from docstrings.

### Build HTML docs

```bash
cd docs
make html
```

Documentation will be in `docs/_build/html/`. Open `index.html` in a browser.

### Clean build

```bash
make clean
make html
```

### View documentation locally

```bash
open _build/html/index.html  # macOS
# or use your preferred browser
```

## Code Quality

### Format code with black

```bash
black btbricks tests
```

### Lint with flake8

```bash
flake8 btbricks tests
```

### Type check with mypy

```bash
mypy btbricks
```

## Testing

### Notes on Testing

Since btbricks is MicroPython-only, traditional unit tests are limited. Full
testing requires:

- Running code directly on MicroPython device
- Testing with actual LEGO hubs or mock BLE devices

### Test stubs (if present)

```bash
pytest tests/
```

## Deploying to MicroPython Devices

### Using mpremote (for ESP32, SPIKE)

```bash
mpremote cp -r btbricks :btbricks
```

### Manual upload via WebREPL or Thonny

1. Copy `btbricks/` folder to device's filesystem
2. Ensure the module is in the Python path

### Verify installation

On the device REPL:

```python
import btbricks
print(btbricks.__version__)
```

## Building and Publishing Package

### Bump version

Update version in two files:

- [btbricks/__init__.py](btbricks/__init__.py) - `__version__` variable

The version will be automatically used by:

- `pyproject.toml` (via `[tool.setuptools.dynamic]`)
- `setup.py` (reads from `__init__.py`)
- `package.json` - updated through setup.py

### Build distribution files

```bash
rm -rf ./dist && python -m build
```

### Test PyPI upload (optional)

```bash
twine upload --repository testpypi dist/*
```

### Upload to PyPI

```bash
twine upload dist/*
```

## Project Structure

``` txt
btbricks/
├── __init__.py           # Package exports and version
├── bt.py                 # Core BLE handler and communication classes
├── bthub.py              # High-level LEGO hub interface
├── ctrl_plus.py          # CTRL+ protocol support
docs/
├── conf.py               # Sphinx configuration
├── index.rst             # Documentation home page
├── api.rst               # API reference (auto-generated from docstrings)
├── _build/               # Generated HTML documentation
tests/
examples/
setup.py                  # Package setup (for PyPI/micropip)
pyproject.toml            # Modern Python project config
```

## Key Classes

- __`BLEHandler`__: Low-level Bluetooth communication
- __`UARTCentral`__: Nordic UART client mode
- __`UARTPeripheral`__: Nordic UART server mode
- __`RCReceiver`__: Receive RC control signals
- __`RCTransmitter`__: Send RC control signals
- __`MidiController`__: Send MIDI commands over BLE
- __`BtHub`__: High-level hub communication interface

## Release Checklist

1. Update version in `setup.py`, `pyproject.toml`, `package.json` and `btbricks/__init__.py`
2. Update `CHANGELOG.md` with changes
3. Build documentation: `cd docs && make html`
4. Build package: `python -m build`
5. Test upload: `twine upload --repository testpypi dist/*`
6. Upload to PyPI: `twine upload dist/*`
7. Commit changes: `git commit -m "Release vX.Y.Z"`
8. Tag release: `git tag vX.Y.Z && git push origin vX.Y.Z`

## Useful Resources

- [MicroPython Documentation](https://docs.micropython.org/)
- [Anton's Mindstorms Docs](https://docs.antonsmindstorms.com/) - LEGO
  Bluetooth protocol details
- [LEGO Bluetooth Specifications](https://lego.github.io/lego-ble-wireless-protocol-docs/)

## Contributing

1. Create a new branch: `git checkout -b feature/my-feature`
2. Make your changes
3. Run tests and linting: `pytest && black . && flake8 . && mypy btbricks`
4. Commit: `git commit -am 'Add my feature'`
5. Push: `git push origin feature/my-feature`
6. Create Pull Request

## Issues and Support

- Report bugs on [GitHub Issues](https://github.com/antonvh/btbricks/issues)
- Check [Documentation](docs/) for usage help
- Review [Examples](examples/) for code samples
