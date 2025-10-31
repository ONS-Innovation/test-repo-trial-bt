# Policy Compliance Checklist

This document verifies compliance with ONS policies for the test-repo-trial-bt project.

## GitHub Usage Policy Compliance

### ✅ Secret Scanning and Push Protection
- **Status**: Enabled via repository settings
- **Implementation**: Configured through Backstage template settings
- **Notes**: Secret scanning enabled for public repositories, baseline file included for detect-secrets pre-commit hook

### ✅ Dependabot Security and Version Updates
- **Status**: Enabled
- **Implementation**: `.github/dependabot.yml` configuration file
- **Configuration**: 
  - Security updates: Always enabled
  - Version updates: Configurable via template options
  - Open PR limit: {{ values.dependabot_open_pull_requests_limit or 10 }}

### ✅ CODEOWNERS File
- **Status**: Generated automatically
- **Location**: `.github/CODEOWNERS`
- **Owners**: {{ values.code_owners }}

### ✅ README File
- **Status**: Generated with comprehensive documentation
- **Content**: Setup instructions, tool descriptions, policy links
- **Compliance**: Meets ONS documentation standards

### ✅ Licensing
- **Status**: MIT License included
- **Location**: `LICENSE` file
- **Badge**: License badge included in README

### ✅ Branching Strategy
- **Default Branch**: {{ values.default_branch }}
- **Protection Rules**: Configured via Backstage template
- **Reviews Required**: Minimum 1 approving review
- **Status Checks**: CI/CD workflows must pass

### ✅ Signed Commits
- **Status**: Required via branch protection rules
- **Implementation**: Enforced through repository settings
- **Documentation**: Included in repository setup guidance

## Software Coding Policy Compliance

### ✅ Maintainable and Consistent Code
- **Linting**: Ruff with comprehensive rule set
- **Formatting**: Automated code formatting with Ruff
- **Type Checking**: MyPy for static type analysis
- **Documentation**: Docstrings required for all functions

### ✅ Use of ONS Technology Radar
- **Python 3.12+**: Latest supported Python version
- **Poetry**: Modern dependency management
- **Ruff**: Fast, modern linting and formatting
- **pytest**: Industry-standard testing framework

### ✅ Architectural Decision Records (ADRs)
- **Location**: `docs/adr/` directory
- **Coverage**: Package manager, linting tools, testing framework
- **Format**: Standardised ADR template provided
- **Significant Libraries**: ADRs required for major technology choices

### ✅ Mandatory Code Reviews
- **Implementation**: Branch protection rules require reviews
- **CODEOWNERS**: Automatic reviewer assignment
- **Conversation Resolution**: Required before merging

## Software Development Coding Guidelines Compliance

### ✅ GDS Style Guides
- **Python**: Follows PEP 8 via Ruff configuration
- **Documentation**: Clear, user-focused documentation
- **Testing**: Comprehensive test coverage requirements

### ✅ Naming Conventions
- **Repository**: Lowercase with hyphens validation
- **Python Modules**: Snake_case convention
- **Functions/Variables**: Python PEP 8 standards
- **Constants**: UPPER_CASE convention

### ✅ Documentation Standards
- **README**: Comprehensive setup and usage instructions
- **Code Documentation**: Docstring requirements
- **ADRs**: Decision documentation
- **API Documentation**: Included in docstrings

### ✅ Test Coverage Requirements
- **Minimum Coverage**: 50% (configurable)
- **Test Types**: Unit and end-to-end tests
- **Coverage Reporting**: pytest-cov with terminal output
- **CI Integration**: Coverage checks in GitHub Actions

### ✅ CI Integration
- **GitHub Actions**: Comprehensive CI/CD pipeline
- **Checks**: Linting, testing, security scanning, type checking
- **Branch Protection**: CI checks required for merging
- **Parallel Execution**: Tests run in parallel for efficiency

## Additional Compliance Features

### ✅ Security Scanning
- **Bandit**: Python security vulnerability scanning
- **Secret Detection**: Pre-commit hooks and baseline
- **Dependency Scanning**: Automated via Dependabot

### ✅ Pre-commit Hooks
- **Linting**: Automatic code quality checks
- **Formatting**: Automatic code formatting
- **Security**: Secret detection and security scanning
- **Notebook Cleaning**: Output stripping for Jupyter notebooks

### ✅ Development Environment
- **DevContainer**: VS Code development container configuration
- **Extensions**: Recommended VS Code extensions
- **Consistent Setup**: Reproducible development environment

## govcookiecutter Alignment

### ✅ Folder Structure
- **Standard Layout**: Python package in module directory
- **Test Organisation**: Separate unit and e2e test directories
- **Documentation**: Centralised docs directory
- **Configuration**: Root-level configuration files

### ✅ Testing Setup
- **pytest**: Primary testing framework
- **Coverage**: Integrated coverage reporting
- **Multiple Test Types**: Unit and integration tests
- **CI Integration**: Automated test execution

### ✅ Pre-commit Hooks
- **Comprehensive**: Multiple hook types
- **Security**: Secret and vulnerability detection
- **Quality**: Code formatting and linting
- **Notebook Support**: Jupyter notebook cleaning

### ✅ CI/CD Workflows
- **Multi-job**: Separate jobs for different check types
- **Parallel Execution**: Efficient resource utilisation
- **Comprehensive**: Covers all quality gates
- **Configurable**: Adaptable to project needs

---

**Compliance Status**: ✅ FULLY COMPLIANT

This template meets all requirements specified in the GitHub Usage Policy, Software Coding Policy, and Software Development Coding Guidelines, while aligning with govcookiecutter standards for government projects.
