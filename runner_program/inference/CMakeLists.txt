cmake_minimum_required(VERSION 3.22)
project(point-one-robot-car-inference)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(depthai_DIR depthai-core/build)
find_package(depthai CONFIG REQUIRED)

include_directories(include)
include_directories(depthai-core/include/depthai)

################ Inference ################

set(libName robot_car_inference.so)

add_library(
        ${libName}
        SHARED
        src/setup_camera.cpp
)

target_link_libraries(${libName} PRIVATE depthai::core depthai::depthai-resources depthai::opencv)

set_target_properties(
        ${libName} PROPERTIES COMPILE_FLAGS "-Wall -Wextra -Wpedantic"
)

################ Executable for tests ################

set(executable
        inference_test
)

set(SRCS
        src/main.cpp
        src/setup_camera.cpp

)

add_executable(${executable} ${SRCS})

find_library(ROBOT_CAR_INFERENCE ${libName} PATHS .)

target_link_libraries(${executable} PRIVATE ${libName})

set_target_properties(
        ${executable} PROPERTIES COMPILE_FLAGS "-Wall -Wextra -Wpedantic"
)

set_target_properties(${executable} PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/..
)

################ Unit_tests ################

set(TEST
        unit_tests
)

set(SRCS_TEST
    tests/unit_tests.cpp
)

add_executable(${TEST} ${SRCS_TEST})

set_target_properties(
        ${TEST} PROPERTIES LINK_FLAGS "-lcriterion -lgcov -fprofile-generate"
)

set_target_properties(
        ${TEST} PROPERTIES COMPILE_FLAGS "--coverage -fprofile-arcs -ftest-coverage"
)