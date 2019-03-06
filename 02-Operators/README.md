# Operators in Python
Whenever there is any transaction happening between 2 entity/humans/etc... there is a information 
recorded represented as a data. Now, In order to squeeze an meaningful information from the data 
we execute an operations on the data.(Operations like Addition, subtraction and lot more...)
such used character are called "Operators"


**Types of Operators in Python**
- Arithmetic operators
- Assignment operators
- Relational operators
- Membership opeartors
- Identity operators

###### 1. Aritmetic Operators
```
	In general there are seven arithmetic operators available and those are 
	explained underneath
```
| Operator Symbol | Operator Name |
| --- | --- |
| + | Addition Operator |
| - | Subtraction Operator |
| * | Multiplication Operator |
| / | Division Operator |
| % | Modulus Operator |
| ** | Exponent Operator |
| // | Integer Division Operator |

![image](https://s3.ap-south-1.amazonaws.com/vbpythoncodes/arithmetic-flowchart.png)

###### 2. Assignment Operators
```
	The Assignment operators helps to perform operations within variable and store the results 
	within variables.
```
| Operator Symbol | Operator Name | Operator Description|
| --- | --- | --- |
| = | Assignment Operator | Responsible for value stored in right hand side variable |
| += | Addition Assignment Operator | Incrementing right handside value |
| -= | Subtraction Assignment Operator | Decrementing right handside value |
| *= | multiplpication Assignment Operator | Multiplication right handside value |
| /= | Division Assignment Operator | Multiplicatiopn right handside value |
| %= | Modulus Assignment Operator | Divides left value and stores result right handside value |
| **= | Exponential Assignment Operator | Execute power value and then stores result in right |
| //= | Floor Division Assignment Operator | Executes division and then stores result in right |

###### 3. Relational Operators
```
	The Relational Operators defines some kind of relation between two entities and many times used to
	compare 2 values. Majorly used in staisfying conditions while proving relation.
	Example : 01-Relational_Operators.py
```
| Operator Symbol | Operator Name |
| --- | --- |
| > | Greater than Operator |
| >= | Greater than or equal Operator |
| < | Less than Operator |
| <= | Less than or equal Operator |
| == | Equal to Operator |
| != | Not Equal to Operator |

###### 4. Membership Operators
```
	The "in" & "not in" operator are useful to test membership in sequence.
	Example : 02-Relational_Operators.py
```

###### 5. Identity Operators
```
	The "is" & "is not" operators are used to compare two memory location
	Example : 03-Identity_Operators.py
```

###### TOP to BOTTOM Operators Precedence.

| Operator Rank| Operator Symbol | Operator Name |
| --- | --- | --- |
| 1 | ( ) | Parenthesis |
| 2 | ** | Exponentiation |
| 3 | -, ~ | Uniary minus, Bitwise compliment | 
| 4 | *,/,//,% | Multiplication, Division, Floor Division, Modulus |
| 5 | + , - | Addition, Subtraction |
| 6 | << , >> | Bitwise Left/Right Shift |
| 7 | & | Bitwise AND | 
| 8 | ^ | Bitwise XOR |
| 9 | "|" | Bitwise OR |
| 10 | >, >= , < , <= , == , != | Relational Operator
| 11 | =, %=, /= , //=, -= , += , *= , **= | Assignment operator|
| 12 | is, is not | Identity Operator |
| 13 | in, not in | Membership Operators | 
| 14 | not | Logical not |
| 15 | or | Logical or |
| 16 | and | Logical and |

