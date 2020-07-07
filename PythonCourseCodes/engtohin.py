from translate import Translator

try:
    with open('ananya.txt',mode='r+',encoding="utf-8") as myfile:
        x = myfile.read()
        trans = Translator(to_lang='hi')
        x = str(trans.translate(x))
        with open('ananya.txt',mode='w',encoding="utf-8") as myfile1:
            print(x)
            x = myfile1.write(x)
except FileNotFoundError:
    print('FileDoesn\'t Exist')
