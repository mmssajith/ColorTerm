# Contributing to ColorTerm

Thank you for your interest in contributing to ColorTerm! This document provides guidelines for contributing to the project.

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/colorterm.git
   cd colorterm
   ```
3. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
4. **Install in development mode**:
   ```bash
   pip install -e ".[dev,ascii]"
   ```

## Development Workflow

### Making Changes

1. **Create a new branch** for your feature or bug fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following the coding standards below

3. **Write tests** for your changes in the `tests/` directory

4. **Run tests** to ensure everything works:
   ```bash
   pytest tests/ -v
   ```

5. **Run code quality checks**:
   ```bash
   # Format code
   black colorterminal/ tests/

   # Check style
   flake8 colorterminal/ tests/

   # Type checking
   mypy colorterminal/
   ```

### Coding Standards

- Follow **PEP 8** style guidelines
- Use **type hints** for function parameters and return values
- Write **docstrings** for all public functions and classes
- Keep functions **focused and small**
- Use **descriptive variable names**

### Documentation

- Update the **README.md** if you add new features
- Add examples to the **examples/** directory
- Update **CHANGELOG.md** following Keep a Changelog format
- Add inline comments for complex logic

### Testing

- Write unit tests for all new functionality
- Ensure existing tests pass
- Aim for high test coverage (>90%)
- Test on multiple Python versions if possible (3.6+)

### Commit Messages

Follow conventional commit format:

```
type(scope): brief description

Detailed explanation if needed

Fixes #issue_number
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

Examples:
- `feat(progress): add circular progress indicator`
- `fix(tables): resolve alignment issue with wide characters`
- `docs(readme): add installation instructions`

## Pull Request Process

1. **Update documentation** if needed
2. **Add tests** for your changes
3. **Update CHANGELOG.md** with your changes
4. **Ensure all tests pass**
5. **Submit a pull request** with a clear description

### Pull Request Checklist

- [ ] Code follows project style guidelines
- [ ] Tests added and passing
- [ ] Documentation updated
- [ ] CHANGELOG.md updated
- [ ] No breaking changes (or clearly documented)
- [ ] Commit messages are clear and descriptive

## Areas for Contribution

We welcome contributions in the following areas:

### Features
- New shape types or drawing utilities
- Additional table styles or formatting options
- New progress bar animations
- Enhanced ASCII art capabilities
- Color palette management
- Terminal capability detection

### Bug Fixes
- Fix reported issues
- Improve error handling
- Cross-platform compatibility fixes

### Documentation
- Improve README examples
- Add tutorials or guides
- Create API documentation
- Translate documentation

### Testing
- Increase test coverage
- Add integration tests
- Add performance benchmarks

### Performance
- Optimize rendering performance
- Reduce memory usage
- Improve startup time

## Code of Conduct

### Our Standards

- Be respectful and inclusive
- Welcome newcomers and help them learn
- Focus on constructive feedback
- Accept responsibility for mistakes
- Prioritize the community's best interest

### Unacceptable Behavior

- Harassment or discriminatory language
- Personal attacks or trolling
- Spam or off-topic discussions
- Publishing others' private information

## Questions?

If you have questions or need help:

1. Check existing **issues** and **discussions**
2. Create a new **issue** with the "question" label
3. Reach out to maintainers via email

## License

By contributing to ColorTerm, you agree that your contributions will be licensed under the MIT License.

## Recognition

Contributors will be acknowledged in:
- Project README
- Release notes
- CHANGELOG.md

Thank you for contributing to ColorTerm! 🎨
