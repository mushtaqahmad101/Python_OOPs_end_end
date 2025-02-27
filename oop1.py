class employee:
    def __init__(self):
        self.id = 123
        self.salary = 50000
        self.designation = 'SDE'
        print('this is temporary')

    def travel(self, designation):
        print(f"employee is now travelling to {designation}")

    


sam = employee()