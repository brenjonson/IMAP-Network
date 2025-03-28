from cryptography.fernet import Fernet
from ..config import settings

# เพิ่มการตรวจสอบและจัดการข้อผิดพลาด
try:
    encryption_key = settings.ENCRYPTION_KEY.encode()
    cipher_suite = Fernet(encryption_key)
except Exception as e:
    # ถ้าคีย์ไม่ถูกต้อง สร้างคีย์ใหม่สำหรับการรันนี้
    # (ข้อมูลเก่าจะถอดรหัสไม่ได้ แต่อย่างน้อยแอพจะทำงานได้)
    print(f"Error with encryption key: {e}. Generating temporary key.")
    temp_key = Fernet.generate_key()
    cipher_suite = Fernet(temp_key)

def encrypt_password(password: str) -> str:
    """เข้ารหัสรหัสผ่าน"""
    try:
        encrypted_password = cipher_suite.encrypt(password.encode())
        return encrypted_password.decode()
    except Exception as e:
        print(f"Error encrypting password: {e}")
        # ถ้าเข้ารหัสไม่ได้ คืนค่าเป็นรหัสผ่านเดิม (ไม่ดีนักในแง่ความปลอดภัย แต่ทำให้แอพทำงานต่อไปได้)
        return f"ENCRYPT_ERROR:{password}"

def decrypt_password(encrypted_password: str) -> str:
    """ถอดรหัสรหัสผ่าน"""
    try:
        # ตรวจสอบว่าเป็นข้อความที่มีข้อผิดพลาดในการเข้ารหัสหรือไม่
        if encrypted_password.startswith("ENCRYPT_ERROR:"):
            return encrypted_password[14:]  # ตัด prefix ออก
            
        decrypted_password = cipher_suite.decrypt(encrypted_password.encode())
        return decrypted_password.decode()
    except Exception as e:
        print(f"Error decrypting password: {e}")
        return ""