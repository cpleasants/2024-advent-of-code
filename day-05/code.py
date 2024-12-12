class Day05:
    def __init__(self, fname):
        self.pairs = []
        self.page_lists = []
        with open(fname) as f:
            for line in f:
                if '|' in line:
                    self.pairs.append(line.strip().split("|"))
                elif line.strip == '':
                    continue
                elif ',' in line:
                    self.page_lists.append(line.strip().split(","))
        self.pairs = [[int(p) for p in pair] for pair in self.pairs]
        self.page_lists = [[int(p) for p in page_list] for page_list in self.page_lists]
        self.check_orders()
        self.reorder()

    def check_order(self, li):
        # Convert page lists to dict for lower complexity when checking indices
        d = {item:i for i, item in enumerate(li)}
        # then check
        correct = True
        for pair in self.pairs:
            if pair[0] not in d or pair[1] not in d:
                continue
            if d[pair[0]] < d[pair[1]]:
                continue
            else:
                correct = False
                break
        return correct

    def check_orders(self):
        self.correctly_ordered = []
        self.incorrectly_ordered = []
        for i, li in enumerate(self.page_lists):
            if self.check_order(li):
                self.correctly_ordered.append(self.page_lists[i])
            else:
                self.incorrectly_ordered.append(self.page_lists[i])
            

    def add_middles(self, correct:bool):
        middle_sum = 0
        if correct:
            for li in self.correctly_ordered:
                middle_sum += li[int((len(li) - 1) / 2)]
        else:
            for li in self.re_ordered:
                middle_sum += li[int((len(li) - 1) / 2)]
        return middle_sum
    
    def find_first_violation(self, li):
        d = {item:i for i, item in enumerate(li)}
        for pair in self.pairs:
            if pair[0] not in d or pair[1] not in d:
                continue
            if d[pair[0]] > d[pair[1]]:
                return pair
    
    def move_violation(self, li, pair_violated):
        new_li = li.copy()
        new_li.insert(new_li.index(pair_violated[1]), new_li.pop(new_li.index(pair_violated[0])))
        return new_li

    def reorder(self):
        self.re_ordered = []
        for i, li in enumerate(self.incorrectly_ordered):
            new_li = li.copy()
            # TODO: change to a while loop. Never reaches 90.
            for j in range(100):
                pair_violated = self.find_first_violation(new_li)
                new_li = self.move_violation(new_li, pair_violated)
                if self.check_order(new_li):
                    break
                if j > 90:
                    print(j)
            self.re_ordered.append(new_li)

day05 = Day05('data/input.txt')
print(day05.add_middles(True))
print(day05.add_middles(False))