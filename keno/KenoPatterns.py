import requests
from datetime import date, timedelta
from collections import Counter
from itertools import combinations

def fetch_keno_results(days):
    """Fetches Keno draw results from the Massachusetts Lottery API."""
    end_date = date.today()
    start_date = end_date - timedelta(days=days)

    start_date_str = start_date.strftime('%Y-%m-%d')
    end_date_str = end_date.strftime('%Y-%m-%d')

    url = f"https://www.masslottery.com/rest/keno/getDrawsByDateRange?startDate={start_date_str}&endDate={end_date_str}"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json().get("draws", [])

def analyze_combos(draws, combo_size, top_n):
    """Finds most and least common number combinations."""
    all_combos = []
    for draw in draws:
        numbers = draw.get("winningNumbers", [])
        numbers = [int(n) for n in numbers]
        all_combos.extend(combinations(sorted(numbers), combo_size))

    counter = Counter(all_combos)
    most_common = counter.most_common(top_n)
    least_common = sorted(counter.items(), key=lambda x: x[1])[:top_n]

    return most_common, least_common
