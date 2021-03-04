want = '안녕하세요. 기계공학과 4학년 강남규입니다.'

euc_kr_encoded = want.encode('euc-kr')
print("euc-kr로 표현 :",euc_kr_encoded)

decoded = euc_kr_encoded.decode('euc-kr')
print("euc-kr로 표현 :",decoded)

print("euc-kr은 2바이트로 표현된다.")
print("즉 xbe xc8에서 x는 표기법이며 bec8이 안이 된다. \n")


utf_f_8_encoded = want.encode('utf-8')
print("utf_f_8로 표현 :",utf_f_8_encoded)

utf_f_8_decoded = utf_f_8_encoded.decode('utf-8')
print("utf_f_8로 표현 :",utf_f_8_decoded)

print("UTF-8의 한글 코드표의 범위는 U+AC00 to U+AD00 이다.")
print("utf-8은 3바이트로 표현된다.")
print("즉 xex x95 x88 에서 0x는 16진수 표기법이며 0xec9588이 안이 된다. \n")

print("UTF-8 코드로보면 이렇습니다.")
print("U+C548 : 안","U+B155 : 녕","U+D558 : 하","U+C138 : 세","U+C694 : 요")
print("U+AE30 : 기","U+ACC4 : 계","U+ACF5 : 공","U+D559 : 학","U+ACFC : 과")
print("U+D559 : 학","U+B144 : 년","U+AC15 : 강","U+B0A8 : 남","U+ADDC : 규")
print("U+C785 : 입","U+B2C8 : 니","U+B2E4 : 다")

utf_f_16_encoded = want.encode('utf-16')
print("utf_f_16로 표현 :",utf_f_16_encoded)

utf_f_16_decoded = utf_f_16_encoded.decode('utf-16')
print("utf_f_16로 표현 :",utf_f_16_decoded)

print("utf-16은 2 or 4바이트로 표현되는 가변 길이 인코딩 방식이다.")