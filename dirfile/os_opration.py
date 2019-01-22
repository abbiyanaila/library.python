import os

print(f"Listing Directory : {os.listdir('/home')}")
print(f'Counting CPU : {os.cpu_count()}')
print(f'Where is My current working directory? : {os.getcwd()}')
print(f"Get my Directory name from /home/abbiyanaila {os.path.dirname('/home/abbiyanaila')}")
print(f"Check The existence of directory /home/abbiyanaila: {os.path.exists('/home/abbiyanaila')}")
print(f"Join path directory : {os.path.join('/home','desi','test')}")

#detele operation with os
mypath = os.getcwd()
myfile = os.path.join(mypath, 'test.txt')
if os.path.exists(myfile):
     os.unlink(myfile)


# create directory recursively
mypath = os.getcwd()
mydir = os.path.join(mypath, 'testdir','test_again','again')
os.makedirs(mydir, exist_ok=True)

#755 for permission
import stat
os.chmod(mydir, stat.S_IRWXG)