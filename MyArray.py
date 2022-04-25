class MyArray():
    def __init__(self, array):
        if array != [] and all(isinstance(l, list) for l in array):
            length = len(array[0])
            for l in array:
                if not all(isinstance(n, int) for n in l):
                    raise ValueError("incorrect arguments")
                else: 
                    count = 0
                    for n in l:
                        count += 1
                    if count != length:
                        raise ValueError("incorrect arguments")       
            self.type = "2D"
        elif all(isinstance(n, int) for n in array):
            self.type = "1D"
        else:
            raise ValueError("incorrect arguments")
        self.array = array
         
    def min(self, **kwargs):
        if "axis" in kwargs:
            theAxis = kwargs["axis"]
            if theAxis == 0:
                if self.type == "2D":
                    minList = []
                    for x in range(len(self.array[0])):
                        testList = []
                        for l in self.array:
                            t = l[x]
                            testList.append(t)
                        m = min(testList)
                        minList.append(m)
                    return minList
                else:
                    return self.array
                            
            elif theAxis == 1:
                if self.type == "2D":
                    minList = []
                    for l in self.array:
                        m = min(l)
                        minList.append(m)
                    return minList
                else:
                    return min(self.array)
            else:
                print("ERROR: incorrect arguments")
        else:
            if self.type == "2D":
                minList = []
                for l in self.array:
                    m = min(l)
                    minList.append(m)
                return min(minList)
            else:
                return min(self.array)
            
            
    def max(self, **kwargs):
        if "axis" in kwargs:
            theAxis = kwargs["axis"]
            if theAxis == 0:
                if self.type == "2D":
                    maxList = []
                    testList = []
                    for x in range(len(self.array[0])):
                        testList = []
                        for l in self.array:
                            t = l[x]
                            testList.append(t)
                        m = max(testList)
                        maxList.append(m)
                    return maxList
                else:
                    return self.array
                            
            elif theAxis == 1:
                if self.type == "2D":
                    maxList = []
                    for l in self.array:
                        m = max(l)
                        maxList.append(m)
                    return maxList
                else:
                    return max(self.array)
            else:
                print("ERROR: incorrect arguments")
        else:
            if self.type == "2D":
                maxList = []
                for l in self.array:
                    m = max(l)
                    maxList.append(m)
                return max(maxList)
            else:
                return max(self.array)
            
    def mean(self, **kwargs):
        if "axis" in kwargs:
            theAxis = kwargs["axis"]
            if theAxis == 0:
                if self.type == "2D":
                    meanList = []
                    testList = []
                    for x in range(len(self.array[0])):
                        testList = []
                        for l in self.array:
                            t = l[x]
                            testList.append(t)
                        m = sum(testList) / len(testList)
                        meanList.append(m)
                    return meanList
                else:
                    return self.array
                            
            elif theAxis == 1:
                if self.type == "2D":
                    meanList = []
                    for l in self.array:
                        m = sum(l) / len(l)
                        meanList.append(m)
                    return meanList
                else:
                    return (sum(self.array) / len(self.array))
            else:
                print("ERROR: incorrect arguments")
        else:
            if self.type == "2D":
                meanList = []
                for l in self.array:
                    m = sum(l) / len(l)
                    meanList.append(m)
                return (sum(meanList) / len(meanList))
            else:
                return (sum(self.array) / len(self.array))
    
    def copy(self): 
        new = []
        if self.type == "2D":
            for x in self.array:
                lst = []
                for y in x:
                    lst.append(y)
                new.append(lst)
        else:
            for x in self.array: 
                new.append(x)
        return MyArray(new)

   
    @classmethod
    def zeros(cls, *args):
        a = []
        if len(args) == 2:
            for r in range(args[0]):
                row = []
                for c in range(args[1]):
                    row.append(0)
                a.append(row)
        elif len(args) == 1:
            for c in range(args[0]):
                a.append(0)
        else:
            raise ValueError("incorrect arguments")
        return cls(a)
    
    def __getitem__(self, index):
        if self.type == "2D":
            try:
                return self.array[index[0]][index[1]]
            except TypeError:
                print("ERROR: incorrect arguments")
        else:
            try:
                return self.array[index]
            except TypeError:
                print("ERROR: incorrect arguments")
    
    def __setitem__(self, index, new):
        if self.type == "2D":
            try:
                self.array[index[0]][index[1]] = new
            except TypeError:
                print("ERROR: incorrect arguments")
        else:
            try:
                self.array[index] = new 
            except TypeError:
                print("ERROR: incorrect arguments")
    
    def __repr__(self):
        p = ""
        if self.type == "1D":
            p += "| "
            for n in self.array:
                p += (str(n) + " ")
            p += "|"
        else:
            for l in self.array:
                p += "| "
                for n in l:
                    p += (str(n) + " ")
                p += "| \n"
        return p