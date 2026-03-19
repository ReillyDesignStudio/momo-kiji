# Installation

## Current Status

momo-kiji is in **Phase 1 (Research & Design)**. Production-ready packages coming in Phase 2 (Q3-Q4 2026).

Currently, you can:

1. Explore the architecture and design
2. Access research documentation
3. Contribute to development
4. Join the community discussions

## Development Setup (For Contributors)

If you want to contribute to momo-kiji development, follow these steps.

### Prerequisites

- **Python 3.10+**
- **Git**
- **Xcode** (for macOS/iOS development)

### Clone the Repository

```bash
git clone https://github.com/ReillyDesignStudio/momo-kiji.git
cd momo-kiji
```

### Install Development Dependencies

```bash
pip install -r requirements-dev.txt
```

This installs:

- `pytest` — Testing framework
- `sphinx` — Documentation builder
- `black` — Code formatter
- `flake8` — Linter
- `mypy` — Type checker

### Set Up Pre-commit Hooks

```bash
pre-commit install
```

This ensures code quality on every commit.

### Run Tests

```bash
pytest tests/
```

### Build Documentation Locally

```bash
cd docs
make html
open build/html/index.html
```

## Future Installation Methods

When momo-kiji reaches Phase 2 (Q3-Q4 2026), you'll be able to install via:

```bash
pip install momo-kiji
```

Then use it like:

```python
import momo_kiji as mk

# Compile a model
mk.compile(
    input_path="model.onnx",
    target="ane",
    output_path="model_ane.mlmodel"
)

# Use in your app
model = mk.load("model_ane.mlmodel")
output = model.predict(input_data)
```

## Getting Help

- **GitHub Issues** — Report bugs or request features
- **Discord** — Ask questions, get support from the community
- **Discussions** — Share ideas and discuss architecture

## What's Included

Once installed, momo-kiji provides:

- **Compiler** — Optimize models for ANE
- **Python API** — High-level interface
- **Command-line Tools** — Compile and profile models
- **Documentation** — Guides, examples, and API reference
- **Examples** — Real-world usage patterns

## System Requirements

### For Development

- **macOS 13.0+** (development happens on Apple Silicon Macs)
- **Xcode 14.0+**
- **Python 3.10+**

### For Production (When Available)

- **macOS 11.0+** (Intel and Apple Silicon)
- **iOS 15.0+**
- **iPadOS 15.0+**

## Troubleshooting

### ImportError: No module named 'momo_kiji'

Make sure you've installed the package:

```bash
pip install momo-kiji
```

Or, if developing:

```bash
pip install -e .
```

### Build Fails

Check that Xcode command-line tools are installed:

```bash
xcode-select --install
```

### Documentation Won't Build

Ensure sphinx is installed:

```bash
pip install sphinx sphinx-rtd-theme myst-parser
```

Then rebuild:

```bash
cd docs
make clean
make html
```

## Next Steps

Once installed, check out the [Quickstart Guide](quickstart.md) to compile your first model.
