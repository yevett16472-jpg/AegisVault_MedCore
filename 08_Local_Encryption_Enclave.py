"""
File 08: Local Encryption Enclave
Project: AegisVault-MedCore
Author: Amadeus Veda
Description: Handles cryptographic hashing, local keys, and data minimization protocols.
"""

import hashlib
import os

class LocalEncryptionEnclave:
    def __init__(self):
        self.salt = os.urandom(16)

    def generate_secure_hash(self, payload: str) -> str:
        """Generates a SHA-256 secure hash for sovereign records."""
        hasher = hashlib.sha256()
        hasher.update(self.salt + payload.encode('utf-8'))
        return hasher.hexdigest()

    def minimize_payload(self, telemetry_data: dict) -> dict:
        """Strips sensitive unencrypted identifiers to enforce local data minimization."""
        minimized = telemetry_data.copy()
        if "patient_id" in minimized:
            minimized["patient_id"] = self.generate_secure_hash(minimized["patient_id"])
        return minimized