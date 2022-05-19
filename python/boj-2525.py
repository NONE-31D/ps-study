h, m = map(int, input().split())
time = int(input())

end_m = (m+time) % 60
end_h = (h + (m+time) // 60) % 24

