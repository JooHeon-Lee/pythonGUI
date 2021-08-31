kor = ["사과", "바나나", "오렌지"]
eng = ["apple", "banana", "orange"]

zip(kor,eng) # 두개를 합침 but 세로로 ex) 사과-apple

print(list(zip(kor,eng)))

mixed = [('사과', 'apple'), ('바나나', 'banana'), ('오렌지', 'orange')]

print(list(zip(*mixed))) # *을 넣으면 unzip 즉 분리해줌 분리방식은 각각항목에 대해 첫번째 끼리 두번재 끼리