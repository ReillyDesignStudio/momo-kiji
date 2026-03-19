# Contributing to momo-kiji

Thank you for your interest in contributing to momo-kiji! This document outlines how to set up your development environment, submit changes, and participate in the community.

## Development Setup

### Prerequisites
- macOS 12+ (Apple Silicon or Intel)
- Xcode Command Line Tools
- Python 3.10+
- Git

### Local Development

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ReillyDesignStudio/momo-kiji.git
   cd momo-kiji
   ```

2. **Set up development environment:**
   ```bash
   # Install dependencies
   pip install -r requirements-dev.txt
   
   # Build the compiler
   python setup.py develop
   ```

3. **Run tests:**
   ```bash
   # Run all tests
   python -m pytest
   
   # Run with verbose output
   python -m pytest -v
   
   # Run specific test file
   python -m pytest tests/test_compiler.py
   ```

4. **Build documentation locally:**
   ```bash
   cd docs
   make html
   open _build/html/index.html
   ```

## Making Changes

### Code Style

We follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) with these preferences:

- 4 spaces (no tabs)
- Line length: 100 characters max
- Type hints for new functions
- Docstrings for all public APIs

**Format code before committing:**
```bash
black .
isort .
flake8 .
```

### Commit Messages

Use clear, descriptive commit messages:

```
type(scope): brief description

Longer explanation if needed. Reference issues with #123.

- Bullet points for changes
- Keep it under 72 chars per line
```

**Types:** `feat`, `fix`, `docs`, `test`, `refactor`, `perf`

**Example:**
```
feat(compiler): add ANE optimization pass for matrix operations

- Detects square matrix multiplications
- Auto-vectorizes using NEON instructions
- 3x speedup on typical ML workloads

Fixes #42
```

### Testing

- Add tests for new features
- Ensure all tests pass: `python -m pytest`
- Aim for 80%+ code coverage

## Submitting Changes

### Before You Start
- Check [existing issues](https://github.com/ReillyDesignStudio/momo-kiji/issues) first
- For major features, [open an issue](https://github.com/ReillyDesignStudio/momo-kiji/issues/new) to discuss
- Small fixes? Jump straight to a PR

### Pull Request Process

1. **Fork the repository** (if external contributor)

2. **Create a feature branch:**
   ```bash
   git checkout -b feat/your-feature-name
   ```

3. **Make your changes**
   - Write tests for new code
   - Update documentation
   - Commit with clear messages

4. **Push and create PR:**
   ```bash
   git push origin feat/your-feature-name
   ```
   - Go to GitHub and click "Create Pull Request"
   - Fill in the PR template completely
   - Link related issues

5. **PR Review Process:**
   - At least one maintainer review required
   - Address feedback (push updates to same branch)
   - Maintainer merges when approved
   - Expect review within 24-48 hours for small PRs

### PR Checklist

- [ ] Tests pass locally (`pytest`)
- [ ] Code formatted (`black`, `isort`, `flake8`)
- [ ] Documentation updated
- [ ] Commit messages are clear
- [ ] No breaking changes (or noted in PR)
- [ ] Related issues linked

## Good First Issues

Looking to contribute but not sure where to start? Check out issues labeled ["good first issue"](https://github.com/ReillyDesignStudio/momo-kiji/labels/good%20first%20issue).

These are tasks explicitly designed for new contributors:
- Clear requirements
- Limited scope
- Maintainer support available
- Estimated time: 1-3 hours

## Code of Conduct

We're committed to providing a welcoming and inclusive environment. Please review our [Code of Conduct](CODE_OF_CONDUCT.md).

**TL;DR:**
- Be respectful and inclusive
- No harassment, discrimination, or abusive behavior
- Report violations to [maintainers](mailto:robert.reilly@reillydesignstudio.com)

## Questions?

- **Usage questions:** Check [documentation](https://momo-kiji.readthedocs.io)
- **Bug reports:** [Open an issue](https://github.com/ReillyDesignStudio/momo-kiji/issues/new?template=bug_report.md)
- **Feature requests:** [Open an issue](https://github.com/ReillyDesignStudio/momo-kiji/issues/new?template=feature_request.md)
- **Chat with community:** [Join Discord](https://discord.gg/ReillyDesignStudio)

---

**Thank you for contributing to momo-kiji!** 🍑
