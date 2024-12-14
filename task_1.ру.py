class AbstractContainer:
    """
    Абстрактный класс, описывающий контейнер.

    Attributes:
        capacity (int): Вместимость контейнера. Должно быть положительным числом.
        contents (list): Список содержимого контейнера.
    """

    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be a positive integer.")
        self.capacity: int = capacity
        self.contents: list = []

    def add_item(self, item: object) -> None:
        """
        Добавляет элемент в контейнер.

        Args:
            item: Элемент для добавления.

        Returns:
            None
        """
        ...

    def remove_item(self, item: object) -> object:
        """
        Удаляет элемент из контейнера.

        Args:
            item: Элемент для удаления.

        Returns:
            Удаленный элемент, или None, если элемент не найден.
        """
        ...

class AbstractNetwork:
    """
    Абстрактный класс, описывающий сеть (например, компьютерную сеть или социальную сеть).

    Attributes:
        nodes (int): Количество узлов в сети. Должно быть неотрицательным числом.
        connections (int): Количество соединений между узлами. Должно быть неотрицательным числом.
    """

    def __init__(self, nodes: int, connections: int):
        if nodes < 0 or connections < 0:
            raise ValueError("Nodes and connections must be non-negative integers.")
        self.nodes: int = nodes
        self.connections: int = connections

    def add_node(self) -> None:
        """
        Добавляет узел в сеть.

        Args:
            None

        Returns:
            None
        """
        ...

    def remove_node(self, node_id: int) -> None:
        """
        Удаляет узел из сети.

        Args:
            node_id: Идентификатор узла для удаления.

        Returns:
            None
        """
        ...

class AbstractProcess:
    """
    Абстрактный класс, описывающий процесс (например, физический или вычислительный).

    Attributes:
        duration (float): Длительность процесса в секундах. Должно быть положительным числом.
        status (str): Статус процесса ("started", "running", "finished", "error").
    """

    def __init__(self, duration: float):
        if duration <= 0:
            raise ValueError("Duration must be a positive number.")
        self.duration: float = duration
        self.status: str = "started"

    def start(self) -> None:
        """
        Запускает процесс.

        Args:
            None

        Returns:
            None
        """
        ...

    def get_status(self) -> str:
        """
        Возвращает статус процесса.

        Args:
            None

        Returns:
            Строка, описывающая статус процесса.

        >>> process = AbstractProcess(5.0)
        >>> process.get_status()
        'started'
        """
        return self.status