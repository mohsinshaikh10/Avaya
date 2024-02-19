#https://www.youtube.com/results?search_query=serial
import webbrowser
import time

def searchyoutube(ans):
    url = "https://www.youtube.com/results?search_query=" + ans
    print(f"Showing results for {ans} Video")
    time.sleep(2)
    webbrowser.register('chrome',
                        None,
                        webbrowser.BackgroundBrowser(r"C:\Users\Mohsin\AppData\Local\Google\Chrome\Application\chrome.exe"))
    webbrowser.get('chrome').open(url)

def searchyoutubefunc():
    print("What do you want to search on Youtube?")
    ans = input("Let me search : ")
    searchyoutube(ans)

# searchyoutubefunc()
