class nums:
    A = 0
    B = 0
    C = 0

nums.A = int(input())
nums.B = int(input())
nums.C = int(input())

# max = nums.A
# if nums.B > max:
#     max = nums.B
# if nums.C > max:
#     max = nums.C

match max(nums.A, nums.B, nums.C):
    case nums.A:
        print(f"№1: {nums.A}")
    case nums.B:
        print(f"№2: {nums.B}")
    case nums.C:
        print(f"№3: {nums.C}")

# def sqr(number):
#     return number*number

# l = enumerate(map(sqr, range(1, 4)))

# print(next(l))

# def read_input(index):
#     return int(input(f"Input number {index + 1}: "))

# def get_value(tuple):
#     return tuple[1]

# tuples = enumerate(map(read_input, range(3)))
# #max_index, max_val = max(tuples, key = get_value)
# #print(f"Max value: {max_val} (at index {max_index + 1})")
# print(max(tuples, key=))

# # http_code = "418"
# # match http_code:
# #     case "200":
# #         print("OK")
# #         do_something_good()
# #     case "404":
# #         print("Not Found")
# #         do_something_bad()
# #     case "418":
# #         print("I'm a teapot")
# #         make_coffee()
# #     case _:
# #         print("Code not found")