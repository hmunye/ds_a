.PHONY: build build-dbg exec clean clean-dbg run

build:
	gcc -Wall -Wextra -o main $(FILE)

build-dbg:
	gcc -g -Wall -Wextra -o main-dbg $(FILE)

exec:
	./main

clean:
	@rm -rf ./main

clean-dbg:
	@rm -rf ./main-dbg

run: build exec clean
