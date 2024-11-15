def find_largest(numbers):
  if not numbers:
    print("the list is empty.")
    return None
  largest=numbers[0]
  for num in numbers:
    if num>largest:
       largest=num
  return largest
numbers=[1,2,10,14,16,8,9]
largest= find_largest(numbers)
if largest is not None:
  print("Largest number:",largest)