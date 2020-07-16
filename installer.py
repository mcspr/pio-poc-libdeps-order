Import("env")

import os
import subprocess


if "1" == os.environ.get("INSTALL_LIBS", "0"):
    print("<<<<<<<<<<<<< INSTALLING")

    PIO_PLATFORM = env.PioPlatform()
    CONFIG = env.GetProjectConfig()

    def subprocess_libdeps(lib_deps, storage=None, silent=True):
        import subprocess

        args = [env.subst("$PYTHONEXE"), "-mplatformio", "lib"]
        if not storage:
            args.append("-g")
        else:
            args.extend(["-d", storage])
        args.append("install")
        if silent:
            args.append("-s")

        args.extend(lib_deps)

        subprocess.check_call(args)

    subprocess_libdeps(env.GetProjectOption("lib_deps"), silent=False)
