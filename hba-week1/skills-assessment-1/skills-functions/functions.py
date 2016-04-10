# SOLUTIONS!

################################################################
# PART ONE


# 1. Write a function that does not take any arguments and
#    prints "Hello World".
def print_hello():
  print "Hello, World"

# 2. Write a function that takes a name as a string and
#    prints "Hi" followed by the name.
def hi_user(name):
  print "Hi", name

# 3. Write a function that takes two integers and multiplies
#    them together. Print the result.
def mult_together(num1, num2):
  print num1 * num2

# 4. Write a function that takes a string and an integer and
#    prints the string that many times
def mult_string(word, num):
  print word * num

# 5. Write a function that takes an integer and prints "Higher
#    than 0" if higher than zero and "Lower than 0" if lower
#    than zero. If integer is 0 print "Zero".
def higher_lower_than_zero(num):
  if num > 0:
    print "Higher than 0"
  elif num == 0:
    print "Equal to zero"
  else:
    print "Lower than 0"

# 6. Write a function that takes an integer and returns a
#    boolean (True or False), depending on whether the number
#    is evenly divisible by 3.
def div_by_three(num):
  if num % 3 == 0:
    return True
  return False

# 7. Write a function that takes a sentence as one string and
#    returns the number of spaces.
def num_of_spaces(sentence):
  counter = 0
  for char in sentence:
    if char == ' ':
      counter = counter + 1
  return counter

# 8. Write a function that can be passed a meal price and a
#    tip percentage. It should return the total amount paid
#    (price + price * tip). **However:** passing in the tip
#    percentage should be optional; if not given, it should
#    default to 15%.
def meal_and_tip(meal_price, tip_percent=0.15):
  amount_paid = meal_price + (meal_price * tip_percent)
  return amount_paid

# 9. Write a function that takes an integer as an argument and
#    returns two pieces of information as strings ---
#    "Positive" or "Negative" and "Even" or "Odd". The two strings
#	 should be returned in a list.
#
# 	Then, write code that shows the calling of this function
# 	on a number and unpack what is returned into two
# 	variables --- sign and parity (whether it's positive
# 	or negative). Print sign and parity.
def string_pos_neg_even_odd(num):
  num_properties = []
  if num > 0:
    num_properties.append('Positive')
  else:
    num_properties.append('Negative')

  if num % 2 == 0:
    num_properties.append('Even')
  else:
    num_properties.append('Odd')

  return num_properties


################################################################
# PART TWO


# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).
#
#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviaton, and the
#    default tax amount as parameters.
#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item including tax.
def item_tax_by_state(item_cost, state):
  tax_amount = 0.05
  if state == 'CA':
    tax_amount = 0.07
  total = item_cost + (item_cost * tax_amount)
  return total

# 2. Turn the block of code from the directions into a function.
#	 Take a name and a job title as parameters, making it so the
# 	 job title defaults to "Engineer" if a job title is not passed in.
#	 Return the person's title and name.
def job_title_and_name(name, job_title="Engineer"):
  return (name, job_title)

# 3. Given a receiver's name, receiver's job title, and sender's name, print the following letter:      
#       Dear JOB_TITLE RECEIVER_NAME, I think you are amazing! Sincerely,
#       SENDER_NAME. 
#    Use the function from #2 to construct the full title for the letter's greeting.
def job_title_and_name_sender(name, sender, job_title='Engineer'):
  print "Dear", job_title, name, "\nI think you are amazing!\nSincerely,", sender 

# 4. Turn the block of code from the directions into a function. This
#    function will take a number and append it to *numbers*. It doesn't
#    need to return anything.
def append_to_nums(num):
  nums = []
  nums.append(num)
  print nums

print_hello()
hi_user('Monique')
mult_together(5, 2)
mult_string("burrito", 3)
higher_lower_than_zero(1)
higher_lower_than_zero(-1)
higher_lower_than_zero(0)
print div_by_three(6)
print div_by_three(22)
print num_of_spaces("Today was a nice day outside")
print meal_and_tip(10)
print meal_and_tip(10, tip_percent=0.2)
print string_pos_neg_even_odd(-1)
print string_pos_neg_even_odd(10)
print string_pos_neg_even_odd(-1)
print item_tax_by_state(10, 'TX')
print item_tax_by_state(10, 'CA')
print job_title_and_name('Monique')
print job_title_and_name('Monique', job_title='Underwater basket weaver')
job_title_and_name_sender('Monique', 'Blake')
job_title_and_name_sender('Monique', 'Blake', job_title='Class Clown')
append_to_nums(3)
