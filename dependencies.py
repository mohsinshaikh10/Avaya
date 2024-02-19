import os
dependencies = ["conda install -c conda-forge opencv","conda install -c conda-forge wikipedia","conda install pyaudio","pip install speechRecognition","pip install pyttsx3","pip install torch","pip install nltk"]
for d in dependencies:
    v=os.system(d)
    print(d," : ",v)