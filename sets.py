# numbers = {10,10,20,20,30,40,50}
# print(type(numbers))
# print(numbers)
# names= ["Billjoy", "Mbaluka", "Mbaluka"]
# print(type(names))
# print(names)
# names= set(names)
# print(names)
# examples
days = {"monday","tuesday","wednesday","thursday", "friday","saturday","sunday","sunday","sunday","sunday"}
print(days)
# Remove friday and sunday from the set using methods.
days.remove("friday")
days.discard("sunday")

# Add them back to the set
days.add("friday")
days.add("sunday")
print(days)
