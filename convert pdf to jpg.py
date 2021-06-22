import pdf2image, os, shutil
from pdf2image import convert_from_path

def convert(fileType):
    for file in os.listdir():                       
        if file.endswith(fileType):  
            images = convert_from_path(file)
            for i in range(len(images)):
                temp = file.split(fileType) #Delete .pdf from the filename
                newFileName = temp[0]
                images[i].save(newFileName+ str(i+1) +'.jpg', 'JPEG')
            print(file + " has been converted to .jpg file(s)")  

def moveTo(fileType, location):                
    if not os.path.exists(location):       
        os.mkdir(location)
    for file in os.listdir():                        
        if file.endswith(fileType):                  
            print(file + " moved to  \""+location+"\"")  
            shutil.move(file, location)              


imageFiles = (".jpg", ".JPG", ".jpeg")

convert(".pdf")
moveTo(imageFiles, "converted")

print("All done!")
input("Press Enter to close this window")
