# Goal is to have the singleton class and the variables within it created once
# So we use __new__ instead of __init__

class MyGlobals(object):
    _instance = None

    def __new__(self):
        if not self._instance:  # Constructor does a check on whether instance is set
            # If instance is not set create an instance
            self._instance = super().__new__(self)

            # Variables
            self.check = True  # check whether an iteration is complete
            self.iteration = 0  # start with initial iteration value
            self.total_iterations = 3  # should be replaced by the length of the auto-array
            self.final_array = []  # array for each final resistance graph
            self.final_array_thickness = []  # array for each final thickness graph
            self.final_array_load = []  # array for each final load graph
            self.dwell_time = 10  # array for dwell time -> Replace with dwell time of loaded profile
            self.row = 4  # Row after preamble for Excel workbook
            self.column = 0  # Column initialisation for Excel workbook
            self.repeat = 4  # number of times measurement will be repeated
            self.repeat_original = 4  # store the original number of repeats
            self.repeat_change = False  # condition variable to see whether measurement has changed repeat cycle
            self.i = 0  # Variable for temp load thickness graph
            self.first_iteration = True  # First iteration check condition
            self.first_repeat = True  # First repeat check condition
            self.final_value = 0.1  # Pseudo value for calculation -> Changed during implementation

            # For Run State Check
            self.run = False

        return self._instance  # return the instance
