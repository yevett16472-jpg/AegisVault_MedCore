CREATE TABLE medical_telemetry_logs (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    module_sequence TEXT NOT NULL,
    encryption_status TEXT CHECK(encryption_status IN ('ENCRYPTED', 'RAW')),
    hipaa_compliant BOOLEAN NOT NULL DEFAULT 1,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
