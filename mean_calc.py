# Making the mean calculator function
"""
The function will be called mean_calculator, because the saul purpose of the function is to calculate the mean/average of the list of values passed.
The return value of the function should be float because the value from division will always be a float.
We itterate through the list of values provided, and sum up them, then we divide the answer by the length of the list which provides the mean. The resulting value is returned from the function.
"""
def mean_calculator(num_list: list = []) -> float:
  sum = 0 # We initialize the value for sum, which will hold the sum of the values in the list.
  for i in num_list: # We iterate throught the list of values using the for loop and add each element to the sum value, which eventually becomes the sum of the elements in the list
    sum += i

  mean = sum/len(num_list) # The mean is gotten from dividing the result from sum by the length of the list.
  return float(mean) # Then we convert the value to float, just to ensure that the value returned is a float.

# Making the main function
"""
This will serve as the entry point to our function. The main function initializes the numbers list, and asks the user to provide the number of values they want to insert into the list. 
Then, we iterate up to the number entered by the user. Each time, we ask the user to provide a number, then, the number is appended to the list.
Once the list is consructed, we can then call the mean_calculator function by passing in the list. Hopefully, it'll return the correct value for the mean.
"""
def main():
  nums = [] # we initialize the list of numbers for which we wanna find the mean.
  num_of_values = int(input("Enter the number of values you wanna insert into the list: ")) # We ask the user to provide the length of the list as they desire.
  if num_of_values <= 0: # We ensure that the user didn't provide a negative number or any number below 1.
    print("Number of values can't be less than 1")
    return
  for i in range(0, num_of_values): # Then we itterate up to the limit set by the user, while adding a value to the list, until the limit is reached.
    val = int(input("Enter a value to the list: "))
    nums[i] = val

  print("Mean for the list of values you provided is: ", mean_calculator(nums)) # We print the mean which is gotten by calculating it by passing in the list of values.

if __name__ == "__main__":
  main() # Here's where we call the main function, which is the entry point into our program.

# The program is bound to fail, as there may be some logical or syntax errors i failed to figure out, because i ain't using an IDE lol. Be sure to check with a trusted person or reach me for clarification. 
  
