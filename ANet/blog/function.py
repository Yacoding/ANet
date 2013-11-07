#-*-coding:utf8-*-
import linecache
import random
'''读取文件内容函数'''
def random_words(filename):
	fp = open(filename, 'r')
	number_of_line = len(fp.readlines())
	lineno = random.randint(1, number_of_line)
	words = linecache.getline(filename, lineno)
	return words


if __name__ == '__main__':
	random_words('random_words.txt')