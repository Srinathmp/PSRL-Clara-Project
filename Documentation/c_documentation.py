if_statement = {
'definition':	"Conditionally executes code.Used where code needs to be executed only if some condition is true.",

'Syntax':
"""
if ( expression ) statement_true	(1)	
if ( expression ) statement_true else statement_false	(2)	
""",
'Explanation':
"""
expression must be an expression of any scalar type.

If expression compares not equal to the integer zero, statement_true is executed.

In the form (2), if expression compares equal to the integer zero, statement_false is executed.

As with all other selection and iteration statements, the entire if-statement has its own block scope:
""",
'Related Keywords':
"if, else,conditional_statement,ift_explanation",
'Example':
"""
#include <stdio.h>
 
int main(void)
{
    int i = 2;
    if (i > 2) {
        printf("first is true\n");
    } else {
        printf("first is false\n");
    }
 
    i = 3;
    if (i == 3) printf("i == 3\n");
 
    if (i != 3) printf("i != 3 is true\n");
    else        printf("i != 3 is false\n");
}
Output:

first is false
i == 3
i != 3 is false
"""
}

else_statement = {'definition':"""The else is always associated with the closest preceding if (in other words, if statement_true is also an if statement, then that inner if statement must contain an else part as well)""",
'Syntax':"if ( expression ) statement_true else statement_false",
'Example':
"""
int j = 1;
if (i > 1)
   if(j > 2)
       printf("%d > 1 and %d > 2\n", i, j);
    else // this else is part of if(j>2), not part of if(i>1) 
       printf("%d > 1 and %d <= 2\n", i, j);
If statement_true is entered through a goto, statement_false is not executed.
""",
'Related Keywords':
"if, else,conditional_statement,ift_explanation"
}

# print(if_statement.keys())
# print(else_statement.keys())
array_doc = {
'definition':"Array is a type consisting of a contiguously allocated nonempty sequence of objects with a particular element type. The number of those objects (the array size) never changes during the array lifetime.",
'Syntax':"""
In the declaration grammar of an array declaration, the type-specifier sequence designates the element type (which must be a complete object type), and the declarator has the form:

[ static(optional) qualifiers(optional) expression(optional) ]  (1) 
[ qualifiers(optional) static(optional) expression(optional) ]  (2) 
[ qualifiers(optional) * ]  (3) 
1,2) General array declarator syntax
3) Declarator for VLA of unspecified size (can appear in function prototype scope only) where
expression  - any expression other than comma operator, designates the number of elements in the array
qualifiers  - any combination of const, restrict, or volatile qualifiers, only allowed in function parameter lists; this qualifies the pointer type to which this array parameter is transformed
float fa[11], *afp[17]; // fa is an array of 11 floats
                        // afp is an array of 17 pointers to floats
                        """,
'Assignment':
"""
Objects of array type are not modifiable lvalues, and although their address may be taken, they cannot appear on the left hand side of an assignment operator. However, structs with array members are modifiable lvalues and can be assigned:

int a[3] = {1,2,3}, b[3] = {4,5,6};
int (*p)[3] = &a; // okay, address of a can be taken
// a = b;            // error, a is an array
struct { int c[3]; } s1, s2 = {3,4,5};
s1 = s2; // okay: can assign structs holding array members
""",
'Multidimensional arrays':
"""
When the element type of an array is another array, it is said that the array is multidimensional:

// array of 2 arrays of 3 ints each
int a[2][3] = {{1,2,3},  // can be viewed as a 2x3 matrix
               {4,5,6}}; // with row-major layout
Note that when array-to-pointer conversion is applied, a multidimensional array is converted to a pointer to its first element, e.g., pointer to the first row:

int a[2][3]; // 2x3 matrix
int (*p1)[3] = a; // pointer to the first 3-element row
int b[3][3][3]; // 3x3x3 cube
int (*p2)[3][3] = b; // pointer to the first 3x3 plane
Multidimensional arrays may be variably modified in every dimension:

int n = 10;
int a[n][2*n];
""",
'Array initialization':
"""
When initializing an object of array type, the initializer must be either a string literal (optionally enclosed in braces) or be a brace-enclosed list of initialized for array members:

= string_literal  (1) 
= { expression , ... }
= { designator(optional) expression , ... }

(2) (until C99)
(since C99)
1) string literal initializer for character and wide character arrays
2) comma-separated list of constant (until C99) expressions that are initializers for array elements, optionally using array designators of the form [ constant-expression ] = (since C99)
Arrays of known size and arrays of unknown size may be initialized, but not VLAs. (since C99).

All array elements that are not initialized explicitly are initialized implicitly the same way as objects that have static storage duration.
""",
'Initialization from strings':
"""
string literal (optionally enclosed in braces) may be used as the initializer for an array of matching type:

Successive bytes of the string literal or wide characters of the wide string literal, including the terminating null byte/character, initialize the elements of the array:

char str[] = "abc"; // str has type char[4] and holds 'a', 'b'. 'c', '\0'

If the size of the array is known, it may be one less than the size of the string literal, in which case the terminating null character is ignored:

char str[3] = "abc"; // str has type char[3] and holds 'a', 'b', 'c'
Note that the contents of such array are modifiable, unlike when accessing a string literal directly with char* str = "abc";.
""",
'Initialization from brace-enclosed lists':
"""
When an array is initialized with a brace-enclosed list of initializers, the first initializer in the list initializes the array element at index zero (unless a designator is specified) (since C99), and each subsequent initializer without a designator (since C99)initializes the array element at index one greater than the one initialized by the previous initializer.

int x[] = {1,2,3}; // x has type int[3] and holds 1,2,3
int y[5] = {1,2,3}; // y has type int[5] and holds 1,2,3,0,0
int z[3] = {0}; // z has type int[3] and holds all zeroes

It's an error to provide more initializers than elements when initializing an array of known size (except when initializing character arrays from string literals).
""",
'Nested arrays':
"""
f the elements of an array are arrays, structs, or unions, the corresponding initializers in the brace-enclosed list of initializers are any initializers that are valid for those members, except that their braces may be omitted as follows:

If the nested initializer begins with an opening brace, the entire nested initializer up to its closing brace initializes the corresponding array element:

int y[4][3] = { // array of 4 arrays of 3 ints each (4x3 matrix)
    { 1 },      // row 0 initialized to {1, 0, 0}
    { 0, 1 },   // row 1 initialized to {0, 1, 0}
    { [2]=1 },  // row 2 initialized to {0, 0, 1}
};  

If the nested initializer does not begin with an opening brace, only enough initializers from the list are taken to account for the elements or members of the sub-array, struct or union; any remaining initializers are left to initialize the next array element:

int y[4][3] = {    // array of 4 arrays of 3 ints each (4x3 matrix)
1, 3, 5, 2, 4, 6, 3, 5, 7 // row 0 initialized to {1, 3, 5}
};                        // row 1 initialized to {2, 4, 6}
                          // row 2 initialized to {3, 5, 7}
                          // row 3 initialized to {0, 0, 0}
 
struct { int a[3], b; } w[] = { { 1 }, 2 }; // array of structs
   // { 1 } is taken to be a fully-braced initializer for element #0 of the array
   // that element is initialized to { {1, 0, 0}, 0}
   // 2 is taken to be the first initialized for element #1 of the array
   // that element is initialized { {2, 0, 0}, 0}
"""

}
