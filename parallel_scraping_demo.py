import concurrent.futures
import requests
import time

# List of URLs to scrape
URLS = [
    'https://www.example.com',
    'https://www.python.org',
    'https://www.github.com',
    'https://www.stackoverflow.com',
    'https://www.reddit.com',
    'https://www.wikipedia.org',
    'https://www.nytimes.com',
    'https://www.cnn.com',
    'https://www.bbc.com',
    'https://www.bloomberg.com',
]

# Function to download a webpage
def fetch_url(url):
    print(f"Fetching {url}...")
    response = requests.get(url)
    return f"{url}: {len(response.content)} bytes"

# Sequential (non-parallel) version
def sequential_scraping(urls):
    results = []
    for url in urls:
        result = fetch_url(url)
        results.append(result)
    return results

# Parallel version using ThreadPoolExecutor
def parallel_scraping(urls):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(fetch_url, urls))
    return results

# Main execution
if __name__ == "__main__":
    print("Starting Sequential Scraping...")
    start_time = time.time()
    sequential_results = sequential_scraping(URLS)
    sequential_time = time.time() - start_time
    print(f"Sequential Scraping Completed in {sequential_time:.2f} seconds.\n")

    print("Starting Parallel Scraping...")
    start_time = time.time()
    parallel_results = parallel_scraping(URLS)
    parallel_time = time.time() - start_time
    print(f"Parallel Scraping Completed in {parallel_time:.2f} seconds.\n")

    # Output results
    print("Results (Sequential):")
    for result in sequential_results:
        print(result)
    
    print("\nResults (Parallel):")
    for result in parallel_results:
        print(result)

    # Compare time taken
    print(f"\nTime taken (Sequential): {sequential_time:.2f} seconds")
    print(f"Time taken (Parallel): {parallel_time:.2f} seconds")
