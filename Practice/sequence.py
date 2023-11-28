"""
    What is a Sequence?
        Sequence basically is just a collection
        of elements.

        a normal variable has only one value assigned
        to it. but a sequence allows you to assign
        a whole collection of values to a variable.

        # one Structure, one object that contains
            multiple values but can be treated 
            as one thing.

        # Most of them are indexed and an index is
            basically just a number that represents
            the value of the variable.

        # Merge the list
            x = [1, 2, 3, 4]
            y = [5, 6, 7, 8]

            z = [1, 2, 3, 4, 5, 6, 7, 8]

        # basic Methods
            len() # this gives us the length
            max() # this gives us the maximum
            min() # this gives us the minimum
        
        # membership operators
                ## they basically check if an element is
                contained in a sequence. and they returns
                True or False
            1. in 
            2. not in

            list = [1, 2, '3]

            print(1 in list) #  True
            print(7 in list) # False
            print(8 not in list) # True



    Types of Sequence.

        1). List # changeable, 
                myList = ["a", "b", "c"]
                #if u do len(myList) it will be 3.
                
                # methods
                    myList.append("value)
                    mylist.remove()
                    mylist.insert(index, "value")
                    mylist.pop(index) # it remove a value at that index
                    mylist.index("value") # returns the index of that
                        value.
                    mylist.sort() # sorts the list.

        2. Tuple # 1). List # changeable unchange, 
                myTuple = (1, 2, 3)

        3. Dictionary # key = name, value = kazembe
                mydict = {'name' : 'kazembe', 'age' : 20}

                # to access the values
                    print(mydict['name']) # u use a key
                # to add more keys.
                    mydict['gender'] = 'male'

                # Methods
                    mydict.items() # returns all of the pairs
                    mydict.keys() # returns all of the keys
                    mydict.values() # returns all of the values

"""