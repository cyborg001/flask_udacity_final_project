import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def load(self):
        self.client.get('/')
    # @task
    # def hello_world(self):
    #     self.client.get("/hello")
    #     self.client.get("/world")

    # @task(3)
    # def view_items(self):
    #     for item_id in range(10):
    #         self.client.get(f"/item?id={item_id}", name="/item")
    #         time.sleep(1)

    def on_start(self):
        self.client.post("/login", json={"username":"foo", "password":"bar"})
    
    def predecir(self):
        data = '{ "CHAS":{"0":0 }, "RM":{"0":6.575},"TAX":{"0":296.0}, \
        "PTRATIO":{"0":15.3},"B":{"0":396.9},"LSTAT":{"0":4.98} }'
        self.client.post('/predict',json=data)