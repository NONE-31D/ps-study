nums = input().split()
start_h = int(nums[0])
start_m = int(nums[1])

time = int(input())
time_m = time % 60 
time_h = time // 60 

end_h = start_h + time_h
end_m = start_m + time_m

if end_m >= 60:
    end_h = end_h + end_m // 60
    # end_h += end_m // 60
    end_m = end_m % 60 

if end_h >= 24:
    end_h = end_h % 24 

print(f"{end_h} {end_m}")
# print(str(end_h)+" "+str(end_m))
