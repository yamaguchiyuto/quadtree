## Quadtree
https://en.wikipedia.org/wiki/Quadtree

## Usage


```
$ python quadtree.py
[USAGE]: python quadtree.py [x left] [y up] [x right] [y down] [maxpoints] [maxdivision] [data filepath]
```

Divide the specified rectangle area into four areas recursively until
1. the number of points in every area is smaller than `maxpoints`, or
2. the depth of the quadtree is equal to `maxdivition`.

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

$ python quadtree.py 0 0 1 1 3 3 sample_data
AreaID,x_left,y_up,x_right,y_down,x_center,y_center
0,0.0,0.0,0.25,0.25,0.125,0.125
1,0.0,0.25,0.25,0.5,0.125,0.375
2,0.25,0.0,0.5,0.25,0.375,0.125
3,0.25,0.25,0.375,0.375,0.348346109137,0.312959224746
4,0.25,0.375,0.375,0.5,0.271957975882,0.450460115198
5,0.375,0.25,0.5,0.375,0.467182120645,0.271196310881
6,0.375,0.375,0.5,0.5,0.414730976498,0.417927105276
7,0.0,0.5,0.25,0.75,0.125,0.625
8,0.0,0.75,0.25,1.0,0.125,0.875
9,0.25,0.5,0.375,0.625,0.350508452053,0.566236807663
10,0.25,0.625,0.375,0.75,0.3125,0.6875
11,0.375,0.5,0.5,0.625,0.427520154678,0.5665272218
12,0.375,0.625,0.5,0.75,0.4375,0.6875
13,0.25,0.75,0.5,1.0,0.375,0.875
14,0.5,0.0,0.75,0.25,0.625,0.125
15,0.5,0.25,0.625,0.375,0.500192599714,0.352420542886
16,0.5,0.375,0.625,0.5,0.565050699943,0.443223849604
17,0.625,0.25,0.75,0.375,0.6875,0.3125
18,0.625,0.375,0.75,0.5,0.627069208861,0.409651503748
19,0.75,0.0,1.0,0.25,0.875,0.125
20,0.75,0.25,1.0,0.5,0.875,0.375
21,0.5,0.5,0.625,0.625,0.529449324271,0.564774334037
22,0.5,0.625,0.625,0.75,0.575245056089,0.66595430217
23,0.625,0.5,0.75,0.625,0.644625936719,0.542486338813
24,0.625,0.625,0.75,0.75,0.6875,0.6875
25,0.5,0.75,0.75,1.0,0.625,0.875
26,0.75,0.5,1.0,0.75,0.875,0.625
27,0.75,0.75,1.0,1.0,0.875,0.875

Query: (0.37,0.55)
Returned Area ID: 9
```