height = [4,4,4,7,1,0]

land_len = len(height)
water = 0
point_hight_info = {}

max_height = max(height)
max_idx = []

now_max = 0
for idx, h in enumerate(height):
    if h == max_height:
        max_idx.append(idx)
    if h > now_max:
        point_hight_info[idx] = h
        now_max = h


max_height_num = len(max_idx)

first_max_idx = max_idx[0]
last_max_idx = max_idx[-1]
now_max = 0

for fidx, h in enumerate(reversed(height[last_max_idx:])):
    idx = land_len - 1 - fidx
    if h > now_max:
        now_max = h
        point_hight_info[idx] = h

point_list = sorted(list(point_hight_info.keys()))



back_pointer = point_list[0]
front_pointer = point_list[1]
criteria = min(point_hight_info[back_pointer], point_hight_info[front_pointer])
i = 0
for idx, h in enumerate(height):
    if idx == front_pointer:
        i += 1
        back_pointer = front_pointer
        if idx != point_list[-1]:
            front_pointer = point_list[1 + i]
        criteria = min(point_hight_info[back_pointer], point_hight_info[front_pointer])
    elif idx > back_pointer:
        water += criteria -h
        print(f'at {idx}, water is {criteria-h}')

print(water)