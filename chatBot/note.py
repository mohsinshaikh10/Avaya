import datetime
from datetime import datetime

def notefunc():
    text = input("Tell me to note: ")
    title = input("What do you want to save this note as: ")
    now = datetime.now()
    date = now.strftime("%H:%M:%S")
    file_name = str(date).replace(":", "-")+"("+title+")-note.txt"
    with open("Notes/"+file_name, "w") as f:
        f.write(f"{title}\n{text}")

    print(f"Note saved as {title}")
    # subprocess.Popen(["notepad.exe", file_name])

# notefunc()