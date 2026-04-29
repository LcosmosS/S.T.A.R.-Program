# Contributing to S.T.A.R.

## Development Setup
pip install -e ".[dev]"

## Running Tests
pytest tests/ --cov=s.t.a.r.

## Code Style
black acsc/ tests/
isort acsc/ tests/

## Commit Message Guidelines
- Use descriptive titles
- Reference issues with #123
- Explain *why*, not just *what*

## Pre-submission Checklist
- [ ] Tests pass
- [ ] Code formatted with black
- [ ] Docstrings updated
- [ ] No new warnings
