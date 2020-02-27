#include <ros/ros.h>
#include <geometry_msgs/Pose.h>
#include <unistd.h>
#include <std_msgs/Float64.h>

int main(int argc, char** argv) {

    ros::init(argc, argv, "second_robot_node");
    ros::NodeHandle nh1;
    ros::NodeHandle nh2;
    
    ros::Publisher pub_arm = nh1.advertise<geometry_msgs::Pose>("/open_manipulator/input_kinematics_pose", 1000);
    ros::Publisher pub_gripper = nh2.advertise<std_msgs::Float64>("/open_manipulator/input_gripper_angle", 1000);

    /*ros::Rate loop_rate(2);*/
    ros::Rate loop_rate(4); // initialize rate of message transmission(topic)
    
    geometry_msgs::Pose up;

    up.orientation.w = 0;
    up.orientation.x = 0;
    up.orientation.y = 0;
    up.orientation.z = 1;
    up.position.x = 0.2;
    up.position.y = 0.0;
    up.position.z = 0.25;

    geometry_msgs::Pose down;

    down.orientation.w = 0;
    down.orientation.x = 0;
    down.orientation.y = 0;
    down.orientation.z = 1;
    down.position.x = 0.2;
    down.position.y = -0.2;
    down.position.z = 0.05;

    /*
    geometry_msgs::Pose obstacle_position;

    down.orientation.w = 0;
    down.orientation.x = 0;
    down.orientation.y = 0;
    down.orientation.z = 1;
    down.position.x = 0.2;
    down.position.y = 0.1;
    down.position.z = 0.04;

    geometry_msgs::Pose init_pose;

    down.orientation.w = 0;
    down.orientation.x = 0;
    down.orientation.y = 0;
    down.orientation.z = 1;
    down.position.x = 0.15;
    down.position.y = 0.0;
    down.position.z = 0.02;

    */
    std_msgs::Float64 open;

    open.data = 0.01;

    std_msgs::Float64 close;

    close.data = -0.01;

    sleep(2.5); // time for making message

    pub_arm.publish(down);
    sleep(2.5); //time used(when moving)
    pub_gripper.publish(open);
    sleep(2.5);
    pub_gripper.publish(close);
    sleep(2.5);

    //okay

    pub_arm.publish(up);
    sleep(2.5);

    
    /*
    pub_gripper.publish(open);
    sleep(2.5);
    pub_gripper.publish(close);
    sleep(2.5);
    pub_arm.publish(down);
    sleep(2.5);
    pub_arm.publish(up);
    sleep(2.5);
    */


    /*basic code for routine(once/fixed)
    sleep(2.5); // time for making message?

    pub.publish(down);
    sleep(2.5); //time used(when moving)
    pub.publish(up);
    sleep(2.5);
    */


    /*basic code for routine(once)
    //ros::spinOnce(); //not need
    loop_rate.sleep(); //must need : why?? -maybe need for sleep
    pub.publish(down);

    sleep(2.5); //time used(when moving)
 
    pub.publish(up);

    sleep(2.5);

    */


    //basic code for routine(iteration)
    /*
    while (ros::ok)
    {
        pub.publish(up);

        ros::spinOnce();

        loop_rate.sleep();

        pub.publish(down);

        ros::spinOnce();

        loop_rate.sleep();
    }
    */
    

    //basic code for only one command(official/roboignite)
    /*
    while (ros::ok())
    {
        pub.publish(up);

        ros::spinOnce();
        loop_rate.sleep();
    }
    */
   

    return 0;
}


