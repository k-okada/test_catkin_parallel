cmake_minimum_required(VERSION 2.8.3)
project(test24)

find_package(catkin REQUIRED test25 rostest)
catkin_package(CATKIN_DEPENDS test25)

add_rostest(test.test)

install(FILES test2.test DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
install(PROGRAMS test2.py DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
