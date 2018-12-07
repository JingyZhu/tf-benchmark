"""
Running scripts for dist-tf-ps
"""
from subprocess import call
import sys
import os

index = int(sys.argv[1])
ps = open('setup', 'r').read().split('Worker:\n')[0].split('PS:\n')[1].split('\n')
workers = open('setup', 'r').read().split('Worker:\n')[1].split('\n')

os.environ['CUDA_VISIBLE_DEVICES'] = ''

while ps[-1] == '':
	del ps[-1]
while workers[-1] == '':
	del workers[-1]

print('python sync-dssm-dist.py --ps_hosts={} \
			--worker_hosts={} \
			--num_workers={} --job_name=ps --task_index={} --gpu=False'.format(','.join(ps), ','.join(workers), len(workers), index))
try:
	call('python sync-dssm-dist.py --ps_hosts={} \
			--worker_hosts={} \
			--num_workers={} --job_name=ps --task_index={} --gpu=False'.format(','.join(ps), ','.join(workers), len(workers), index), shell=True, env=os.environ)
except Exception as e:
	print(str(e))