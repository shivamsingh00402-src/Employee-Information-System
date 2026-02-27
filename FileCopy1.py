#Program for Copying the content of One Program into Another Program
#FileCopy1.py
def filecopy():
    try:
        srcfile=input("Enter Source File:")
        with open(srcfile,"r") as rp:
            dstfile=input("Enter Destination File:")
            with open(dstfile,"a") as wp:
                srcfiledata=rp.readlines() # Reading Source file Data
                wp.write(srcfiledata) # Writing Source file Data to Destination file
                print("Source File Content Copied into Destination File ")
    except FileNotFoundError:
        print("Source File Does Not Exist")

# Main Program
filecopy()