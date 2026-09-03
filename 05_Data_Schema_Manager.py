import sqlite3

SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS medical_telemetry_logs (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    module_sequence TEXT NOT NULL,
    encryption_status TEXT CHECK(encryption_status IN ('ENCRYPTED', 'RAW')),
    hipaa_compliant BOOLEAN NOT NULL DEFAULT 1,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
"""

def initialize_schema():
    conn = sqlite3.connect("medcore.db")
    cursor = conn.cursor()
    cursor.executescript(SCHEMA_SQL)
    conn.commit()
    conn.close()
    print("[+] Database schema initialized successfully.")

if __name__ == "__main__":
    initialize_schema()