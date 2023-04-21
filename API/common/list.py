class CustomList(list):
    def __setitem__(self, index, value):
        try:
            super().__setitem__(index, value)
        except IndexError:
            for _ in range(index-len(self)+1):
                self.append(None)
            super().__setitem__(index, value)


def set_list(lst, index, value):
    try:
        lst[index] = value
    except IndexError:
        for _ in range(index - len(lst) + 1):
            lst.append(None)
        lst[index] = value
