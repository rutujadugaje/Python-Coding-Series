# Python program to fill in a letter template

letter = '''Dear <|Name|>,
You are selected!
<|Date|>'''

print(letter.replace("<|Name|>", "Rutu").replace("<|Date|>", "1st June 2025"))
# Output:Dear Rutu,
# You are selected!
# 1st June 2025