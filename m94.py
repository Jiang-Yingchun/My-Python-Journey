# 列表 a = [2, 4, 6] 已给定，要求：
# 从键盘输入 3 个整数，组成列表 b
# 计算 a 和 b 对应元素的差，生成新列表 c（c[i] = a[i] - b[i]）
# 输出列表 c
# 示例输入：1 2 3
# 示例输出：[1, 2, 3]
a=[2,4,6]
b=list(map(int,input().split()))
c=[]
for i in range(len(a)):
    c.append(a[i]-b[i])
print(c)