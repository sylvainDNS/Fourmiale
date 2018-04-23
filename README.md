# Fourmiale

> Code available on GitHub : [SylvainDNS/Fourmiale](https://github.com/sylvainDNS/Fourmiale)

School project : find the shortest way to visit all pubs in London using ACO-Pants \
I filter on London's pub due to OOM errors.

## Data structure

I use an array of nodes to represent pubs. Each node is a pub (and an array), defined by 2 coordonates : northing and easting.

```json
node :
    {
        northing,
        easting
    }
```

## Fitness function

I use Pythagoras' theorem to find shortest path between pubs.\
I divide by 1000 to use distance in kilometers.

**_a_** and **_b_** are 2 nodes (=2 pubs)

```python
distance = math.sqrt(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2)) / 1000
```

## Launch

Just type : `python fourmiale.py` or `python3 fourmiale.py` if you use different python version.

![Result on MatPlotLib](img/path.png 'Result on MatPlotLib')
