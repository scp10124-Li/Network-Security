import hmac
import hashlib

if __name__ == "__main__":
    message = input("請輸入要驗證的訊息: ")
    key = "B11217059"  
    provided_hmac = input("請輸入HMAC: ")
    
    computed_hmac = hmac.new(key.encode(), message.encode(), hashlib.sha256).hexdigest()
    
    if hmac.compare_digest(computed_hmac, provided_hmac):
        print("驗證成功")
    else:
        print("驗證失敗")
