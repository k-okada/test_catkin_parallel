cmake_minimum_required(VERSION 2.8.3)
project(test99)

find_package(catkin REQUIRED rostest)
catkin_package()

add_rostest(test.test)

install(FILES test.test DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
install(PROGRAMS test.py DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
