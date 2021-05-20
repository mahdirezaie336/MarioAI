class Map:

    def __init__(self, arr: [str]):
        self.__arr = arr
        self.__h, self.__w = len(arr), len(arr[0])

    def get_width(self):
        return self.__w

    def get_height(self):
        return self.__h

    def get_array(self):
        return self.arr
