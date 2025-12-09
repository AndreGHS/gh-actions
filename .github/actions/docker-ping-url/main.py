import requests
import time

def ping_url(url, delay, max_trials):
    for attemp in range(max_trials):
        try:
            response = requests.get(url)
            if response.status_code==200:
                print(f"URL reachable: {url}")
                return True
            else:
                print(f"URL not reachable, retrying in {delay} seconds...")
                time.sleep(delay)

       # except requests.ConnectionError:
        #    print(f"URL not reachable, retrying in {delay} seconds...")
         #   time.sleep(delay)
        #except requests.exceptions.missing_schema:
        #    print(f"Invalid URL schema: {url}")
        #    return False
    return False

def run():
    url = os.getenv("INPUT_URL")
    delay = os.getenv("INPUT_DELAY")
    max_trials = os.getenv("INPUT_MAX_TRIALS")
    reachable = ping_url(url, delay, max_trials)
    if not reachable:
        Raise Exception(f"URL not reachable - {url}")
    
    print(f"URL reachable - {url}")


if __name__ == "__main__":
    print("Hello World")
    run()
