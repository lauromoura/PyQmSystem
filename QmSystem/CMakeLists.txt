project(qmsystem)

set(QmSystem_SRCS
    ${CMAKE_CURRENT_BINARY_DIR}/QmSystem/qmsystem_module_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/QmSystem/meego_qmaccelerometer_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/QmSystem/meego_qmaccelerometerreading_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/QmSystem/meego_qmactivity_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/QmSystem/meego_qmals_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/QmSystem/meego_qmbattery_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/QmSystem/meego_qmcabc_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/QmSystem/meego_qmcallstate_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/QmSystem/meego_qmcompass_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/QmSystem/meego_qmcompassreading_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/QmSystem/meego_qmdevicemode_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/QmSystem/meego_qmdisplaystate_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/QmSystem/meego_qmheartbeat_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/QmSystem/meego_qmkeys_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/QmSystem/meego_qmled_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/QmSystem/meego_qmlocks_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/QmSystem/meego_qmmagnetometer_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/QmSystem/meego_qmmagnetometerreading_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/QmSystem/meego_qmorientation_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/QmSystem/meego_qmorientationreading_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/QmSystem/meego_qmproximity_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/QmSystem/meego_qmrotation_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/QmSystem/meego_qmrotationreading_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/QmSystem/meego_qmsensor_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/QmSystem/meego_qmsensorreading_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/QmSystem/meego_qmintreading_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/QmSystem/meego_qmsysteminformation_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/QmSystem/meego_qmsystemstate_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/QmSystem/meego_qmtap_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/QmSystem/meego_qmtapreading_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/QmSystem/meego_qmthermal_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/QmSystem/meego_qmtime_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/QmSystem/meego_qmusbmode_wrapper.cpp
    ${CMAKE_CURRENT_BINARY_DIR}/QmSystem/meego_qmprocesswatchdog_wrapper.cpp
    )

set(QmSystem_INCLUDE_DIRS
    ${QMSYSTEM_INCLUDE_DIRS}
    ${PYTHON_INCLUDE_DIRS}
    ${SHIBOKEN_INCLUDE_DIR}
    ${PYSIDE_INCLUDE_DIR}
    ${PYSIDE_INCLUDE_DIR}/QtCore
    )

set(QmSystem_LIBRARY_DIRS
    ${QMSYSTEM_LIBRARY_DIRS}
    ${PYSIDE_LIBRARY_DIR}
    ${SHIBOKEN_LIBRARY_DIR}
)
string(REGEX REPLACE ";" ":" QmSystem_INCLUDE_DIRS_COLON "${QmSystem_INCLUDE_DIRS}")

link_directories(${QmSystem_LIBRARY_DIRS})
include_directories(QmSystem ${QmSystem_INCLUDE_DIRS})
add_library(QmSystem MODULE ${QmSystem_SRCS})
set_property(TARGET QmSystem PROPERTY PREFIX "")
target_link_libraries(QmSystem
    ${PYTHON_LIBRARIES}
    ${SHIBOKEN_LIBRARY}
    ${PYSIDE_LIBRARY}
    ${QT_QTCORE_LIBRARY}
    ${QMSYSTEM_LIBRARIES}
)

add_custom_command(OUTPUT ${QmSystem_SRCS}
                   COMMAND ${GENERATOR} ${GENERATOR_EXTRA_FLAGS}
                   ${CMAKE_SOURCE_DIR}/${BINDING_NAME}/global.h
                   --include-paths=${QmSystem_INCLUDE_DIRS_COLON}
                   --typesystem-paths=${CMAKE_CURRENT_SOURCE_DIR}:${PYSIDE_TYPESYSTEMS}
                   --output-directory=${CMAKE_CURRENT_BINARY_DIR}
                   --license-file=${CMAKE_CURRENT_SOURCE_DIR}/../licensecomment.txt
                   ${CMAKE_CURRENT_SOURCE_DIR}/typesystem_qmsystem.xml
                   --api-version=${BINDING_API_MAJOR_VERSION}.${BINDING_API_MINOR_VERSION}
                   WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
                   COMMENT "Running generator for QmSystem..."
                   )


install(FILES ${CMAKE_CURRENT_BINARY_DIR}/${BINDING_NAME}${CMAKE_DEBUG_POSTFIX}.so DESTINATION "${SITE_PACKAGE}")
