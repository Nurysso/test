package dummy

import "fmt"

func init() {
	fmt.Println("this is init from dummy bruhhh")
}

// SayHello is exported because it starts with a capital letter.
func SayHello(name string) string {
	return fmt.Sprintf("Yo %s, dummy lib is working!", name)
}
