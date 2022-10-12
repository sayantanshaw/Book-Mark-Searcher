import fileReader as fr
import searcher as sc


def searchMark(Key):
    bookMarks = fr.HtmlReader()
    filteredList = sc.search(Key, bookMarks)
    return filteredList
