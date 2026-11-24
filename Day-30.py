#File Handling-->
'''
f=open('Newfile.txt')
print(f.read())

#Best practice is we will use with statement

with open('Newfile.txt','r') as file:
    print(file.read())

#Writing to a file
#'w' mode will create a new file if not existing ,else if already exists it will overwrite the content
g=open('Newfile.txt','w')
print(g)
g.write("Hello...! Deepak")
g.close()

h=open("tNewfile.txt","w")
h.write("my name is balu")
h.write("\n i am from etikoppaka")
logs=['\nFirst ID','\nVinay','\tAjay']
#h.write(logs) #it needs only text
h.writelines(logs) #writelines(iterable)--->writes an iterable of strings(such as list or tuple)
h.close()
print('done')

subjects=['Python','\nSQL','\nAptitude']
with open("Newfile.txt",'w') as file:
    file.writelines(subjects)
    print(file.read())# Io Error
#when we use with block,we need not use close()
    
#Appending to a file-> if file is already existing no change u can add the content,
#if not ne wfile will be created
with open('Today.txt','a') as file:
    file.write("\n student need to finish last week ai mock Interview")
    file.writelines["\n Vijay","\n Vinay","\n Deepak","\n Ramu"]

#usecase: Logging System
def log_activity(activity):
    """User Logs stored"""
    with open('log.txt','a') as log_file:
        log_file.write(activity+'\n')
log_activity("Vinay Logged in for AI MockInterview...")
log_activity("Vinay is testing his microphone and camera")
log_activity("Vinay started his AI MockInterview")
log_activity("Vinnay is Writing the code")
log_activity("Vinay has finished and report created")

#with exceptions
def log_activity(activity):
    """User Logs stored"""
    try:
        with open('log.txt','a') as log_file:
            log_file.write(activity+'\n')
            log_file.read()  #it will get into except block
    except Exception as e:
        print("Error is",e)
    finally:
        print("File handling is importante")
log_activity("Vinay Logged in for AI MockInterview...")
log_activity("Vinay is testing his microphone and camera")
log_activity("Vinay started his AI MockInterview")
log_activity("Vinnay is Writing the code")
log_activity("Vinay has finished and report created")
'''
#r+-->read and write-->preserve the existing content(data),
#new writes overwrite the character from the start of the cursor...
'''
with open('saketh.txt','r+') as file:
    file.write("Testing phase")
    print(file.read())

with open('log.txt','r+') as log_file:
    print(log_file.read())
    log_file.write("End of class")
'''
#Now we will perform write first then read later

with open('Log.txt','r+')as log_file:
    log_file.write("PFS-VSP-007")
    print(log_file.read())

#in above case we are performimg write frst content is overwritten
#from the start of the cursor and when u read it rmng content will
#be shown
#Use case: Modifyng or Updating parts of an exisitng file




































