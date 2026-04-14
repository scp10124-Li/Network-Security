import hmac
import hashlib

def verify_hmac(message, key, provided_hmac):
    # Create a new HMAC object using the key and the message
    computed_hmac = hmac.new(key.encode(), message.encode(), hashlib.sha256).hexdigest()
    
    # Compare the computed HMAC with the provided HMAC
    if hmac.compare_digest(computed_hmac, provided_hmac):
        return "驗證成功"
    else:
        return "驗證失敗"

if __name__ == "__main__":
    # Input: message, key, and HMAC
    message = input("請輸入要驗證的訊息: ")
    key = "B11217059"  # Replace with your student ID
    provided_hmac = input("請輸入HMAC: ")

    # Output: verification result
    result = verify_hmac(message, key, provided_hmac)
    print(result)
