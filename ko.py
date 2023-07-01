### 1 vazifa
# my_fav_dishes = ['osh', 'somsa', 'shashlik', 'norin']
#
# for item in my_fav_dishes:
#     print(f"My favorite dish is {item}")
#     # print("My favorite dish is " + item)

### 2 vazifa
# my_dishes = ['osh', 'somsa', 'shashlik', 'norin']
# friend_dishes = my_dishes.copy()
# friend_dishes_1 = my_dishes[:]
# friend_dishes_2 = [item for item in my_dishes]

# print(my_dishes)
# print(friend_dishes_2)
# my_dishes.append('steak')
# friend_dishes_2.append('olot somsa')
# print(my_dishes)
# print(friend_dishes_2)
### 3 vazifa
# user_num = input('Sonni kiriting: ')
# nums = [num for num in range(1, int(user_num)+ 1)]
# print(nums)
# result = 0
# for item in nums:
#     result += item
# print(result)
# print(sum(nums))

# num_odd = [item for item in range(1, 101) if item % 2 != 0]
# num_juft = [item for item in range(1, 101) if item % 2 == 0]
# print(num_odd)
# print(num_juft)

# numbers = [
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412,
#     566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445,
#     742, 717, 958, 743, 527
# ]
#
# result = []
# for num in numbers:
#     if num == 815:
#         break
#     else:
#         result.append(num)
#
# result.sort()
# print(result)
