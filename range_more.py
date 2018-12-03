#bottles
#of beer on the wall
#of beer.
#Take one down.
#Pass it around
#No more bottles of beer on the wall
#handle scenario for one bollle

word="bottles"
for i in range(3,0,-1):
    print(i, word, "of beer on the wall")
    print(i, word, "of beer")
    print("Take one down")
    print("Pass it around")
    if i==1:
        print("No more bottles of beer on the wall")
    else:
        newi=i-1
        if(newi==1):
              word="bottle"
        print(newi,word,"on the wall")
    print()
              
        
            
