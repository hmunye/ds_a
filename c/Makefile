.PHONY: build build-dbg exec exec-dbg clean clean-dbg run run-dbg

build:
	gcc -Wall -Wextra -o main $(FILE)

build-dbg:
	gcc -g -Wall -Wextra -o main-dbg $(FILE)

exec:
	./main

exec-dbg:
	./main-dbg

clean:
	@rm -rf ./main

clean-dbg:
	@rm -rf ./main-dbg

run: build exec clean
run-dbg: build-dbg exec-dbg clean-dbg
