cmake_minimum_required(VERSION 2.8.3)
project(test11)

find_package(catkin REQUIRED test12 test13 rostest)
catkin_package(CATKIN_DEPENDS test12 test13)

add_rostest(test.test)

install(FILES test1.test DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
install(PROGRAMS test1.py DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
