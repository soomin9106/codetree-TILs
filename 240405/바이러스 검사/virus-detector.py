n = int(input())
customers = list(map(int, input().split()))
max1, max2 = map(int, input().split())


ans = 0
for customer in customers:
    if customer < max1:
        ans += 1
        continue
    else:
        customer -= max1
        ans += 1

        if customer < max2:
            ans += 1
            continue
        else:
            while customer > max2:
                ans += (customer // max2)
                customer = customer % max2

            ans += 1

print(ans)