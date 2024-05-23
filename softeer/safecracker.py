import sys

input = sys.stdin.readline

W, N = map(int, input().split())

jewels = [list(map(int, input().split())) for _ in range(N)]

jewels.sort(key=lambda x: x[1], reverse=True)

price = 0

for jewel in jewels:
    # 가방 무게가 0이 된다면, 종료
    if W == 0:
        break
    # 만약 가방의 남은 무게보다 현재 보석의 무게가 더 작다면, 보석무게*가격만큼 더하고 가방 무게에서 뺀다
    elif W >= jewel[0]:
        price += jewel[0] * jewel[1]
        W -= jewel[0]
    # 가방의 남은 무게보다 현재 보석의 무게가 더 크다면, 남은무게*가격만큼 더하고 가방 무게에서 뺀다
    elif W < jewel[0]:
        price += W * jewel[1]
        W -= W

print(price)
