{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"authorship_tag":"ABX9TyOhW8GHuMyDBtSNjB4ku+8x"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"markdown","source":["두 번째 알고리즘 기초 실습 문제\n","- 팩토리얼 구하기\n","- 최대공약수 구하기\n","- 하노이의 탑 옮기기"],"metadata":{"id":"6VYEKVuDMRxQ"}},{"cell_type":"markdown","source":["최대공약수 구하기"],"metadata":{"id":"h-_mwlmFMUVn"}},{"cell_type":"code","execution_count":null,"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"kg5Yp4WlMOIh","executionInfo":{"status":"ok","timestamp":1712974448421,"user_tz":-540,"elapsed":321,"user":{"displayName":"김성원","userId":"15056001630390828466"}},"outputId":"fd6aac3f-7c65-4d33-9035-dc0df276bf29"},"outputs":[{"output_type":"stream","name":"stdout","text":["3\n","12\n","27\n"]}],"source":["# 최대공약수 구하기\n","# 두 자연수 a와 b의 최대공약수를구하는 알고리즘을 만들어 보세요\n","\n","# 입력값 : a, b\n","# 출력값 : a와 b의 최대 공약수\n","\n","def gcd(a,b):\n","    i = min(a, b) # a와 b중 작은 수를 i에 저장\n","    while True:\n","        if (a % i == 0) and (b % i == 0): # i가 1이 되면 조건은 무조건 만족하게 되므로 종료조건\n","            return i\n","        i -= 1 # i를 1씩 감소시켜서 종료조건에 도달하게 하기\n","\n","print(gcd(3, 6))\n","print(gcd(60, 24))\n","print(gcd(81, 27))"]},{"cell_type":"code","source":["# 최대공약수 구하기\n","# 유클리그 알고리즘\n","# a, b의 최대 공약수는 b와 a를 b로 나눈 나머지의 최대공약수와 같음\n","# 즉 gcd(a, b) = gcd(b, a % b)\n","# 어떤 수와 0의 최대 공약수는 자기 자신\n","# gcd(n, 0) = n\n","\n","# 따라서 gcd(60,24) = gcd(24, 60 % 24) = gcd(24, 12) = gcd(12, 24 % 12) = gcd(12, 0) = 12 >> 즉, 60과 24의 최대공약수는 12 라는 것을 알 수 있다.\n","# >> 재귀 호출로 최대 공약수를 구할 수 있다는 증거\n","\n","def gcd2(a,b):\n","    if b == 0: # b가 영이되면 gcd(a,0) = a 이므로 a를 반환해준다 >> 종료 조건\n","        return a\n","    return gcd(b, a%b) # a%b로 값을 계속 감소시켜서 종료 조건이 되도록 해준다.\n","\n","print(gcd(3, 6))\n","print(gcd(60, 24))\n","print(gcd(81, 27))"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"j2WwcAt6OJFb","executionInfo":{"status":"ok","timestamp":1712974705590,"user_tz":-540,"elapsed":9,"user":{"displayName":"김성원","userId":"15056001630390828466"}},"outputId":"c1a6245b-83a2-49ec-aac9-148b9f026bfd"},"execution_count":null,"outputs":[{"output_type":"stream","name":"stdout","text":["3\n","12\n","27\n"]}]},{"cell_type":"code","source":["# 연습 문제\n","# 피보나치 수열이 0번부터 시작한다고 가정할 때 n번째 피보나치 수를 구하는 알고리즘을 재귀호출을 활용하여 만들기\n","# 피보나치 수열 : n번째 값이 n-2번째 값과 n-1번째 값의 합이 되는  수열\n","\n","def fibo(n):\n","    if n <= 1:\n","        return n # n = 0 >> 0 / n = 1 >> 1\n","    return fibo(n-2) + fibo(n-1) # n이 감소되면서 결국 0 또는 1에 도달하여 종료조건을 만족 시키게 됨\n","\n","print(fibo(5))"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"nNOTyBiyP6-5","executionInfo":{"status":"ok","timestamp":1712975623260,"user_tz":-540,"elapsed":293,"user":{"displayName":"김성원","userId":"15056001630390828466"}},"outputId":"8ac5402a-cd0d-40bb-fcf7-0e27bcbb990b"},"execution_count":null,"outputs":[{"output_type":"stream","name":"stdout","text":["5\n"]}]},{"cell_type":"markdown","source":["하노이의 탑 옮기기"],"metadata":{"id":"EvSFKllzT3SJ"}},{"cell_type":"code","source":["# 하노이의 탑 옮기기\n","# 크기가 다른 원반 n개를 출발점 기둥에서 도착점 기둥으로 전부 옮겨야 함\n","# 원반은 한 번에 한 개씩만 옮길 수 있음\n","# 원반을 옮길 때는 한 기둥의 맨 위 원반을 뽑아, 다른 기둥의 맨 위로만 옮길 수 있음(기둥의 중간에서 원반을 빼내거나 빼낸 원반을 다른 기둥의 중간으로 끼워 넣을 수 없음).\n","# 원반을 옮기는 과정에서 큰 원반을 작은 원반 위로 올릴 수 없음\n","\n","# 입력값 : 원반 개수 n, 옮길 원반이 현재 있는 출발점 기둥 from_pos, 원반을 옮길 도착점 기둥 to_pos, 옮기는 과정에서 사용할 보조 기둥 aux_pos\n","# 출력값 : 원반을 옮기는 순서\n","\n","# 알고리즘 단순화\n","# n개의 원판이 있는 경우\n","# 1. 가장 큰 원판을 제외한 모든 원판이 ap에 있도록한다.\n","# 2. 가장 큰 원판을 tp로 옮긴다.\n","# 3. ap에 있는 원판을 전부 tp로 옮긴다.\n","\n","# 여기서 1과 3의 과정은 n-1개의 원판이 있는 경우의 1,2,3을 반복하면 된다.\n","# 즉 'n개의 원판을 옮기는 횟수'는 'n-1개 원판을 옮기는 횟수' + 1 + 'n-1개 원판을 옮기는 횟수' 이다.\n","\n","def hanoi(n, fp, tp, ap):\n","    if n == 1: # n 이 줄어들어 1이되면 종료하게 되는 종료 조건\n","        print(fp, \"->\", tp)\n","        return\n","    hanoi(n-1, fp, ap, tp) # 1. 가장 큰 원판을 제외한 모든 원판이 ap에 있도록한다.\n","    print(fp, \"->\", tp) # 2. 가장 큰 원판을 tp로 옮긴다.\n","    hanoi(n-1, ap, tp, fp) # 3. ap에 있는 원판을 전부 tp로 옮긴다.\n","\n","print('n=1')\n","print(hanoi(1,'fp', 'tp', 'ap'))\n","print()\n","print('n=2')\n","print(hanoi(2,'fp', 'tp', 'ap'))\n","print()\n","print('n=3')\n","print(hanoi(3,'fp', 'tp', 'ap'))"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"AhKiOAKDTHCa","executionInfo":{"status":"ok","timestamp":1712976125748,"user_tz":-540,"elapsed":289,"user":{"displayName":"김성원","userId":"15056001630390828466"}},"outputId":"4c2021e6-c65a-462d-a5b4-ca62719105e0"},"execution_count":null,"outputs":[{"output_type":"stream","name":"stdout","text":["n=1\n","fp -> tp\n","None\n","\n","n=2\n","fp -> ap\n","fp -> tp\n","ap -> tp\n","None\n","\n","n=3\n","fp -> tp\n","fp -> ap\n","tp -> ap\n","fp -> tp\n","ap -> fp\n","ap -> tp\n","fp -> tp\n","None\n"]}]},{"cell_type":"markdown","source":["### 세 번째 알고리즘 기초 실습 문제 ###\n","- 순차 탐색\n","- 선택 정렬\n","- 삽입 정렬\n","- 병합 정렬\n","- 퀵 정렬\n","- 이분 탐색"],"metadata":{"id":"FRrtjl17WmXj"}},{"cell_type":"markdown","source":["순차 탐색"],"metadata":{"id":"GDvQ3Wy2XGqC"}},{"cell_type":"code","source":["# 순차 탐색\n","# 주어진 리스트에 특정한 값이 있는지 찾아 그 위치를 돌려주는 알고리즘\n","# 리스트에 찾는 값이 없다면 -1을 반환\n","\n","# 입력값 : 리스트 x와 찾는 값 n\n","# 출력값 : 찾는 값의 위치 인덱스 또는 -1\n","\n","def loca(x, n):\n","    for i in range(len(x)):\n","        if x[i] == n:\n","            return i\n","    return -1\n","\n","l = [15, 80, 34, 564, 30, 43, 56, 8]\n","\n","print(loca(l,30))\n","print(loca(l,100))\n","\n","# 순차 탐색의 경우 찾는 값이 리스트 처음부분에 있으면 쉽게 찾아지지만 최악의 경우 마지막에 있으면 처음부터 마지막까지 하나씩 다 비교해야함\n","# 따라서 최악의 경우를 비교했을때 리스트의 길이가 길어지면 계산 횟수가 늘어나므로 O(n)으로 표기 가능"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"hPyg7IiKVHvi","executionInfo":{"status":"ok","timestamp":1712977441941,"user_tz":-540,"elapsed":328,"user":{"displayName":"김성원","userId":"15056001630390828466"}},"outputId":"756f2ee7-b0b9-421d-a564-d32ba4d83cbd"},"execution_count":null,"outputs":[{"output_type":"stream","name":"stdout","text":["4\n","-1\n"]}]},{"cell_type":"code","source":["# 연습문제\n","# 리스트에서 찾는 값이 여러개 있더라도 첫 번째 위치만 돌려주는 알고리즘을 변형시켜 찾는 값이 여러개 있을때 찾는 값의 모든 위치를 리스트로 돌려주는 알고리즘을 만들기\n","# 찾는 값이 없다면 빈 리스트를 반환\n","\n","def loca2(x, n):\n","    res = [] # 결과값을 담아서 출력할 빈 리스트 생성\n","    for i in range(len(x)):\n","        if x[i] == n: # 찾는 값이 리스트안 요소와 같으면 해당 요소의 인덱스를 res 리스트에 추가\n","            res.append(i)\n","    return res\n","\n","l = [15, 80, 30, 564, 30, 43, 56, 8]\n","\n","print(loca2(l,30))\n","print(loca2(l,100))"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"bkw-4EZdZeiU","executionInfo":{"status":"ok","timestamp":1712977692797,"user_tz":-540,"elapsed":323,"user":{"displayName":"김성원","userId":"15056001630390828466"}},"outputId":"28e84c76-e79a-433e-cd2d-485af8558b22"},"execution_count":null,"outputs":[{"output_type":"stream","name":"stdout","text":["[2, 4]\n","[]\n"]}]},{"cell_type":"code","source":["# 학생 번호에 해당하는 학생 이름 찾기\n","# 입력값 : 학생 번호 리스트, 학생 이름 리스트, 찾는 학생 번호\n","# 출력값 : 해당하는 학생 이름, 학생 이름이 없으면 물음표'?' 출력\n","\n","def search_name(num, name, n):\n","    for i in range(len(num)):\n","        if num[i] == n:\n","            return name[i]\n","    return '?'\n","\n","num = [1,2,3,4,5]\n","name = ['길동', '길수', '민지', '민수', '예은']\n","\n","print(search_name(num, name, 4))"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"CwKxjrtra8tE","executionInfo":{"status":"ok","timestamp":1712977943303,"user_tz":-540,"elapsed":286,"user":{"displayName":"김성원","userId":"15056001630390828466"}},"outputId":"cf342971-afc3-43d8-acf5-d436602784bc"},"execution_count":null,"outputs":[{"output_type":"stream","name":"stdout","text":["민수\n"]}]},{"cell_type":"markdown","source":["선택 정렬"],"metadata":{"id":"P8N765i1cewU"}},{"cell_type":"code","source":["# 선택 정렬\n","# 주어진 리스트 안의 자료를 작은 수부터 큰 수 순서로 배열하는 정렬 알고리즘\n","# 정렬(sort): 자료를 크기 순서대로 정렬\n","\n","# 입력값 : 정렬할 리스트\n","# 출력값 : 정렬된 리스트\n","\n","# 1. 새로운 리스트에 최소값을 차례대로 넣어주는 알고리즘\n","def min_i(x):\n","    min_idx = 0 # 최소값 인덱스 초기화\n","\n","    for i in range(1, len(x)):\n","        if x[i] < x[min_idx]: # 만약 i를 인덱스로 가지는 값이 최소값보다 작다면 최소값의 인덱스를 해당 값의 인덱스로 변경\n","            min_idx = i\n","\n","    return min_idx\n","\n","def sort_list(a):\n","    res = []\n","    while a: # 리스트 a의 범위안에서 동작\n","        min_idx = min_i(a)\n","        value = a.pop(min_idx) # value는 리스트 a에서 최소값이 떨어져 나와서 들어감\n","        res.append(value) # 리스트 res에 떨어져 나온 value 값이 하나씩 들어간다. >> 즉, 최소값부터 차례대로 누적되어 들어가게 된다.\n","    return res\n","\n","\n","l = [5,3,4,2,1,6]\n","print(min_i(l)) # 최소값의 인덱스가 출력된다.\n","print()\n","print(sort_list(l))"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"QXu6iCd3cPj9","executionInfo":{"status":"ok","timestamp":1712981016687,"user_tz":-540,"elapsed":3,"user":{"displayName":"김성원","userId":"15056001630390828466"}},"outputId":"a7893c7a-1385-49be-a59a-15525d0fb3f4"},"execution_count":null,"outputs":[{"output_type":"stream","name":"stdout","text":["4\n","\n","[1, 2, 3, 4, 5, 6]\n"]}]},{"cell_type":"code","source":["# 2. 주어진 리스트 안에서 재배치 하는 알고리즘\n","\n","def sort_list2(a):\n","    n = len(a)\n","    for i in range(n-1): # 0부터 n-2까지 반복 >> 0~(n-2)까지가 n-1개 / 마지막 n번째꺼는 비교할 필요 없음(앞에서 이미 다 비교되기 때문)\n","        min_idx = i\n","        for j in range(i+1, n): # (i+1) ~ n >> i 다음꺼부터 비교해서 n번째 마지막 요소까지 비교\n","            if a[j] < a[min_idx]: # a[i]보다 a[j]가 작으면 min_idx를 j로 바꿔준다.\n","                                    # 1단계 : a[i]와 a[i+1]을 비교한 뒤 작은 값을 min_idx에 넣는다\n","                                    # 2단계 : 1단계에서 정해진 작은 값과 a[i+2]를 비교하여 작은 값을 min_idx에 넣는다\n","                                    # 3단계 : 2단계를 n까지 계속 반복하여 최종적으로 가장 작은 값의 인덱스가 min_idx에 담기게 된다.\n","                min_idx =j\n","\n","        a[i], a[min_idx] = a[min_idx], a[i] # 앞서 구한 가장 작은 값의 인덱스 min_idx를 이용하여 위치를 바꿔준다.\n","        # 위치를 바꿔주는 코드\n","        # a[i], a[min_idx]의 순서를 = a[min_idx], a[i] 이렇게 바꿔주겠다.\n","\n","l = [5,3,4,2,1,6]\n","sort_list2(l)\n","print(l)"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"aVkc9NO3d1Hd","executionInfo":{"status":"ok","timestamp":1713135421094,"user_tz":-540,"elapsed":9,"user":{"displayName":"김성원","userId":"15056001630390828466"}},"outputId":"314c91ea-5fd0-4941-cc20-b1c73dd9f352"},"execution_count":null,"outputs":[{"output_type":"stream","name":"stdout","text":["[1, 2, 3, 4, 5, 6]\n"]}]},{"cell_type":"code","source":["# 연습 문제\n","# 내림차순으로 정렬하도록 알고리즘 바꾸기\n","\n","def sort_desc(a):\n","    n = len(a)\n","    for i in range(n-1):\n","        min_idx = i\n","        for j in range(i+1, n):\n","            if a[j] > a[min_idx]: # '<'를 '>'로 바꿔주기만 하면 된다\n","\n","                min_idx =j\n","\n","        a[i], a[min_idx] = a[min_idx], a[i]\n","\n","l = [5,3,4,2,1,6]\n","sort_desc(l)\n","print(l)"],"metadata":{"id":"HUXFn0ADpf_6","colab":{"base_uri":"https://localhost:8080/"},"executionInfo":{"status":"ok","timestamp":1713135531817,"user_tz":-540,"elapsed":322,"user":{"displayName":"김성원","userId":"15056001630390828466"}},"outputId":"63957e95-41fb-4e5a-e853-285387efa75c"},"execution_count":null,"outputs":[{"output_type":"stream","name":"stdout","text":["[6, 5, 4, 3, 2, 1]\n"]}]},{"cell_type":"markdown","source":["삽입 정렬"],"metadata":{"id":"t1X-Vyhm3EIm"}},{"cell_type":"code","source":["# 삽입 정렬\n","\n","# 1. 새로운 리스트에 값을 정렬하는 알고리즘\n","\n","# 리스트 r에서 v가 들어가야할 idx를 돌려주는 함수\n","def find_ins_idx(r, v):\n","    for i in range(len(r)): # 0 ~ 리스트r의 크기\n","        if v < r[i]: # 만약 v의 값이 i번째 값보다 작으면\n","            return i # v가 들어갈 idx는 i\n","    return len(r) # 그게 아니라면 v를 가장 마지막에 넣기 위해 len(r)을 idx 값으로 반환\n","\n","def ins_sort(a):\n","    res = [] # 결과값이 새롭게 정렬될 빈 리스트\n","    while a: # 리스트 a에 자료가 남아있다면 True\n","        value = a.pop(0) # 리스트 a에서 인덱스 0번째 값을 하나씩 추출해서 value로 사용 >> 하나씩 pop되므로 리스트 a의 요소들이 하나씩 줄어든다\n","        ins_idx = find_ins_idx(res, value) # 리스트 res와 value를 함수 find_ins_idx를 사용하여 value의 위치값 추출\n","        res.insert(ins_idx, value) # 추출된 value의 위치에 value 삽입\n","    return res\n","\n","d = [2,4,5,1,3]\n","print(ins_sort(d))"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"Dj72rXIP1bL-","executionInfo":{"status":"ok","timestamp":1713137600092,"user_tz":-540,"elapsed":300,"user":{"displayName":"김성원","userId":"15056001630390828466"}},"outputId":"abfef07b-5cc0-4b5e-f290-b97bfaa7b464"},"execution_count":null,"outputs":[{"output_type":"stream","name":"stdout","text":["[1, 2, 3, 4, 5]\n"]}]},{"cell_type":"code","source":["# 2. 주어진 리스트 안에서 재배치 하는 알고리즘\n","\n","def ins_sort2(a):\n","    n = len(a)\n","    for i in range(1, n): # i에 1부터 n-1까지 차례대로 들어감\n","        key = a[i] # key를 idx 가 i인 리스트 a의 요소값으로 지정\n","        j = i - 1 # j를 i 왼쪽에 배치해주기 위해 -1함\n","\n","        while j >= 0 and a[j] > key: # j가 0보다 크거나 같고 idx 를 j로 가지는 리스트 a의 값이 key보다 크면\n","            a[j+1] = a[j] # 삽입할 공간 확보를 위해서 a[j]를 j+1의 위치로 이동\n","\n","\n","            j = j - 1 # 삽입할 위치 조정\n","\n","        a[j+1] = key # 찾은 위치에 key 저장\n","\n","d = [2,4,5,1,3]\n","ins_sort2(d)\n","print(d)"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"mNAiM_QA38iX","executionInfo":{"status":"ok","timestamp":1713139135856,"user_tz":-540,"elapsed":7,"user":{"displayName":"김성원","userId":"15056001630390828466"}},"outputId":"f2271adb-85a8-4b69-f7cb-ef48eb7f03c0"},"execution_count":null,"outputs":[{"output_type":"stream","name":"stdout","text":["[1, 2, 3, 4, 5]\n"]}]},{"cell_type":"code","source":["# 연습 문제\n","\n","# 내림차순\n","\n","def ins_sort2(a):\n","    n = len(a)\n","    for i in range(1, n):\n","        key = a[i]\n","        j = i - 1\n","\n","        while j >= 0 and a[j] < key: # '>'를 '<'로 바꿔준다\n","            a[j+1] = a[j]\n","\n","\n","            j = j - 1\n","\n","        a[j+1] = key\n","\n","d = [2,4,5,1,3]\n","ins_sort2(d)\n","print(d)"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"57DUvVtE-OrI","executionInfo":{"status":"ok","timestamp":1713139267260,"user_tz":-540,"elapsed":310,"user":{"displayName":"김성원","userId":"15056001630390828466"}},"outputId":"243a7c3f-6335-49e0-ac73-c42b83460b4f"},"execution_count":null,"outputs":[{"output_type":"stream","name":"stdout","text":["[5, 4, 3, 2, 1]\n"]}]},{"cell_type":"markdown","source":["병합 정렬"],"metadata":{"id":"OqK01ggQD4Lx"}},{"cell_type":"code","source":["# 병합 정렬\n","\n","def merge_sort(a):\n","    n = len(a)\n","    if n <= 1: # 종료 조건\n","        return a\n","\n","    mid = n // 2 # 중간값 idx\n","    g1 = merge_sort(a[:mid]) # 재귀 호출로 첫번째 그룹을 정렬\n","    g2 = merge_sort(a[mid:]) # 재귀 호출로 두번째 그룹을 정렬\n","\n","    res = [] # 두 그룹 비교 결과를 담을 빈 리스트 생성\n","    while g1 and g2: # 두 그룹 모두 자료가 남아 있는 동안 반복\n","        if g1[0] < g2[0]: # 두그룹의 첫번째 요소의 값 크기를 비교\n","            res.append(g1.pop(0))\n","        else:\n","            res.append(g2.pop(0))\n","\n","    # 나머지 요소들도 마저 비교해서 결과 리스트에 삽입\n","    while g1:\n","        res.append(g1.pop(0))\n","    while g2:\n","        res.append(g2.pop(0))\n","    return res\n","\n","d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]\n","print(merge_sort(d))\n"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"B-GWAxrODrKa","executionInfo":{"status":"ok","timestamp":1713256934265,"user_tz":-540,"elapsed":8,"user":{"displayName":"김성원","userId":"15056001630390828466"}},"outputId":"292bc4d2-1349-4b00-ff91-8b93e4ceb06f"},"execution_count":2,"outputs":[{"output_type":"stream","name":"stdout","text":["[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n"]}]},{"cell_type":"code","source":["# 병합 정렬 일반 버전\n","\n","def merge_sort(a):\n","    n = len(a)\n","    if n <= 1:\n","        return\n","\n","    # 재귀 호출로 두 그룹으로 나눈뒤 정렬\n","    mid = n // 2\n","    g1 = a[:mid]\n","    g2 = a[mid:]\n","    merge_sort(g1)\n","    merge_sort(g2)\n","\n","    i1 = 0 # g1 의 인덱스값\n","    i2 = 0 # g2 의 인덱스값\n","    ia = 0 # a의 인덱스값\n","\n","    while i1 < len(g1) and i2 < len(g2): # g1의 위치 정보가 마지막보다 작고 g2의 위치 정보가 마지막보다 작은 동안 반복\n","        if (g1[i1] < g2[i2]): # g1의 값이 작으면\n","            a[ia] = g1[i1] # a에 g1값 삽입\n","            i1 += 1\n","            ia += 1\n","        else:\n","            a[ia] = g2[i2] # g2의 값이 작으면 a에 g2값 삽입\n","            i2 += 1\n","            ia += 1\n","\n","    # 남은 요소들도 비교해서 리스트에 넣어주기\n","    while i1 < len(g1):\n","        a[ia] = g1[i1]\n","        i1 += 1\n","        ia += 1\n","\n","    while i2 < len(g2):\n","        a[ia] = g2[i2]\n","        i2 += 1\n","        ia += 1\n","\n","d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]\n","merge_sort(d)\n","print(d)"],"metadata":{"id":"A_MtY9DzEx2q","colab":{"base_uri":"https://localhost:8080/"},"executionInfo":{"status":"ok","timestamp":1713258385770,"user_tz":-540,"elapsed":13,"user":{"displayName":"김성원","userId":"15056001630390828466"}},"outputId":"b6aca314-ddfe-4f24-e60c-bfe7ddba9278"},"execution_count":6,"outputs":[{"output_type":"stream","name":"stdout","text":["[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n"]}]},{"cell_type":"code","source":[],"metadata":{"id":"nwpNhrP4J5tr"},"execution_count":null,"outputs":[]}]}