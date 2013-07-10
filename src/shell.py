import logging

class Shell():

    def __init__(self):
        self.kernel = None
        self.users = {} ##Users dictionary(key=user-name, value=object-user)
        self.currentUser = None #User who is using the shell,
                                #      it is set at 'login'
        self.validCommands = {'login': self.login,
                              'logout': self.logout,
                              'exit': self.exit,
                              'help': self.help,
                              'addUser': self.addUserShell,
                              'addAdmin': self.addAdminShell,
                              'removeAdmin': self.removeAdminShell,
                              'whoAmI': self.whoAmI,
                              'changeCurrentUserPW': self.changeCurrentUserPWShell,
                              'changeUserPW': self.changeUserPW}

        self.programs = {}

        ##Set up for logging
        logging.basicConfig(level=logging.DEBUG, format='%(message)s')

        #Initial setup, adds principal admin.
        admin = User("admin", "adminPW")
        admin.setAdmin(True)
        self.currentUser = admin
        self.addUser(admin.name, admin.pw)
        self.setAdmin("admin", True)
        self.currentUser = None

    def addAdmin(self, userName):
        """Adds admin privilege to userName on the shell"""
        self.setAdmin(userName, True)

    def addAdminShell(self):
        """Gives follow steps for client of the shell"""
        if self.currentUser.isAdmin():
            userName = input('Please enter user: ')
            if self.existUser(userName):
                self.addAdmin(userName)
            else:
                logging.info("Specified user does not exist.")
        else:
            logging.info("Current user is not an admin.")

    def removeAdmin(self, userName):
        """Removes admin privilege to userName on the shell"""
        self.setAdmin(userName, False)

    def removeAdminShell(self):
        """Gives follow steps for client of the shell"""
        if self.currentUser.isAdmin():
            userName = input('Please enter user: ')
            if self.existUser(userName):
                self.removeAdmin(userName)
            else:
                logging.info("Specified user does not exist.")
        else:
            logging.info("Current user is not an admin.")

    def addUser(self, userName, userPW):
        """It can only be used by a logged in admin.
		 to add a new user to the user dictionary.
        """
        user = User(userName, userPW)
        self.users.update({user.name:user})

    def addUserShell(self):
        """Gives follow steps for client of the shell"""
        if self.currentUser.isAdmin:
            userName = input('Please enter new user alias: ')
            userPW = None
            if self.existUser(userName):
                logging.info("User alias already exists.")
            else:
                userPW = input("Please enter new user's password: ")
                self.addUser(userName, userPW)
        else:
            logging.info('Current user is not an admin.')

    def login(self):
        """Log in user, ask for pw,
		compare and if correct set currentUser.
        """
        userName = input('Login: ')
        if self.existUser(userName):
            user = self.getUser(userName)
            rawI = input('Password: ')
            if rawI == user.pw:
                self.currentUser = user
            else:
                logging.info("Incorrect password!")
                self.login()
        else:
            logging.info("User does not exist.")
            self.login()

    def logout(self):
        """Log out user, without any kind of check."""
        if self.currentUser is not None:
            self.currentUser = None
            self.run() #For return to login user
        else: print("There is not a login user.")

    def whoAmI(self):
        """Returns what user is current using the shell."""
        print(self.currentUser.name)

    def setAdmin(self, userName, bool):
        """Only for logged in admin user.
		set as admin al already added user.
        """
        if self.existUser(userName):
            user = self.getUser(userName)
            user.setAdmin(bool)
            self.updateUser(userName, user)
        else:
            logging.info("Sorry, specified user does not exist.")

    def changeCurrentUserPW(self, oldPW, newPW):
        """For normal user.
		change its pw for a new one.
        """
        self.currentUser.pw = newPW
        self.updateUser(self.currentUser.name, self.currentUser)

    def changeCurrentUserPWShell(self):
        """Gives follow steps for client on the shell"""
        oldPW = input("Please enter current password: ")
        newPW = input("Please enter new password: ")
        if self.currentUser.pw == oldPW:
            self.changeCurrentUserPW(newPW)
        else:
            logging.info("Passwords don't match!")

    def changeUserPW(self, userName, newPW):
        """Only for logged in admin user.
		change an user's pw.
        """
        user = self.getUser(userName)
        user.pw = newPW
        self.updateUser(userName, user)

    def changeUserPWShell(self):
        """Gives follow steps for admin on the shell"""
        if self.currentUser.isAdmin:
            userName = input('Please enter target user: ')
            newPW = None
            if self.existUser(userName):
                newPW = input('Please enter target user new password: ')
                self.changeUserPW(userName, newPW)
            else:
                logging.info("Target user does not exist.")
        else:
            logging.info("Sorry, you are not an admin!")


    def existUser(self, userName):
        """Ask if a user is on users dictionary."""
        return userName in self.users.keys()

    def getUser(self, userName):
        """Get a user from users dictionary.
                preCond: -userName must be a string
                         -user must already exists.
        """
        return self.users.get(userName)

    def updateUser(self, userName, user):
        """Update a user's object at the users dictionary."""
        if self.existUser(userName):
            self.users.update({userName: user})
        else:
            logging.info("User does not exist")

    def run(self):
        """Run while loop for input commands."""
        self.runCommand('login')
        while(True):
            rawI = input('>')
            self.runCommand(rawI)

    def runCommand(self, command):
        """For prompt cut while
               capture commands
        """
        if command in self.validCommands.keys():
            r = self.validCommands.get(command)
            r()
        elif command in self.programs.keys():
            p = self.programs.get(command)
            self.loadProgram(p)
        elif command == '':
            return
        else: print(str(command) + " is not a valid command! Type 'help' for view valid commands.")

    def exit(self):
        """Same as logout"""
        self.logout()

    def help(self):
        """Shows on client screen the list of validCommands"""
        for command in self.validCommands.keys():
            print (str(command))

    def setKernel(self, kernel):
        self.kernel = kernel

    def addProgram(self, aProgram):
        self.programs.update({str(aProgram):aProgram})

    def loadProgram(self, aProgram):
        self.kernel.loadProgram(aProgram)

class User:
    def __init__(self, userName, userPW):
        """Only for creation.
		isAdmin variable must be used only by the shell.
        """
        self.name = userName
        self.pw = userPW
        self.admin = False

    def isAdmin(self):
        return self.admin

    def setAdmin(self, bool):
        self.admin = bool

