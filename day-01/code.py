class Day1:
    def __init__(self, fname):
        with open(fname) as f:
            data = f.readlines()
        self.l0 = [float(row.strip().split('   ')[0]) for row in data]
        self.l1 = [float(row.strip().split('   ')[1]) for row in data]
    
    def total_distance(self):
        out_l = []
        for i in range(len(self.l0)):
            out_l.append(abs(sorted(self.l1)[i] - sorted(self.l0)[i]))
        return sum(out_l)
    
    def similarity_score(self):
        l1_counter = {}
        for item in self.l1:
            if item in l1_counter:
                l1_counter[item] += 1
            else:
                l1_counter[item] = 1
        similarity_score = 0
        for item in self.l0:
            if item in l1_counter:
                similarity_score += item * l1_counter[item]
        return similarity_score
