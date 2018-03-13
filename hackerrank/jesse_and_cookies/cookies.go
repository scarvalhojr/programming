package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"os"
	"strconv"
)

type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func numOperations(cookies []int, minSweet int) (ops int) {
	minheap := &IntHeap{}
	hasSweetCookie := false
	ops = 0

	for _, cookie := range cookies {
		if cookie < minSweet {
			heap.Push(minheap, cookie)
		} else {
			hasSweetCookie = true
		}
	}

	for {
		var cookie1, cookie2, combined int

		if minheap.Len() == 0 {
			break
		}
		cookie1 = heap.Pop(minheap).(int)
		if minheap.Len() == 0 {
			if hasSweetCookie {
				ops++
			} else {
				ops = -1
			}
			break
		}
		cookie2 = heap.Pop(minheap).(int)
		combined = cookie1 + 2*cookie2
		ops++
		if combined >= minSweet {
			hasSweetCookie = true
		} else {
			heap.Push(minheap, combined)
		}
	}
	return
}

func main() {

	var (
		count, minSweet int
		cookies         []int
	)

	if _, err := fmt.Fscanf(os.Stdin, "%d %d\n", &count, &minSweet); err != nil {
		fmt.Println("Invalid input:", err)
		os.Exit(1)
	}
	cookies = make([]int, count)

	scanner := bufio.NewScanner(bufio.NewReader(os.Stdin))
	scanner.Split(bufio.ScanWords)
	for i := 0; i < count && scanner.Scan(); {
		if value, err := strconv.Atoi(scanner.Text()); err != nil {
			fmt.Println("Invalid input:", err)
			os.Exit(1)
		} else {
			cookies[i] = value
			i++
		}
	}

	fmt.Println(numOperations(cookies, minSweet))
}
