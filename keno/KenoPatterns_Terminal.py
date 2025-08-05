from KenoPatterns import fetch_keno_results, analyze_combos
import argparse

# Argument parser
parser = argparse.ArgumentParser(description="Keno Analyzer (Terminal)")
parser.add_argument("combo_size", type=int, help="Number of spots")
parser.add_argument("top_n", type=int, help="Number of results to show")
parser.add_argument("days", type=int, help="Number of days to look back")
args = parser.parse_args()

# Fetch results
draws = fetch_keno_results(args.days)
most_common, least_common = analyze_combos(draws, args.combo_size, args.top_n)

# Display most common
print(f"\nTop {args.top_n} MOST common {args.combo_size}-number combinations in the last {args.days} days:")
for combo, count in most_common:
    if len(combo) == 1:
        print(f"{combo[0]}: {count} times")
    else:
        print(f"{combo}: {count} times")

# Display least common
print(f"\nTop {args.top_n} LEAST common {args.combo_size}-number combinations in the last {args.days} days:")
for combo, count in least_common:
    if len(combo) == 1:
        print(f"{combo[0]}: {count} times")
    else:
        print(f"{combo}: {count} times")
