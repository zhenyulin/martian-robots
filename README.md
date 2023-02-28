## Martian-Robots

Send a list of robots to explore Mars (a 2D surface)

### Inspect

```shell
make install # you will need poetry to set up the test environment
make test

# or if you have pytest already
pytest . -vv -s
```

### Possible Improvements

* More efficient parser since the number of robots isn't capped
* Can be set up as an API or put in a notebook for interaction
