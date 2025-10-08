# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.2] - 2025-10-08

### Fixed
- Fixed all ruff linting errors (E402, B904, B007, F841)
- Fixed circular import issues in `colorterminal/__init__.py`
- Fixed exception handling to properly chain exceptions (B904)
- Fixed unused loop variables in tests and base modules (B007)
- Fixed unused variable assignments in test files (F841)

### Changed
- Simplified pre-commit configuration to use only ruff for linting and formatting
- Removed Black, isort, mypy, bandit, and pydocstyle from pre-commit hooks
- Consolidated all Python code quality checks into ruff
- Added E402 exception for `colorterminal/__init__.py` to allow imports after code definitions (necessary to avoid circular imports)

### Improved
- Better code quality and consistency across the codebase
- Faster pre-commit hook execution with fewer dependencies
- All 277 tests passing

## [2.0.1] - 2025-10-08

### Added
- ASCII Art module with `TextArt` and `ImageToASCII` classes
- Support for converting images to colored ASCII art
- ASCII banner text generation
- Example file for ASCII art demonstrations

### Changed
- Updated documentation and examples
- Improved README with comprehensive feature descriptions
- Enhanced package metadata for better PyPI presentation
- Added shields/badges to README (PyPI version, downloads, license, Python version)
- Added comparison table with similar libraries (colorama, rich, termcolor)
- Fixed author name typo in setup.py and pyproject.toml

### Fixed
- Package import issues resolved
- Improved MANIFEST.in for better package distribution

## [2.0.0] - 2024-10-08

### Added
- **Progress Bars Module**
  - `ProgressBar` - Static progress bar with customizable colors and characters
  - `AnimatedProgressBar` - Animated progress bar with smooth transitions
  - `SpinnerProgressBar` - Progress bar with spinner animation (dots, line, arrow, circle styles)
  - `MultiProgressBar` - Display multiple progress bars simultaneously

- **Tables Module**
  - `Table` - Basic table with headers, rows, and multiple border styles
  - `ColoredTable` - Table with row coloring and alternating colors support
  - `Grid` - Grid layout for cell-based content display
  - Support for 5 border styles: light, heavy, double, rounded, ascii
  - Column alignment options: left, center, right

- **Shapes Module**
  - `Line` - Draw horizontal and vertical lines
  - `Rectangle` - Draw filled or bordered rectangles
  - `Circle` - Draw filled or bordered circles
  - `Triangle` - Draw triangles in 4 orientations (up, down, left, right)
  - `Diamond` - Draw diamond shapes
  - `Box` - Draw Unicode box with multiple styles and optional titles

- **Enhanced Printers**
  - `StylePrinter` - Combined color and style methods (bold_red, bold_green, etc.)
  - Improved `SemanticPrinter` with icons (✓, ✗, ⚠, ℹ)

- **Testing**
  - Comprehensive test suite with 188 tests
  - Unit tests for all modules
  - Integration tests for real-world scenarios
  - 100% test coverage for core functionality

- **Examples**
  - `basic_example.py` - Simple colored text and styles
  - `shapes_example.py` - All shape types demonstration
  - `tables_example.py` - Table and grid examples
  - `progress_example.py` - Progress bar demonstrations
  - `dashboard_example.py` - Complete dashboard example

### Changed
- Improved documentation with detailed usage examples
- Refactored codebase with better class organization
- Enhanced error handling and validation
- Updated README with comprehensive feature list

### Improved
- Better color consistency across all modules
- Optimized rendering performance
- Cleaner API design

## [1.0.1] - 2024-10-07

### Changed
- Initial release with basic colored text output
- Support for basic colors and styles
- Simple text formatting functions

## [1.0.0] - 2024-10-06

### Added
- Initial release
- Basic ANSI color codes support
- Simple text coloring functions
