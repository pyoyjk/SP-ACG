import hmac, hashlib
session_key = b'ab213e02830ba'
message1 = b'cow jumped over the moon'
message2 = b'cow jumped over the moon2'
message_hmac1 = hmac.digest(key=session_key, msg=message1, digest=hashlib.sha256)
message_hmac2 = hmac.digest(key=session_key, msg=message2, digest=hashlib.sha256)
print(hmac.compare_digest(message_hmac1, message_hmac2))