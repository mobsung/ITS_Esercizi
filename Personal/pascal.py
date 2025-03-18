


def generate(numRows: int) -> list[list[int]]:
        
        
        result: list = [[1],[1,1],[1,2,1]]
        cicle = 0

        if numRows == 1:
            return [result[0]]
        elif numRows == 2:
            return [result[0],result[1]]
        else:
            cicle = 4
            while cicle <= numRows:
                row: list = result[-1]
                temp_row = []            
                for i in range(len(row) - 1):
                    temp_row.append(row[i] + row[i + 1])
                temp_row.append(1)
                temp_row.reverse()
                temp_row.append(1)
                temp_row.reverse()
                result.append(temp_row)
                cicle += 1
            return result
                  
        

print(generate(6))



#result[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]

