'''
This module sets up the log-in GUI.

Notes:
    As you can see, variables loginWin and signinWin are globals,
    the reason they are submit as function parameters
    is to increase compatibility for future usage elsewhere.
'''

##functions

#set-up functions
def loginWin_config(win):
    
    win.protocol('WM_DELETE_WINDOW',
                 lambda: win.destroy() or ROOT.quit()) #click 'X' shuts down the whole program

    ##call-backs and binds
    loginFrame = win.loginFrame
    #call-backs
    loginFrame.signin.config(command=signin)
    loginFrame.login. config(command=lambda: login(loginFrame))
    #binds
    win.bind('<Return>', lambda event: login(loginFrame))

def signinWin_config(win):
    win.protocol('WM_DELETE_WINDOW',
                 lambda: win.destroy() or ROOT.quit()) #same as loginWin_setup()
    
    ##call-backs and binds
    signinFrame = win.signinFrame
    #call-backs
    signinFrame.cancel.config(command=cancel)
    signinFrame.signin.config(command=lambda: submit(signinFrame))
    #binds
    win.bind('<Return>', lambda event: submit(signinFrame))

def startWin_config(win):

    win.protocol('WM_DELETE_WINDOW',
                 lambda: win.destroy() or ROOT.quit()) #same as loginWin_setup()


    ##call-backs and binds
    startFrame = win.startFrame
    #call-backs
    startFrame.start.config(command=lambda: start(startFrame))
    startFrame.exit .config(command=lambda: win.destroy() or ROOT.quit())
    #binds
    win.bind('<Return>', lambda event: start(startFrame))

#call-backs
def signin():
    '''
there should only be one window displayed at a time.
    '''
    global loginWin, signinWin
    loginWin .withdraw ()
    signinWin.deiconify()
    signinWin.signinFrame.username.entry.focus() #regain focus

def cancel():
    '''
    similar as signin().
    '''
    global loginWin, signinWin
    signinWin.withdraw ()
    loginWin .deiconify()
    loginWin .loginFrame.username.entry.focus() #regain focus

def submit(signinFrame):
    if signinFrame.isValidSubmit():
        cancel()
    else:
        signinWin.deiconify()
        signinFrame.username.entry.focus()

def login(loginFrame):
    isValidSubmit, loginDict = loginFrame.submitResult()
    if isValidSubmit:
        loginWin.withdraw()
        startWin.setupViaLoginInfo(loginDict)
        startWin_config(startWin)
        startWin.deiconify()
    else:
        loginWin.deiconify()
        loginFrame.username.entry.focus()

def start(startFrame):
    print('shutting down log-in GUI...')
    startWin.destroy()
    ROOT.quit()
    updateTempUser(startFrame.userDict)

    print('starting game...')
    from subprocess import Popen, PIPE

    import sys

    if len(sys.argv) > 1:
        if   (sys.argv[1], sys.argv[2]) == ('-m', 'py'):
            'launch StartGame.py'
            pipe = Popen('python StartGame.py', stdout=PIPE, stderr=PIPE, text=True)
        elif (sys.argv[1], sys.argv[2]) == ('-m', 'exe'):
            'launch StartGame.exe'
            pipe = Popen('StartGame.exe', stdout=PIPE, stderr=PIPE, text=True)
    else:
        print('NO ARGS PASSED')
        input()
        raise SystemExit

    stdout, stderr = pipe.communicate()
    print('\n===== GAME STDOUT =====\n')
    print(stdout, end='')
    print('\n===== GAME STDERR =====\n')
    print(stderr, end='')
    print('\n===== MAIN STDOUT =====\n')
    print('returncode: %d' % pipe.returncode)

if __name__ == '__main__':
    try:
        ###imports
        ##debug tools, should be imported first
        from Modules.DebugTools import beforeExit, traceBug
        ##claeees
        #windows
        from tkinter import Tk
        #interfaces
        from Modules.Classes.GUITools import LoginWin, SigninWin, StartWin
        ##constants
        #paths
        from Modules.Locals.Paths import TEMP
        ##functions
        from Modules.Data.Running import updateTempUser
        ##modules
        import os

        print('\n===== MAIN STDOUT =====\n')
        ###
        ROOT = Tk(); ROOT.withdraw()

        loginWin = LoginWin (ROOT); loginWin.focus()
        signinWin= SigninWin(ROOT); signinWin.withdraw()
        startWin = StartWin (ROOT); startWin .withdraw()

        loginWin_config (loginWin )
        signinWin_config(signinWin)
        #startWin_config is called via call-back login()

        ROOT.mainloop()
    except Exception:
        print('-'*32)
        print('BUG OCCURED!')
        print('IN GUI:')
        traceBug()
        beforeExit()
