package main

import (
	"fmt"
	"os"
)

func init() {
	fmt.Println("this is init bruhhh")
}

func main() {
	file, _ := os.Open("test")
	if file != nil {
		fmt.Println("file exists")
	} else {
		fmt.Println("file no exists")
	}
}
