import types


class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
#
    def __iter__(self):
        self.counter = 0
        self.i = -1
        return self

    def __next__(self):
        self.i += 1
        self.item = self.list_of_list[self.counter]
        self.count_i = len(self.item)
        if self.count_i == self.i:
            self.counter += 1
            if self.counter == len(self.list_of_list):
                raise StopIteration
            self.i = 0
        item = self.list_of_list[self.counter][self.i]
        return item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()



def flat_generator(list_of_lists_1):
    counter = 0
    i = 0
    while True:
         if len(list_of_lists_1) - 1 >= counter:
            if len(list_of_lists_1[counter]) - 1 >= i:
                item = list_of_lists_1[counter][i]
                yield item
                i += 1
            else:
                i = 0
                counter += 1
         else:
            break

def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()



def flat_generator(list_of_lists_2):
    for i in list_of_lists_2:
        if isinstance(i, list):
            yield from flat_generator(i)
        else:
            yield i

def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()



