### Question 1 ###

myVar = 100

def f1():
    myVar = 200
    return myVar

def f2():
    global myVar
    return myVar

print(f1())
print(f2())


### Question 2 ###

myString = "testing 123"
print(myString[::-1])


### Question 3 ###

def f1(someString):
    foo    = "aeiouAEIOU"
    result = ""
    for l in someString:
        if l in foo:
            continue
        result += l
    return result

print(f1("This fruit is a banana and not a peach"))


### Question 4 ###

def f1(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Only Chuck Norris can divide by zero")
        return None
    except TypeError:
        print("I am not sure how to divide that")
        return None
    else:
        return int(result)

testCases = [
        (10, 2),
        (10, 0),
        ("hello", 5)
        ]

for x,y in testCases:
    result = f1(x,y)
    if result:
        print(f"{x} divided by {y} is {result}")


### Question 5 ###

# file myCSV.txt on disk contains this: 
#    Name,Age,City,Grade,Score
#    Alice,25,New York,A,92
#    Bob,30,Los Angeles,B,85
#    Charlie,28,Chicago,A,95
#    David,22,Houston,C,78
#    Emily,27,Philadelphia,B,88
#    Frank,31,Phoenix,A,90
#    Grace,24,San Antonio,C,76

with open("myCSV.txt","r") as f:
    content = f.readlines()

myData = {}
for people in content[1:]:
    fields = people.split(',')
    k1 = fields[0]
    v1 = fields[1]
    myData[k1]=v1

try:
    print(myData['Charlie'])
except:
    print("I don't know what to do")


### Question 6 ###

for i in range(10):
    if (i % 2 == 0):
        continue
    if (i == 3):
        break
    if (i == 5):
        pass
    if (i == 8):
        print("bingo")

### Question 7 ###

def f1(x):
    return(x*2)

numbers = [1, 2, 3, 4]
result  = [x**2 for x in numbers]
y = 0
for x in result:
    y += f1(x)
print(y)


#### Question 8 ###

data = {
  "company": "ExampleCorp",
  "departments": [
    {
      "name": "Engineering",
      "employees": [
        {
          "name": "Alice Smith",
          "role": "Software Engineer",
          "skills": ["Python", "JavaScript", "AWS"]
        },
        {
          "name": "Bob Johnson",
          "role": "Data Scientist",
          "skills": ["Python", "R", "SQL"]
        }
      ],
      "projects": ["Project Alpha", "Project Beta"]
    },
    {
      "name": "Marketing",
      "employees": [
        {
          "name": "Carol Williams",
          "role": "Marketing Manager",
          "skills": ["SEO", "Social Media", "Content Creation"]
        },
        {
          "name": "David Lee",
          "role": "Graphic Designer",
          "skills": ["Adobe Photoshop", "Illustrator", "InDesign"]
        }
      ],
      "projects": ["Campaign X", "Campaign Y", "Campaign Z"]
    }
  ],
  "offices": ["New York", "London", "Tokyo"],
  "inventory": [
    {"item_id": "123", "quantity": 100, "details": {"color":"blue", "material":"steel"}},
    {"item_id": "456", "quantity": 50, "details": {"color":"red", "material":"plastic"}}
  ]
}

### Question 8a
print("Write a function that returns the total number of employees per department")

### Question 8b
print("Write the expression that retrieves \"Content Creation\" from this data structure")

