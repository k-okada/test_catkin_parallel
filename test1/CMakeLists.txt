cmake_minimum_required(VERSION 2.8.3)
project(test1)

find_package(catkin REQUIRED test2 test3 rostest)
catkin_package(CATKIN_DEPENDS test2 test3)

add_rostest(test.test)

install(FILES test.test DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
install(PROGRAMS test.py DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
