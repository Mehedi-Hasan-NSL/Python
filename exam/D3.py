input_ = [int(i) for i in input().split(',')]

#print(input_)

## generator 
def fib(n):
	t1, t2 = 0, 1 
	for _ in range(n):
		yield t1 
		t1, t2 = t2, t1+t2

for i in range(len(input_)):
	print(*list(fib(input_[i])))