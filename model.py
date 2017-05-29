import numpy as np
from numpy.random import rand
from random import random, uniform
from math import sqrt
# K = np.array([[1, 1, 1], [1, 1, 1]])
# p = np.array([1, 2, 1])
#
# eta = rand(*K.shape)
#
# X = K*p + eta
# print(X)
#
# R = np.cov(eta)
# print(R)
# p_ = np.dot(
#     np.dot(
#         np.linalg.inv(
#             np.dot(
#                 np.transpose(K), K)),
#         np.transpose(K)), X)
#
# print(p_)


def prognose(trend, name, variance):
    x = []
    for i in range(13):
        x.append(trend + uniform(-variance, variance))
    print("прогноз: {0}".format(x[12]))
    p0 = sum(x) / len(x)
    dd = sum([(x - p0) ** 2 for x in x]) / (len(x) - 1)
    d = sqrt(dd)
    u1 = True
    for i, k in enumerate(x):
        if k - p0 >= 2 * d:
            u1 = False

    u2 = True
    if p0 > 2*d:
        u2 = True
    else:
        u2 = False

    u3 = True
    for i in x:
        if i <= 0:
            u3 = False

    mask = 0
    if u1:
        mask += 0b1
    if u2:
        mask += 0b10
    if u3:
        mask += 0b100
    if mask < 4:
        print("{0} Красный".format(name))
    elif mask == 4:
        print("{0} Оранжевый".format(name))
    elif mask == 7:
        print("{0} Зеленый".format(name))
    else:
        print("{0} Желтый".format(name))


prognose(10, "Картошка", 0.1)
prognose(15, "Чипсы", 1)
prognose(3, "Пицца", 50)
prognose(114, "Сметана", 50)
prognose(32, "Окорочка", 12)
prognose(22, "Творог", 1)
prognose(145, "Сосиски", 40)
prognose(356, "Колбаса", 1)
prognose(112, "Шоколад", 10)
