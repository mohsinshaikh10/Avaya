import webbrowser
import time
def searchgooglefunc(ans):
    # ans = input("What do you want to search: ")
    url = "https://www.google.com/search?q="+ans
    print(f"Showing results for {ans}")
    time.sleep(2)
    webbrowser.register('chrome',
        None,
        webbrowser.BackgroundBrowser(r"C:\Users\Mohsin\AppData\Local\Google\Chrome\Application\chrome.exe"))
    webbrowser.get('chrome').open(url)

# ans = input("What do you want to search: ")
# searchgooglefunc(ans)

def callgooglesearch():
    ans = input("What do you want to search: ")
    searchgooglefunc(ans)