"""
Test project structure and basic configuration.
"""
import os
import sys
from pathlib import Path

import pytest


class TestProjectStructure:
    """Test that the project structure is properly set up."""

    def test_project_root_exists(self):
        """Test that we're in the correct project directory."""
        current_path = Path.cwd()
        assert current_path.name == "CLASS4"

    def test_source_directory_exists(self):
        """Test that the src directory exists."""
        src_path = Path("src")
        assert src_path.exists()
        assert src_path.is_dir()

    def test_tests_directory_exists(self):
        """Test that the tests directory exists."""
        tests_path = Path("tests")
        assert tests_path.exists()
        assert tests_path.is_dir()

    def test_sample_data_directory_exists(self):
        """Test that the sample data directory exists."""
        sample_data_path = Path("tests/sample_data")
        assert sample_data_path.exists()
        assert sample_data_path.is_dir()

    def test_python_package_files_exist(self):
        """Test that __init__.py files exist for Python packages."""
        src_init = Path("src/__init__.py")
        tests_init = Path("tests/__init__.py")

        assert src_init.exists()
        assert tests_init.exists()

    def test_requirements_file_exists(self):
        """Test that requirements.txt exists."""
        requirements_path = Path("requirements.txt")
        assert requirements_path.exists()

    def test_dockerfile_exists(self):
        """Test that Dockerfile exists."""
        dockerfile_path = Path("Dockerfile")
        assert dockerfile_path.exists()

    def test_env_example_exists(self):
        """Test that .env.example exists."""
        env_example_path = Path(".env.example")
        assert env_example_path.exists()

    def test_gitignore_exists(self):
        """Test that .gitignore exists."""
        gitignore_path = Path(".gitignore")
        assert gitignore_path.exists()


class TestRequirementsFile:
    """Test that requirements.txt is properly configured."""

    def test_requirements_contains_essential_packages(self):
        """Test that requirements.txt contains the essential packages."""
        requirements_path = Path("requirements.txt")
        if requirements_path.exists():
            content = requirements_path.read_text()

            # Essential packages for the project
            essential_packages = [
                "streamlit",
                "pandas",
                "numpy",
                "plotly",
                "requests",
                "python-dotenv",
                "pytest",
                "black",
                "ruff",
                "detect-secrets",
                "pre-commit",
            ]

            for package in essential_packages:
                assert (
                    package in content
                ), f"Package {package} not found in requirements.txt"


class TestEnvironmentConfiguration:
    """Test environment configuration files."""

    def test_env_example_has_required_variables(self):
        """Test that .env.example contains required environment variables."""
        env_example_path = Path(".env.example")
        if env_example_path.exists():
            content = env_example_path.read_text()

            required_vars = ["OPENAI_API_KEY", "ANTHROPIC_API_KEY", "LLM_PROVIDER"]

            for var in required_vars:
                assert (
                    var in content
                ), f"Environment variable {var} not found in .env.example"
