#key value pair
people={"John":23,"Rob":32}
print(people["John"])
O/p-23

Dictionary Functions
numbers = {
   1: "one",
   2: "two",
   3: "three"

}
# To check Particular key is present or not
print(1 in numbers)
# To get Particular Value of a key
print(numbers.get(2))
print(numbers.get(5), "Key not found")
O/p-
True
two
None Key not found
