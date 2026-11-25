list = [17, 38, 10, 25, 72]

# Sort and display the list
list.sort()
print("Sorted:", list)

# Add 12 and display the list
list.append(12)
print("After adding 12:", list)

# Reverse and display the list
list.reverse()
print("Reversed:", list)

# Display the index of 17
print("Index of 17:", list.index(17))

# Remove 38 and display the list
list.remove(38)
print("After removing 38:", list)

# Display the sublist from the 2nd to the 3rd element
print("2nd to 3rd elements:", list[1:3])

# Display the sublist from the beginning to the 2nd element
print("Beginning to 2nd element:", list[:2])

# Display the sublist from the 3rd element to the end
print("3rd element to the end:", list[2:])

# Display the complete list as a sublist
print("Complete list:", list[:])

# Display the last element using negative indexing
print("Last element:", list[-1])
