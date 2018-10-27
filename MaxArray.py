def maxProduct(arr, n):

if (n < 2): 
    print("No pairs exists") 
    return
  
# Initialize max product pair 
a = arr[0]; b = arr[1] 


for i in range(0, n): 
      
    for j in range(i + 1, n): 
        if (arr[i] * arr[j] > a * b): 
            a = arr[i]; b = arr[j] 

print("Max product pair is {", a, ",", b, "}", 
                                      sep = "") 
