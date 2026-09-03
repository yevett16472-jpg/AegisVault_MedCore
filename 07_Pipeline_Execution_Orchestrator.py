# ==============================================================================
# File 07: Pipeline Execution Orchestrator & Master Workflow Controller
# Project: AegisVault MedCore
# Author/Architect: Axiom Veda (AI Architect & Systems Engineer)
# Description: End-to-end multi-agent orchestration, error handling, and status output
# ==============================================================================

import importlib
import logging
from datetime import datetime

# Dynamic imports for numerically prefixed Python files
module_01 = importlib.import_module("01_AegisVault_MedCore_main")
module_02 = importlib.import_module("02_Pandora_Engine_Controller")
module_03 = importlib.import_module("03_Sovereign_Agent_Roster")
module_04 = importlib.import_module("04_System_Config_Loader")
module_05 = importlib.import_module("05_Data_Schema_Manager")
module_06 = importlib.import_module("06_Telemetry_Logging_Service")

# Extract required classes from imported modules
AegisVaultCore = module_01.AegisVaultCore
MedCoreDecisionSupport = module_01.MedCoreDecisionSupport
PandoraCompartmentalEngine = module_02.PandoraCompartmentalEngine
TacticalAgent = module_03.TacticalAgent
SecurityShieldAgent = module_03.SecurityShieldAgent
NetworkPegasusAgent = module_03.NetworkPegasusAgent
ConfigLoader = module_04.ConfigLoader
SchemaManager = module_05.SchemaManager
TelemetryLogger = module_06.TelemetryLogger


class AegisMasterOrchestrator:
    """
    01.01 Master Orchestrator Engine
    Connects system configuration, security protocols, multi-agent workflows,
    and schema validation into a unified execution pipeline.
    """
    def __init__(self):
        self.architect = "Axiom Veda"
        self.config = ConfigLoader()
        self.telemetry = TelemetryLogger()
        self.schema_mgr = SchemaManager()
        self.engine = PandoraCompartmentalEngine()
        self.shield = SecurityShieldAgent()
        
    def execute_sovereign_pipeline(self, raw_telemetry_payload: dict) -> dict:
        """
        01.02 End-to-End Execution Sequence
        Processes raw medical telemetry through multi-agent validation and database logging.
        """
        self.telemetry.log_event("INFO", "Orchestrator", "PIPELINE_STARTED", raw_telemetry_payload)

        # Step 01: Verify Data Sovereignty
        if not self.shield.verify_sovereignty(str(raw_telemetry_payload)):
            raise PermissionError("Data sovereignty verification failed.")

        # Step 02: Dispatch Task via Pandora Engine
        dispatch_result = self.engine.dispatch_agent_workflow("Shield", raw_telemetry_payload)

        # Step 03: Record Telemetry to SQL Schema
        self.schema_mgr.record_telemetry("07_Pipeline_Execution_Orchestrator", "EXECUTION_COMPLETE")

        self.telemetry.log_event("INFO", "Orchestrator", "PIPELINE_FINISHED", dispatch_result)
        
        return {
            "orchestrator_status": "SUCCESS",
            "architect": self.architect,
            "pipeline_details": dispatch_result,
            "timestamp": datetime.utcnow().isoformat()
        }


if __name__ == "__main__":
    # 02.01 Master System Integration Test
    orchestrator = AegisMasterOrchestrator()
    sample_payload = {"patient_id": "px_881902", "metric": "genetic_marker_alpha"}
    
    pipeline_output = orchestrator.execute_sovereign_pipeline(sample_payload)
    print(f"[07.01 Pipeline Execution Complete]: {pipeline_output}")