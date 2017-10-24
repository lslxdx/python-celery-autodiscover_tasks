# 1. Start redis server
redis-server

# 2. Enter to the directory
cd /path/to/autodiscover_tasks/

# 3. Run the client
python my_client.py

# 4. Run the worker and interrupt it after a while
celery -A my_worker worker
<Ctrl + C>

# 5. Run the consumer with the task-id printed by the worker previously
python my_consumer.py 38121448-1d17-4b1e-a6ff-0d37bf9664e9
