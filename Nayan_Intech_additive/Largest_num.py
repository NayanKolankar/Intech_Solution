(e)Coin Denomination

To find the minimum number of coins needed to make a given sum of money, we often employ a greedy approach. This strategy involves selecting the largest coin denominations, which are less than or equal to the target amount. However, for a more efficient solution, dynamic programming comes into play. In this approach, we break down the problem into smaller subproblems and create a systematic way of solving them.
In the dynamic programming solution, we utilize two main arrays: one to store the available coin denominations and another to keep track of previously calculated results. The coin array contains all the different denominations, and an index is used to navigate through it. The "ways" array is employed to store the number of ways the sum can be formed using the given denominations.
Consider an example where the target sum is 20, and the available coins are 1, 5, and 10. Multiple combinations can be used to make 20, such as using only 1 coin, only 5 coins, only 10 coins, or a combination of them. The "ways" array records the number of ways for each possible sum. To determine the minimum number of coins required, we iterate through the coin denominations, comparing each index value of the "ways" array with the value of the current coin. The goal is to find the minimum number of coins needed to reach the target sum, and the result is stored in the "ways" array at the position corresponding to the target sum.


Remove a digit to print the largest number (Python code)

input_numbers = ["1234", "2356", "5479", "25412"]
min_digit=0
output_numbers = []
for i in input_numbers:
   min_digit=i[0]
   for j in range(1,len(i)):
       if min_digit > i[j]:
           min_digit=i[j]
   output_numbers.append(i.replace(min_digit,""))
for i in output_numbers:
   print(i)



(f) Dot product and Cross product

The dot product, also known as the scalar product or inner product, is a mathematical operation that takes two equal-length sequences of numbers (usually coordinate vectors) and returns a single number. In the context of vectors A=(a1,a2,a3) and B=(b1,b2,b3),  the dot product is given by:
A⋅B=a1⋅b1+a2⋅b2+a3⋅b3
Use Cases of Dot Product in Graphics:
Projection: In computer graphics, the dot product is often used to determine the projection of one vector onto another. This is useful for calculating shadows, reflections, and lighting effects in 3D scenes.
Angle Between Vectors: The dot product can be used to find the angle θ between two vectors A and B using the formula 
cos(θ)=A⋅B / ∥A∥⋅∥B∥ 
Normalization: The dot product is used in normalizing vectors. If A is a vector, then the normalized vector A^ is obtained by dividing each component of A by its magnitude, which involves the dot product.
Cross Product:
The cross product, also known as the vector product or outer product, is another mathematical operation involving two vectors, resulting in a vector that is perpendicular to the plane formed by the original vectors. In the context of vectors
A=(a1,a2,a3) and B=(b1,b2,b3), the cross product is given by:
A×B=(a2b3−a3b2,a3b1−a1b3,a1b2−a2b1)
Use Cases of Cross Product in Graphics:
Normal Vector: The cross product is used to find the normal vector to a plane defined by two vectors. This normal vector is crucial in shading and lighting calculations in computer graphics.
Orientation: In 3D graphics, the cross product is used to determine the orientation of a set of three points. This is valuable in tasks such as polygon winding order determination.
Rotation Axis: The cross product can be employed to find the axis of rotation when transforming one vector into another. This is useful in animation and modeling.
Both the dot product and cross product play essential roles in computer graphics, helping to calculate angles, projections, lighting effects, and geometric transformations in three-dimensional space.





(g)
My favorite subject would be Operating systems.


(h)

A code crash is an event where a software application stops working or terminates unexpectedly due to errors or bugs in the code. This can lead to unexpected behavior, data loss, or a complete halt of the application or system.


Code crashes can be caused by :-
faulty error handling
Memory leaks
Infinite loops
insufficient resource management
Bugs
incompatible software components


Preventing a code crash can be achieved by ensuring proper error handling, input validation, memory management, and thorough testing. It is also important to keep software up-to-date and to use quality programming practices such as using type-safe languages, following established coding standards, and implementing robust exception handling mechanisms.
