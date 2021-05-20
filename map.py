class Map:

    def __init__(self, arr: list[list[str]]):
        self.__arr = arr
        self.__h, self.__w = len(arr), len(arr[0])

    def get_width(self) -> int:
        return self.__w

    def get_height(self) -> int:
        return self.__h

    def get_array(self) -> list[list[str]]:
        return self.__arr
