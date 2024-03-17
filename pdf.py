from PyPDF2 import PdfReader, PdfWriter

filename = input("Enter the file path: ")
filename = filename.strip()
file = open(filename, "rb")
pdfreader = PdfReader(file)
print(pdfreader)

#print(len(pdfreader.pages))

#page = pdfreader.pages[0]
#print(page.extract_text())

count = 0

if not pdfreader.is_encrypted:
    print("Open the file directly!")
else:
    wordListfile = open("words.txt", "r", errors="ignore")
    body = wordListfile.read().lower()
    words = body.split("\n")

    for i in range(len(words)):
        word = words[i]
        print("Trying to decode the password by :{}".format(word))
        result = pdfreader.decrypt(word)
        print(result)

        if result == 1:
            print("The password is: " + word)
            break
        elif result == 0:
            count += 1
            print("Passwords tried: " + str(count))
            continue
