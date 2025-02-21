from PIL import Image
import sys
import os.path

n = len(sys.argv)

if (n >= 2):
    image = sys.argv[1]
    imageNoExt = os.path.splitext(os.path.basename(image))[0]
    imageExt = os.path.splitext(os.path.basename(image))[1]
    
    if (os.path.isfile(image)):
        try:
            img = Image.open(image)
            r, g, b = img.split()
            
            outpath = ".\\out"
            
            if(n==3):
                outpath = sys.argv[2]
            
            outdirectory = outpath + "\\" + imageNoExt
            
            if not os.path.exists(outdirectory):
                print("Creating output dirrectory.")
                os.makedirs(outdirectory)
                
            r.save(outdirectory + "\\" + imageNoExt + "_M" + imageExt)
            g.save(outdirectory + "\\" + imageNoExt + "_R" + imageExt)
            b.save(outdirectory + "\\" + imageNoExt + "_AO" + imageExt)
        except IOError:
            print("User supplied file is not an image, or unsuported image file (psd / svg do not supported)")
    else:
        print("Image does not exist, check file name / path")
else:
    print("Usage: ChannelExtractor.py pathToImage OPTIONAL:OutputPath")