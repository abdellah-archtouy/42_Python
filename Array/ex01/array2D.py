import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slice the family list from start to end index (inclusive).
    and write its first shape, and last shape.

    :param family: List of family members.
    :param start: Starting index for slicing.
    :param end: Ending index for slicing (inclusive).
    :return: Sliced list of family members.
    """

    try:
        arr = np.array(family)
        assert arr.ndim == 2, \
            "AssertionError: The array must be 2-dimensional."
        assert isinstance(family, list), \
            "AssertionError: Input must be a list."
        assert all(isinstance(member, list) for member in family), \
            "AssertionError: All family members must be lists."
        print(f"My family shape is : {arr.shape}")
        sliced_family = arr[start:end]
        print("My new shape is :", sliced_family.shape)
        return sliced_family.tolist()
    except AssertionError as e:
        print(e)

family = [[1.80, 78.4],
[2.15, 102.7],
[2.10, 98.5],
[1.88, 75.2]]
print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))
