def search(para, strLis):
    ans = list()
    for val in strLis:
        if para in val:
            ans.append(val)
    return ans



