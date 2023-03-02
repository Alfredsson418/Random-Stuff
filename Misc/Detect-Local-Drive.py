import string,time
from ctypes import windll


def get_driveStatus():
    devices = []
    record_deviceBit = windll.kernel32.GetLogicalDrives()#The GetLogicalDrives function retrieves a bitmask
                                                         #representing the currently available disk drives.
    
    for label in string.ascii_uppercase : #The uppercase letters 'A-Z'
        if record_deviceBit & 1:
            devices.append(label)
        record_deviceBit >>= 1
    return devices


def notifyProgram(drive):

    # This is where you put what the script should do when local drive is inserted
    pass

    


def detect_device():
        original = set(get_driveStatus())

        time.sleep(2)
        
        add_device =  set(get_driveStatus())- original
        subt_device = original - set(get_driveStatus())
        

        if (len(add_device)):
            for drive in add_device:
                    notifyProgram(drive)
                 
        elif(len(subt_device)):
            for drive in subt_device:
                    pass
    


if __name__ == '__main__':
    
    while True:
        detect_device()      

