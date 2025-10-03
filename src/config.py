"""
Configuration management for CSV Storyteller Dashboard.
"""
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


@dataclass
class AppConfig:
    """Application configuration settings."""
    
    # File processing settings
    max_file_size_mb: int = int(os.getenv("MAX_FILE_SIZE_MB", "50"))
    
    # LLM configuration
    llm_provider: str = os.getenv("LLM_PROVIDER", "openai")
    openai_api_key: Optional[str] = os.getenv("OPENAI_API_KEY")
    openai_model: str = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
    anthropic_api_key: Optional[str] = os.getenv("ANTHROPIC_API_KEY")
    anthropic_model: str = os.getenv("ANTHROPIC_MODEL", "claude-3-haiku-20240307")
    
    # Application settings
    enable_offline_mode: bool = os.getenv("ENABLE_OFFLINE_MODE", "true").lower() == "true"
    chart_theme: str = os.getenv("CHART_THEME", "plotly_white")
    
    # Development settings
    debug: bool = os.getenv("DEBUG", "false").lower() == "true"
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    
    def validate(self) -> list[str]:
        """
        Validate configuration and return list of validation errors.
        
        Returns:
            List of error messages, empty if configuration is valid.
        """
        errors = []
        
        # Validate file size
        if self.max_file_size_mb <= 0:
            errors.append("MAX_FILE_SIZE_MB must be greater than 0")
        
        # Validate LLM provider
        valid_providers = ["openai", "anthropic", "local"]
        if self.llm_provider not in valid_providers:
            errors.append(f"LLM_PROVIDER must be one of: {valid_providers}")
        
        # Validate API keys based on provider
        if self.llm_provider == "openai" and not self.openai_api_key:
            if not self.enable_offline_mode:
                errors.append("OPENAI_API_KEY is required when using OpenAI provider")
        
        if self.llm_provider == "anthropic" and not self.anthropic_api_key:
            if not self.enable_offline_mode:
                errors.append("ANTHROPIC_API_KEY is required when using Anthropic provider")
        
        return errors


# Global configuration instance
config = AppConfig()