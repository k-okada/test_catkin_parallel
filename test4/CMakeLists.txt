cmake_minimum_required(VERSION 2.8.3)
project(test4)

find_package(catkin REQUIRED test5 rostest)
catkin_package(CATKIN_DEPENDS test5)

add_rostest(test.test)

install(FILES test.test DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
install(PROGRAMS test.py DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
