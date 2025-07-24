class calculator:

    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculates the dot product of two vectors."""
        if len(V1) != len(V2):
            raise ValueError("Vectors must be of the same length.")
        result = sum(v1 * v2 for v1, v2 in zip(V1, V2))
        print(f"Dot product: {result}")

    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Adds two vectors."""
        if len(V1) != len(V2):
            raise ValueError("Vectors must be of the same length.")
        result = [float(v1 + v2) for v1, v2 in zip(V1, V2)]
        print(f"Add vector is: {result}")

    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Subtracts two vectors."""
        if len(V1) != len(V2):
            raise ValueError("Vectors must be of the same length.")
        result = [float(v1 - v2) for v1, v2 in zip(V1, V2)]
        print(f"Sous vector is: {result}")


a = [5, 10, 2]
b = [2, 4, 3]
calculator.dotproduct(a, b)
calculator.add_vec(a, b)
calculator.sous_vec(a, b)
