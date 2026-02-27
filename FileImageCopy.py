#Program for Copying the Image
#FileImageCopy.py
def filecopy():
    try:
        with open("C:\\Users\\shiva\\OneDrive\\Pictures\\shivam.jpg","rb") as rp:
            with open("Sm.png","wb") as wp:
                srcfiledata=rp.read() # Reading Source file Data
                wp.write(srcfiledata)# writing Source file Data to destination file
                print("Image Copied--Verify")
    except FileNotFoundError:
        print("Source File Does Not Exist")

#Main Program
filecopy()
