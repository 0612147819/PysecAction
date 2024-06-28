import os 

def insecure_function ():
    password = "hardcode password"
    os.system(f'echo {password}')

defsecure_function ():
    password = os.getenv("PASSWORD")
    print(password)
