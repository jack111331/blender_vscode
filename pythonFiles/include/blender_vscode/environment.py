import bpy
import sys
import addon_utils
from pathlib import Path

python_path = Path(bpy.app.binary_path_python)

# python_path = Path(sys.executable)
blender_path = Path(bpy.app.binary_path)
blender_directory = blender_path.parent
use_own_python = blender_directory in python_path.parents

version = bpy.app.version
scripts_folder = blender_path.parent / ("%d.%d"%(version[0], version[1])) / "scripts"
user_addon_directory = Path(bpy.utils.user_resource('SCRIPTS', path="addons"))
addon_directories = tuple(map(Path, addon_utils.paths()))
