import json
from api.client import Client


class Api(Client):
    USER = '/users'
    BASE_URL = 'https://reqres.in/api'
    REGISTER = '/register'

    def list_users(self):
        """
        :method:    get
        :rout:      /users?page=2
        :status:    200
        """
        url = self.BASE_URL + self.USER + '?page2'
        return self.get(url)

    def single_user_not_found(self):
        """
        :method:    get
        :rout:      /api/users/23
        :status:    404
        """
        url = self.BASE_URL + self.USER + '/23'
        return self.get(url)

    def single_user(self):
        """
        :method:    get
        :rout:      /users?page=2
        :status:    200
        """
        url = self.BASE_URL + self.USER + '/2'
        return self.get(url)

    def create(self, name: str, job: str):
        """
        :method:    post
        :rout:      /api/users
        :status:    201
        :body:     {
                        "name": "",
                        "job": ""
                    }
        """

        url = self.BASE_URL + self.USER
        payload = json.dumps({
            "name": f"{name}",
            "job": f"{job}"
        })
        headers = {
            'Content-Type': 'application/json'
        }
        return self.post(url, headers, payload)

    def delete_user(self, id: int):
        """
        :method:    delete
        :rout:      /api/users/id
        :status:    204
        """
        url = self.BASE_URL + self.USER + f"/{id}"
        return self.delete(url)

    def register_successful(self, password, email="eve.holt@reqres.in", ):
        """
        :method:    post
        :rout:      /api/register
        :status:    201
        :body:     {
                        "email": "eve.holt@reqres.in",
                        "password": ""
                    }
        """
        url = self.BASE_URL + self.REGISTER
        payload = json.dumps({
            "email": f"{email}",
            "password": f"{password}"
        })
        headers = {
            'Content-Type': 'application/json'
        }
        return self.post(url, headers, payload)


api = Api()
