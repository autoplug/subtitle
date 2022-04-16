import os

files = os.listdir("./data")
subtitles = []


def isWord(word):
    if not word:
        return False
    for char in word:
        if not ((char >= "A" and char <= "Z") or (char >= "a" and char <= "z") or char == "'"):
            return False
    return True


for file in files:
    if ".sub" in file:
        try:
            file_open = open("./data/"+file, "r")
            subtitles.append(file_open.read())
            file_open.close()
        except:
            print(file)

dic = {}
for subtitle in subtitles:
    subtitle = subtitle.replace('<i>', '')
    subs = subtitle.split("\n")
    for sub in subs:
        words = sub.split(" ")
        for word in words:
            word = word.lower()
            if isWord(word):
                if dic.get(word):
                    dic[word] += 1
                else:
                    dic[word] = 1

dic = {k: v for k, v in sorted(
    dic.items(), key=lambda item: item[1], reverse=True)}
print(len(dic.items()))
# for x in dic.items():
# print(x[1], x[0])
