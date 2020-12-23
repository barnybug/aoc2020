package main

import "fmt"

const n = 1000000
const times = 10000000

func main() {
	data := []int{2, 5, 3, 1, 4, 9, 8, 6, 7}
	datalen := len(data)
	nodes := make([]int, n+1)
	for i := 0; i < n; i++ {
		a := i + 1
		if i < datalen {
			a = data[i]
		}
		b := i + 2
		if (i+1)%n < datalen {
			b = data[(i+1)%n]
		}
		nodes[a] = b
	}
	current := data[0]
	for i := 0; i < times; i++ {
		a := nodes[current]
		b := nodes[a]
		c := nodes[b]
		nodes[current] = nodes[c]
		destination := current
		for {
			destination--
			if destination < 1 {
				destination = n
			}
			if destination != a && destination != b && destination != c {
				break
			}
		}

		nodes[c] = nodes[destination]
		nodes[destination] = a
		current = nodes[current]
	}

	answer := nodes[1] * nodes[nodes[1]]
	fmt.Println(answer)
}
