def get_pascals_triangle_row(row_number: int) -> list:
    row = [1]
    for _ in range(row_number):
        row = [1] + [row[i] + row[i+1] for i in range(len(row)-1)] + [1]
    return row

def debug(x):
    row = [1]
    for i in range(2-1):
        print(i)

if __name__ == "__main__":
    #debug(3)
    for r in range(5):
        print(r)
        print(get_pascals_triangle_row(r))
