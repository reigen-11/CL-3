import random

class LoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.index = 0

    def round_robin(self):
        server = self.servers[self.index]
        self.index = (self.index + 1) % len(self.servers)
        return server

    def random_selection(self):
        return random.choice(self.servers)

servers = ['S1', 'S2', 'S3']
lb = LoadBalancer(servers)
n = 15

print("Round Robin Algorithm")
for i in range(n):
    print(f"Request {i+1} -> {lb.round_robin()}")

print("Random Selection Algorithm")
for i in range(n):
    print(f"Request {i+1} -> {lb.random_selection()}")