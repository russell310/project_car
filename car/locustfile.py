from locust import HttpUser, TaskSet, task, between


class CarSearchTasks(TaskSet):
    """
    Task set for simulating user interactions with the car search functionality.

    This class defines a set of tasks to be performed during load testing, simulating different user actions
    such as searching for cars, viewing the car list, and exporting car data to XML.
    """

    @task(1)
    def search_cars(self):
        self.client.get("/?color=Red&length=4.5&weight=1500&velocity=220")

    @task(2)
    def view_car_list(self):
        self.client.get("/")

    @task(1)
    def export_cars_to_xml(self):
        self.client.get("/?export=1")


class WebsiteUser(HttpUser):
    """
   User class for simulating website users during load testing.
   This class assigns the set of tasks to be performed and specifies the wait time between each task.
   """
    tasks = [CarSearchTasks]
    wait_time = between(1, 5)
