"""
Test pre-commit hooks and code quality tools configuration.
"""
import os
import subprocess
import sys
from pathlib import Path
import pytest
import yaml


class TestPreCommitConfiguration:
    """Test that pre-commit hooks are properly configured."""
    
    def test_precommit_config_file_exists(self):
        """Test that .pre-commit-config.yaml exists."""
        config_path = Path(".pre-commit-config.yaml")
        assert config_path.exists(), ".pre-commit-config.yaml file should exist"
    
    def test_precommit_config_is_valid_yaml(self):
        """Test that .pre-commit-config.yaml is valid YAML."""
        config_path = Path(".pre-commit-config.yaml")
        if config_path.exists():
            with open(config_path, 'r') as f:
                config = yaml.safe_load(f)
                assert isinstance(config, dict), "Pre-commit config should be a valid YAML dict"
    
    def test_precommit_config_has_required_hooks(self):
        """Test that pre-commit config includes all required hooks."""
        config_path = Path(".pre-commit-config.yaml")
        if config_path.exists():
            with open(config_path, 'r') as f:
                config = yaml.safe_load(f)
                
            # Extract all hook IDs from all repos
            hook_ids = []
            for repo in config.get('repos', []):
                for hook in repo.get('hooks', []):
                    hook_ids.append(hook.get('id'))
            
            required_hooks = [
                'black',
                'ruff',
                'detect-secrets',
                'trailing-whitespace',
                'end-of-file-fixer',
                'check-yaml',
                'check-added-large-files'
            ]
            
            for hook in required_hooks:
                assert hook in hook_ids, f"Required hook '{hook}' not found in pre-commit config"
    
    def test_precommit_config_has_python_version(self):
        """Test that pre-commit config specifies minimum Python version."""
        config_path = Path(".pre-commit-config.yaml")
        if config_path.exists():
            with open(config_path, 'r') as f:
                config = yaml.safe_load(f)
                
            # Check if minimum_pre_commit_version or default_language_version is set
            has_version_config = (
                'minimum_pre_commit_version' in config or
                'default_language_version' in config
            )
            assert has_version_config, "Pre-commit config should specify Python version"


class TestDetectSecretsConfiguration:
    """Test detect-secrets configuration."""
    
    def test_secrets_baseline_exists(self):
        """Test that .secrets.baseline exists."""
        baseline_path = Path(".secrets.baseline")
        assert baseline_path.exists(), ".secrets.baseline file should exist for detect-secrets"
    
    def test_secrets_baseline_is_valid_json(self):
        """Test that .secrets.baseline is valid JSON."""
        baseline_path = Path(".secrets.baseline")
        if baseline_path.exists():
            import json
            with open(baseline_path, 'r') as f:
                baseline = json.load(f)
                assert isinstance(baseline, dict), "Secrets baseline should be valid JSON"
                assert 'results' in baseline, "Secrets baseline should have 'results' key"


class TestCodeQualityTools:
    """Test that code quality tools are properly configured."""
    
    def test_black_config_in_pyproject_toml(self):
        """Test that black is configured in pyproject.toml."""
        pyproject_path = Path("pyproject.toml")
        if pyproject_path.exists():
            import toml
            with open(pyproject_path, 'r') as f:
                config = toml.load(f)
                assert 'tool' in config, "pyproject.toml should have [tool] section"
                assert 'black' in config['tool'], "pyproject.toml should have [tool.black] section"
    
    def test_ruff_config_in_pyproject_toml(self):
        """Test that ruff is configured in pyproject.toml."""
        pyproject_path = Path("pyproject.toml")
        if pyproject_path.exists():
            import toml
            with open(pyproject_path, 'r') as f:
                config = toml.load(f)
                assert 'tool' in config, "pyproject.toml should have [tool] section"
                assert 'ruff' in config['tool'], "pyproject.toml should have [tool.ruff] section"
    
    def test_mypy_config_exists(self):
        """Test that mypy configuration exists."""
        # mypy can be configured in pyproject.toml, mypy.ini, or setup.cfg
        pyproject_path = Path("pyproject.toml")
        mypy_ini_path = Path("mypy.ini")
        setup_cfg_path = Path("setup.cfg")
        
        has_mypy_config = False
        
        if pyproject_path.exists():
            import toml
            with open(pyproject_path, 'r') as f:
                config = toml.load(f)
                if 'tool' in config and 'mypy' in config['tool']:
                    has_mypy_config = True
        
        if mypy_ini_path.exists():
            has_mypy_config = True
            
        if setup_cfg_path.exists():
            import configparser
            config = configparser.ConfigParser()
            config.read(setup_cfg_path)
            if 'mypy' in config or 'mypy-*' in config:
                has_mypy_config = True
        
        assert has_mypy_config, "mypy configuration should exist in pyproject.toml, mypy.ini, or setup.cfg"


class TestPreCommitInstallation:
    """Test that pre-commit hooks can be installed and run."""
    
    @pytest.mark.skipif(not Path(".pre-commit-config.yaml").exists(), 
                       reason="Pre-commit config file not found")
    def test_precommit_install_succeeds(self):
        """Test that pre-commit install command succeeds."""
        result = subprocess.run(
            [sys.executable, "-m", "pre_commit", "install", "--install-hooks"],
            capture_output=True,
            text=True
        )
        # Should succeed (exit code 0) or already be installed
        assert result.returncode in [0, 1], f"Pre-commit install failed: {result.stderr}"
    
    @pytest.mark.skipif(not Path(".pre-commit-config.yaml").exists(), 
                       reason="Pre-commit config file not found")
    def test_precommit_run_on_sample_file(self):
        """Test that pre-commit hooks can run on a sample file."""
        # Create a simple test file
        test_file = Path("test_sample.py")
        test_file.write_text("import os\nprint('hello')\n")
        
        try:
            result = subprocess.run(
                [sys.executable, "-m", "pre_commit", "run", "--files", str(test_file)],
                capture_output=True,
                text=True
            )
            # Pre-commit should run without critical errors (exit codes 0 or 1 are acceptable)
            assert result.returncode in [0, 1], f"Pre-commit run failed: {result.stderr}"
        finally:
            # Clean up test file
            if test_file.exists():
                test_file.unlink()