# dssm on Tensorflow

Document at http://liaha.github.io/models/2016/06/21/dssm-on-tensorflow.html

Please refer to https://www.microsoft.com/en-us/research/project/dssm/ for more information.

# Notice
Thank everyone for your attention on this project. Two important things that we want to clarify:
- This is not the official repository of DSSM project. 
- ~~We are not authorized to provide any training or test data that belongs to original authors.~~
- To generate fake data (only used for benchmarks). Run:
```sh
    cd data
    python3 fake_data.py
```
- To run distributed version:
    - Config the servers and workers ```ip:port``` in ```dist/setup```
    - Run: 
```sh
    cd dist
    # Run on each PS
    python3 ps.py <ps_id>
    # Run on each worker
    python3 worker.py <worker_id>
```

~~Sorry for any inconveniences caused.~~
