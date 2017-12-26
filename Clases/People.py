class People:
    def __init__(self,name,job):
        self.name = name
        self.job = job

    def info(self):
        print("Name: {} , Job: {}".format(self.name,self.job))


And = People("andrey",'manager')
print(And.job)
And.info()