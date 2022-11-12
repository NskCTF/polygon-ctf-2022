package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	validator := []int32{8180,
		682,
		8175,
		727,
		8208,
		654,
		8184,
		699,
		8161,
		691,
		8208,
		654,
		8184,
		637,
		8184,
		652,
		8210,
		651,
		8161,
		650,
		8159,
		651,
		8212,
		721}

	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter flag: ")

	text, _ := reader.ReadString('\n')
	if len(text) < 26 {
		println("Bad flag!")
		return
	}
	validFlag := true
	for i, char := range text[:24] {
		if i%2 == 0 {
			if (char ^ 12 + 8101) != validator[i] {
				validFlag = false
				break
			}
		} else {
			if (char ^ 5 + 601) != validator[i] {
				validFlag = false
				break
			}
		}
	}
	if validFlag {
		println("Good flag!")
	} else {
		println("Bad flag!")
	}

}
