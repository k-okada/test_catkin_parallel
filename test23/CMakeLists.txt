cmake_minimum_required(VERSION 2.8.3)
project(test23)

find_package(catkin REQUIRED rostest)
catkin_package()

add_rostest(test.test)

install(FILES test2.test DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
install(PROGRAMS test2.py DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
