'''
시작 시각 :16시
종료 시각 :16시 40분

참고 링크:https://coding-groot.tistory.com/103
다음 코드에서, 출력되는 결과값이 왜 실제 출력되어야 하는 결과값보다 작은지 설명하시오.
-> 아래 코드에서 같은 변수를 동시에 접근했기 때문이다. 여러개의 thread가 동시다발적으로 worker 객체에 접근하면
    마찬가지로 count함수에 동시에 여러 thread들이 작업을 진행할 것이므로, count가 순차적으로 값이 갱신되야 하는데
    오류가 생길 것이다.

해당 문제점을 해결하기 위해 사용해야 하는 해결책을 서술하고,
-> Lock을 걸어서 만약 하나의 thread가 변수를 사용하고 있으면 다른 쪽은 사용 못하도록 해야한다.
   Lock.acquire(): 다른 thread가 접근 못하도록 잠금
   Lock.release(): 잠금해제
해당 개념을 자율차 코드에 적용하였을 때
1) 어느 부분에 적용할 수 있을지,
-> 자율차에는 cam 4개 및 각종 센서들 (lidar, imu, gps 등등),platform 이 동시에 작업을 해야 하므로 thread를 이용하고있다.
   따라서 만약 이러한 센서값들에서 얻은 data를 통해 Database class나 controldata.py에 있는 data들을 얻는 과정에서
   다음과같은 multithreading으로 인한 오류가 발생하면 그러한 부분에서 적용할 수 있을 것 같다.
2) 이를 통해 어떤 이점을 얻을 수 있는지
서술하시오.
-> 더 정확한 값을 얻을수 있을 것이다. (하지만, 오버헤드가 생기는 단점이 있있.)
(Optional) 아래 코드의 실행 결과값이 실제 출력되어야 하는 결과값과 동일하게 출력되도록 변경하시오.
-> 맞게 한거 같은데 왜 안될까? ㅠㅠ
*** Write Your Answer Below ***
위에다가 각각 적었습니다.

*** Your Answer Ends Here ***
'''

from threading import Lock
from threading import Thread

lock=Lock()
class Count:
    def __init__(self):
        self.count = 0

    def add_offset(self, offset):
        lock.acquire()
        self.count += offset
        print("count")
        lock.release()


def worker(idx, limit, count_obj): ## idx limit=1000000 ,count_obj
    print(idx)
    for _ in range(limit):
        count_obj.add_offset(1)


def run_threads(func, thread_num, limit, count_obj):
    threads = []
    for i in range(thread_num):
        args = (i, limit, count_obj)
        thread = Thread(target=func, args=args)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


limit = 10 ** 6
thread_num = 7
count = Count()
run_threads(worker, thread_num, limit, count)
print(f"Result should be {thread_num * limit}, but the total count is {count.count}")
