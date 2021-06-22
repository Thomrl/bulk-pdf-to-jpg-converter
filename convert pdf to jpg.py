import pdf2image, os, shutil
from pdf2image import convert_from_path

os.chdir(r"C:\Users\thomas\Documents\test")
cwd = os.getcwd()

def work(fileType, location):
    for file in os.listdir():                       
        if file.endswith(fileType):                 
            if not os.path.exists(location):       
                os.mkdir(location)

            images = convert_from_path(file)
            print(images)
            for i in range(len(images)):
                temp = file.split(fileType)
                newFileName = temp[0]
                images[i].save(newFileName+ str(i+1) +'.jpg', 'JPEG')
            print(file + " --->> \""+location+"\"")  


def sortByFile(fileType, location):
    for file in os.listdir():                        
        if file.endswith(fileType):                  
            if not os.path.exists(location):         
                os.mkdir(location)                   
            print(file + " --->> \""+location+"\"")  
            shutil.move(file, location)              


pdfFiles = (".pdf")
imgFiles = (".jpg", ".JPG", ".jpeg", ".png", ".gif")

work(pdfFiles, "converted")
sortByFile(imgFiles, "converted")
