from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(5, 10)

    @task
    def my_task(self):
        self.client.get("/")

#test commadn : locust -f p_test.py --host=http://localhost:8089