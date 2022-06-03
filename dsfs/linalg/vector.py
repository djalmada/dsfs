from __future__ import annotations
from typing import List
import math


class Vector:
    def __init__(self, data: List[float]):
        self.data = data

    def __add__(self, rhs: Vector) -> Vector:
        """Element-wise addition of two Vector objects"""
        assert len(self) == len(rhs), "Vectors must be the same length"

        return Vector([v_i + w_i for v_i, w_i in zip(self.data, rhs.data)])

    def __sub__(self, rhs: Vector) -> Vector:
        """Element-wise subtraction of two Vector objects"""
        assert len(self) == len(rhs), "Vectors must be the same length"

        return Vector([lhs_i - rhs_i 
            for lhs_i, rhs_i in zip(self.data, rhs.data)])

    def __mul__(self, scalar: float) -> Vector:
        return Vector([lhs_i * scalar  for lhs_i in self])

    __rmul__ = __mul__

    def __floordiv__(self, divisor: int) -> Vector:
        return Vector([lhs_i // divisor for lhs_i in self])

    def __truediv__(self, divisor: float) -> Vector:
        return Vector([lhs_i / divisor for lhs_i in self])

    def __getitem__(self, key: int) -> float:
        assert key >= 0, "Key must be a positive integer"

        return self.data[key]

    def __len__(self) -> int:
        return len(self.data)

    def __repr__(self) -> str:
        return f"Vector({self.data})"

    def __str__(self) -> str:
        return self.data.__str__()


def vector_sum(vectors: List[Vector]) -> Vector:
    """Sums all corresponding elements"""
    assert vectors, "The list of Vectors was empty"

    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), \
        "The lengths of the Vectors do not match"
    
    return Vector([sum(vector[i] for vector in vectors) 
        for i in range(num_elements)])


def vector_mean(vectors: List[Vector]) -> Vector:
    """Computes the element-wise average"""
    num_vectors = len(vectors)

    return vector_sum(vectors) / float(num_vectors)


def dot(v: Vector, w: Vector) -> float:
    """Computes the dot product between two Vectors"""
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


def sum_of_squares(v: Vector) -> float:
    """Returns the sum of ghe squares of the elements of a Vector"""
    return dot(v, v)


def magnitude(v: Vector) -> float:
    """Returns the magnitude of a Vector"""
    return math.sqrt(sum_of_squares(v))


def squared_distance(v: Vector, w: Vector) -> float:
    """Computes the squared distance between two Vectors"""
    return sum_of_squares(v - w)


def distance(v: Vector, w: Vector) -> float:
    """Computes the distance between two Vectors"""
    return math.sqrt(squared_distance(v, w))
