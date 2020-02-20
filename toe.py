def bert_backwards(string):
    new_string = string.lower()
    a = new_string.split("bert")
    if new_string.count("bert") ==2:
        return a[1][::-1]
    else:
        return ""

print(bert_backwards("xxBertfridgebERtyy"))
