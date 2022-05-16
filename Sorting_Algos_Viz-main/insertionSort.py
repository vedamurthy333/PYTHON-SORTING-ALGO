import time

def insertionSort(data, drawData, timeTick):
    
    for step in range(1, len(data)):
        key = data[step]
        # drawData(data, ['green' if x == j or x == j+1 else 'red' for x in range(len(data))])
        j = step - 1
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].
        while j >= 0 and key < data[j]:     
            
            data[j + 1] = data[j]
            
            j = j - 1    
            drawData(data, ['green' if x == step or x == j else 'red' for x in range(len(data))])       
        # Place key at after the element just smaller than it.
        data[j + 1] = key
        
        time.sleep(timeTick)
        
    # drawData(data, ['green' for x in range(len(data))])