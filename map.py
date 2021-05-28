class Map:

    def __init__(self, arr: str):
        self.__string = arr
        self.__h, self.__w = len(arr), len(arr[0])

    def get_width(self) -> int:
        return self.__w

    def get_height(self) -> int:
        return self.__h

    def get_array(self) -> str:
        return self.__string
