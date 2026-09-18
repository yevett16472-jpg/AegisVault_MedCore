import importlib
import os
import sys

MODULE_ROSTER = {
    "1": ("01_AegisVault_MedCore_main", "Primary System Entry Point & Signature Engine"),
    "2": ("02_Pandora_Engine_Controller", "Pandora's Box Strategy Controller"),
    "3": ("03_Sovereign_Agent_Roster", "Agent Roster Management (Oscar, Eva, Lyrica, Shield)"),
    "4": ("04_System_Config_Loader", "System Configuration & Environment Loader"),
    "5": ("05_Data_Schema_Manager", "SQLite Database Schema Manager"),
    "6": ("06_Telemetry_Logging_Service", "Telemetry & Event Logging Service"),
    "7": ("07_Pipeline_Execution_Orchestrator", "Pipeline Execution Orchestrator"),
    "8": ("08_Local_Encryption_Enclave", "Local Cryptographic Enclave"),
    "9": ("09_System_Integration_Validator", "Full System Integration Validator"),
}

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def print_banner():
    print("=" * 65)
    print("      AEGISVAULT-MEDCORE // PANDORA'S BOX CONTROL PANEL      ")
    print("=" * 65)

def run_module(module_name: str):
    print(f"\n[+] Executing: {module_name}.py ...\n" + "-" * 50)
    try:
        # Dynamically import or reload module to trigger execution cleanly
        if module_name in sys.modules:
            importlib.reload(sys.modules[module_name])
        else:
            importlib.import_module(module_name)
    except Exception as e:
        print(f"\n[!] Error executing module {module_name}: {e}")
    print("-" * 50)
    input("\nPress Enter to return to main menu...")

def main():
    while True:
        clear_screen()
        print_banner()
        print("Select a module to run:\n")
        
        for key, (mod_name, description) in MODULE_ROSTER.items():
            print(f"  [{key}] {mod_name:<35} - {description}")
            
        print("\n  [A] Run All Modules (Sequential Validation)")
        print("  [Q] Exit Control Panel\n")
        
        choice = input("Select an option [1-9, A, Q]: ").strip().upper()
        
        if choice in MODULE_ROSTER:
            run_module(MODULE_ROSTER[choice][0])
        elif choice == "A":
            run_module("09_System_Integration_Validator")
        elif choice == "Q":
            print("\n[+] Exiting AegisVault Control Panel. Systems Nominal.\n")
            sys.exit(0)
        else:
            input("\n[!] Invalid selection. Press Enter to try again...")

if __name__ == "__main__":
    main()
    