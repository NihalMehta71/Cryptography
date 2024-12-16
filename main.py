import hashlib

def generate_md5(input_string):
    # Compute the MD5 hash of the input string
    md5_hash = hashlib.md5(input_string.encode())
    return md5_hash.hexdigest()

if __name__ == "__main__":
    print("Welcome to the MD5 Hash Generator!")
    user_input = input("Enter a string to generate its MD5 hash: ")
    hash_result = generate_md5(user_input)
    print(f"MD5 Hash: {hash_result}")
