import unittest
import json
import requests


class TestApi(unittest.TestCase):

    def test_get_all(self):
        res = requests.get('http://localhost:5000/students')
        self.assertEqual(200, res.status_code)

    def test_add_student(self):
        data = {
            "name": "Test Name",
            "mark": 15,
        }
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

        res = requests.post('http://localhost:5000/students/add',json=data,headers=headers)
        self.assertEqual(200, res.status_code)

    def test_update_student(self):
        data = {
            "id":1,
            "name": "Tested Name",
            "mark": 12,
        }
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        res = requests.post('http://localhost:5000/students/update',json=data,headers=headers)
        self.assertEqual(200, res.status_code)


    def test_remove_student(self):
        data = {
            "id": 1
        }
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

        res = requests.post('http://localhost:5000/students/delete',json=data,headers=headers)
        self.assertEqual(200, res.status_code)


if __name__ == '__main__':
    unittest.main()
