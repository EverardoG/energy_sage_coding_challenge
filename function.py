"""
Please write a function that takes in two collections of objects and returns another
collection that contains only those objects that are in both input collections. Assume
that the input collections are large, and this function will be called frequently so
performance matters.
"""

def matchObjects( collection_1, collection_2):
    """
    INPUTS:
    (str, list, set, or tuple) collection_1
    (str, list, set, or tuple) collection_2
    Returns:
    (same type as collection_1) collection_match

    This function takes in two collections of objects and returns a
    collection that contains only those objects that are in both
    input collections
    """

    # Check that both inputs are iterable
    try:
        iter(collection_1)
    except TypeError:
        raise TypeError(collection_1, "is not iterable")
    try:
        iter(collection_2)
    except TypeError:
        raise TypeError(collection_2, "is not iterable")

    # Check if either collection is empty, if so, return the empty collection
    if len(collection_1) == 0:
        return collection_1
    elif len(collection_2) == 0:
        return collection_2

    # Check if collection_1 and collection_2 are the same collection - if so, just return collection_1
    if collection_1 is collection_2:
        return collection_1

    # Build a hashmap of all the objects in collection_1 - key is the object, value is true
    # Runtime: O(N) where N is the length of collection_1
    dict_1 = { obj:True for obj in collection_1 }

    # Iterate through collection_2, checking the object is a key for dict_1, meaning it's in collection_1
    # If so, place it in collection_match
    # Runtime: O(M) where M is the length of collection_2
    # It is worth noting here that obj in dict_1 uses the dictionary's hashing, which means each check is an O(1) runtime
    collection_match = [ obj for obj in collection_2 if obj in dict_1 ]

    # Total Runtime: O(N + M)
    return collection_match
