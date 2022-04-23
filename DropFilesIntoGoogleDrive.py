from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
from datetime import datetime


# Creating Access Token to connect to Google Drive API
# If Access Token is Empty, load new tokens
# Else refresh the tokens


# ** make sure you generate client_secrets.json. ( Create Google Drive OAuth Key)


gauth = GoogleAuth()
# Try to load saved client credentials
gauth.LoadCredentialsFile("mycreds.txt")
if gauth.credentials is None:
    # Authenticate if they're not there
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    # Refresh them if expired
    gauth.Refresh()
else:
    # Initialize the saved creds
    gauth.Authorize()
    print("Authentication Successful")

# Save the current credentials to a file
gauth.SaveCredentialsFile("mycreds.txt")

folder_Name = 'TestUploadFolder'
cwd = os.getcwd()

drive = GoogleDrive(gauth)

# parent folder id
# set manually
folder_id = '---folder id ---'  # Replace placeholder with folder ID

'''

Copy the Folder ID found in the URL. This is everything that comes after “folder/” in the URL. 
For example, if the URL was “https://drive.google.com/drive/folders/1dyUEebJaFnWa3Z4n0BFMVAXQ7mfUH11g”, 
then the Folder ID would be “1dyUEebJaFnWa3Z4n0BFMVAXQ7mfUH11g”.

'''


def CreateNewFolder(parent_id, new_folder_name):

    try:
        new_folder = drive.CreateFile({'title': new_folder_name, 'parents':[{'id':parent_id}], \
                'mimeType':'application/vnd.google-apps.folder'})
        new_folder.Upload()
        return True
    except:
        print("Error Occured during creation of Folder!")
        return False

def UploadFiles(file,newFolder_id):

    uploader = drive.CreateFile({'parents':[{'id':newFolder_id}]})
    uploader.SetContentFile(file)
    uploader.Upload()
    print('Uploaded {0}'.format(file))
    





if __name__=='__main__':

    scriptstarttime = datetime.now()
    
'''   
	code you logic to create a new folder in Gdrive or upload to Gdrive
    
'''
 
    print("Finished Uploading!")
