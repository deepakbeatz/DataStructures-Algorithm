import heapq

h=[10,20,80,40,50]

heapq._heapify_max(h) #heapq.heapify for min heap

print("enter the element:")
element=int(input())

heapq.heappush(h,element)
print(h)

max=heapq._heappop_max(h)
print("max:"+str(max))
print(h)
