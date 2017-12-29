# coding=utf-8
import random

def generate_key():
	key_list = []
	while True:
		a = random.randint(0,9)
		if a not in key_list: key_list.append(a)
		if len(key_list) == 5: break
	return ''.join([str(x) for x in key_list])

def check_position(guess,key):
	count = 0
	for i in range(len(g)): 
		if guess[i] in key[i]: count += 1
	return count

def check_correct(guess,key):
	count = 0
	for n in guess: 
		if n in key: count += 1
	return count
	

print "猜数字游戏：迷底是五位不重复的0-9的数字，每次可以输入猜测值并得到例如1A2B的判断返回值。\n1A表示猜测值中有一个位置正确的值，2B表示猜测值中有2个位置错误但猜测正确的值。"
key = generate_key()
turn = 0
while True:
	turn += 1
	print "turn:  " + str(turn)
	guess = raw_input("your guess:   ")
	g = list(guess)
	k = list(key)
	A = check_position(g,k)
	total = check_correct(g,k)
	B = total - A
	res = str(A) + 'A' + str(B) + 'B'
	print "your result:  %s\n" % res
	if res == "5A0B": 
		print "你全猜对了，只用了%d轮，好棒！！" % turn
		break
	if guess == "q": break
	if guess == "tip": print key



