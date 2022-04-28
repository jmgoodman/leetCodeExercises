rowsList = ["" for _ in range(4)]
rowsList[2] += "a"
rowsList[2] += "b"
rowsList[2].join("c")
print(rowsList)