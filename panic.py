text="Don't panic!"#Target String "on tap"
ltext=list(text)
print(text)
print(ltext)
for i in range(4):
    ltext.pop()
#"Don't pa"
ltext.remove("D")
#"on't pa"
ltext.remove("'")
#"ont pa"
ltext.extend([ltext.pop(),ltext.pop()])
ltext.insert(2,ltext.pop(3))
new_text="".join(ltext)
print(new_text)
print(ltext)

