import hashlib
import json
import logging
from datetime import datetime, timezone

logging.basicConfig(level=logging.INFO, format="%(message)s")

class AegisVaultMedCoreMain:
    def __init__(self, architect_name: str = "Axiom Veda"):
        self.architect_name = architect_name
        self.status = "Protocol Initialized"

    def generate_patient_hash(self, patient_id: str) -> str:
        """Generates a secure hash for a patient identifier."""
        return f"px_{hashlib.sha256(patient_id.encode()).hexdigest()[:8]}"

    def process_telemetry_payload(self, patient_id: str, data_payload: dict) -> dict:
        """Processes and cryptographically signs incoming telemetry data."""
        patient_hash = self.generate_patient_hash(patient_id)
        
        # Modern timezone-aware UTC timestamping
        timestamp = datetime.now(timezone.utc).isoformat()
        
        payload_record = {
            "timestamp": timestamp,
            "architect": self.architect_name,
            "patient_hash": patient_hash,
            "payload": data_payload
        }
        
        # Calculate payload verification signature
        serialized_data = json.dumps(payload_record, sort_keys=True).encode()
        verification_hash = hashlib.sha256(serialized_data).hexdigest()
        
        return {
            "status": "SECURE",
            "architect": self.architect_name,
            "patient_hash": patient_hash,
            "verification_hash": verification_hash,
            "timestamp": timestamp,
            "data": payload_record
        }

if __name__ == "__main__":
    controller = AegisVaultMedCoreMain(architect_name="Axiom Veda")
    print(f"[01.01 System Status]: {controller.status}")
    print(f"[01.02 Architect]: {controller.architect_name}")
    
    sample_payload = {"heart_rate": 72, "systolic": 120, "diastolic": 80}
    result = controller.process_telemetry_payload(patient_id="PATIENT_99482710", data_payload=sample_payload)
    
    print(f"[01.03 Processing Result]: {result}")
    