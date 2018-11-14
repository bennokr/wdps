ES_PORT=9200
ES_BIN=/home/bbkruit/scratch/wdps/elasticsearch-2.4.1/bin/elasticsearch
prun -o .es_log -v -np 1 ESPORT=$ES_PORT $ES_BIN </dev/null 2> .es_node &
ES_NODE=$(cat .es_node | grep -oP '(node...)')
ES_PID=$!

source venv/bin/activate
python3 kb.py $ES_NODE:$ES_PORT "Vrije Universiteit Amsterdam"
deactivate

kill $ES_PID
