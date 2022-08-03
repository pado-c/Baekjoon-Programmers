import sys
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]
nums.sort() #정렬

# 산술평균 | 소수점 이하 첫째 자리에서 반올림한 값
print(round(sum(nums)/N))

# 중앙값 | N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
print(nums[N//2])

# 최빈값 | N개의 수들 중 가장 많이 나타나는 값
cnt = {}
for num in nums:
    if num not in cnt:
        cnt[num] = 1
    else:
        cnt[num] += 1

# 딕셔너리를 키와 값을 쌍으로 리턴 [(key, value), (key, value)]
sorted_cnt = sorted(cnt.items(), key = lambda x : x[1], reverse=True)

# 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값 출력
if N == 1 or sorted_cnt[0][1] > sorted_cnt[1][1]:
    print(sorted_cnt[0][0])
elif sorted_cnt[0][1] == sorted_cnt[1][1]:
    print(sorted_cnt[1][0])

# 범위 | N개의 수들 중 최댓값과 최솟값의 차이
print(max(nums) - min(nums))