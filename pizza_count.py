tomato_slices, cheese_slices=map(int,input().split())
Big_count=0
small_count=0
val=0
if(tomato_slices>cheese_slices):
  val=tomato_slices
else:
  val=cheese_slices
for i in range(1,val):
  if(4*i<=tomato_slices and 1*i<=cheese_slices):
    Big_count+=1
  else:
    break
for j in range(1,val):
  if(2*j<=tomato_slices and 1*j<=cheese_slices):
    small_count+=1
  else:
    break
print('Big Pizza:',Big_count)
print('Small Pizza:',small_count)
