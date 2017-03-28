//
// Using an implicit treap with an "object-oriented" implementation.
//

package main

import (
	"os"
    "fmt"
    "bufio"
	"strconv"
	"math/rand"
)

const MaxCount = 10000

type ImplicitTreap struct {
	value int
	priority int
	size int
	left *ImplicitTreap
	right *ImplicitTreap
}

func NewNode(value int) *ImplicitTreap {
	rnd := rand.Intn(10 * MaxCount)
	return &ImplicitTreap{value: value, priority: rnd, size: 1}
}

func (node *ImplicitTreap) UpdateSize() {
	node.size = 1
	if node.left != nil {
		node.size += node.left.size
	}
	if node.right != nil {
		node.size += node.right.size
	}
}

func (node *ImplicitTreap) MergeRight(other *ImplicitTreap) *ImplicitTreap {

	var root *ImplicitTreap

	if other == nil {
		return node
	}

	if node.priority > other.priority {
		if node.right != nil {
			node.right = node.right.MergeRight(other)
		} else {
			node.right = other
		}
		root = node
	} else {
		if other.left != nil {
			other.left = node.MergeRight(other.left)
		} else {
			other.left = node
		}
		root = other
	}

	root.UpdateSize()

	return root
}

func scanInt(scanner *bufio.Scanner) int {
	scanner.Scan()
	val, err := strconv.Atoi(scanner.Text())
	if err != nil {
		fmt.Println("Invalid input.")
		os.Exit(1)
	}
	return val
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Split(bufio.ScanWords)

	length := scanInt(scanner)
	queries := scanInt(scanner)

	root := NewNode(scanInt(scanner))

	for i := 1; i < length; i++ {
		root = root.MergeRight(NewNode(scanInt(scanner)))
	}

	var oper, pos_i, pos_j int
	for i := 0; i < queries; i++ {
		oper = scanInt(scanner)
		pos_i = scanInt(scanner)
		pos_j = scanInt(scanner)

		if pos_i < 1 || pos_i > length || pos_j < 1 || pos_j > length || pos_j < pos_i {
			fmt.Printf("Invalid array positions: '%d, %d'.\n", pos_i, pos_j)
			os.Exit(1)
		}

		switch oper {
		case 1:
			if pos_i > 1 {
			}
		case 2:
			if pos_j < length {
			}
		default:
			fmt.Printf("Invalid query type: '%d'.\n", oper)
			os.Exit(1)
		}
	}

	//diff := 0
	//if diff < 0 {
	//	diff = -diff
	//}

	// fmt.Printf("%d\n%d", diff, numbers[0])
	// for i := 1; i < length; i++ {
	// 	fmt.Printf(" %d", numbers[i])
	// }
	// fmt.Printf("\n")
}
