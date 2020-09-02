
#might make a class, with path, text, freq_table, and ori variables
def PatternCount(text, pattern):
    count = 0
    for i in range(len(text)):
        if text[i:len(pattern)] == pattern:
            count = count + 1
    return count

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

#find keys in table greater than specified amount
def loc_rep(table, reps): #input frequency table, repetitions
    keys = []
    for i,j in table.items():
        if j >= reps:
            keys.append(i)
    return keys

#find likely ori given dataset
def find_ori(path, k):
    data = open(path, 'r')
    text = data.read()
    table = frequency(text, k)
    ori = max_rep(table)
    return ori

def findClumps(text, k, L, t): #k is size of k-mer, L size of region searching, t is frequency 
    ans = []
    for i in range(len(text)):
        length = i + L
        if length < len(text):
            region = text[i:length] #takes the region of however many characters, make frequency table, find the patterns of length k that repeat at least t times
            table = frequency(region, k)
            toAdd = loc_rep(table, t)
            #now to check for repeats:
            for j in range(len(toAdd)):
                inAns = False
                for b in range(len(ans)):
                    if (ans[b] == toAdd[j]):
                        inAns = True
                if not inAns:
                    ans.append(toAdd[j])
    return ans

def main():
    ori = find_ori('bio_data/Vibrio_cholerae.txt', 9)
    print(ori)

if __name__ == "__main__":
    main()
