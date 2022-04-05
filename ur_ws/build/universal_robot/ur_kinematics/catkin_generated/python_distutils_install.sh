#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/rrqq/TableRearrangement/ur_ws/src/universal_robot/ur_kinematics"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/rrqq/TableRearrangement/ur_ws/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/rrqq/TableRearrangement/ur_ws/install/lib/python2.7/dist-packages:/home/rrqq/TableRearrangement/ur_ws/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/rrqq/TableRearrangement/ur_ws/build" \
    "/usr/bin/python2" \
    "/home/rrqq/TableRearrangement/ur_ws/src/universal_robot/ur_kinematics/setup.py" \
     \
    build --build-base "/home/rrqq/TableRearrangement/ur_ws/build/universal_robot/ur_kinematics" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/rrqq/TableRearrangement/ur_ws/install" --install-scripts="/home/rrqq/TableRearrangement/ur_ws/install/bin"
