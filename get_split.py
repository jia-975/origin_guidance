import numpy as np

# 创建包含从0到103608的数字的numpy数组
# all_numbers = np.arange(103609)
# all_numbers = np.arange(69800)
all_numbers = np.arange(133100)
with open("data/QM9/train_split.npy", 'rb') as fin:
    train = np.load(fin)
with open("data/QM9/val_split.npy", 'rb') as fin:
    val = np.load(fin)
with open("data/QM9/test_split.npy", 'rb') as fin:
    test = np.load(fin)
    # print(data)
# # 从中随机抽取40000个数字到train中
# train = np.random.choice(all_numbers, size=60000, replace=False)
# #
# # # 从剩下的数字中再随机抽取5000个到val中
remaining_numbers = np.setdiff1d(all_numbers, train)
# val = np.random.choice(remaining_numbers, size=7000, replace=False)

# # 从剩下的数字中随机抽取200个到test中
remaining_numbers = np.setdiff1d(remaining_numbers, val)
# test = np.random.choice(remaining_numbers, size=400, replace=False)
remaining_numbers = np.setdiff1d(remaining_numbers, test)

prop = np.random.choice(remaining_numbers, size=700, replace=False)
# 打印结果
# print("Train:", train)
# np.save('data/DRUGS/train_split.npy', train)
# print("Validation:", val)
# np.save('data/DRUGS/val_split.npy', val)

# print("Test:", test)
# np.save('data/DRUGS/test_split.npy', test)
print("prop:", prop)
np.save('data/QM9/prop_split_500.npy', prop)


# 打印结果
# print("Train:", len(train))
# print("Validation:", len(val))
# print("Test:", len(test))
# res = [train, val, test]
# np.save('DRUGS_split.npy', res)
