# locustfile.py
from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):

    @task
    def get_homepage(self):
        self.client.get("/")

    @task
    def get_konsumen_produc(self):
        self.client.get("/Konsumen/Produk")

    @task
    def get_konsumen_cara_pembayaran(self):
        self.client.get("/Konsumen/Cara-Pembayaran")

    @task
    def get_bermitra_dengan_kami(self):
        self.client.get("/Mitra/Bermitra-dengan-Kami")

    @task
    def get_jadi_mitra_kami(self):
        self.client.get("/Mitra/Menjadi-Mitra-Kami")

    @task
    def get_tentang_kami(self):
        self.client.get("/Tentang-Perusahaan/Tentang-Kami")

    @task
    def get_penghargaan_kami(self):
        self.client.get("/Corporate/Penghargaan-Kami")

    @task
    def get_Karir_peluang(self):
        self.client.get("/Tentang-Perusahaan/Tentang-Kami")

    @task
    def get_tentang_kami(self):
        self.client.get("/Karirs/Peluang-karir")

    @task
    def get_Nilai_Perusahaan(self):
        self.client.get("/Karir/Nilai-nilai-Perusahaan")

    @task
    def get_blog(self):
        self.client.get("/Blog")

    @task
    def get_hubungi_kami(self):
        self.client.get("/Hubungi-Kami")


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
