def PatternCount(text, pattern):
    count = 0
    for i in range(len(text)):
        end = i + len(pattern)
        if (end < len(text)):
            if text[i:end] == pattern:
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
def find_most_common(path, k):
    data = open(path, 'r')
    text = data.read()
    table = frequency(text, k)
    ori = max_rep(table)
    return ori

def reverse_complement(text): #finds the reverse complement of a gene
    comp_key = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    comp = ""
    for i in range(len(text) - 1, -1, -1):
        comp = comp + comp_key[text[i]]
    return comp

def pattern_match(text, pattern): #finds indeces of pattern occurences
    appearances = []
    for i in range(len(text)):
        end = i + len(pattern)
        if (end < len(text)):
            if text[i:end] == pattern:
                appearances.append(i)
    return appearances

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

def min_skew(text): #G - C, used to find DnaA box regions due to DNA replication stuff
    skew_count = 0
    skew_count_arr = []
    arr_min = 0
    indeces = []
    for i in range(len(text)):
        if (text[i] == "C"):
            skew_count = skew_count - 1
        elif (text[i] == "G"):
            skew_count = skew_count + 1
        skew_count_arr.append(skew_count)

    for i in range(len(skew_count_arr)):
        if (skew_count_arr[i] < arr_min):
            arr_min = skew_count_arr[i]

    for i in range(len(skew_count_arr)):
        if (skew_count_arr[i] == arr_min):
            indeces.append(i)
    return indeces
    
def HammingDistance(a, b):
    count = 0
    for i in range(len(a)):
        if(a[i] != b[i]):
            count = count + 1
    return count

def ApproxPatternMatch(pattern, text, d):
    table = frequency(text, len(pattern))
    match_arr = []
    pos = []
    for i in table.keys():
        if (HammingDistance(pattern, i) <= d):
            match_arr.append(i)      
    for i in range(len(text)):
        end = i + len(pattern)
        if end < len(text):
            if (text[i:end] in match_arr):
                pos.append(i)
    return pos
