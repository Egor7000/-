from abc import ABC, abstractmethod


class Chair(ABC):
    """
    Абстрактный класс, описывающий стул.

    Attributes:
        material (str): Материал стула.
        legs (int): Количество ножек.
        max_weight (float): Максимально допустимый вес (кг).

    >>> isinstance("wood", str)
    True
    """

    def __init__(self, material: str, legs: int, max_weight: float) -> None:
        if not material:
            raise ValueError("Материал стула не может быть пустым")
        if legs <= 0:
            raise ValueError("Количество ножек должно быть положительным")
        if max_weight <= 0:
            raise ValueError("Максимальный вес должен быть положительным")

        self.material = material
        self.legs = legs
        self.max_weight = max_weight

    @abstractmethod
    def sit(self, weight: float) -> None:
        """
        Сесть на стул.

        Args:
            weight (float): Вес человека.

        Returns:
            None

        >>> 70 > 0
        True
        """
        ...

    @abstractmethod
    def move(self) -> None:
        """
        Передвинуть стул.

        Returns:
            None

        >>> True
        True
        """
        ...

    @abstractmethod
    def break_chair(self) -> None:
        """
        Сломать стул.

        Returns:
            None

        >>> True
        True
        """
        ...


class Car(ABC):
    """
    Абстрактный класс, описывающий автомобиль.

    Attributes:
        brand (str): Марка автомобиля.
        max_speed (float): Максимальная скорость (км/ч).
        fuel (float): Количество топлива (л).

    >>> isinstance("BMW", str)
    True
    """

    def __init__(self, brand: str, max_speed: float, fuel: float) -> None:
        if not brand:
            raise ValueError("Марка автомобиля не может быть пустой")
        if max_speed <= 0:
            raise ValueError("Максимальная скорость должна быть больше нуля")
        if fuel < 0:
            raise ValueError("Количество топлива не может быть отрицательным")

        self.brand = brand
        self.max_speed = max_speed
        self.fuel = fuel

    @abstractmethod
    def drive(self, distance: float) -> None:
        """
        Проехать заданное расстояние.

        Args:
            distance (float): Расстояние в километрах.

        Returns:
            None

        >>> 10.0 > 0
        True
        """
        ...

    @abstractmethod
    def refuel(self, amount: float) -> None:
        """
        Заправить автомобиль.

        Args:
            amount (float): Количество топлива.

        Returns:
            None

        >>> 5.0 > 0
        True
        """
        ...

    @abstractmethod
    def stop(self) -> None:
        """
        Остановить автомобиль.

        Returns:
            None

        >>> True
        True
        """
        ...


class Tree(ABC):
    """
    Абстрактный класс, описывающий дерево.

    Attributes:
        species (str): Вид дерева.
        height (float): Высота дерева (м).
        age (int): Возраст дерева (лет).

    >>> isinstance("Oak", str)
    True
    """

    def __init__(self, species: str, height: float, age: int) -> None:
        if not species:
            raise ValueError("Вид дерева не может быть пустым")
        if height <= 0:
            raise ValueError("Высота дерева должна быть положительной")
        if age < 0:
            raise ValueError("Возраст дерева не может быть отрицательным")

        self.species = species
        self.height = height
        self.age = age

    @abstractmethod
    def grow(self, meters: float) -> None:
        """
        Увеличить высоту дерева.

        Args:
            meters (float): Прирост в метрах.

        Returns:
            None

        >>> 1.0 > 0
        True
        """
        ...

    @abstractmethod
    def shed_leaves(self) -> None:
        """
        Сбросить листья.

        Returns:
            None

        >>> True
        True
        """
        ...

    @abstractmethod
    def photosynthesis(self) -> None:
        """
        Процесс фотосинтеза.

        Returns:
            None

        >>> True
        True
        """
        ...


if __name__ == "__main__":
    import doctest
    doctest.testmod()
