def search(para, strLis):
    """
    Note: Basic search function to search the URL list
    Input: para(the search key, or a part of URL used to filter the search), strList(List of the URLs in the form of string)
    Output: ans(list of filtered URLs)
    """
    ans = list()
    for val in strLis:
        if para in val:
            ans.append(val)
    return ans



