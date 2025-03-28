from cryptography.fernet import Fernet

# สร้างคีย์ใหม่
key = Fernet.generate_key()
print("Generated Fernet key:")
print(key.decode())

# ทดสอบคีย์โดยการเข้ารหัสและถอดรหัส
cipher = Fernet(key)
test_text = "test password"
encrypted = cipher.encrypt(test_text.encode())
decrypted = cipher.decrypt(encrypted).decode()

print(f"Original: {test_text}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
print(f"Match: {test_text == decrypted}")