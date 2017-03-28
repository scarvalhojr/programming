//
// Pure brute force, copying array slices.
//

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func scanInt(scanner *bufio.Scanner, desc string) int {
	scanner.Scan()
	input := scanner.Text()
	val, err := strconv.Atoi(input)
	if err != nil {
		fmt.Printf("Invalid input for %s: '%s'.\n", desc, input)
		os.Exit(1)
	}
	return val
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Split(bufio.ScanWords)

	length := scanInt(scanner, "N")
	queries := scanInt(scanner, "M")

	numbers := make([]int, length)
	for i := 0; i < length; i++ {
		numbers[i] = scanInt(scanner, "array element")
	}

	buffer := make([]int, length)

	var oper, pos_i, pos_j, count int
	for i := 0; i < queries; i++ {
		oper = scanInt(scanner, "query type")
		pos_i = scanInt(scanner, "array position")
		pos_j = scanInt(scanner, "array position")

		if pos_i < 1 || pos_i > length || pos_j < 1 || pos_j > length || pos_j < pos_i {
			fmt.Printf("Invalid input for array positions: '%d, %d'.\n", pos_i, pos_j)
			os.Exit(1)
		}

		count = pos_j - pos_i + 1

		// map to zero-based indices
		pos_i -= 1
		pos_j -= 1

		switch oper {
		case 1:
			if pos_i > 0 {
				copy(buffer, numbers[:pos_i])
				copy(numbers, numbers[pos_i:pos_j+1])
				copy(numbers[count:], buffer[:pos_i])
			}
		case 2:
			if pos_j < length-1 {
				copy(buffer, numbers[pos_i:pos_j+1])
				copy(numbers[pos_i:], numbers[pos_j+1:])
				copy(numbers[length-count:], buffer[:count])
			}
		default:
			fmt.Printf("Invalid input for query type: '%d'.\n", oper)
			os.Exit(1)

		}
	}

	diff := numbers[length-1] - numbers[0]
	if diff < 0 {
		diff = -diff
	}

	fmt.Printf("%d\n%d", diff, numbers[0])
	for i := 1; i < length; i++ {
		fmt.Printf(" %d", numbers[i])
	}
	fmt.Printf("\n")
}
