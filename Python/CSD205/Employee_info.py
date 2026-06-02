#CSD 205 Assignment 10.2
# Author: Timothy Martin
# Date: 05/13/26


# Employee class
class Employee:

    # Constructor
    def __init__(self, name, gender, pay_rate, number):
        self.__employee_name = name
        self.__employee_gender = gender
        self.__hourly_pay_rate = pay_rate
        self.__employee_number = number

    # Setters
    def set_employee_name(self, name):
        self.__employee_name = name

    def set_employee_gender(self, gender):
        self.__employee_gender = gender

    def set_hourly_pay_rate(self, pay_rate):
        self.__hourly_pay_rate = pay_rate

    def set_employee_number(self, number):
        self.__employee_number = number

    # Getters
    def get_employee_name(self):
        return self.__employee_name

    def get_employee_gender(self):
        return self.__employee_gender

    def get_hourly_pay_rate(self):
        return self.__hourly_pay_rate

    def get_employee_number(self):
        return self.__employee_number


# ProductionWorker class inheriting from Employee
class ProductionWorker(Employee):

    # Constructor
    def __init__(self, name, gender, pay_rate, number, shift):
        super().__init__(name, gender, pay_rate, number)
        self.__shift_number = shift

    # Setter
    def set_shift_number(self, shift):
        self.__shift_number = shift

    # Getter
    def get_shift_number(self):
        return self.__shift_number


# Main function
def main():

    # Create two Employee objects
    employee1 = Employee("John Smith", "Male", 22.50, "E101")
    employee2 = Employee("Sarah Johnson", "Female", 25.75, "E102")

    # Create two ProductionWorker objects
    worker1 = ProductionWorker("Mike Davis", "Male", 28.00, "PW201", 1)
    worker2 = ProductionWorker("Emily Brown", "Female", 30.25, "PW202", 3)

    # Display Employee information
    print("========== EMPLOYEE INFORMATION ==========\n")

    print(f"""
Employee 1
Name: {employee1.get_employee_name()}
Gender: {employee1.get_employee_gender()}
Hourly Pay Rate: ${employee1.get_hourly_pay_rate():.2f}
Employee Number: {employee1.get_employee_number()}
""")

    print(f"""
Employee 2
Name: {employee2.get_employee_name()}
Gender: {employee2.get_employee_gender()}
Hourly Pay Rate: ${employee2.get_hourly_pay_rate():.2f}
Employee Number: {employee2.get_employee_number()}
""")

    # Display Production Worker information
    print("======= PRODUCTION WORKER INFORMATION =======")

    print(f"""
Production Worker 1
Name: {worker1.get_employee_name()}
Gender: {worker1.get_employee_gender()}
Hourly Pay Rate: ${worker1.get_hourly_pay_rate():.2f}
Employee Number: {worker1.get_employee_number()}
Shift Number: {worker1.get_shift_number()}
""")

    print(f"""
Production Worker 2
Name: {worker2.get_employee_name()}
Gender: {worker2.get_employee_gender()}
Hourly Pay Rate: ${worker2.get_hourly_pay_rate():.2f}
Employee Number: {worker2.get_employee_number()}
Shift Number: {worker2.get_shift_number()}
""")


# Run the program
main()