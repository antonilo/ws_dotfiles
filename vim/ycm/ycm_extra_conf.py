#!/usr/bin/env python3
# This file is NOT licensed under the GPLv3, which is the license for the rest
# of YouCompleteMe.
#
# Here's the license text for this file:
#
# This is free and unencumbered software released into the public domain.
#
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.
#
# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# For more information, please refer to <http://unlicense.org/>

import os
import ycm_core

# These are the compilation flags that will be used in case there's no
# compilation database set (by default, one is not set).
# CHANGE THIS LIST OF FLAGS. YES, THIS IS THE DROID YOU HAVE BEEN LOOKING FOR.
flags = [
'-Wall',
'-Wextra',
# '-Werror',
'-fexceptions',
'-DNDEBUG',
# THIS IS IMPORTANT! Without a "-std=<something>" flag, clang won't know which
# language to use when compiling headers. So it will guess. Badly. So C++
# headers will be compiled as C headers. You don't want that so ALWAYS specify
# a "-std=<something>".
# For a C project, you would set this to something like 'c99' instead of
# 'c++11'.
'-std=c++17',
# ...and the same thing goes for the magic -x option which specifies the
# language that the files to be compiled are written in. This is mostly
# relevant for c++ headers.
# For a C project, you would set this to 'c' instead of 'c++'.
'-x',
'c++',
'-isystem',
'../BoostParts',
'-isystem',
# This path will only work on OS X, but extra paths that don't exist are not
# harmful
'/System/Library/Frameworks/Python.framework/Headers',
'-isystem',
'../llvm/include',
'-isystem',
'../llvm/tools/clang/include',
'-I',
'.',
'-I',
'./ClangCompleter',
'-isystem',
'./tests/gmock/gtest',
'-isystem',
'./tests/gmock/gtest/include',
'-isystem',
'./tests/gmock',
'-isystem',
'./tests/gmock/include',
'-I/opt/ros/melodic/include',
'-I/opt/ros/melodic/share/xmlrpcpp/cmake/../../../include/xmlrpcpp',
'-I/usr/include/eigen3',
'-I/home/eggerk/catkin_ws/build/voxblox',
'-I/usr/include/pcl-1.7',
'-I/usr/include/ni',
'-I/usr/include/vtk-6.2',
'-I/usr/include/freetype2',
'-I/usr/include/x86_64-linux-gnu/freetype2',
'-I/usr/include/x86_64-linux-gnu',
'-I/usr/lib/openmpi/include/openmpi/opal/mca/event/libevent2021/libevent',
'-I/usr/lib/openmpi/include/openmpi/opal/mca/event/libevent2021/libevent/include',
'-I/usr/lib/openmpi/include',
'-I/usr/lib/openmpi/include/openmpi',
'-I/usr/include/python2.7',
'-I/usr/include/jsoncpp',
'-I/usr/include/hdf5/openmpi',
'-I/usr/include/libxml2',
'-I/usr/include/tcl',
'-I/usr/include/pcl-1.8/',
'-DENABLE_TIMING=TRUE',
'-DENABLE_STATISTICS=TRUE',
'-DHAVE_OPENCV',
'-mssse3',
]

def _CheckFolder(folder):
  all_elements_in_dir = os.listdir(folder);
  for e in all_elements_in_dir:
    path = os.path.join(folder, e)
    if os.path.islink(path):
      continue
    if os.path.isdir(path):
      if e == 'include':
        flags.append('-I' + path)
      else:
        _CheckFolder(path)

# Get all catkin folders.
if 'CATKIN_WS' in os.environ:
  catkin_ws = os.environ["CATKIN_WS"]
  if os.path.isdir(catkin_ws):
    print 'catkin_ws:', catkin_ws
    devel_include_folder = os.path.join(catkin_ws, 'devel', 'include')
    flags.append('-I' + devel_include_folder)
    flags.append('-I' + os.path.join(devel_include_folder, 'opencv'))

    # Find all include folders in src.
    src_dir = os.path.join(catkin_ws, 'src')
    _CheckFolder(src_dir)


def include_folder_for_file(file_name):
  dir_name = os.path.dirname(file_name)
  for _ in range(5):
    include_folder = os.path.join(dir_name, 'include')
    if os.path.isdir(include_folder):
      flags.append('-I' + include_folder)
      return
    dir_name = os.path.dirname(dir_name)


def include_folders_for_repo(file_name):
  dir_name = os.path.dirname(file_name)
  print 'looking for git'
  for _ in range(5):
    git_folder = os.path.join(dir_name, '.git')
    if os.path.isdir(git_folder):
      print 'found git folder:,', git_folder
      _CheckFolder(dir_name)
      return
    dir_name = os.path.dirname(dir_name)


# Set this to the absolute path to the folder (NOT the file!) containing the
# compile_commands.json file to use that instead of 'flags'. See here for
# more details: http://clang.llvm.org/docs/JSONCompilationDatabase.html
#
# You can get CMake to generate this file for you by adding:
#   set( CMAKE_EXPORT_COMPILE_COMMANDS 1 )
# to your CMakeLists.txt file.
#
# Most projects will NOT need to set this to anything; you can just change the
# 'flags' list of compilation flags. Notice that YCM itself uses that approach.
compilation_database_folder = '' # '%%%BUILD_FOLDER_PATH%%%'

if os.path.exists( compilation_database_folder ):
  database = ycm_core.CompilationDatabase( compilation_database_folder )
  print(compilation_database_folder)
else:
  database = None

SOURCE_EXTENSIONS = [ '.cpp', '.cxx', '.cc', '.c', '.m', '.mm' ]

def DirectoryOfThisScript():
  return os.path.dirname( os.path.abspath( __file__ ) )


def MakeRelativePathsInFlagsAbsolute( flags, working_directory ):
  if not working_directory:
    return list( flags )
  new_flags = []
  make_next_absolute = False
  path_flags = [ '-isystem', '-I', '-iquote', '--sysroot=' ]
  for flag in flags:
    new_flag = flag

    if make_next_absolute:
      make_next_absolute = False
      if not flag.startswith( '/' ):
        new_flag = os.path.join( working_directory, flag )

    for path_flag in path_flags:
      if flag == path_flag:
        make_next_absolute = True
        break

      if flag.startswith( path_flag ):
        path = flag[ len( path_flag ): ]
        new_flag = path_flag + os.path.join( working_directory, path )
        break

    if new_flag:
      new_flags.append( new_flag )
  return new_flags


def IsSourceFile( filename ):
  extension = os.path.splitext( filename )[ 1 ]
  return extension in [ '.c', '.cxx', '.cpp', '.cc' ]


def IsHeaderFile( filename ):
  extension = os.path.splitext( filename )[ 1 ]
  return extension in [ '.h', '.hxx', '.hpp', '.hh' ]


def CheckFolderForCompilationInfo( folder, filename ):
  basename = os.path.splitext( filename )[ 0 ]
  for extension in SOURCE_EXTENSIONS:
    replacement_file = basename + extension
    if os.path.exists( replacement_file ):
      compilation_info = database.GetCompilationInfoForFile(
        replacement_file )
      if compilation_info.compiler_flags_:
        return compilation_info

  all_elements_in_dir = os.listdir(folder);
  for e in all_elements_in_dir:
    new_path = folder + '/' + e
    if os.path.isdir(new_path):
      return CheckFolderForCompilationInfo(new_path, filename)

  return None


def GetCompilationInfoForFile( filename ):
  # The compilation_commands.json file generated by CMake does not have entries
  # for header files. So we do our best by asking the db for flags for a
  # corresponding source file, if any. If one exists, the flags for that file
  # should be good enough.
  if IsHeaderFile( filename ):
    basename = os.path.dirname(filename)
    filename_without_path = os.path.basename(filename)
    compilation_info = CheckFolderForCompilationInfo(".", filename_without_path)

    src_path = ""
    src_found = False
    if compilation_info == None:
      # Check for source folder.
      for i in range(1, 5):
        if src_found:
          break
        basename = basename + "/.."
        all_elements_in_dir = os.listdir(basename);
        for e in all_elements_in_dir:
          src_path = basename + '/' + e
          if e == 'src' and os.path.isdir(src_path):
            compilation_info = CheckFolderForCompilationInfo(src_path, filename)
            src_found = True
            break

      if compilation_info == None and src_path != "":
        # Use first entry in src folder.
        all_elements_in_dir = os.listdir(src_path);
        for e in all_elements_in_dir:
          file_path = src_path + '/' + e
          if IsSourceFile(file_path):
            return database.GetCompilationInfoForFile( file_path )

    return None
  return database.GetCompilationInfoForFile( filename )


def FlagsForFile( filename, **kwargs ):
  if database:
    # Bear in mind that compilation_info.compiler_flags_ does NOT return a
    # python list, but a "list-like" StringVec object
    compilation_info = GetCompilationInfoForFile( filename )
    if not compilation_info:
      return None

    final_flags = MakeRelativePathsInFlagsAbsolute(
      compilation_info.compiler_flags_,
      compilation_info.compiler_working_dir_ )

    # NOTE: This is just for YouCompleteMe; it's highly likely that your project
    # does NOT need to remove the stdlib flag. DO NOT USE THIS IN YOUR
    # ycm_extra_conf IF YOU'RE NOT 100% SURE YOU NEED IT.
    try:
      final_flags.remove( '-stdlib=libc++' )
    except ValueError:
      pass
  else:
    include_folder_for_file(filename)
    include_folders_for_repo(filename)
    relative_to = DirectoryOfThisScript()
    final_flags = MakeRelativePathsInFlagsAbsolute( flags, relative_to )

  return {
    'flags': final_flags,
    'do_cache': True
  }
