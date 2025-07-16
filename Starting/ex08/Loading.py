import sys
import time

def ft_tqdm(iterable):
    total = len(iterable)
    for i in iterable:
        percent = int(((i + 1) / total) * 100)
        bar = '=' * (percent // 2) + '-' * (50 - percent // 2)
        print(f"\r{percent}% [{bar}] {i + 1}/{total}", end="")
        yield i


for i in ft_tqdm(range(100)):
    time.sleep(0.05)
print()