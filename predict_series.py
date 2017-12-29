#coding=utf-8
import random
import numpy as np
import time

d = ["1.金","1.金","1.金","1.金", "2.木","2.木","2.木","3.水","3.水","4.火"]
d_list = [int(x.split('.')[0]) for x in d]
c_list = [x.split('.')[1] for x in d]
uniq = ["金","木","水","火"]
rate = [2, 3, 5, 10]
total = 5000
history = []

while True:
	print '-------------------------------'
	print "历史开奖结果：" + ''.join(history)
	b = len(history)
	for n in uniq:
		if n not in history:
			print "从来开过%s" % n
		else: 
			idx = list(reversed(history)).index(n)
			a = history.count(n)
			print "%d轮之前开过%s\t%d/%d\t%f" % (idx+1,n, a, b, round(a/float(b),3))
	print '-------------------------------'
	print "目前你的本金是：%d元" % total

	rate_hint = '倍\t'.join([str(x) for x in rate]) + '倍'
 	num = raw_input("请选择你的下注: \n" + rate_hint + "\n%s\t%s\t%s\t%s\n\n" % tuple(sorted(set(d))))
	if num != '':
		num_list = [int(x) for x in num.split(',')]
		if 8 in num_list: break

	 	money = raw_input("请选择你的下注金额: \n")
		money_list = [int(x) for x in money.split(',')]
	

	total -= sum(money_list)
	print '-------------------------------'
	print "下注成功！\t目前你的本金是：** %d元 **" % total
	print '-------------------------------'
	for j,k in enumerate(num_list):
		print "你买了%d元%s" % (money_list[j],uniq[k-1])
	print "\n\n开奖中...\n\n"
	time.sleep(2)
	print ''.join(['\n']*2)

	i = random.randint(0,9)
	deal = c_list[i]
	history.append(deal)
	print "本期开奖结果：%s\n\n" % deal
	print ''.join(['\n']*5)

	if d_list[i] in num_list:	
		idx = num_list.index(d_list[i])		
		won = money_list[idx] * rate[d_list[i]-1]
		print "恭喜你中了%d元！\n" % won
		total += won
	else: 
		print "很可惜，你没中奖！\n"
	print ''.join(['\n']*5)
	
	if total <= 0: 
		print "你已经输光光了！"
		break 
	time.sleep(2)



