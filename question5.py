#!/usr/bin/env python
# coding: utf-8

from itertools import product

# ----------------------------------------
# 準備
# ----------------------------------------
# 演算子
OPERATIONS = ["+", "-", ""]

# 数字
NUMBERS = range(1, 10)  # [1,2,...,9]

# 式算出用テンプレート生成
def generate_template(nums):
    u"""generate_template([1,2,3])
        => "1{0}2{1}3"
    """
    result = []
    base = "{{{0}}}"
    for i, num in enumerate(nums):
        result.extend([str(num), base.format(i)])
    return "".join(result[:-1])

# ----------------------------------------
# Main Logic
# ----------------------------------------
def main():
    # テンプレート生成
    template = generate_template(NUMBERS)

    # 演算子のすべての組み合わせ
    all_operations = product(*[OPERATIONS]*(len(NUMBERS)-1))

    for operations in all_operations:
        # テンプレートに演算子を適用
        applied = template.format(*operations)
        # 評価
        evaluated = eval(applied)
        if evaluated == 100:
            # 表示を調整
            print applied.ljust(16, " "), "=", evaluated
    pass

if __name__ == '__main__':
    main()
    print "OK"
