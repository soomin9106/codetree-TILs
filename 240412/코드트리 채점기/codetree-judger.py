from sortedcontainers import SortedSet, SortedDict
import heapq
import sys

class PriorityQueue:
    def __init__(self):
        self.items = []

    def push(self, item):
        heapq.heappush(self.items, item)

    def empty(self): # 비어있으면 True 를 반환
        return not self.items

    def size(self):
        return len(self.items)

    def pop(self):
        if self.empty():
            raise Exception("empty queue")
        
        return heapq.heappop(self.items)

    def top(self):
        if self.empty():
            raise Exception("empty queue")
        
        return self.items[0]

# 도메인 개수 최대값, 채점기 개수 최대값
MAX_D = 300 
MAX_N = 500
INF = int(1e9)

# 해당 도메인에서 해당 문제ID가 레디큐에 있는지 관리해줍니다.
is_in_readyq = [SortedSet() for _ in range(MAX_D + 1)]

# 현재 쉬고 있는 채점기
rest_judger = PriorityQueue()

# 각 채점기들이 채점할 때, 도메인의 인덱스 저장
judging_domain = [0] * (MAX_N + 1) 

# 각 도메인별로 시간 관리
s = [0 for _ in range(MAX_D + 1)]
g = [0 for _ in range(MAX_D + 1)]
e = [0 for _ in range(MAX_D + 1)]   

# 도메인을 관리하기 위해 cnt를 이용합니다.
# 도메인 문자열을 int로 변환해주는 map을 관리합니다.
domainToIdx = SortedDict()
global cnt
cnt = 0

# 현재 채점 대기 큐에 있는 task의 개수를 관리합니다.
global ans
ans = 0

# 각 도메인별로 priority queue를 만들어
# 우선순위가 가장 높은 url을 뽑아줍니다.
url_pq = [PriorityQueue() for _ in range(MAX_D + 1)]

# 채점기를 준비합니다.
def Init(query):
    global n
    (empty, n, url) = query
    n = int(n)

    global cnt

    for i in range(1, n + 1):
        rest_judger.push(i)
    
    # Url 에서 도메인 부분과 숫자 부분을 나누어줌
    domain, num = url.split('/')
    num = int(num)

    # 만약 도메인이 처음 나온 도메인이라면 domainToIdx 에 갱신
    if not domain in domainToIdx:
        cnt += 1
        domainToIdx[domain] = cnt
    domain_idx = domainToIdx[domain]

    # 도메인 번호에 맞는 레디큐에 숫자를 넣어줌
    is_in_readyq[domain_idx].add(num)

    newUrl = (1, 0, num)
    url_pq[domain_idx].push(newUrl)

    # 대기 큐 개수 추가
    global ans
    ans += 1

# 새로운 url 을 입력 받아 레디큐에 추가
def NewUrl(query):
    (empth, tme, id, url) = query
    tme= int(tme)
    id = int(id)

    global cnt

    # Url 에서 도메인 부분과 숫자 부분을 나누어줌
    domain, num = url.split('/')
    num = int(num)

    # 만약 도메인이 처음 나온 도메인이라면 domainToIdx 에 갱신
    if not domain in domainToIdx:
        cnt += 1
        domainToIdx[domain] = cnt

    domain_idx = domainToIdx[domain]

    if num in is_in_readyq[domain_idx]:
        return 
    is_in_readyq[domain_idx].add(num)

    newUrl = (id, tme, num)
    url_pq[domain_idx].push(newUrl)

    global ans 
    ans += 1

# 도메인 - 채점기 assign
def Assign(query):
    (empty, tme) = query
    tme = int(tme)

    if rest_judger.empty():
        return

    min_domain = 0
    minUrl = (INF, 0, 0)

    global cnt

    for i in range(1, cnt + 1):
        if e[i] > tme:
            continue

        if not url_pq[i].empty():
            curUrl = url_pq[i].top()

            if minUrl > curUrl:
                minUrl = curUrl
                min_domain = i

    if min_domain:
        judger_idx = rest_judger.top()
        rest_judger.pop()

        url_pq[min_domain].pop()

        s[min_domain] = tme
        e[min_domain] = INF

        judging_domain[judger_idx] = min_domain

        is_in_readyq[min_domain].remove(minUrl[2])

        global ans 
        ans -= 1

def Finish(query):
    (empty, tme, id) = query

    tme = int(tme)
    id = int(id)

    if judging_domain[id] == 0:
        return 

    rest_judger.push(id)
    domain_idx = judging_domain[id]
    judging_domain[id] = 0

    g[domain_idx] = tme - s[domain_idx]
    e[domain_idx] = s[domain_idx] + 3 * g[domain_idx]

def Check(qurey):
    (empty, tme) = query

    global ans
    print(ans)

q = int(input())

for _ in range(q):
    query = input().split()

    if int(query[0]) == 100:
        # 채점기를 준비합니다.
        Init(query)
    if int(query[0]) == 200:
        # 새로운 url을 입력받아 레디큐에 추가해줍니다.
        NewUrl(query)
    if int(query[0]) == 300:
        # 다음 도메인을 찾아 assign합니다.
        Assign(query)
    if int(query[0]) == 400:
        # 채점 하나를 마무리합니다.
        Finish(query)
    if int(query[0]) == 500:
        # 현재 채점 대기 큐에 있는 url의 개수를 출력해줍니다.
        Check(query)