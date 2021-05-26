file_name =input("enter the file name: ")
g = file_name.split(".")
dic ={
    'py' : 'python',
    'doc' : 'Word',
    'pdf' : 'PDF',
    'html' : 'HTML',
    'txt' : 'text'
}
extension = g[-1]
print(" The extension of the file is ", dic[extension])

'''
output
enter the file name: hello.py
The extension of the file is  python
 
'''
