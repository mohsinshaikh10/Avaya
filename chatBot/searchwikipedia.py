import wikipedia
from chatBot.websearch import searchgooglefunc
def searchwikipediafunc():
    try:
        searchr = input("What do you want to Wiki: ")
        result = wikipedia.summary(searchr,sentences=5)
        searchurl = wikipedia.page(searchr).url
        print(result)
        print(f"You can read more on : {searchurl}")
    except:
        print("Showing results from Google")
        searchgooglefunc(searchr)