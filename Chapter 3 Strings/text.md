***String***

```
String is a sequence of charecters enclosed in quotes
```

we can write a string in 3 ways
```
a = 'harry'         #Single Quoted string
a = "harry"         #double Quoted string
a = '''harry'''     #triple Quoted string
```
```
# string is immutable in python , it cannot be changed
```

positive and negative indexing start from here
```
 0  1  2  3  4
 H  a  r  r  y
-5 -4 -3 -2 -1
```


Inclusive and Exclusive in slicing mean:

***Inclusive: That index is included in the result.***

***Exclusive: That index is NOT included in the result.***


📌 In Python string slicing: string[start:stop]
start → Inclusive (starts from this index)
stop → Exclusive (stops before this index)


name = "Rutuja"

#         012345
# name = "Rutuja"

print(name[1:4])  # 'utu'
Explanation:

Index 1 → inclusive → 'u' ✅
Index 4 → exclusive → 'j' ❌ (so it stops before 4)

So it prints characters at index 1, 2, and 3.


***In slicing syntax:***

```
[start:stop:step]
start → where to start (inclusive)
```

```
stop → where to stop (exclusive)

step → how many characters to skip each time
```

***example explain***
```
a = "Abcdefghijkl"
# Index:  0123456789011

```
✅ 1. a[1:9]
Means:

Start at index 1 → 'b'

Go up to but not including index 9 → up to 'i'

Result:

```
'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i' → "bcdefghi"
```
```
✅ 2. a[1:9:4]
```
Now we use step = 4:

Start at index 1 → 'b'

Then skip 4 letters → index 5 → 'f'

Next would be index 9, but it's exclusive, so stop before 9

Result:

```
Index 1: 'b', Index 5: 'f' → "bf"
```





***✅ Basic String Methods***
```
Function	        Description	                        Example

len()	Returns the length of the string	        len("hello") → 5
str()	Converts other data types to string	        str(123) → '123'
```

***🔠 String Case Methods***
```
Method	            Description	                                     Example

.lower()	    Converts to lowercase	                    "HELLO".lower() → 'hello'
.upper()	    Converts to uppercase	                    "hello".upper() → 'HELLO'
.capitalize()	Capitalizes first letter	                "python".capitalize() → 'Python'
.title()	    Capitalizes each word                       "hello world".title() → 'Hello World'
.swapcase()	Swaps lowercase to uppercase and vice versa	    "HeLLo".swapcase() → 'hEllO'
```


***🔍 Searching and Replacing***
```
Method	                Description	                        Example
.find()	        Returns first index of substring	    "apple".find("p") → 1
.rfind()	Returns last index of substring	            "apple apple".rfind("p") → 7
.index()	Like find() but raises error if not found	"apple".index("p") → 1
.count()	Counts occurrences of substring	            "banana".count("a") → 3
.replace()	Replaces substring with another	            "hello".replace("l", "x") → 'hexxo'
```

***🧱 String Splitting & Joining***
```
Method	                Description	                                     Example
.split()	        Splits into list	                    "a,b,c".split(",") → ['a', 'b', 'c']
.rsplit()	        Splits from right	                    "a,b,c".rsplit(",", 1) → ['a,b', 'c']
.join()	        Joins iterable into string	                ",".join(['a','b']) → 'a,b'
.partition()	Splits into 3 parts around separator	    "apple-pie".partition("-") → ('apple', '-', 'pie')
```

***🧪 Testing (Returns True/False)***
```
Method	                    Description	                                   Example
.startswith()	Checks if string starts with prefix	            "hello".startswith("he") → True
.endswith()	    Checks if string ends with suffix	            "hello".endswith("lo") → True
.isalpha()	    All letters?	                                   "abc".isalpha() → True
.isdigit()	    All digits?	                                        "123".isdigit() → True
.isalnum()	    Letters and numbers?	                            "abc123".isalnum() → True
.isspace()	    Only whitespace?	                                    " ".isspace() → True
.islower()	    All lowercase?	                                        "abc".islower() → True
.isupper()	    All uppercase?                                      	"ABC".isupper() → True
.istitle()  	Is title case?	                                        "Hello World".istitle() → True
```

***🧹 Trimming***
```
Method	                   Description	                                Example
.strip()	Removes both leading and trailing spaces	        " hello ".strip() → 'hello'
.lstrip()	Removes leading spaces	                            " hello".lstrip() → 'hello'
.rstrip()	Removes trailing spaces                         	"hello ".rstrip() → 'hello'
```