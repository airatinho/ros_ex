import rospy
import rostest
import unittest
from  src.counter.src import main
import random
from std_msgs.msg import Int64
from time import sleep

class Data:
    def __init__(self,data):
        self.data=data


class TestCase(unittest.TestCase):
    talker_status=False
    def clbk(self,data):
        """change status"""
        self.talker_status=True

    def test_publishing(self):
        """Test publishing"""
        rospy.init_node('test_pub')
        rospy.Subscriber('total',Int64,callback=self.clbk)
        counter=0
        while not rospy.is_shutdown() and (counter<3) and (not self.talker_status):
            sleep(1)
            counter+=1
        self.assertTrue(self.talker_status)

    def test_val(self):
        """Test data values"""
        random_val=random.randrange(2**63)
        data=Data(random_val)
        test_data=data.data
        test_result=main.current_val+test_data
        main.callback(data)
        self.assertEqual(
            main.current_val,test_result,
            msg=f"Value {main.current_val} is not equal {test_result}"
        )

    def test_type(self):
        """Test type of data"""
        random_val=random.randrange(2**63)
        data=Data(random_val)
        test_data=data.data
        self.assertEqual(
            type(main.current_val),type(data.data),
            msg=f"Type {type(main.current_val)} is type(data.data)"

        )
        test_result=main.current_val+test_data
        main.callback(data)
        self.assertEqual(
            type(main.current_val) , type(test_result),
            msg=f"Type {type(main.current_val)} is not equal "
                f"{type(test_result)} "
        )

    def test_pep(self):
        self.assertEqual(True,bool(main.talker.__doc__))
        self.assertEqual(True, bool(main.callback.__doc__))
        self.assertEqual(True, bool(main.listener.__doc__))
        self.assertEqual(True,bool(main.talker.__annotations__))
        self.assertEqual(True,bool(main.callback.__annotations__))
        self.assertEqual(True, bool(main.listener.__annotations__))
if __name__=="__main__":
    rostest.rosrun('counter','test_code',TestCase)