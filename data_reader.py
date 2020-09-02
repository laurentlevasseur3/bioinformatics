#make frequency table of k-mers,
def frequency(text, k):  #input dataset and k
    table = {}
    #loop thru, make sure it doesn't go out of bounds, make sure no repeats
    for i in range(len(text)):
        end = i + k
        if end < len(text):
            if text[i:end] in table:
                table[text[i:end]] += 1
            else:
                table[text[i:end]] = 1
    return table

#find max repetitions in dataset
def max_rep(table): # input frequency table
    maxi = ""
    maxj = 0
    for i,j in table.items():
        if j > maxj:
            maxi = i
            maxj = j
    return maxi

class Dataset:
    def loc_rep(reps):
        keys = []
        for i,j in self.table.items():
            if j >= reps:
                keys.append(i)
        return keys
    
    def __init__(self, path, k):
        data = open(path, 'r')
        self.text = data.read()
        self.table = frequency(self.text, k)
        self.ori = max_rep(self.table)
        self.reps = self.table[self.ori]

def main():
    d1 = Dataset('bio_data/Vibrio_cholerae.txt', 9)
    print(d1.ori)
    print(d1.reps)

if __name__ == "__main__":
    main()
