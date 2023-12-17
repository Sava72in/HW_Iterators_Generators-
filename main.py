class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.end = len(self.list_of_list)
        self.start = -1
        self.item = []
    def __iter__(self):
        self.list_of_list
        return self

    def __next__(self):
        self.start += 1
        if self.start >= self.end:
            raise StopIteration
        return next([i for i in self.list_of_list[self.start]])



# list_of_lists_1 = [
#         ['a', 'b', 'c'],
#         ['d', 'e', 'f', 'h', False],
#         [1, 2, None]
#     ]
#
# for item in FlatIterator(list_of_lists_1):
#     print(item)

def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            list_of_lists_1,
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(list_of_lists_1) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
