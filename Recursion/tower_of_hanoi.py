def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n-1, source, target, auxiliary)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n-1, auxiliary, source, target)

def towers_of_hanoi2(n, source, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    other = 6 - (source + target)
    towers_of_hanoi2(n-1, source, other)
    print(f"Move disk {n} from {source} to {target}")
    towers_of_hanoi2(n-1, other, target)



if __name__ == "__main__":
    n = 3 # int(input("Enter the number of disks: "))
    tower_of_hanoi(n, 'A', 'B', 'C')
    print("===============")
    towers_of_hanoi2(n, 1, 3)  # Assuming pegs are labeled as 1, 2, 3
