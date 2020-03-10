# cybertech
## 이것은 cybertech 동계방학 인턴동안 진행한 내용을 담은 것입니다.

0. 이것은 OpenCV를 이용해 물건을 감지하는 것과 Open manipulator-X를 특정 좌표로 이동시키기 위한 코드를 담고 있습니다.
1. opencv_node_detection 폴더 안에는 세 개의 파이썬 파일이 존재합니다.
2. 'color_node_detection.py'는 파란색을 물체를 감지해 중심값을 산출하는 코드입니다.
3. 'trans_detection_txt.py'는 투명한 물체를 감지해 중심값을 산출하는 코드입니다. 그리고 결과값을 텍스트파일로 만듭니다.
4. 'trans_detection_mqtt.py'는 투명한 물체를 감지해 중심값을 산출하는 코드와 mqtt를 연계시킨 코드입니다.

5. topic_manipulator 폴더 안에는 두 개의 파일이 패키지가 존재하며 이들 패키지는 catkin_ws/src 내부에 위치해야 실행됩니다.
6. ex_topic 패키지는 파이썬을 이용해 매니퓰레이터를 제어하는 노드입니다. 2개의 토픽을 사용합니다.
7. second_topic 패키지는 C++ 을 이용해 매니퓰레이터를 제어하는 노드입니다. 2개의 토픽을 사용합니다.
8. 위의 코드들(5~7)을 사용하기 위해서는 modified_teleop 패키지가 필요합니다.
