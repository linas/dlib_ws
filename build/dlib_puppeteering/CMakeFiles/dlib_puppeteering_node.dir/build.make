# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/meareg/dlib_ws/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/meareg/dlib_ws/build

# Include any dependencies generated for this target.
include dlib_puppeteering/CMakeFiles/dlib_puppeteering_node.dir/depend.make

# Include the progress variables for this target.
include dlib_puppeteering/CMakeFiles/dlib_puppeteering_node.dir/progress.make

# Include the compile flags for this target's objects.
include dlib_puppeteering/CMakeFiles/dlib_puppeteering_node.dir/flags.make

dlib_puppeteering/CMakeFiles/dlib_puppeteering_node.dir/src/dlib_facenew.cpp.o: dlib_puppeteering/CMakeFiles/dlib_puppeteering_node.dir/flags.make
dlib_puppeteering/CMakeFiles/dlib_puppeteering_node.dir/src/dlib_facenew.cpp.o: /home/meareg/dlib_ws/src/dlib_puppeteering/src/dlib_facenew.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /home/meareg/dlib_ws/build/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object dlib_puppeteering/CMakeFiles/dlib_puppeteering_node.dir/src/dlib_facenew.cpp.o"
	cd /home/meareg/dlib_ws/build/dlib_puppeteering && /usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/dlib_puppeteering_node.dir/src/dlib_facenew.cpp.o -c /home/meareg/dlib_ws/src/dlib_puppeteering/src/dlib_facenew.cpp

dlib_puppeteering/CMakeFiles/dlib_puppeteering_node.dir/src/dlib_facenew.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/dlib_puppeteering_node.dir/src/dlib_facenew.cpp.i"
	cd /home/meareg/dlib_ws/build/dlib_puppeteering && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/meareg/dlib_ws/src/dlib_puppeteering/src/dlib_facenew.cpp > CMakeFiles/dlib_puppeteering_node.dir/src/dlib_facenew.cpp.i

dlib_puppeteering/CMakeFiles/dlib_puppeteering_node.dir/src/dlib_facenew.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/dlib_puppeteering_node.dir/src/dlib_facenew.cpp.s"
	cd /home/meareg/dlib_ws/build/dlib_puppeteering && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/meareg/dlib_ws/src/dlib_puppeteering/src/dlib_facenew.cpp -o CMakeFiles/dlib_puppeteering_node.dir/src/dlib_facenew.cpp.s

dlib_puppeteering/CMakeFiles/dlib_puppeteering_node.dir/src/dlib_facenew.cpp.o.requires:
.PHONY : dlib_puppeteering/CMakeFiles/dlib_puppeteering_node.dir/src/dlib_facenew.cpp.o.requires

dlib_puppeteering/CMakeFiles/dlib_puppeteering_node.dir/src/dlib_facenew.cpp.o.provides: dlib_puppeteering/CMakeFiles/dlib_puppeteering_node.dir/src/dlib_facenew.cpp.o.requires
	$(MAKE) -f dlib_puppeteering/CMakeFiles/dlib_puppeteering_node.dir/build.make dlib_puppeteering/CMakeFiles/dlib_puppeteering_node.dir/src/dlib_facenew.cpp.o.provides.build
.PHONY : dlib_puppeteering/CMakeFiles/dlib_puppeteering_node.dir/src/dlib_facenew.cpp.o.provides

dlib_puppeteering/CMakeFiles/dlib_puppeteering_node.dir/src/dlib_facenew.cpp.o.provides.build: dlib_puppeteering/CMakeFiles/dlib_puppeteering_node.dir/src/dlib_facenew.cpp.o

# Object files for target dlib_puppeteering_node
dlib_puppeteering_node_OBJECTS = \
"CMakeFiles/dlib_puppeteering_node.dir/src/dlib_facenew.cpp.o"

# External object files for target dlib_puppeteering_node
dlib_puppeteering_node_EXTERNAL_OBJECTS =

/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: dlib_puppeteering/CMakeFiles/dlib_puppeteering_node.dir/src/dlib_facenew.cpp.o
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: dlib_puppeteering/CMakeFiles/dlib_puppeteering_node.dir/build.make
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /opt/ros/indigo/lib/libdynamic_reconfigure_config_init_mutex.so
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /opt/ros/indigo/lib/libcv_bridge.so
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libopencv_videostab.so.2.4.8
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libopencv_video.so.2.4.8
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libopencv_superres.so.2.4.8
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libopencv_stitching.so.2.4.8
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libopencv_photo.so.2.4.8
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libopencv_ocl.so.2.4.8
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libopencv_objdetect.so.2.4.8
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libopencv_ml.so.2.4.8
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libopencv_legacy.so.2.4.8
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libopencv_imgproc.so.2.4.8
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libopencv_highgui.so.2.4.8
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libopencv_gpu.so.2.4.8
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libopencv_flann.so.2.4.8
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libopencv_features2d.so.2.4.8
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libopencv_core.so.2.4.8
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libopencv_contrib.so.2.4.8
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libopencv_calib3d.so.2.4.8
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /opt/ros/indigo/lib/libimage_transport.so
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /opt/ros/indigo/lib/libmessage_filters.so
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /opt/ros/indigo/lib/libclass_loader.so
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/libPocoFoundation.so
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libdl.so
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /opt/ros/indigo/lib/libroslib.so
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /opt/ros/indigo/lib/librospack.so
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libpython2.7.so
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libboost_program_options.so
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libtinyxml.so
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /opt/ros/indigo/lib/libroscpp.so
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libboost_signals.so
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libboost_filesystem.so
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /opt/ros/indigo/lib/librosconsole.so
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /opt/ros/indigo/lib/librosconsole_log4cxx.so
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /opt/ros/indigo/lib/librosconsole_backend_interface.so
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/liblog4cxx.so
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libboost_regex.so
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /opt/ros/indigo/lib/libxmlrpcpp.so
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /opt/ros/indigo/lib/libroscpp_serialization.so
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /opt/ros/indigo/lib/librostime.so
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libboost_date_time.so
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /opt/ros/indigo/lib/libcpp_common.so
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libboost_system.so
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libboost_thread.so
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libpthread.so
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libconsole_bridge.so
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /opt/ros/indigo/lib/libusb_cam.so
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /home/meareg/dlib_ws/devel/lib/libdlib.a
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libopencv_videostab.so.2.4.8
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libopencv_video.so.2.4.8
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libopencv_superres.so.2.4.8
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libopencv_stitching.so.2.4.8
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libopencv_photo.so.2.4.8
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libopencv_ocl.so.2.4.8
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libopencv_objdetect.so.2.4.8
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libopencv_ml.so.2.4.8
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libopencv_legacy.so.2.4.8
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libopencv_imgproc.so.2.4.8
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libopencv_highgui.so.2.4.8
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libopencv_gpu.so.2.4.8
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libopencv_flann.so.2.4.8
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libopencv_features2d.so.2.4.8
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libopencv_core.so.2.4.8
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libopencv_contrib.so.2.4.8
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libopencv_calib3d.so.2.4.8
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libnsl.so
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libSM.so
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libICE.so
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libX11.so
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libXext.so
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libpng.so
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libjpeg.so
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/libatlas.so
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/libcblas.so
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/liblapack.so
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libsqlite3.so
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libopencv_photo.so.2.4.8
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libopencv_legacy.so.2.4.8
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libopencv_video.so.2.4.8
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libopencv_objdetect.so.2.4.8
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libopencv_ml.so.2.4.8
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libopencv_calib3d.so.2.4.8
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libopencv_features2d.so.2.4.8
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libopencv_highgui.so.2.4.8
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libopencv_imgproc.so.2.4.8
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libopencv_flann.so.2.4.8
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: /usr/lib/x86_64-linux-gnu/libopencv_core.so.2.4.8
/home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node: dlib_puppeteering/CMakeFiles/dlib_puppeteering_node.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX executable /home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node"
	cd /home/meareg/dlib_ws/build/dlib_puppeteering && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/dlib_puppeteering_node.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
dlib_puppeteering/CMakeFiles/dlib_puppeteering_node.dir/build: /home/meareg/dlib_ws/devel/lib/dlib_puppeteering/dlib_puppeteering_node
.PHONY : dlib_puppeteering/CMakeFiles/dlib_puppeteering_node.dir/build

dlib_puppeteering/CMakeFiles/dlib_puppeteering_node.dir/requires: dlib_puppeteering/CMakeFiles/dlib_puppeteering_node.dir/src/dlib_facenew.cpp.o.requires
.PHONY : dlib_puppeteering/CMakeFiles/dlib_puppeteering_node.dir/requires

dlib_puppeteering/CMakeFiles/dlib_puppeteering_node.dir/clean:
	cd /home/meareg/dlib_ws/build/dlib_puppeteering && $(CMAKE_COMMAND) -P CMakeFiles/dlib_puppeteering_node.dir/cmake_clean.cmake
.PHONY : dlib_puppeteering/CMakeFiles/dlib_puppeteering_node.dir/clean

dlib_puppeteering/CMakeFiles/dlib_puppeteering_node.dir/depend:
	cd /home/meareg/dlib_ws/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/meareg/dlib_ws/src /home/meareg/dlib_ws/src/dlib_puppeteering /home/meareg/dlib_ws/build /home/meareg/dlib_ws/build/dlib_puppeteering /home/meareg/dlib_ws/build/dlib_puppeteering/CMakeFiles/dlib_puppeteering_node.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : dlib_puppeteering/CMakeFiles/dlib_puppeteering_node.dir/depend

