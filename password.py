import zipfile
import time

folderpath = input("Enter the path of the zipped file: ")
folderpath = folderpath.strip()
zipfolder = zipfile.ZipFile(folderpath)

print(zipfolder)

if not zipfolder:
    print("This is not password protected! You can open the folder normally.")
else:
    startime = time.time()
    result = 0
    c = 0
    characters = ['0','1','2','3','4','5','6','7','8','9', 'a','b','c','d','e','f','g','h','i','j','l','k','m','n','o','p','q','r','s','t','u','v','w','x','y','z', 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','p','Q','R','S','T','U','V','W','X','Y','Z', '!','@','#','$','%','=',':','?','.','/','|','~','>','*','(',')','<','}','{','^','[',']',' ','+','-','_','&',';','"','?','`',"'",'\\']
    print("Brute force started....")
    if (result == 0):
        for i in characters:
            for j in characters:
                for k in characters:
                    for l in characters:
                        guess = str(i) + str(j) + str(k) + str(l)
                        password = guess.encode("utf-8").strip()
                        print("Guess: ", guess)
                        c+=1
                        try:
                            with zipfile.ZipFile(folderpath, 'r') as f:
                                f.extractall(pwd=password)
                                print("Successfully extracted the zipped folder" + guess)
                                endtime = time.time()
                                result = 1
                                break 
                        except:
                            pass
                    if result == 1:
                        break
                if result == 1:
                    break
            if result == 1:
                break
        if result ==0:
            duration = endtime-startime
            print("Unable to encrypt the password. A total of " 
                  + str(c) + " possible combinations tried in " + str(duration) + " seconds")
        else:
            duration = endtime-startime
            print("Password is encrypted. A total of " 
                  + str(c) + " possible combinations tried in " + str(duration) + " seconds")