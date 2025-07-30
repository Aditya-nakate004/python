import requests

def check_connection():
    try:
        requests.head("https://google.com", timeout=1)
        return True
    except requests.ConnectionError:
        return False
    
if __name__ == "__main__":
    if check_connection():
        print("Internet connection is avilable.")
    else:
        print("Internet connection is unavailable.")