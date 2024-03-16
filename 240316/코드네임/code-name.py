class Agent:
    def __init__(self, codename = "", score = 0):
        self.codename = codename
        self.score = score

agents = []
for _ in range(5):
    codename, score = map(str, input().split())
    agents.append(Agent(codename, int(score)))

agents = sorted(agents, key = lambda x: x.score)

print(agents[0].codename, agents[0].score)