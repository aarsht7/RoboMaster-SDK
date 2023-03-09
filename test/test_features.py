from robomaster import version
import robomaster
from robomaster import robot

if __name__ == "__main__":
    sdk_version = version.__version__
    print("sdk version:", sdk_version)

    robomaster.enable_logging_to_file()
    robomaster.config.LOCAL_IP_STR = "192.168.2.22"

    ep_robot = robot.Robot()

    # 指定连接方式为AP 直连模式
    ep_robot.initialize(conn_type='ap')

    version = ep_robot.get_version()
    print("Robot version: {0}".format(version))
    ep_robot.close()
