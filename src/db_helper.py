from mysql import connector


class DbHelper:

    def __init__(self):
        self.database = connector.connect(
            host="localhost",
            user="root",
            password="sazclone@123"
        )

    def __set_cursor(self):
        self.cursor = self.database.cursor()

    def get_maximum_salary(self):
        '''
        Implement the logic to find and return maximum salary from employee table
        '''
        self.__set_cursor()
        self.cursor.execute("SELECT Name, max(salary) FROM grokr.employee")
        output = self.cursor.fetchone()
        return output[1]

    def get_minimum_salary(self):
        '''
        Implement the logic to find and return minimum salary from employee table
        '''
        self.__set_cursor()
        self.cursor.execute("SELECT Name, min(salary) FROM grokr.employee")
        output = self.cursor.fetchone()
        return output[1]


if __name__ == "__main__":
    db_helper = DbHelper()
    min_salary = db_helper.get_minimum_salary()
    max_salary = db_helper.get_maximum_salary()
    print(max_salary)
    print(min_salary)
