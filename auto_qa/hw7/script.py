import requests


class EmployeeApi:
    __api_url = 'http://5.101.50.27:8000/employee'
    def create_employee(self, employee_info: dict):
        return requests.post(f'{self.__api_url}/create', employee_info)

    def create_employee_info(self):
        return requests.get(f'{self.__api_url}/info')

    def change_employee_info(self, employee_info: dict):
        return requests.patch(f'{self.__api_url}/change', employee_info)

