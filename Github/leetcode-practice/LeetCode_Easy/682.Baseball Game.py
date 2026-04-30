class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record =[]
        for i in range(len(operations)):
            if operations[i] == '+':
                num= record[-1]+ record[-2]
                record.append(num)
            elif operations[i] == 'D':
                num = 2* record[-1] 
                record.append(num)
            elif operations[i] == 'C':
                record.pop()
            else:
                record.append(int(operations[i]))
        return sum(record)
        



            

