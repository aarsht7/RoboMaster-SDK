```
2023-03-02 12:56:01,822 INFO robot.py:1299 Robot: try to connection robot.
2023-03-02 12:56:01,823 INFO conn.py:281 CONN TYPE is ap
2023-03-02 12:56:01,823 INFO conn.py:291 Robot: request_connection, ap get local ip:192.168.2.22
2023-03-02 12:56:01,823 INFO conn.py:322 SdkConnection: request_connection, local addr ('192.168.2.22', 10151), remote_addr ('192.168.2.1', 20020), proxy addr ('192.168.2.1', 30030)
2023-03-02 12:56:06,827 ERROR conn.py:271 SdkConnection: RECV TimeOut!
2023-03-02 12:56:06,827 WARNING conn.py:340 SdkConnection: Connection Failed, please check hareware connections!!!
2023-03-02 12:56:06,827 ERROR robot.py:1354 Robot: Connection Failed, Please Check Hareware Connections!!! conn_type ap, host ('192.168.2.22', 10151), target ('192.168.2.1', 20020).
2023-03-02 12:56:06,827 INFO robot.py:1305 Robot: initialized, try to use default Client.
2023-03-02 12:56:06,827 ERROR client.py:70 Client: __init__, create Connection, exception: module 'robomaster.config' has no attribute 'DEFAULT_CONN_PROTO'
2023-03-02 12:56:06,827 WARNING client.py:105 Client: initialize, no connections, init connections first.
2023-03-02 12:56:06,839 ERROR client.py:153 Client: send_sync_msg, client recv_task is not running.
2023-03-02 12:56:06,839 WARNING robot.py:1453 Robot: enable_sdk error.
2023-03-02 12:56:06,839 INFO dds.py:186 Subscriber: dispatcher_task is running...
2023-03-02 12:56:06,839 INFO uart.py:68 serial: dispatcher_task is running...
2023-03-02 12:56:06,839 ERROR client.py:153 Client: send_sync_msg, client recv_task is not running.
2023-03-02 12:56:06,840 WARNING robot.py:1523 Robot: reset dds node fail!
2023-03-02 12:56:06,840 ERROR client.py:153 Client: send_sync_msg, client recv_task is not running.
2023-03-02 12:56:06,840 WARNING robot.py:1509 Robot: enable_dds err.
2023-03-02 12:56:06,840 ERROR client.py:153 Client: send_sync_msg, client recv_task is not running.
2023-03-02 12:56:06,840 ERROR client.py:153 Client: send_sync_msg, client recv_task is not running.
2023-03-02 12:56:06,840 WARNING vision.py:260 Robot: enable vision failed.
Robot: Can not connect to robot, check connection please.
```