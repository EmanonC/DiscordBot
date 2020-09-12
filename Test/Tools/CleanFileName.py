import os

filePath="../data/NightStory"
l=os.listdir(filePath)
print(l)
i=0
for file in l:
    newName=f"Story {i}.mp3"
    i+=1
    print(newName)
    src=filePath+'/'+file
    dst=filePath+'/'+newName
    try:
        os.rename(src, dst)
    except:
        pass