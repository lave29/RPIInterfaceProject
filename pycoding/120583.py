#중복된 숫자 개수
#정수가 담긴 배열 array와 정수 n이 매개변수로 주어질 때, array에 n이 몇 개 있는 지를 return 하도록 solution 함수를 완성해보세요.'

# def solution(array, n):
#     answer = 0
#     return answer

day=[1, 2, 3, 'MON', 'TUE', 'WED']

def solution(array, n):
    answer = array.count(n)
    return answer

print(solution(day, 1))

# def solution(array, n):
#     answer = 0
#     for n in array :
#         answer+=1
#     return answer