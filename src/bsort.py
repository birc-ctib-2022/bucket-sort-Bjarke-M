"""Module for bucket sorting."""

from typing import Any


def count_keys(keys: list[int]) -> list[int]:
    """
    Count how many times we see each key in `keys`.

    You can assume that all elements in `keys` are
    non-negative. This is not a requirement for
    bucket sort in general--it can handle negative
    numbers--but it is a little more complicated and
    we will keep it simple here.

    You should return a list, `counts`. The list you
    return should have `len(counts) == max(keys) + 1`
    so we can index into any key (including those
    that might not be included in `keys`) and for each
    key `0 <= k <= max(keys)` `counts[k]` should be
    the number of times `k` occurs in `x`.

    The function should take time `O(len(keys))` and
    not more.

    >>> count_keys([1, 2, 2, 1, 4])
    [0, 2, 2, 0, 1]
    """
    # we can get the number of keys from keys if
    # it is non-empty. Otherwise we must assume that
    # there are no keys.
    if keys != []: #check that it is non empty
        max_keys=max(keys) # find the length of the list 
        result=[0 for i in range(0,max_keys+1)] #make a list with zeros 
        for i in keys:
            result[i]+=1 # count every occurence of the int and change the count for the int
        return result
    else:
        return [] # if empty


def count_sort(x: list[int]) -> list[int]:
    """
    Sort the values in x using count sort.

    The values in x must satisfy the constraints
    mentioned in `count_keys()`.

    >>> count_sort([])
    []
    >>> count_sort([1, 2, 1, 2, 4])
    [1, 1, 2, 2, 4]
    """
    result=[] # empty list
    if x != []: #check that input is not empty
        y=count_keys(x) #make a list which counts every occurence
        for i in range(len(y)):
            if y[i] != 0: # in the result we dont want the ints that does not occur in the list
                k=y[i] # to append the ints in the right order and the right number of times
                while k:
                    result.append(i) #appending the ints 
                    k -= 1 # increment sp we dont run forever
    return result


def cumsum(x: list[int]) -> list[int]:
    """
    Calculate the cumulative sum of x.

    >>> cumsum([1, 2, 3])
    [0, 1, 3]
    >>> cumsum([0, 2, 2, 0, 1])
    [0, 0, 2, 4, 4]
    """
    accumulator=0
    seq1=x #mmh not the smartest way of editing a sequence, but it works
    for i, val in enumerate(seq1): #enumerate takes both the index and the value, Thanks Andreas!
            seq1[i]=accumulator # changes the sequences[index] to our accumulator 
            accumulator += val # and changes the accumulator for every step
    return seq1


def bucket_sort(x: list[tuple[int, Any]]) -> list[tuple[int, Any]]:
    """
    Sort the keys and values in x using count sort.

    The keys in x must satisfy the constraints
    mentioned in `count_keys()`.

    >>> bucket_sort([])
    []
    >>> bucket_sort([(1, "a"), (2, "b"), (1, "c"), (2, "d"), (4, "e")])
    [(1, 'a'), (1, 'c'), (2, 'b'), (2, 'd'), (4, 'e')]
    """
    buckets = cumsum(count_keys([i for i,_ in x])) #constructs buckets, a list of accumulated sum of the first index in the tuples 
    out = [(0, None)] * len(x) # making a list of tuples as long as the input
    if x != []: # making sure it's no empty
        for i,v in x: # taking both the first and second index of the input ex. 1,a or 2,b etc
            out[buckets[i]] = (i,v)  # using the value of value of cumsum to determine the index i the result in which we want out key and value
            buckets[i] += 1 # making sure that we do not try to overwrite our data, by shifting indexes to the 'right'
    else: 
        out=[]
    return out

# I dont think i made the most efficient or even readable code, enumerate helped, and if there are other smart moves 
# feedback is always appreciated.
