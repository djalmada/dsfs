from typing import (
    Callable,
    List,
    Tuple,
)


class Matrix:
    def __init__(self, data: List[List[float]]):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def shape(self) -> Tuple[int, int]:
        return self.rows, self.cols

    def __repr__(self):
        return f"Matrix({self.data})"

    def __str__(self):
        return self.data.__str__()


def make_matrix(rows: int, cols: int,
                entry_fn: Callable[[List, List], float]) -> Matrix:
    return [[entry_fn(i, j) for j in range(cols)] for i in range(rows)]


def zeros(rows: int, cols: int) -> Matrix:
    return make_matrix(rows, cols, lambda i, j: 0)


def ones(rows: int, cols: int) -> Matrix:
    return make_matrix(rows, cols, lambda i, j: 1)


def eye(rows: int) -> Matrix:
    return make_matrix(rows, rows, lambda i, j: 1 if i == j else 0)