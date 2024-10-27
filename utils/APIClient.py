import yaml
import requests

class APIClient:
    def __init__(self) -> None:
        with open("config/yaml", "r") as file:
            config = yaml.safe_load(file)
            self.base_url = config('base-url')
            self.headers = config('headers')
            self.endpoints = config('endpoints')

    def request(self, method, end_point_key, end_poind_path=' ', data=None, param=None):
        url = f'{self.base_url}{self.endpoints[end_point_key]}{end_poind_path}'
        
        if method == 'GET':
            response = requests.get(url, params=param, headers=self.headers)
        elif method == 'POST':
            response = requests.post(url, json=data, headers=self.headers)
        elif method == 'PUT':
            response = requests.put(url, json=data, headers=self.headers)
        else:
            raise Exception(f'Bad HTTP method "{method}" was received')
        
        # put logger code here
        return response