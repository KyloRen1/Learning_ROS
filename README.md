# ROS/ROS2 Learning Repository

Hello! This is the repository where I am learning ROS/ROS2.

P.S.: I am using MacOS, which adds a bit of complexity to installing ROS. Therefore, I've created a `docker-compose` setup that simplifies the process. The current `src` folder is mapped to the home directory within the ROS Docker container, making it easy to write code in the code editor of your choice.

</br>

## Getting started
1. Starting the container
```python
docker-compose up -d
docker exec -it ros2 /ros_entrypoint.sh bash 
```

2. Run testing case, to check that ros2 is available

```python
ros2 run demo_nodes_cpp talker
```
3. To view ui go to `http://localhost:8080/vnc.html`


------ 
## ROS functionality 

- __Creating a Node__: Update the src folder with your node and run the following commands within the ROS Docker container. This will update the build, install, and log folders with the current node build.

    ```python
    colcon build --symlink-install

    # after node is created update the source
    source install/setup.sh
    ```