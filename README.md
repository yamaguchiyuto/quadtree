## Quadtree
https://en.wikipedia.org/wiki/Quadtree

## Usage


```
$ python quadtree.py
[USAGE]: python quadtree.py [x left] [y up] [x right] [y down] [maxpoints] [maxdivision] [data filepath]
```

Divide the specified rectangle area into four areas recursively until

1. the number of points in every area is smaller than `maxpoints`, or
2. the depth of the quadtree is equal to `maxdivition-1`.

### Sample data

```
$ cat sample_data
0.567603099626 0.410160220857
0.405568042222 0.555583016695
0.450289054963 0.252870772505
0.373657009068 0.549501477427
0.500192599714 0.352420542886
0.626796922 0.422685113179
0.527521290061 0.483502904656
0.407737520746 0.570049935936
0.578095278433 0.6959689898
0.271957975882 0.450460115198
0.56451369371 0.491139311353
0.532304354436 0.486931064003
0.553942716039 0.51953331907
0.627341495722 0.396617894317
0.454210189397 0.570214499065
0.327359895038 0.582972137899
0.422271372537 0.560892624101
0.443036148978 0.434529240506
0.644625936719 0.542486338813
0.447813648487 0.575896033203
0.534217713171 0.636123087401
0.348346109137 0.312959224746
0.484075186327 0.289521849258
0.588417643962 0.387831556678
0.613422176662 0.665770829308
0.60994411786 0.399778040078
0.425443751505 0.402619561402
0.504955932504 0.610015349003
0.402852203978 0.382379275531
0.387591801531 0.452180343665
```
