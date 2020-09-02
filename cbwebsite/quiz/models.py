from django.db import models

qbank = {
	'easy': {
		'1': {
			'question': 'Rahul loves to play with recursion. He thought of writing a weird code in Turbo C++.\n```int main()\n{\nstatic int n = 8;\nprintf("%d", n=n-2);\nif(n!=0)\n    main();\n}```\nWhat would be the output of this code?',
			'options': ["86420", "6420", "Compile Error", "Infinite Loop"],
		},
		'2': {
			'question': "It's JAVA time. What will the output of this code?\n```class test{\npublic char x,y;\n}```\n```\npublic class Main{\npublic static void main(String[] args) {\ntest t = new test();\nSystem.out.println(t.x+\" \"+t.y);\n}\n}```",
			'options': ["No output", "2 Garbage Values", "'' ''", "None of the above"],
		},
		'3': {
			'question': "An Artificial Intelligence want to test your intelligence. It wrote a code for you and asked you to predict its output.\n```printf(\"%d\", 'Z' - 'A');```",
			'options': ["Compile Error", "0", "26", "25"],
		},
		'4': {
			'question': 'Do you know what is the return type of the function ```System.out.println()``` in JAVA?',
			'options': ["int", "String", "void", "char"],
		},
		'5': {
			'question': 'What will be the output for this snippet of code?\n```int n = (1)?((printf("1")?printf("0"):printf("1"))):((printf("0")?printf("1"):printf("0")));\ncout<<n;```',
			'options': ["010", "110", "101", "100"],
		},
	},
	'medium': {
		'1': {
			'question': 'Tell me the output of this JAVA snippet.\n```System.out.println(((((15<<3)>>2)>>1)<<2)>>3);```',
			'options': ["12", "15", "9", "7"],
		},
		'2': {
			'question': "Do you remember the memory size used by various data types? Try to find the ouput of the following code.\n```printf(\"%d\", printf(\"%d\", (int)sizeof(\"WELCOME\")));```",
			'options': ["81", "71", "84", "74"],
		},
		'3': {
			'question': 'Alex wrote a simple code in C++.\n```int main()\n{\nint x;\ncin>>x;\nif(x>0){\ncout<<"POSITIVE";\n}\nelse if(x<0){\ncout<<"NEGATIVE";\n}\nelse{\ncout<<"ZERO";\n}\nreturn 0;\n}```\nAlex wanted to try something different. That is why he ran the above code and entered ```"a"``` when prompted. What would be the output of the code now?',
			'options': ["An error will be raised", "NEGATIVE", "POSITIVE", "ZERO"],
		},
	},
	'hard': {
		'1': {
			'question': "Write a program in Java to enter the length of an array ```n``` from the user. After that, take ```n``` integer numbers as an input from the user and check whether those numbers are in power of 2 or not.\n\nFor Example,\n*INPUT:*\n```Enter the length of array: 5\nEnter 5 integers: 1 2 16 1024 31```\n*OUTPUT:*\n```True True True True False```\n\nExplaination:\nThe integers 1,2,16 and 1024 are in power of 2 but 31 is not.\n\nHint: There is a toolbox named as 'java.Math' and I think you can find some tool to help you solve this problem.",
		},
		'2': {
			'question': "As you all know that COVID-19 is spreading like crazy. Its transmission can be minimized if we follow social distancing. People have been advised to stay at least 6 feet away from any other person. Now, people are lining up in a queue at the local shop and it is your duty to check whether they are all following this advice.\nThere are total of ```N``` spots (numbered 1 through N) where people can stand in front of the local shop. The distance between each pair of adjacent spots is 1 foot. Each spot may be either empty or occupied; you are given a sequence ```A(1), A(2),..., A(N)``` , where for each valid ```i```, ```A(i) = 0``` means that the ```i-th``` spot is empty, while ```A(i) = 1``` means that there is a person standing at this spot. It is guaranteed that the queue is not completely empty.\nYou need to determine whether the people outside the local shop are following the social distancing advice or not. As long as some two people are standing at a distance smaller than 6 feet from each other, it is bad and you should report it, since social distancing is not being followed.\n\nFor Example,\n*INPUT:*\n```Enter value of N: 12\nEnter the queue: 0 1 0 0 0 0 0 0 1 0 0 0```\n*OUTPUT:*\n```YES```\n\n*INPUT:*\n```Enter value of N: 12\nEnter the queue: 0 1 0 0 1 0 0 0 0 0 0 1```\n*OUTPUT:*\n```NO```\n\nExplaination:\nIn the 1st example, the distance betweem two person is 7ft and thus, they are following social distancing.\nIn 2nd example, there are 3 person, 5th and 12th person are following the social distancing but 2nd and 5th person aren't following it.",
		},
	},
}

answer_key = ['b', 'a', 'd', 'c', 'c', 'd', 'a', 'd']

class participants(models.Model):
	class Meta:
		verbose_name = "PARTICIPANTS"
		verbose_name_plural = "PARTICIPANTS"

	def __str__(self):
		return self.username

	fullname = models.CharField(max_length=40)
	emailid = models.CharField(max_length=40, unique=True)
	rollno = models.CharField(max_length=4, unique=True)
	team = models.CharField(max_length=1)
	username = models.CharField(max_length=20, unique=True)
	login_flag = models.CharField(max_length=1)

class omrsheet(models.Model):
	class Meta:
		verbose_name = "OMR SHEET"
		verbose_name_plural = "OMR SHEET"

	username = models.CharField(max_length=20, unique=True)
	q1 = models.CharField(max_length=1, default='x')
	q2 = models.CharField(max_length=1, default='x')
	q3 = models.CharField(max_length=1, default='x')
	q4 = models.CharField(max_length=1, default='x')
	q5 = models.CharField(max_length=1, default='x')
	q6 = models.CharField(max_length=1, default='x')
	q7 = models.CharField(max_length=1, default='x')
	q8 = models.CharField(max_length=1, default='x')
	q9 = models.TextField(default='x')
	q10 = models.TextField(default='x')
	final_submit = models.CharField(max_length=1, default='0')

	def __str__(self):
		return self.username

	def get_solved_questions(self):
		easy = 0
		for _ in range(1,6):
			if eval("self.q"+str(_)+"!='x'"):
				easy += 1
		medium = 0
		for _ in range(6,9):
			if eval("self.q"+str(_)+"!='x'"):
				medium += 1
		hard = 0
		for _ in range(9,11):
			if eval("self.q"+str(_)+"!='x'"):
				hard += 1
		return easy, medium, hard

class scorecard(models.Model):
	class Meta:
		verbose_name = "SCORE CARD"
		verbose_name_plural = "SCORE CARD"

	username = models.CharField(max_length=20, unique=True)
	score = models.CharField(max_length=5, default='x')

	def __str__(self):
		return self.username

	def calculate_result(self):
		if self.score == 'x':
			self.score = "0"
			sheet = omrsheet.objects.all().get(username=self.username)
			ans = [sheet.q1, sheet.q2, sheet.q3, sheet.q4, sheet.q5, sheet.q6, sheet.q7, sheet.q8]
			for _ in range(8):
				if _ in [0,1,2,3,4] and ans[_] == answer_key[_]:
					self.score = str(int(self.score) + 25)
				elif _ in [5,6,7] and ans[_] == answer_key[_]:
					self.score = str(int(self.score) + 50)
			self.save()
		return self.score
