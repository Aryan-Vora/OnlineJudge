import sys

def find_lucky_pages(test_cases):
    results = []
    for case_number, pages in enumerate(test_cases, start=1):
        max_relevance = max(pages, key=lambda x: x[1])[1]
        lucky_pages = [url for url, relevance in pages if relevance == max_relevance]
        
        results.append(f"Case #{case_number}:")
        results.extend(lucky_pages)
    
    return results

input_data = sys.stdin.read().strip().split('\n')

T = int(input_data[0])
index = 1
test_cases = []

for _ in range(T):
    pages = []
    for _ in range(10):
        url, relevance = input_data[index].rsplit(' ', 1)
        pages.append((url, int(relevance)))
        index += 1
    test_cases.append(pages)

results = find_lucky_pages(test_cases)

for result in results:
    print(result)
