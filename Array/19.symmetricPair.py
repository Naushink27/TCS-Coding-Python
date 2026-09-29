# Given an array of pairs of integers pairs[][] where each pair contains two integers [a, b]. Your task is to find all the symmetric pairs in the given array.
# Two pairs [a, b] and [c, d] are said to be symmetric if b == c and a == d.
# • If a pair has multiple symmetric matches, only output the match once.
# • If a pair matches with itself (e.g., [2, 2]), it is not considered a symmetric pair unless another identical [2, 2] exists in the array.


seenPairs=set()
res=[]

pairs = [[11, 20], [30, 40], [5, 10], [40, 30], [10, 5]]

for first,second in pairs:
    target_pair=(second,first)
    if target_pair in seenPairs:
        res.append([first,second])
    else:
        seenPairs.add((first,second))

print(res)