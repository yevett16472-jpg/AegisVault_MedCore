import sqlite3

def test_database():
    conn = sqlite3.connect("medcore.db")
    cursor = conn.cursor()

    # 1. Insert sample records
    sample_data = [
        ('SEQ-001', 'ENCRYPTED', 1),
        ('SEQ-002', 'RAW', 0),
        ('SEQ-003', 'ENCRYPTED', 1)
    ]
    
    cursor.executemany("""
        INSERT INTO medical_telemetry_logs (module_sequence, encryption_status, hipaa_compliant)
        VALUES (?, ?, ?);
    """, sample_data)
    
    conn.commit()
    print("[+] Test records inserted successfully.\n")

    # 2. Query and verify the inserted records
    cursor.execute("SELECT * FROM medical_telemetry_logs;")
    records = cursor.fetchall()

    print(f"{'Log ID':<8} | {'Sequence':<12} | {'Encryption':<12} | {'HIPAA':<6} | {'Timestamp'}")
    print("-" * 65)
    for row in records:
        print(f"{row[0]:<8} | {row[1]:<12} | {row[2]:<12} | {row[3]:<6} | {row[4]}")

    conn.close()

if __name__ == "__main__":
    test_database()