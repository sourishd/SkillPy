text="Don't panic!"#Target String "on tap"
ltext=list(text)
print(text)
print(ltext)
new_text=''.join(ltext[1:3])
print(new_text)
new_text=new_text+''.join([ltext[5],ltext[4],ltext[7],ltext[6]])
print(new_text)

