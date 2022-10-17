import fileReader as fr
import searcher as sc


def searchMark(Key):
    """
    Note: Basically an interface function to read the html file and perform a search in it
    Input: Key(The search key, to be passed to sc.search())
    Output: filteredList(List of filtered URLs wew get from sc.search())
    """
    bookMarks = fr.HtmlReader()
    filteredList = sc.search(Key, bookMarks)
    return filteredList
