# ==============================================================================
# File 04: System Configuration Loader & Local Environment Settings
# Project: AegisVault MedCore
# Author/Architect: Axiom Veda (AI Architect & Systems Engineer)
# Description: Manages local settings, schema paths, and security constraints
# ==============================================================================

import json
import os
from pathlib import Path


class ConfigLoader:
    """
    01.01 Configuration Controller
    Loads local settings without exposing cloud tokens or credentials.
    """
    DEFAULT_CONFIG = {
        "project_name": "AegisVault-MedCore",
        "architect": "Axiom Veda",
        "version": "1.0.0",
        "data_sovereignty": {
            "local_only": True,
            "cloud_sync": False,
            "storage_path": "./data/sql_schemas"
        },
        "active_modules": [
            "01_AegisVault_MedCore_main",
            "02_Pandora_Engine_Controller",
            "03_Sovereign_Agent_Roster"
        ]
    }

    def __init__(self, config_filename: str = "config/settings.json"):
        self.config_path = Path(config_filename)
        self.settings = self._load_or_create_config()

    def _load_or_create_config(self) -> dict:
        """01.02 Settings Ingestion & Fallback Creation"""
        if not self.config_path.exists():
            # Ensure folder exists and write local defaults
            self.config_path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.config_path, "w", encoding="utf-8") as f:
                json.dump(self.DEFAULT_CONFIG, f, indent=4)
            return self.DEFAULT_CONFIG

        with open(self.config_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def get_setting(self, key: str, default=None):
        """01.03 Key Query Accessor"""
        return self.settings.get(key, default)


if __name__ == "__main__":
    # 02.01 Configuration Verification
    config = ConfigLoader()
    print(f"[04.01 Config Initialized]: {config.get_setting('project_name')}")
    print(f"[04.02 System Architect]: {config.get_setting('architect')}")
    print(f"[04.03 Data Policy]: Local-Only = {config.get_setting('data_sovereignty')['local_only']}")