'''
실습일: 2024.10.22
이름: 201910852 심기윤
실습명: 직원 클래스를 만들고 직원 클래스를 상속받는 정규직, 비정규직 클래스 구현
'''

class Employee:
    total_salary = 0
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


class FullTimeEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def get_salary(self):
        return self.salary

    def set_salary(self, salary):
        self.salary = salary

    def calculate_salary(self):
        print(f'{self.name}: 정규직, 연봉 {self.salary}')


class PartTimeEmployee(Employee):
    sum = 0
    def __init__(self, name, salary, time, over):
        super().__init__(name)
        self.salary = salary
        self.time = time
        self.over = over

    def get_salary(self):
        return self.salary

    def set_salary(self, salary):
        self.salary = salary

    def get_time(self):
        return self.time

    def set_time(self, time):
        self.time = time

    def get_over(self):
        return self.over

    def set_over(self, over):
        self.over = over

    def calculate_salary(self):
        if self.over == 0:
            self.sum += self.salary * self.time
            print(f'{self.name}: 비정규직, 시급 {self.salary}, 일한 시간 {self.time}, 초과 근무 {self.over}시간, 총 연봉 {int(self.sum)}')
        else:
            self.sum += (self.salary * self.time) + ((self.salary * 1.5) * self.over)
            print(f'{self.name}: 비정규직, 시급 {self.salary}, 일한 시간 {self.time}, 초과 근무 {self.over}시간, 총 연봉 {int(self.sum)}')


employee1 = FullTimeEmployee("직원1", 5000000)
employee2 = PartTimeEmployee("직원2", 20000, 160, 10)
employee3 = FullTimeEmployee("직원3", 4500000)

employee1.calculate_salary()
employee2.calculate_salary()
employee3.calculate_salary()

print(f'총 급여 비용: {employee1.get_salary() + employee3.get_salary() + int(employee2.sum)}')