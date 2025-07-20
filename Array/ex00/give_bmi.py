from numpy import array


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    Calculate the Body Mass Index (BMI) for each person \
given their height and weight.
    :param height: List of heights in meters.
    :param weight: List of weights in kilograms.
    :return: List of BMI values.
    """
    try:
        assert len(height) == len(weight), "AssertionError: Height and \
        weight lists must have the same length."
        assert all(isinstance(h, (int, float)) for h in height), "\
AssertionError: All heights must be integers or floats."
        assert all(isinstance(w, (int, float)) for w in weight), "\
AssertionError: All weights must be integers or floats."
        assert all(h > 0 for h in height), "AssertionError: \
All heights must be greater than zero."
        assert all(w > 0 for w in weight), "AssertionError: \
All weights must be greater than zero."
        resulte = array(weight) / (array(height) ** 2)
        return resulte.tolist()
    except AssertionError as e:
        print(e)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Check if each BMI value is below a specified limit.
    :param bmi: List of BMI values.
    :param limit: The BMI limit to check against.
    :return: List of boolean values indicating if each BMI is below the limit.
    """
    try:
        assert len(bmi) == len(limit), "AssertionError: \
BMI list and limit must have the same length."
        assert isinstance(limit, (int, float)), "AssertionError: \
Limit must be an integer or float."
        assert all(isinstance(b, (int, float)) for b in bmi), "\
AssertionError: All BMI values must be integers or floats."
        assert all(b > 0 for b in bmi), "AssertionError: \
All BMI values must be greater than zero."
        return [b < limit for b in bmi]
    except AssertionError as e:
        print(e)


# from give_bmi import give_bmi, apply_limit
height = [2.71, 1.15]
weight = [165.3, 38.4]
bmi = give_bmi(height, weight)
print("bmi is", bmi, type(bmi))
print(apply_limit(bmi, 26))
