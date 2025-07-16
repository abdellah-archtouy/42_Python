# from time import sleep
# from tqdm import tqdm


# def ft_tqdm(lst: range) -> None:
#     """A simple tqdm-like function to simulate progress bar."""
#     total = len(lst)
#     for i, item in enumerate(lst):
#         percent = (i + 1) / total * 100
#         print(f"\rProgress: {percent:.2f}%", end="")
#     print()  # New line at the end

# for elem in ft_tqdm(range(333)):
#     sleep(0.005)
# print()
# for elem in tqdm(range(333)):
#     sleep(0.005)
# print()
