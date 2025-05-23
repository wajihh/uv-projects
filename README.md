# UV Projects

A collection of Python projects using the UV package manager and modern Python tooling.

## Features

- Uses UV for fast and reliable package management
- Modern Python project structure
- Type checking with MyPy
- Linting with Ruff
- Testing with Pytest
- CrewAI integration for AI agent development
- LangChain support for LLM applications

## Prerequisites

- Python 3.8 or higher
- UV package manager installed
- Git (for version control)

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd uv-projects
```

2. Create a virtual environment:
```bash
uv venv
```

3. Activate the virtual environment:
```bash
# On Windows
.venv\Scripts\activate
# On Unix/MacOS
source .venv/bin/activate
```

4. Install dependencies:
```bash
uv pip install -e .
```

5. Install development dependencies:
```bash
uv pip install -e ".[dev]"
```

## Development Workflow

### Setting Up Your Development Environment

1. Create a `.env` file in the project root:
```bash
touch .env
```

2. Add your environment variables (example):
```env
OPENAI_API_KEY=your_api_key_here
```

### Code Quality Tools

1. Run linting:
```bash
# Check for issues
ruff check .

# Auto-fix issues
ruff check . --fix
```

2. Run type checking:
```bash
mypy .
```

3. Run tests:
```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=src/uv_projects

# Run specific test file
pytest tests/test_specific.py
```

### Adding New Dependencies

1. Add production dependencies to `pyproject.toml`:
```toml
[project]
dependencies = [
    "your-package-name",
]
```

2. Add development dependencies:
```toml
[project.optional-dependencies]
dev = [
    "your-dev-package",
]
```

3. Install new dependencies:
```bash
uv pip install -e .
```

### Project Structure

```
uv-projects/
├── src/
│   └── uv_projects/
│       ├── __init__.py
│       ├── agents/         # CrewAI agents
│       ├── chains/         # LangChain chains
│       └── utils/          # Utility functions
├── tests/
│   ├── __init__.py
│   ├── test_agents/
│   └── test_chains/
├── pyproject.toml
├── README.md
├── .env.example
└── .gitignore
```

### Best Practices

1. Code Style:
   - Follow PEP 8 guidelines
   - Use type hints
   - Write docstrings for all functions and classes
   - Keep functions small and focused

2. Testing:
   - Write tests for all new features
   - Maintain test coverage above 80%
   - Use pytest fixtures for test setup

3. Git Workflow:
   - Create feature branches for new development
   - Write descriptive commit messages
   - Keep commits atomic and focused

## Troubleshooting

1. If you encounter build errors:
```bash
# Clean build artifacts
rm -rf build/ dist/ *.egg-info/
# Reinstall in editable mode
uv pip install -e .
```

2. If virtual environment issues occur:
```bash
# Remove existing venv
rm -rf .venv
# Create new venv
uv venv
# Reinstall dependencies
uv pip install -e ".[dev]"
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and linting
5. Submit a pull request

## License

MIT 