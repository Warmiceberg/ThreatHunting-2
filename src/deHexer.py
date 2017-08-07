import re
pth = raw_input("Enter the obfuscated file - ")
with open(pth,'r') as f:
    with open("final.txt", "a") as w:
        for line in f:
            for word in line.split(';'):
                word = word.replace('_', '')
                try:
                    if re.match(r'^\\x', word):
                        print "word " + word
                        word1 = word.replace('\\x', '')
                        deobs = word1.decode('hex')
                        print "deob " + deobs
                        w.write(deobs)
                    else:
                        w.write(word)
                except Exception,e:
                    print str(e)
                    w.write(word)
                    pass
                    

            