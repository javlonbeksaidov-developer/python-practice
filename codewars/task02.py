"""
Satr bilan tugaydi?

Yechimni shunday yakunlangki, agar birinchi argument (satr)
ikkinchi argument (shuningdek, satr) bilan tugasa, u true qiymatini qaytaradi.

Misollar:

Inputs: "abc", "bc"
Output: true

Inputs: "abc", "d"
Output: false
"""


def solution(text, ending):
    # your code here...
    return bool(text.endswith(ending))
