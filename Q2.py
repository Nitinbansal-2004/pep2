# Write a program to use filter() function and a lambda function to extract all strings longer
# than 5 characters from this list:  words = 
# [‘python’, ‘fun’, ‘java’, ‘ai, ‘data analysis’, ‘practice’, ‘patience’, ‘go’]  
#  Output: [‘python’, ‘data analysis’, ‘practice’, ‘patience’] [5 marks]

w=['python', 'fun', 'java', 'ai', 'data analysis', 'practice', 'patience', 'go']
r=filter(lambda x: len(x)>5,w)
print(list(r))
