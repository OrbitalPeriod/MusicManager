import sys

class argumentHandler():
    #template = {function : {"-l" : [isRequired, dataType]}}

    def __init__(self, sysarguments, config, linkdict):
        self.config = config

        self.linkdict = linkdict
        self.sysarguments = sysarguments
    
    def startFunction(self):
        try:
            func = self.linkdict[self.sysarguments[1]]
        except:
            print("first argument not found")
            exit()
            
        args = self.getArguments(func, self.sysarguments)
        func(args)
        
            
    
    def getArguments(self, function, sysarguments):
        args = self.config[function] #{"-l" : [isRequired, dataType]}
        argcalls = args.keys()
        
        
        returnDict = {}
        for key in args.keys():
            curritem = args[key] #  [isRequired, dataType]
            if key not in sysarguments:
                if curritem[0]:
                    print("Argument: " + key + " not given yet required")
                    exit()
                else:
                    continue
            else:
                index = sysarguments.index(key)
                try:
                    arg = curritem[1](sysarguments[index+ 1])
                except IndexError:
                    print("Argument for: " + key + " not given")
                    exit()
                except ValueError:
                    print("Invalid argument for: " + key)
                    exit()
                if arg in argcalls:
                    print("Argument for: " + key + " not given")
                    exit()
                
                returnDict[key] = arg
        return returnDict
                    
                    
                    
                    
        
